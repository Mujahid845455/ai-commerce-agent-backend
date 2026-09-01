import uuid

from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Integer,
    DateTime,
    ForeignKey,
    UUID
)

from app.core.database import Base


class Order(Base):

    __tablename__ = "orders"

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
        String(30),
        default="PENDING",
        nullable=False
    )

    payment_status = Column(
        String(30),
        default="PENDING",
        nullable=False
    )

    total_amount_paise = Column(
        BigInteger,
        nullable=False
    )

    currency = Column(
        String(3),
        default="INR",
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
    razorpay_order_id = Column(
        String(100),
        nullable=True
    )

    razorpay_payment_id = Column(
        String(100),
        nullable=True
    )


class OrderItem(Base):

    __tablename__ = "order_items"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    order_id = Column(
        UUID(as_uuid=True),
        ForeignKey("orders.id"),
        nullable=False
    )

    product_id = Column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False
    )

    product_name = Column(
        String(255),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    unit_price_paise = Column(
        BigInteger,
        nullable=False
    )

    total_price_paise = Column(
        BigInteger,
        nullable=False
    )