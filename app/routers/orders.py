from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.auth import get_current_user

from app.models.cart import Cart, CartItem
from app.models.product import Product
from app.models.order import Order, OrderItem

from app.schemas.order import OrderResponse

from app.services.razorpay_service import (
    create_razorpay_order,
    verify_payment_signature
)

from app.schemas.payment import PaymentVerifyRequest


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post(
    "/checkout",
    response_model=OrderResponse
)
def checkout(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # ==================================================
    # 1. Find active cart
    # ==================================================

    cart = (
        db.query(Cart)
        .filter(
            Cart.user_id == current_user.id,
            Cart.status == "ACTIVE"
        )
        .first()
    )

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Active cart not found"
        )

    # ==================================================
    # 2. Get cart items
    # ==================================================

    cart_items = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id
        )
        .all()
    )

    if not cart_items:
        raise HTTPException(
            status_code=400,
            detail="Cart is empty"
        )

    # ==================================================
    # 3. Validate products + calculate total
    # ==================================================

    total_amount = 0

    order_items_data = []

    for item in cart_items:

        product = (
            db.query(Product)
            .filter(
                Product.id == item.product_id,
                Product.is_active == True
            )
            .first()
        )

        if not product:
            raise HTTPException(
                status_code=400,
                detail=f"Product {item.product_id} is unavailable"
            )

        if product.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for {product.name}"
            )

        # Never trust price from client/cart.
        # Always use current DB product price.

        unit_price = product.price_paise

        item_total = unit_price * item.quantity

        total_amount += item_total

        order_items_data.append({
            "product": product,
            "quantity": item.quantity,
            "unit_price": unit_price,
            "total_price": item_total
        })

    # ==================================================
    # 4. Create local Order
    # ==================================================

    order = Order(
        user_id=current_user.id,
        status="PENDING",
        payment_status="PENDING",
        total_amount_paise=total_amount,
        currency="INR"
    )

    db.add(order)

    db.flush()

    # ==================================================
    # 5. Create Order Items
    # ==================================================

    for data in order_items_data:

        product = data["product"]

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            product_name=product.name,
            quantity=data["quantity"],
            unit_price_paise=data["unit_price"],
            total_price_paise=data["total_price"]
        )

        db.add(order_item)

    # ==================================================
    # 6. Create Razorpay Test Order
    # ==================================================

    try:

        razorpay_order = create_razorpay_order(
            amount_paise=total_amount,
            receipt=str(order.id),
            notes={
                "internal_order_id": str(order.id),
                "user_id": str(current_user.id)
            }
        )

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=502,
            detail=f"Razorpay order creation failed: {str(e)}"
        )

    # ==================================================
    # 7. Save Razorpay Order ID
    # ==================================================

    order.razorpay_order_id = razorpay_order["id"]

    # ==================================================
    # 8. IMPORTANT:
    # Do NOT decrease stock yet.
    #
    # Stock should be reduced only after successful
    # payment verification.
    # ==================================================

    # ==================================================
    # 9. Close cart
    # ==================================================

    cart.status = "CHECKED_OUT"

    # ==================================================
    # 10. Commit
    # ==================================================

    db.commit()

    db.refresh(order)

    # ==================================================
    # 11. Load Order Items
    # ==================================================

    order.items = (
        db.query(OrderItem)
        .filter(
            OrderItem.order_id == order.id
        )
        .all()
    )

    return order

@router.post("/payment/verify")
def verify_payment(
    payment_data: PaymentVerifyRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # ==================================================
    # 1. Find the local order
    # ==================================================

    order = (
        db.query(Order)
        .filter(
            Order.id == payment_data.order_id,
            Order.user_id == current_user.id
        )
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    # ==================================================
    # 2. Check order is still pending
    # ==================================================

    if order.payment_status == "PAID":

        raise HTTPException(
            status_code=400,
            detail="Payment already verified"
        )

    # ==================================================
    # 3. Verify Razorpay Order ID
    # ==================================================

    if order.razorpay_order_id != payment_data.razorpay_order_id:

        raise HTTPException(
            status_code=400,
            detail="Razorpay order ID mismatch"
        )

    # ==================================================
    # 4. Verify Razorpay signature
    # ==================================================

    try:

        verify_payment_signature(
            razorpay_order_id=payment_data.razorpay_order_id,
            razorpay_payment_id=payment_data.razorpay_payment_id,
            razorpay_signature=payment_data.razorpay_signature
        )

    except Exception:

        order.payment_status = "FAILED"

        db.commit()

        raise HTTPException(
            status_code=400,
            detail="Payment signature verification failed"
        )

    # ==================================================
    # 5. Load order items
    # ==================================================

    order_items = (
        db.query(OrderItem)
        .filter(
            OrderItem.order_id == order.id
        )
        .all()
    )

    if not order_items:

        raise HTTPException(
            status_code=400,
            detail="Order has no items"
        )

    # ==================================================
    # 6. Verify stock before marking payment successful
    # ==================================================

    products = []

    for item in order_items:

        product = (
            db.query(Product)
            .filter(
                Product.id == item.product_id,
                Product.is_active == True
            )
            .first()
        )

        if not product:

            order.payment_status = "FAILED"

            db.commit()

            raise HTTPException(
                status_code=400,
                detail=f"Product unavailable: {item.product_name}"
            )

        if product.stock_quantity < item.quantity:

            order.payment_status = "FAILED"

            db.commit()

            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for {item.product_name}"
            )

        products.append(
            (product, item.quantity)
        )

    # ==================================================
    # 7. Payment successful
    # ==================================================

    order.razorpay_payment_id = (
        payment_data.razorpay_payment_id
    )

    order.payment_status = "PAID"

    order.status = "CONFIRMED"

    # ==================================================
    # 8. Reduce stock
    # ==================================================

    for product, quantity in products:

        product.stock_quantity -= quantity

    # ==================================================
    # 9. Commit everything together
    # ==================================================

    db.commit()

    db.refresh(order)

    # ==================================================
    # 10. Return result
    # ==================================================

    return {
        "success": True,
        "message": "Payment verified successfully",
        "order_id": str(order.id),
        "status": order.status,
        "payment_status": order.payment_status,
        "razorpay_order_id": order.razorpay_order_id,
        "razorpay_payment_id": order.razorpay_payment_id,
        "total_amount_paise": order.total_amount_paise,
        "currency": order.currency
    }