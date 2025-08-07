from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, UUID, ForeignKey, TIMESTAMP, func, Integer
from sqlalchemy.orm import relationship

from src.order_service.models.database import Base


class Status(Base):
    __tablename__ = 'status'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    type = Column(String, nullable=False)

class Product(Base):
    __tablename__ = 'product'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("order.id"))
    order = relationship("Order", back_populates="products")

class Order(Base):
    __tablename__ = 'order'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True))
    status_id = Column(UUID(as_uuid=True), ForeignKey('status.id'))
    created_at = Column(Integer, default=lambda: int(datetime.now().timestamp()))
    updated_at = Column(Integer, onupdate=lambda: int(datetime.now().timestamp()))
    products = relationship('Product', back_populates="order")
    status = relationship('Status')



