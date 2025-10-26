from typing import Optional, Union
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from order_service.models.database import get_db
from order_service.repositories.order_repo import get_order_by_id, get_order_by_user_id, get_orders, get_all_users
from order_service.schemas import OrderResponse
from order_service.schemas.orders_schemas import UserResponse

order_router = APIRouter(prefix='/orders', tags=["orders"])
user_router = APIRouter(prefix='/users', tags=["users"])

@order_router.get("/",  response_model=Union[OrderResponse, list[OrderResponse]])
def read_orders_by_order_id(orderId: Optional[str] = None,
                            userId: Optional[str] = None,
                            db: Session = Depends(get_db)):
    if orderId is not None:
        try:
            orders = get_order_by_id(db, UUID(orderId))
            return orders
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="orderId parameter is required"
            )

    if userId is not None:
        try:
            orders = get_order_by_user_id(db, UUID(userId))
            return orders
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="orderId parameter is required"
            )

    return get_orders(db)

@user_router.get("/", response_model=list[UserResponse])
def read_all_users(db: Session = Depends(get_db)):
    return get_all_users(db)