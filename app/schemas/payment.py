from uuid import UUID


from pydantic import BaseModel, Field


class PaymentItem(BaseModel):
    product_id: str
    quantity: int = Field(default=1, ge=1)


class CreateOrderRequest(BaseModel):
    items: list[PaymentItem]


class CreateOrderResponse(BaseModel):
    order_id: str
    amount_paise: int
    currency: str
    items: list[dict]
    status: str


class PaymentVerifyRequest(BaseModel):
    items: list[PaymentItem]

    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str