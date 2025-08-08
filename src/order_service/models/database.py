from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from pathlib import Path
from sqlalchemy.orm import sessionmaker


ORDERS_DB_PATH = Path(__file__).parent.parent / "orders.db"
ORDERS_DB_URL = f"sqlite:///{ORDERS_DB_PATH}"

engine = create_engine(ORDERS_DB_URL)
Base = declarative_base()

def create_tables():
    from src.order_service.models.models import Status, Order, Product
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()

