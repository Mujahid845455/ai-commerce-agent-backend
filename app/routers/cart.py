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

from app.schemas.cart import (
    AddToCartRequest,
    CartResponse,
    CartItemResponse
)


router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@router.post(
    "/items",
    response_model=CartResponse
)
def add_to_cart(

    data: AddToCartRequest,

    current_user=Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)

):

    product = (
        db.query(Product)
        .filter(
            Product.id == data.product_id,
            Product.is_active == True
        )
        .first()
    )

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.stock_quantity < data.quantity:

        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    cart = (
        db.query(Cart)
        .filter(
            Cart.user_id == current_user.id,
            Cart.status == "ACTIVE"
        )
        .first()
    )

    if not cart:

        cart = Cart(
            user_id=current_user.id,
            status="ACTIVE"
        )

        db.add(cart)

        db.flush()

    item = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id,
            CartItem.product_id == product.id
        )
        .first()
    )

    if item:

        new_quantity = item.quantity + data.quantity

        if product.stock_quantity < new_quantity:

            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )

        item.quantity = new_quantity

    else:

        item = CartItem(
            cart_id=cart.id,
            product_id=product.id,
            quantity=data.quantity,
            unit_price_paise=product.price_paise
        )

        db.add(item)

    db.commit()

    db.refresh(cart)

    return build_cart_response(
        cart,
        db
    )
def build_cart_response(
    cart: Cart,
    db: Session
):

    items = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id
        )
        .all()
    )

    total = sum(
        item.quantity * item.unit_price_paise
        for item in items
    )

    return {
        "id": cart.id,
        "user_id": cart.user_id,
        "status": cart.status,
        "items": items,
        "total_paise": total
    }

@router.get(
    "",
    response_model=CartResponse
)
def get_cart(

    current_user=Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)

):

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
            detail="Cart is empty"
        )

    return build_cart_response(
        cart,
        db
    )