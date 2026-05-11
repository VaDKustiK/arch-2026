from decimal import Decimal
from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db import SessionLocal

from app.balance.service import (
    create_balance,
    credit_balance,
    debit_balance
)

from app.balance.models.balance_view import BalanceView
from app.balance.models.balance_history import BalanceHistory

router = APIRouter(prefix="/balances", tags=["balances"])


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/{user_id}/create")
def create_balance_endpoint(user_id: UUID, db: Session = Depends(get_db)):
    create_balance(db, user_id)

    return {"status": "created"}


@router.post("/{user_id}/credit")
def credit_balance_endpoint(
    user_id: UUID,
    amount: Decimal,
    db: Session = Depends(get_db)
):
    credit_balance(db, user_id, amount)

    return {"status": "credited"}


@router.post("/{user_id}/debit")
def debit_balance_endpoint(
    user_id: UUID,
    amount: Decimal,
    db: Session = Depends(get_db)
):
    debit_balance(db, user_id, amount)

    return {"status": "debited"}


@router.get("/{user_id}")
def get_balance(user_id: UUID, db: Session = Depends(get_db)):
    balance = db.query(BalanceView).filter(
        BalanceView.user_id == user_id
    ).first()

    return balance


@router.get("/{user_id}/history")
def get_history(user_id: UUID, db: Session = Depends(get_db)):
    history = db.query(BalanceHistory).filter(
        BalanceHistory.user_id == user_id
    ).all()

    return history
