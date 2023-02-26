from pydantic import BaseModel

from src.models.service_entities.request_call_model import RequestCallType
from src.rest.schemas.base_schema import BaseSchema


class RequestCallInputSchema(BaseModel):
    fullname: str
    phone_number: str
    type: RequestCallType | None


class RequestCallSchema(RequestCallInputSchema, BaseSchema):
    class Config:
        orm_mode = True
