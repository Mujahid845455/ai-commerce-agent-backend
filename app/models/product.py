import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    BigInteger,
    Boolean,
    ForeignKey,
    JSON,
    UUID
)

from app.core.database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    merchant_id = Column(
        UUID(as_uuid=True),
        ForeignKey("merchants.id"),
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    description = Column(Text)

    category = Column(
        String(100),
        nullable=False
    )

    price_paise = Column(
        BigInteger,
        nullable=False
    )

    currency = Column(
        String(3),
        default="INR",
        nullable=False
    )

    stock_quantity = Column(
        Integer,
        default=0,
        nullable=False
    )

    attributes = Column(
        JSON,
        default=dict
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )