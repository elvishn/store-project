from sqlalchemy.orm import Session
from order_service.models.database import engine
from order_service.models.models import Status, StatusType


def init_statuses():
    with Session(engine) as session:
        if session.query(Status).count() == 0:
            for status in StatusType:
                session.add(Status(type=status.value))
            session.commit()

if __name__ == "__main__":
    init_statuses()