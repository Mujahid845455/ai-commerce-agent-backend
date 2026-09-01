import uuid

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.product import Product
from app.models.audit import AuditLog

from app.schemas.payment import (
    CreateOrderRequest,
    CreateOrderResponse,
    PaymentVerifyRequest
)

from app.services.razorpay_service import (
    create_razorpay_order,
    verify_payment_signature
)


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


# Bounded Action Limit (₹5,000 = 500,000 paise)
MAX_AI_CHECKOUT_LIMIT_PAISE = 500000


@router.post(
    "/create-order",
    response_model=CreateOrderResponse
)
def create_order(
    data: CreateOrderRequest,
    db: Session = Depends(get_db)
):

    # ------------------------------------------------
    # SERVER-SIDE PRODUCT VALIDATION
    # ------------------------------------------------
    
    total_amount_paise = 0
    validated_items = []
    product_names = []

    for item in data.items:
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
                status_code=404,
                detail=f"Product not found: {item.product_id}"
            )

        if product.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for {product.name}"
            )

        item_total = product.price_paise * item.quantity
        total_amount_paise += item_total
        
        validated_items.append({
            "product_id": str(product.id),
            "product_name": product.name,
            "quantity": item.quantity,
            "price_paise": product.price_paise
        })
        product_names.append(product.name)

    # ------------------------------------------------
    # BOUNDED SPEND LIMIT
    # ------------------------------------------------
    if total_amount_paise > MAX_AI_CHECKOUT_LIMIT_PAISE:
        # Graceful failure logged
        failure_audit = AuditLog(
            action="AI_CHECKOUT_GENERATED",
            status="BLOCKED_BY_LIMIT",
            amount_paise=total_amount_paise,
            details={
                "error": "Exceeded maximum AI checkout limit of ₹5000",
                "items": validated_items
            }
        )
        db.add(failure_audit)
        db.commit()

        raise HTTPException(
            status_code=403,
            detail="Automated checkout limit exceeded (Max ₹5,000). Please review in cart manually."
        )

    # ------------------------------------------------
    # AUDIT — AI CHECKOUT ATTEMPT
    # ------------------------------------------------

    audit = AuditLog(
        action="AI_CHECKOUT_GENERATED",
        status="APPROVED",
        amount_paise=total_amount_paise,
        details={
            "items": validated_items,
            "currency": "INR",
            "source": "ai_agent_in_app"
        }
    )

    db.add(audit)
    db.commit()

    # ------------------------------------------------
    # RAZORPAY TEST ORDER
    # ------------------------------------------------

    receipt = (
        f"agentpay_{uuid.uuid4().hex[:20]}"
    )

    try:

        razorpay_order = create_razorpay_order(
            amount_paise=total_amount_paise,
            receipt=receipt,
            notes={
                "products": ", ".join(product_names)[:250] # Limit notes length
            }
        )

    except Exception as error:

        failure_audit = AuditLog(
            action="AI_CHECKOUT_GENERATED",
            status="FAILED",
            amount_paise=total_amount_paise,
            details={
                "error": str(error)
            }
        )

        db.add(failure_audit)
        db.commit()

        raise HTTPException(
            status_code=502,
            detail="Unable to create Razorpay test order"
        )

    return {
        "order_id": razorpay_order["id"],
        "amount_paise": total_amount_paise,
        "currency": "INR",
        "items": validated_items,
        "status": "created"
    }


@router.post("/verify")
def verify_payment(
    data: PaymentVerifyRequest,
    db: Session = Depends(get_db)
):

    # ------------------------------------------------
    # VERIFY PRODUCT
    # ------------------------------------------------
    total_amount_paise = 0
    products_to_update = []

    for item in data.items:
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
                status_code=404,
                detail=f"Product not found: {item.product_id}"
            )

        if product.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Stock is no longer available for {product.name}"
            )

        total_amount_paise += (product.price_paise * item.quantity)
        products_to_update.append((product, item.quantity))

    # ------------------------------------------------
    # VERIFY RAZORPAY SIGNATURE
    # ------------------------------------------------

    try:
        verify_payment_signature(
            razorpay_order_id=data.razorpay_order_id,
            razorpay_payment_id=data.razorpay_payment_id,
            razorpay_signature=data.razorpay_signature
        )

    except Exception as error:

        audit = AuditLog(
            action="PAYMENT_VERIFICATION",
            status="FAILED",
            amount_paise=total_amount_paise,
            details={
                "razorpay_order_id":
                    data.razorpay_order_id,
                "razorpay_payment_id":
                    data.razorpay_payment_id,
                "error": str(error)
            }
        )

        db.add(audit)
        db.commit()

        raise HTTPException(
            status_code=400,
            detail="Payment verification failed"
        )

    # ------------------------------------------------
    # PAYMENT VERIFIED
    # ------------------------------------------------

    audit = AuditLog(
        action="PAYMENT_VERIFICATION",
        status="SUCCESS",
        amount_paise=total_amount_paise,
        details={
            "razorpay_order_id": data.razorpay_order_id,
            "razorpay_payment_id": data.razorpay_payment_id
        }
    )

    db.add(audit)

    # ------------------------------------------------
    # STOCK UPDATE
    # ------------------------------------------------
    for product, quantity in products_to_update:
        product.stock_quantity -= quantity

    db.commit()

    return {
        "status": "verified",
        "message": "Payment verified successfully",
        "amount_paise": total_amount_paise,
        "razorpay_order_id": data.razorpay_order_id,
        "razorpay_payment_id": data.razorpay_payment_id
    }