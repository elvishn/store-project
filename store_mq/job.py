from sqlalchemy.orm import Session
from store_mq.database import mq_engine
from store_mq.models import Event, Offset
import logging

logging.basicConfig(level=logging.DEBUG)

def check_events():
    with Session(mq_engine) as session:
        offset = session.query(Offset).first()
        if offset:
            stop_event = session.query(Event).filter(Event.id == offset.offset).first().created_at
            new_events = session.query(Event).filter(Event.created_at >= stop_event).all()
            logging.debug('NEW EVENTS:' + str(len(new_events)))
            if new_events:
                offset.offset = new_events[-1].id
                session.commit()
        else:
            events = session.query(Event).all()
            if events:
                last_offset = Offset(client_name='order_service',
                                     offset=events[-1].id)
                session.add(last_offset)
                session.commit()
