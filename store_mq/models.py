from datetime import datetime
from enum import Enum
from uuid import uuid4
from sqlalchemy import Column, String, UUID, ForeignKey, TIMESTAMP, func, Integer
from sqlalchemy.orm import relationship
from .database import Base

class EventType(Base):
    __tablename__ = 'event_type'
    __table_args__ = {'extend_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    type = Column(String(50), nullable=False, unique=True)

class DefaultType(Enum):
    ORDER_CREATED = "ORDER_CREATED"
    ORDER_UPDATED = "ORDER_UPDATED"


class Event(Base):
    __tablename__ = 'event'
    __table_args__ = {'extend_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    type = Column(String, ForeignKey('event_type.id'))
    created_at = Column(Integer, default=lambda: int(datetime.now().timestamp()))
    message_id = Column(UUID(as_uuid=True), ForeignKey('message.id'))

    message = relationship("Message", back_populates="events")

class Offset(Base):
    __tablename__ = 'offset'
    __table_args__ = {'extend_existing': True}
    client_name = Column(String, primary_key=True)
    offset = Column(UUID)

class Message(Base):
    __tablename__ = 'message'
    __table_args__ = {'extend_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    message = Column(String)

    events = relationship("Event", back_populates="message")


