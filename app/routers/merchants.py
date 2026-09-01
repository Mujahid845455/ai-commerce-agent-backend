from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.auth import require_role

from app.models.merchant import Merchant

from app.schemas.merchant import (
    MerchantCreate,
    MerchantResponse
)


router = APIRouter(
    prefix="/merchants",
    tags=["Merchants"]
)


@router.post(
    "/profile",
    response_model=MerchantResponse
)
def create_merchant_profile(

    data: MerchantCreate,

    current_user=Depends(
        require_role("MERCHANT")
    ),

    db: Session = Depends(get_db)

):

    existing = (
        db.query(Merchant)
        .filter(
            Merchant.owner_id == current_user.id
        )
        .first()
    )

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Merchant profile already exists"
        )

    merchant = Merchant(

        owner_id=current_user.id,

        business_name=data.business_name,

        description=data.description,

        currency=data.currency

    )

    db.add(merchant)

    db.commit()

    db.refresh(merchant)

    return merchant