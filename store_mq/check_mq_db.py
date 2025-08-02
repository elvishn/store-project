from sqlalchemy.orm import Session
from sqlalchemy import inspect
from store_mq.database import mq_engine, create_tables_mq
from store_mq.init_data import init_mq_data
from store_mq.models import EventType


def check_connection():
    try:
        with mq_engine.connect():
            print('Успешно подключенно к БД!')
    except Exception as e:
        print(f'Ошибка : {e}')
        return

def check_EventType():
    with Session(mq_engine) as session:
        events = session.query(EventType).all()
        if not events:
            print('Таблица пуста')
        for event in events:
            print(f'ID: {event.id}, type: {event.type}')

def check_db_structure():
    inspector = inspect(mq_engine)
    for table_name in inspector.get_table_names():
        print(f'\nТаблица: {table_name}')
        for col in inspector.get_columns(table_name):
            print(f' Поле: {col['name']}, ({col['type']})')

if __name__ == "__main__":
    check_connection()
    create_tables_mq()
    init_mq_data()
    check_EventType()
    check_db_structure()

