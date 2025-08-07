from sqlalchemy.orm import Session
from .database import mq_engine
from .models import Base, EventType


def init_mq_data():
    DEFAULT_TYPE = ["ORDER_CREATED", "ORDER_UPDATED"]
    with Session(mq_engine) as session:
        if not session.query(EventType).first():
            for mq_type in DEFAULT_TYPE:
                session.add(EventType(type=mq_type))
            session.commit()

if __name__ == "__main__":
    init_mq_data()