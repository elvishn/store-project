from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, UUID, ForeignKey, TIMESTAMP, func, Integer
from sqlalchemy.orm import relationship
from .database import Base


class EventType(Base):
    __tablename__ = 'event_type'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    type = Column(String(50), nullable=False, unique=True)

class Event(Base):
    __tablename__ = 'event'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    type = Column(String, ForeignKey('event_type.id'))
    created_at = Column(Integer, default=lambda: int(datetime.now().timestamp()))
    messages = relationship("Message", back_populates="event")

class Offset(Base):
    __tablename__ = 'offset'
    client_name = Column(String, primary_key=True)
    offset = Column(UUID)

class Message(Base):
    __tablename__ = 'message'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    type_id = Column(UUID(as_uuid=True), ForeignKey("event.id"))
    message = Column(String)
    event = relationship("Event", back_populates="messages")


