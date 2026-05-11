from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal


class CreateBalanceCommand(BaseModel):
    user_id: UUID


class CreditBalanceCommand(BaseModel):
    user_id: UUID
    amount: Decimal


class DebitBalanceCommand(BaseModel):
    user_id: UUID
    amount: Decimal
