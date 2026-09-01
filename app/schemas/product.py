from typing import Dict, Any
from uuid import UUID

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=255
    )

    description: str | None = None

    category: str = Field(
        min_length=2,
        max_length=100
    )

    price_paise: int = Field(
        ge=0
    )

    currency: str = Field(
        default="INR",
        min_length=3,
        max_length=3
    )

    stock_quantity: int = Field(
        ge=0
    )

    attributes: Dict[str, Any] = Field(
        default_factory=dict
    )

class ProductUpdate(BaseModel):

    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=255
    )

    description: str | None = None

    category: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    price_paise: int | None = Field(
        default=None,
        ge=0
    )

    currency: str | None = Field(
        default=None,
        min_length=3,
        max_length=3
    )

    stock_quantity: int | None = Field(
        default=None,
        ge=0
    )

    attributes: Dict[str, Any] | None = None

    is_active: bool | None = None
class ProductResponse(BaseModel):

    id: UUID

    merchant_id: UUID

    name: str

    description: str | None

    category: str

    price_paise: int

    currency: str

    stock_quantity: int

    attributes: Dict[str, Any]

    is_active: bool

    class Config:
        from_attributes = True