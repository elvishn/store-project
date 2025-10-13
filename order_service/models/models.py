from datetime import datetime
from enum import Enum
from uuid import uuid4
from sqlalchemy import Column, String, UUID, ForeignKey, TIMESTAMP, func, Integer
from sqlalchemy.orm import relationship
from order_service.models.database import Base


class Status(Base):
    __tablename__ = 'status'
    __table_args__ = {'extend_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    type = Column(String, nullable=False)

    def __str__(self):
        return self.type

class StatusType(Enum):
    PENDING = "PENDING"
    ASSEMBLING = "ASSEMBLING"
    DELIVERING = "DELIVERING"
    CLOSED = "CLOSED"

class Product(Base):
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("order.id"))
    order = relationship("Order", back_populates="products")

class Order(Base):
    __tablename__ = 'order'
    __table_args__ = {'extend_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True))
    status_id = Column(UUID(as_uuid=True), ForeignKey('status.id'))
    created_at = Column(Integer, default=lambda: int(datetime.now().timestamp()))
    updated_at = Column(Integer, onupdate=lambda: int(datetime.now().timestamp()))
    products = relationship('Product', back_populates="order")
    status = relationship('Status')



