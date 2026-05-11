from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, UTC
import uuid
from app.db import Base


class EventStore(Base):
    __tablename__ = "event_store"

    id = Column(Integer, primary_key=True, index=True)

    event_type = Column(String, nullable=False)

    user_id = Column(UUID(as_uuid=True), nullable=False)

    amount = Column(Numeric, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
