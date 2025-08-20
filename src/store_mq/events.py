import json
from sqlalchemy.orm import Session
from src.store_mq.database import mq_engine
from src.store_mq.models import EventType, Event, Message

CREATED_MESSAGE = {
    "message_id" : "2102fb1a-2a61-4cd2-aeda-5439adedd809",
    "order_id" : "29beb177-edfa-42f4-9460-1e78e6d6b1b0",
    "created_at" : 1752421617
}

UPDATED_MESSAGE = {
    "message_id" : "0378337e-737c-4c45-a354-2e2c50100944",
    "order_id" : "29beb177-edfa-42f4-9460-1e78e6d6b1b0",
    "new_status" : "CLOSED",
    "created_at" : 1752421765
}

def create_events(type_event, message_data):
    with Session(mq_engine) as session:
        order_type = str(session.query(EventType).filter_by(type=type_event).first().id)
        new_event = Event(type=order_type)
        session.add(new_event)
        session.flush()

        new_message = Message(
            type_id=new_event.id,
            message=json.dumps(message_data)
        )
        session.add(new_message)
        session.commit()

def check_new_event(model):
    with Session(mq_engine) as session:
        events = session.query(model).all()
        if not events:
            print('Пусто')
            return

        columns = model.__table__.columns.keys()
        for event in events:
            print()
            for column in columns:
                value = getattr(event, column)
                print(f"{column}: {value}")

if __name__ == '__main__':
    check_new_event(Event)
    check_new_event(Message)
    create_events('ORDER_CREATED', CREATED_MESSAGE)
    create_events('ORDER_UPDATED', UPDATED_MESSAGE)
    check_new_event(Event)
    check_new_event(Message)
