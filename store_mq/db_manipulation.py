import json
from sqlalchemy.orm import Session
from store_mq.database import mq_engine
from store_mq.models import Message, EventType, Event

def create_events(type_event, mes_id):
    with Session(mq_engine) as session:
        order_type = str(session.query(EventType).filter_by(type=type_event).first().id)
        new_event = Event(type=order_type, message_id=mes_id)
        session.add(new_event)
        session.flush()
        session.commit()

def message_to_events():
    with Session(mq_engine) as session:
        messages = session.query(Message).all()
        for m in messages:
            data = json.loads(m.message)
            if 'updated_at' in data:
                create_events("ORDER_UPDATED", m.id)
            else:
                create_events("ORDER_CREATED", m.id)

if __name__ == '__main__':
    message_to_events()
