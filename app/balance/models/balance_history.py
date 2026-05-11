from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, UTC
from app.db import Base


class BalanceHistory(Base):
    __tablename__ = "balance_history"

    id = Column(Integer, primary_key=True)

    user_id = Column(UUID(as_uuid=True), nullable=False)

    event_type = Column(String, nullable=False)

    amount = Column(Numeric, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
