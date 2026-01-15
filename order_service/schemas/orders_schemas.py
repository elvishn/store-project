from uuid import UUID
from pydantic import BaseModel, UUID4, Field, validator
from typing import Optional, Union
from order_service.models.models import StatusType

class StatusCreateRequest(BaseModel):
    type: StatusType

    class Config:
        from_attributes = True

class StatusResponse(BaseModel):
    id: UUID
    type: StatusType

    class Config:
        from_attributes = True

class ProductCreateRequest(BaseModel):
    order_id: UUID

    class Config:
        from_attributes = True

class ProductUpdateRequest(BaseModel):
    order_id: Optional[UUID] = None

    class Config:
        from_attributes = True

class ProductResponse(BaseModel):
    id: UUID
    order_id: UUID

    class Config:
        from_attributes = True

class UniversalOrderModel(BaseModel):
    id: Optional[Union[UUID, str]] = None
    user_id: Optional[Union[UUID, str]] = None
    status_id: Optional[Union[UUID, str]] = None
    created_at: Optional[Union[int, str]] = None
    updated_at: Optional[Union[int, str]] = None

    @validator('id', 'user_id', 'status_id', pre=True)
    def convert_to_uuid(cls, v):
        if v is None or v == '':
            return None
        try:
            return UUID(str(v))
        except (ValueError, AttributeError):
            return v

    @validator('created_at', 'updated_at', pre=True)
    def convert_to_int(cls, v):
        if v is None or v == '':
            return None
        try:
            return int(v)
        except (ValueError, AttributeError):
            return v

    class Config:
        extra = 'ignore'

class OrderCreateRequest(BaseModel):
    user_id: UUID
    status_id: UUID

    class Config:
        from_attributes = True
class OrderUpdateRequest(BaseModel):
    user_id: Optional[UUID] = None
    order_id: Optional[UUID] = None

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: UUID
    user_id: UUID
    status_id: UUID
    created_at: int
    updated_at: int

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    user_id: Optional[UUID] = None

    class Config:
        from_attributes = True