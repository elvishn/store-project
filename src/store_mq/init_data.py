from sqlalchemy.orm import Session
from .database import mq_engine
from .models import Base, EventType, DefaultType


def init_mq_data():
    with Session(mq_engine) as session:
        if not session.query(EventType).first():
            for mq_type in DefaultType:
                session.add(EventType(type=mq_type.value))
            session.commit()

if __name__ == "__main__":
    init_mq_data()