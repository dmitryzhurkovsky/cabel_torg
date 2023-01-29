from pydantic import BaseModel

from src.rest.schemas.base_schema import BaseSchema


class DeliveryTypeInputSchema(BaseModel):
    payload: str


class DeliveryTypeSchema(DeliveryTypeInputSchema, BaseSchema):
    class Config:
        orm_mode = True
