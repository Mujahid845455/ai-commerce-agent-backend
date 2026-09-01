from uuid import UUID

from pydantic import BaseModel

from typing import List


class OrderItemResponse(BaseModel):

    id: UUID
    product_id: UUID
    product_name: str
    quantity: int
    unit_price_paise: int
    total_price_paise: int

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):

    id: UUID
    user_id: UUID

    status: str
    payment_status: str

    total_amount_paise: int
    currency: str

    razorpay_order_id: str | None = None
    razorpay_payment_id: str | None = None

    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True