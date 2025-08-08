from sqlalchemy import inspect
from sqlalchemy.orm import Session
from src.order_service.models.init_data import init_statuses
from database import engine, Base, create_tables
from src.order_service.models.models import Status


def database_connection():
    with engine.connect():
        print('Усешно подключенно к БД')

def check_statuses():
    with Session(engine) as session:
        statuses = session.query(Status).all()
        if not statuses:
            print('Таблица пуста')
        for status in statuses:
            print(f'ID: {status.id}, Type: {status.type}')

def check_db_structure():
    inspector = inspect(engine)
    for table_name in inspector.get_table_names():
        print(f'\nТаблица: {table_name}')
        for col in inspector.get_columns(table_name):
            print(f' Поле: {col['name']}, type({col['type']})')


if __name__ == '__main__':
    database_connection()
    create_tables()
    init_statuses()
    check_statuses()
    check_db_structure()
