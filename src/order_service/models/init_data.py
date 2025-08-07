from sqlalchemy.orm import Session

from src.order_service.models.database import engine
from src.order_service.models.models import Status, Base



def init_statuses():
    DEFAULT_STATUSES = ["PENDING",
                        "ASSEMBLING",
                        "DELIVERING",
                        "CLOSED"]
    with Session(engine) as session:
        existing_statuses = session.query(Status).count()
        if existing_statuses == 0:
            for status_type in DEFAULT_STATUSES:
                session.add(Status(type=status_type))
            session.commit()

if __name__ == "__main__":
    init_statuses()