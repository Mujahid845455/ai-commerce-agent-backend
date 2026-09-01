import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class Merchant(Base):

    __tablename__ = "merchants"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    owner_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    business_name = Column(
        String(200),
        nullable=False
    )

    description = Column(Text)

    currency = Column(
        String(3),
        default="INR",
        nullable=False
    )