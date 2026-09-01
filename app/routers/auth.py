from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User

from app.schemas.auth import (
    RegisterRequest,
    UserResponse,
    TokenResponse
)

from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.core.auth import get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    if data.role not in [
        "CUSTOMER",
        "MERCHANT"
    ]:

        raise HTTPException(
            status_code=400,
            detail="Invalid role"
        )

    user = User(
        name=data.name,
        email=data.email,
        password_hash=hash_password(
            data.password
        ),
        role=data.role
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.email == form_data.username
        )
        .first()
    )

    if not user:
        if form_data.username == "customer@agentpay.demo":
            user = User(
                name="Arjun Sharma",
                email="customer@agentpay.demo",
                password_hash=hash_password("Customer@123"),
                role="CUSTOMER"
            )
            db.add(user)
            db.commit()
            db.refresh(user)
        elif form_data.username == "merchant@agentpay.demo":
            user = User(
                name="AgentPay Sports Admin",
                email="merchant@agentpay.demo",
                password_hash=hash_password("Merchant@123"),
                role="MERCHANT"
            )
            db.add(user)
            db.commit()
            db.refresh(user)
        else:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

    if not verify_password(
        form_data.password,
        user.password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        str(user.id),
        user.role
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(
        get_current_user
    )
):

    return current_user