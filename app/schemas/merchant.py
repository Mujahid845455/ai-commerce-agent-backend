from uuid import UUID

from pydantic import BaseModel


class MerchantCreate(BaseModel):

    business_name: str

    description: str | None = None

    currency: str = "INR"


class MerchantResponse(BaseModel):

    id: UUID

    owner_id: UUID

    business_name: str

    description: str | None

    currency: str

    class Config:
        from_attributes = True