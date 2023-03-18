from pydantic import BaseModel, ValidationError, validator

from src.models.service_entities.request_call_model import RequestCallType
from src.rest.schemas.base_schema import BaseSchema
from src.rest.schemas.product_schema import ProductRequestCallSchema


class RequestCallInputSchema(BaseModel):
    fullname: str
    phone_number: str
    product_id: int | None
    type: RequestCallType | None

    @validator('product_id')
    def product_id_is_required_for_goods_receipt(cls, v):
        if not v and v == RequestCallType.GOODS_RECEIPT.value:
            raise ValidationError(f'product_id is required if type is {RequestCallType.GOODS_RECEIPT.value}')

        return v


class RequestCallSchema(RequestCallInputSchema, BaseSchema):
    product: ProductRequestCallSchema | None

    class Config:
        orm_mode = True
