from datetime import datetime
from uuid import UUID
from sqlalchemy.orm import Session
from src.order_service.models.database import engine
import random
from src.order_service.models.models import Order, Product, Status

def print_answer(model, lst):
    columns = model.__table__.columns.keys()
    if not lst:
        print('None')
    for event in lst:
        print()
        for column in columns:
            value = getattr(event, column)
            print(f"{column}: {value}")

def order_user_id(): #заказ для пользователя по id
    with Session(engine) as session:
        user_ids = [user_id for (user_id,) in session.query(Order.user_id).distinct().all()]
        rand_id = random.choice(user_ids)
        orders = session.query(Order).filter(Order.user_id == rand_id).all()
        print_answer(Order, orders)

def product_id(): #продукты для заказа по id
    with Session(engine) as session:
        product_ids = [product_id for (product_id,) in session.query(Product.id).distinct().all()]
        rand_id = random.choice(product_ids)
        products = session.query(Product).filter(Product.id == rand_id).all()
        print(rand_id)
        print_answer(Product, products)

def product_by_order(): #продукты для заказа по id пользователя
    with Session(engine) as session:
        user_ids = [user_id for (user_id,) in session.query(Order.user_id).distinct().all()]
        rand_id = random.choice(user_ids)
        products = session.query(Product)\
        .filter(Product.order.has(user_id=rand_id))\
        .all()
        print_answer(Product, products)

def clossed_order(): #закрытые заказы
    with Session(engine) as session:
        closed_status = session.query(Status).filter(Status.type == 'CLOSED').first().id
        orders = session.query(Order).filter(Order.status_id == closed_status).all()
        print_answer(Order, orders)

def clossed_order_for_user(): #закрытые заказы для пользователя по id за 2024 год
    with Session(engine) as session:
        user_ids = [user_id for (user_id,) in session.query(Order.user_id).distinct().all()]
        rand_id = random.choice(user_ids)
        closed_status = session.query(Status).filter(Status.type == 'CLOSED').first().id
        start_2024 = int(datetime(2024, 1, 1).timestamp())
        end_2024 = int(datetime(2025, 1, 1).timestamp()) #есть только 1 закрытый заказ за 2024 год
        orders = session.query(Order).filter(
            Order.user_id == rand_id,
            Order.status_id == closed_status,
            Order.created_at >= start_2024,
            Order.created_at < end_2024
        ).all()
        print_answer(Order, orders)
clossed_order_for_user()
