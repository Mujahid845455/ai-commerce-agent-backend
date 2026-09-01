from pydantic import BaseModel, Field


class CheckoutItem(BaseModel):
    product_id: str
    quantity: int = Field(default=1, ge=1)


class CheckoutRequest(BaseModel):
    items: list[CheckoutItem]
    customer_email: str | None = None
    confirmation: bool = False


class CheckoutResponse(BaseModel):
    status: str
    message: str

    order_id: str | None = None
    amount_paise: int | None = None
    currency: str = "INR"

    requires_confirmation: bool = False