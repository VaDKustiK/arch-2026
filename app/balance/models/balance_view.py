from sqlalchemy import Column, Numeric
from sqlalchemy.dialects.postgresql import UUID
from app.db import Base


class BalanceView(Base):
    __tablename__ = "balance_view"

    user_id = Column(UUID(as_uuid=True), primary_key=True)

    balance = Column(Numeric, nullable=False, default=0)
