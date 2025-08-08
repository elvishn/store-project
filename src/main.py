from src.order_service.models.database import create_tables
from src.order_service.models.init_data import init_statuses

from src.store_mq.database import create_tables_mq
from src.store_mq.init_data import init_mq_data

def deploy_db():
    create_tables()
    init_statuses()
    create_tables_mq()
    init_mq_data()

if __name__ == "__main__":
    deploy_db()
