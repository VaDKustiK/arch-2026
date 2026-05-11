from decimal import Decimal

from sqlalchemy.orm import Session

from app.balance.models.balance_view import BalanceView
from app.balance.models.balance_history import BalanceHistory


def apply_balance_created(db: Session, user_id):
    balance_view = BalanceView(
        user_id=user_id,
        balance=Decimal("0")
    )

    db.add(balance_view)

    history = BalanceHistory(
        user_id=user_id,
        event_type="CREATE",
        amount=Decimal("0")
    )

    db.add(history)

    db.commit()


def apply_balance_credited(db: Session, user_id, amount):
    balance = db.query(BalanceView).filter(
        BalanceView.user_id == user_id
    ).first()

    balance.balance += amount

    history = BalanceHistory(
        user_id=user_id,
        event_type="CREDIT",
        amount=amount
    )

    db.add(history)

    db.commit()


def apply_balance_debited(db: Session, user_id, amount):
    balance = db.query(BalanceView).filter(
        BalanceView.user_id == user_id
    ).first()

    balance.balance -= amount

    history = BalanceHistory(
        user_id=user_id,
        event_type="DEBIT",
        amount=amount
    )

    db.add(history)

    db.commit()
