from typing import Optional

from fastapi import (
    APIRouter,
    Depends,
    Query
)

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.product import Product
from app.schemas.product import ProductResponse


router = APIRouter(
    prefix="/catalog",
    tags=["Catalog"]
)


@router.get(
    "/products",
    response_model=list[ProductResponse]
)
def get_catalog_products(
    db: Session = Depends(get_db)
):

    products = (
        db.query(Product)
        .filter(
            Product.is_active == True,
            Product.stock_quantity > 0
        )
        .all()
    )

    return products


@router.get(
    "/search",
    response_model=list[ProductResponse]
)
def search_catalog(
    q: Optional[str] = Query(
        default=None,
        description="Search product name or description"
    ),

    category: Optional[str] = Query(
        default=None
    ),

    min_price: Optional[int] = Query(
        default=None,
        ge=0,
        description="Minimum price in paise"
    ),

    max_price: Optional[int] = Query(
        default=None,
        ge=0,
        description="Maximum price in paise"
    ),

    color: Optional[str] = Query(
        default=None
    ),

    brand: Optional[str] = Query(
        default=None
    ),

    size: Optional[str] = Query(
        default=None
    ),

    db: Session = Depends(get_db)
):

    query = (
        db.query(Product)
        .filter(
            Product.is_active == True,
            Product.stock_quantity > 0
        )
    )

    # Text search
    if q:

        search_pattern = f"%{q}%"

        query = query.filter(
            Product.name.ilike(search_pattern)
            |
            Product.description.ilike(search_pattern)
        )

    # Category filter
    if category:

        query = query.filter(
            Product.category.ilike(category)
        )

    # Price filters
    if min_price is not None:

        query = query.filter(
            Product.price_paise >= min_price
        )

    if max_price is not None:

        query = query.filter(
            Product.price_paise <= max_price
        )

    # JSON attributes
    if color:

        query = query.filter(
            Product.attributes["color"].as_string().ilike(color)
        )

    if brand:

        query = query.filter(
            Product.attributes["brand"].as_string().ilike(brand)
        )

    if size:

        query = query.filter(
            Product.attributes["size"].as_string() == size
        )

    return query.all()