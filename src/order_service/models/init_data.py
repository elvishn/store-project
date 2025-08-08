from sqlalchemy.orm import Session

from src.order_service.models.database import engine
from src.order_service.models.models import Status, Base, StatusType


def init_statuses():
    with Session(engine) as session:
        if session.query(Status).count() == 0:
            for status in StatusType:
                session.add(Status(type=status.value))
            session.commit()

if __name__ == "__main__":
    init_statuses()