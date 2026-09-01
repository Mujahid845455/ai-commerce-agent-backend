import uuid

from sqlalchemy import Column, String, Integer, Text, DateTime, JSON, UUID
from sqlalchemy.sql import func

from app.core.database import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    action = Column(
        String(100),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False
    )

    product_id = Column(
        UUID(as_uuid=True),
        nullable=True
    )

    amount_paise = Column(
        Integer,
        nullable=True
    )

    details = Column(
        JSON,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )