from uuid import UUID

from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):

    name: str

    email: EmailStr

    password: str

    role: str = "CUSTOMER"



class UserResponse(BaseModel):

    id: UUID

    name: str

    email: EmailStr

    role: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):

    access_token: str

    token_type: str = "bearer"