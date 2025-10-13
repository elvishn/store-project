from __future__ import annotations
from uuid import UUID
from sqlalchemy.orm import Session
from order_service.models.models import Order, Product, Status, StatusType

def get_orders(db: Session): #все заказы
    orders = db.query(Order).all()
    return orders

def get_order_by_user_id(db: Session, user_id: UUID): #заказ для пользователя по id
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return orders

def get_order_by_id(db: Session, order_id: UUID): #Заказы по id заказа
    orders = db.query(Order).filter(Order.id == order_id).first()
    return orders

def get_product_id(db: Session, product_id: UUID): #продукты для заказа по id
    products = db.query(Product).filter(Product.id == product_id).all()
    return products

def get_product_by_order(db: Session, user_id: UUID): #продукты для заказа по id пользователя
    products = db.query(Product)\
        .filter(Product.order.has(user_id=user_id))\
        .all()
    return products

def get_orders_by_status(db: Session, status_type: StatusType): #заказы по статусу
    status = db.query(Status).filter(Status.type == status_type.value).first()
    orders = db.query(Order).filter(Order.status_id == status.id).all()
    return orders
