import uuid

from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID

from datetime import datetime

from app.core.database import Base


class Cart(Base):

    __tablename__ = "carts"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    status = Column(
        String(20),
        default="ACTIVE",
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )


class CartItem(Base):

    __tablename__ = "cart_items"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    cart_id = Column(
        UUID(as_uuid=True),
        ForeignKey("carts.id"),
        nullable=False
    )

    product_id = Column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=1
    )

    unit_price_paise = Column(
        BigInteger,
        nullable=False
    )