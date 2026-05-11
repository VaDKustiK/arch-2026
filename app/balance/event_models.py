from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal


class BalanceCreatedEvent(BaseModel):
    user_id: UUID


class BalanceCreditedEvent(BaseModel):
    user_id: UUID
    amount: Decimal


class BalanceDebitedEvent(BaseModel):
    user_id: UUID
    amount: Decimal