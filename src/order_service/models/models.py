from uuid import uuid4

from sqlalchemy import Column, String, UUID, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .database import Base

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
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    products = relationship('Product', back_populates="order")
    status = relationship('Status')


