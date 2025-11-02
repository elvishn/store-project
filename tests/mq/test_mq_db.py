import unittest
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from store_mq.database import mq_engine, create_tables_mq
from store_mq.init_data import init_mq_data
from store_mq.models import EventType, Offset

class TestMq(unittest.TestCase):
    def test_connect(self):
        with mq_engine.connect() as connection:
            self.assertIsNotNone(connection, 'There is no connection to the database')

    def test_db_structure(self):
        inspector = inspect(mq_engine)
        tables = inspector.get_table_names()
        self.assertGreater(len(tables), 0, 'Database is empty')
        for table in tables:
            columns = inspector.get_columns(table)
            self.assertGreater(len(columns), 0, 'The table has no columns')

    def test_check_EventType(self):
        with Session(mq_engine) as session:
            events = session.query(EventType).all()
            self.assertGreater(len(events), 0, 'Table EventType is empty')

    def test_check_Offset(self):
        with Session(mq_engine) as session:
            offsets = session.query(Offset).all()
            self.assertGreater(len(offsets), 0, 'Table Offset is empty')

if __name__ == "__main__":
    create_tables_mq()
    init_mq_data()
    unittest.main()