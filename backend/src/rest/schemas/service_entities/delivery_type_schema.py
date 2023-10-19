from pydantic import BaseModel

from src.rest.schemas.base_schema import BaseSchema


class DeliveryTypeInputSchema(BaseModel):
    payload: str
    is_pickup: bool | None = None


class DeliveryTypeSchema(DeliveryTypeInputSchema, BaseSchema):
    class Config:
        from_attributes = True
