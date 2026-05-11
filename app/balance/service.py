from decimal import Decimal

from sqlalchemy.orm import Session

from app.balance.models.event_store import EventStore
from app.balance.models.balance_view import BalanceView

from app.balance.projection import (
    apply_balance_created,
    apply_balance_credited,
    apply_balance_debited
)


def create_balance(db: Session, user_id):
    existing = db.query(BalanceView).filter(
        BalanceView.user_id == user_id
    ).first()

    if existing:
        raise Exception("Balance already exists")

    event = EventStore(
        event_type="BalanceCreatedEvent",
        user_id=user_id,
        amount=Decimal("0")
    )

    db.add(event)
    db.commit()

    apply_balance_created(db, user_id)


def credit_balance(db: Session, user_id, amount):
    if amount <= 0:
        raise Exception("Amount must be > 0")

    balance = db.query(BalanceView).filter(
        BalanceView.user_id == user_id
    ).first()

    if not balance:
        raise Exception("Balance not found")

    event = EventStore(
        event_type="BalanceCreditedEvent",
        user_id=user_id,
        amount=amount
    )

    db.add(event)
    db.commit()

    apply_balance_credited(db, user_id, amount)


def debit_balance(db: Session, user_id, amount):
    if amount <= 0:
        raise Exception("Amount must be > 0")

    balance = db.query(BalanceView).filter(
        BalanceView.user_id == user_id
    ).first()

    if not balance:
        raise Exception("Balance not found")

    if balance.balance < amount:
        raise Exception("Insufficient funds")

    event = EventStore(
        event_type="BalanceDebitedEvent",
        user_id=user_id,
        amount=amount
    )

    db.add(event)
    db.commit()

    apply_balance_debited(db, user_id, amount)
