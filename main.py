import sys
from contextlib import asynccontextmanager
from uuid import UUID
import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from order_service.models.database import create_tables, get_db
from order_service.models.init_data import init_statuses
from order_service.models.models import Order
from order_service.routing.endpoints import order_router
from store_mq.database import create_tables_mq
from store_mq.init_data import init_mq_data
from fastapi import FastAPI, Depends
import os
from typing import Optional
from sqlalchemy.orm import Session

from store_mq.job import check_events

scheduler = BackgroundScheduler()
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    create_tables_mq()
    init_statuses()
    init_mq_data()
    scheduler.add_job(check_events,
                      trigger=IntervalTrigger(seconds=5),
                      id="check_events_job",
                      name="Check for new events every 5 seconds",
                      replace_existing=True)
    scheduler.start()
    print('Начало')
    yield
    scheduler.shutdown()
    print('Конец')
app = FastAPI(lifespan=lifespan)
app.include_router(order_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000) #Запуск веб-сервера
