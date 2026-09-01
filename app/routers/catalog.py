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
    q: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    color: Optional[str] = None,
    brand: Optional[str] = None,
    size: Optional[str] = None,
    db: Session = Depends(get_db)
):
    if hasattr(q, "default"): q = None
    if hasattr(category, "default"): category = None
    if hasattr(min_price, "default"): min_price = None
    if hasattr(max_price, "default"): max_price = None
    if hasattr(color, "default"): color = None
    if hasattr(brand, "default"): brand = None
    if hasattr(size, "default"): size = None

    query = (
        db.query(Product)
        .filter(
            Product.is_active == True,
            Product.stock_quantity > 0
        )
    )

    # Text search
    if q:
        q_clean = q.strip()
        search_pattern = f"%{q_clean}%"

        exact_query = query.filter(
            Product.name.ilike(search_pattern)
            |
            Product.description.ilike(search_pattern)
        )
        exact_results = exact_query.all()

        if exact_results:
            query = exact_query
        else:
            # Fallback for multi-word queries like "laptop setup"
            words = [w for w in q_clean.split() if len(w) >= 2]
            if words:
                from sqlalchemy import or_
                token_conditions = []
                for word in words:
                    wp = f"%{word}%"
                    token_conditions.append(
                        Product.name.ilike(wp) | Product.description.ilike(wp)
                    )
                query = query.filter(or_(*token_conditions))

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