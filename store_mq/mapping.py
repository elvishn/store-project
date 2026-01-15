import json
from sqlite3 import IntegrityError

from order_service.models.database import engine
from order_service.models.models import Status, Order, Product
from order_service.schemas.orders_schemas import UniversalOrderModel
from store_mq.database import mq_engine
from sqlalchemy.orm import Session
from store_mq.models import Message


def get_status():
    with Session(engine) as session:
        statuses = session.query(Status).all()
        dct = {}
        for i in statuses:
            dct[i.type] = i.id
        return dct

with Session(mq_engine) as mq_session, Session(engine) as order_session:
    messages = mq_session.query(Message).all()
    statuses = get_status()
    try:
        for m in messages:
            data = json.loads(m.message)
            field_mapping = {
                'order_id': 'id',
                'status': 'status_id',
            }
            standardized_data = {}
            for key, value in data.items():
                standardized_key = field_mapping.get(key, key)
                standardized_data[standardized_key] = value
            if 'status_id' in standardized_data:
                status_text = standardized_data['status_id']
                if status_text in statuses:
                    standardized_data['status_id'] = statuses[status_text]
            validated = UniversalOrderModel(**standardized_data)
            new_order = Order(**validated.model_dump(exclude_none=True))
            order_session.add(new_order)
            if validated.id is None:
                order_session.flush()
            new_product = Product(order_id=validated.id or new_order.id)
            order_session.add(new_product)
            order_session.commit()
    except IntegrityError:
        order_session.rollback()



