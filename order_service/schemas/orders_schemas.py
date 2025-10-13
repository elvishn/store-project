from uuid import UUID
from pydantic import BaseModel, UUID4
from typing import Optional
from order_service.models.models import StatusType

class StatusCreateRequest(BaseModel):
    type: StatusType

    class Config:
        from_attributes = True

class StatusResponse(BaseModel):
    id: UUID4
    type: StatusType

    class Config:
        from_attributes = True

class ProductCreateRequest(BaseModel):
    order_id: UUID4

    class Config:
        from_attributes = True

class ProductUpdateRequest(BaseModel):
    order_id: Optional[UUID4] = None

    class Config:
        from_attributes = True

class ProductResponse(BaseModel):
    id: UUID4
    order_id: UUID4

    class Config:
        from_attributes = True
class OrderCreateRequest(BaseModel):
    user_id: UUID
    status_id: UUID

    class Config:
        from_attributes = True
class OrderUpdateRequest(BaseModel):
    user_id: Optional[UUID4] = None
    order_id: Optional[UUID4] = None

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: UUID4
    user_id: UUID4
    status_id: UUID4
    created_at: int
    updated_at: int

    class Config:
        from_attributes = True

