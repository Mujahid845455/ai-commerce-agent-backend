from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.product import Product
from app.schemas.checkout import (
    CheckoutRequest,
    CheckoutResponse,
)
from app.services.razorpay_service import (
    create_razorpay_order,
)


router = APIRouter(
    prefix="/checkout",
    tags=["Checkout"],
)


@router.post(
    "",
    response_model=CheckoutResponse,
)
def create_checkout(
    data: CheckoutRequest,
    db: Session = Depends(get_db),
):
    if not data.items:
        raise HTTPException(
            status_code=400,
            detail="Cart is empty",
        )

    total_amount = 0
    validated_items = []

    # --------------------------------
    # 1. Validate products from DB
    # --------------------------------

    for item in data.items:

        product = (
            db.query(Product)
            .filter(
                Product.id == item.product_id,
                Product.is_active == True,
            )
            .first()
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product not found: {item.product_id}",
            )

        if product.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Insufficient stock for "
                    f"{product.name}"
                ),
            )

        item_total = (
            product.price_paise *
            item.quantity
        )

        total_amount += item_total

        validated_items.append(
            {
                "product_id": str(product.id),
                "name": product.name,
                "quantity": item.quantity,
                "price_paise": product.price_paise,
            }
        )

    # --------------------------------
    # 2. Safety limit
    # --------------------------------

    MAX_CHECKOUT_AMOUNT = 500000
    # ₹5,000

    if total_amount > MAX_CHECKOUT_AMOUNT:

        raise HTTPException(
            status_code=400,
            detail=(
                "Checkout amount exceeds "
                "the allowed limit of ₹5,000."
            ),
        )

    # --------------------------------
    # 3. Confirmation gate
    # --------------------------------

    if not data.confirmation:

        return CheckoutResponse(
            status="confirmation_required",
            message=(
                f"Your total is "
                f"₹{total_amount / 100:.2f}. "
                "Please confirm before payment."
            ),
            amount_paise=total_amount,
            requires_confirmation=True,
        )

    # --------------------------------
    # 4. Create Razorpay TEST order
    # --------------------------------

    receipt = (
        f"agentpay_{uuid4().hex[:16]}"
    )

    razorpay_order = create_razorpay_order(
        amount_paise=total_amount,
        receipt=receipt,
        notes={
            "source": "AgentPay AI Agent",
            "customer_email": (
                data.customer_email or ""
            ),
        },
    )

    return CheckoutResponse(
        status="order_created",
        message=(
            "Razorpay test order created "
            "successfully."
        ),
        order_id=razorpay_order["id"],
        amount_paise=total_amount,
        currency="INR",
        requires_confirmation=False,
    )