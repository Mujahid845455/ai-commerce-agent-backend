from uuid import UUID

from pydantic import BaseModel, Field


class AddToCartRequest(BaseModel):

    product_id: UUID

    quantity: int = Field(
        default=1,
        ge=1
    )


class CartItemResponse(BaseModel):

    id: UUID

    product_id: UUID

    quantity: int

    unit_price_paise: int

    class Config:
        from_attributes = True


class CartResponse(BaseModel):

    id: UUID

    user_id: UUID

    status: str

    items: list[CartItemResponse]

    total_paise: int