from uuid import UUID

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.utils.security import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload"
        )

    try:
        user_uuid = UUID(str(user_id))

    except (ValueError, TypeError):

        raise HTTPException(
            status_code=401,
            detail="Invalid user ID"
        )

    user = (
        db.query(User)
        .filter(User.id == user_uuid)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


def require_role(*allowed_roles):

    def role_checker(
        current_user: User = Depends(
            get_current_user
        )
    ):

        if current_user.role not in allowed_roles:

            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions"
            )

        return current_user

    return role_checker