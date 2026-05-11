from app.db import Base, engine
from app.balance.models.event_store import EventStore
from app.balance.models.balance_view import BalanceView
from app.balance.models.balance_history import BalanceHistory


def create_balance_tables():
    Base.metadata.create_all(bind=engine)
