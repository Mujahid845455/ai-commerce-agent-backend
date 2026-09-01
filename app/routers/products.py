from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.auth import require_role

from app.models.merchant import Merchant
from app.models.product import Product

from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "/",
    response_model=ProductResponse
)
def create_product(
    product_data: ProductCreate,

    current_user=Depends(
        require_role("MERCHANT")
    ),

    db: Session = Depends(get_db)
):

    # Find the merchant owned by the logged-in user
    merchant = (
        db.query(Merchant)
        .filter(
            Merchant.owner_id == current_user.id
        )
        .first()
    )

    if not merchant:

        raise HTTPException(
            status_code=404,
            detail="Merchant profile not found"
        )

    # Create product for the authenticated merchant
    product = Product(

        merchant_id=merchant.id,

        name=product_data.name,

        description=product_data.description,

        category=product_data.category,

        price_paise=product_data.price_paise,

        currency=product_data.currency,

        stock_quantity=product_data.stock_quantity,

        attributes=product_data.attributes
    )

    db.add(product)

    db.commit()

    db.refresh(product)

    return product

@router.get(
    "/",
    response_model=list[ProductResponse]
)
def get_my_products(
    current_user=Depends(
        require_role("MERCHANT")
    ),
    db: Session = Depends(get_db)
):

    merchant = (
        db.query(Merchant)
        .filter(
            Merchant.owner_id == current_user.id
        )
        .first()
    )

    if not merchant:

        raise HTTPException(
            status_code=404,
            detail="Merchant profile not found"
        )

    products = (
        db.query(Product)
        .filter(
            Product.merchant_id == merchant.id
        )
        .all()
    )

    return products
@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: UUID,
    db: Session = Depends(get_db)
):

    product = (
        db.query(Product)
        .filter(
            Product.id == product_id,
            Product.is_active == True
        )
        .first()
    )

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.patch(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: UUID,
    product_data: ProductUpdate,

    current_user=Depends(
        require_role("MERCHANT")
    ),

    db: Session = Depends(get_db)
):

    merchant = (
        db.query(Merchant)
        .filter(
            Merchant.owner_id == current_user.id
        )
        .first()
    )

    if not merchant:

        raise HTTPException(
            status_code=404,
            detail="Merchant profile not found"
        )

    product = (
        db.query(Product)
        .filter(
            Product.id == product_id,
            Product.merchant_id == merchant.id
        )
        .first()
    )

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    update_data = product_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():

        setattr(
            product,
            field,
            value
        )

    db.commit()

    db.refresh(product)

    return product

@router.delete(
    "/{product_id}",
    response_model=ProductResponse
)
def deactivate_product(
    product_id: UUID,

    current_user=Depends(
        require_role("MERCHANT")
    ),

    db: Session = Depends(get_db)
):

    merchant = (
        db.query(Merchant)
        .filter(
            Merchant.owner_id == current_user.id
        )
        .first()
    )

    if not merchant:

        raise HTTPException(
            status_code=404,
            detail="Merchant profile not found"
        )

    product = (
        db.query(Product)
        .filter(
            Product.id == product_id,
            Product.merchant_id == merchant.id
        )
        .first()
    )

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.is_active = False

    db.commit()

    db.refresh(product)

    return product