import json
from sqlalchemy.orm import Session
from store_mq.database import mq_engine
from store_mq.models import EventType, Event, Message

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
        new_message = Message(
            message=json.dumps(message_data)
        )
        session.add(new_message)
        order_type = str(session.query(EventType).filter_by(type=type_event).first().id)
        new_event = Event(type=order_type, message_id=new_message.id)
        session.add(new_event)
        session.flush()
        session.commit()

if __name__ == '__main__':
    create_events('ORDER_CREATED', CREATED_MESSAGE)
    create_events('ORDER_UPDATED', UPDATED_MESSAGE)



