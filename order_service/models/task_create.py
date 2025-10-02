from datetime import datetime, timedelta
import random
from uuid import uuid4
from sqlalchemy.orm import Session, sessionmaker
from models import Status, Product, Order
from order_service.models.database import engine
Session = sessionmaker(bind=engine)
session = Session()

pending_status = session.query(Status).filter(Status.type == 'PENDING').first().id
assembling_status = session.query(Status).filter(Status.type == 'ASSEMBLING').first().id
delivering_status = session.query(Status).filter(Status.type == 'DELIVERING').first().id
closed_status = session.query(Status).filter(Status.type == 'CLOSED').first().id
users_id = [uuid4() for _ in range(3)]
orders_id = [uuid4() for _ in range(10)]
start_2024 = int(datetime(2024, 1, 1).timestamp())
end_2024 = int(datetime(2025, 1, 1).timestamp())

for i in orders_id:
    random_seconds = random.randint(0, end_2024 - start_2024)
    created_at_timestamp = start_2024 + random_seconds
    updated_at_timestamp = created_at_timestamp + random.randint(3600, 172800)
    order = Order(
        id=i,
        user_id=random.choice(users_id),
        status_id=random.choice([pending_status, assembling_status, delivering_status, closed_status]),
        created_at=created_at_timestamp,
        updated_at=updated_at_timestamp
    )
    session.add(order)

session.commit()

for j in range(15):
    prod = Product(
        id=uuid4(),
        order_id=random.choice(orders_id)
    )
    session.add(prod)

session.commit()
