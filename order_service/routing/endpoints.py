from typing import Optional, Union
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from order_service.models.database import get_db
from order_service.repositories.order_repo import get_order_by_id, get_order_by_user_id, get_orders
from order_service.schemas import OrderResponse

order_router = APIRouter(prefix='/orders', tags=["orders"])

@order_router.get("/",  response_model=Union[OrderResponse, list[OrderResponse]])
def read_orders_by_order_id(order_id: Optional[str] = None,
                            db: Session = Depends(get_db)):
    if order_id is None:
        return get_orders(db)
    orders = get_order_by_id(db, UUID(order_id))
    return orders

@order_router.get("/users", response_model=list[OrderResponse])
def read_orders_by_user_id(user_id: Optional[str] = None,
                        db: Session = Depends(get_db)):
    if user_id is None:
        return get_orders(db)
    orders = get_order_by_user_id(db, UUID(user_id))
    return orders



