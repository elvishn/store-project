from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from pathlib import Path
from sqlalchemy.orm import sessionmaker

DB_PATH = Path(__file__).parent / "mq.db"
MQ_DATABASE_URL = f"sqlite:///{DB_PATH}"

mq_engine = create_engine(MQ_DATABASE_URL)
Base = declarative_base()

def create_tables_mq():
    from .models import Event, Message, Offset
    Base.metadata.create_all(bind=mq_engine)

if __name__ == "__main__":
    create_tables_mq()
