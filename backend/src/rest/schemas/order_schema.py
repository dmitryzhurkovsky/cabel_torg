from datetime import datetime

from pydantic import BaseModel, EmailStr

from src.models.order_model import OrderStatus
from src.rest.schemas.base_schema import BaseSchema
from src.rest.schemas.product_schema import ProductSchema


class OrderBaseSchema(BaseModel):
    # requisites
    promo_code: str | None
    company_name: str | None
    unp: str | None
    legal_address: str | None
    IBAN: str | None
    BIC: str | None
    serving_bank: str | None

    # contact information
    full_name: str | None
    phone_number: str | None
    email: EmailStr | None

    # delivery information
    city: str | None
    address: str | None
    house: str | None
    flat: str | None
    delivery_type_id: int | None
    # todo check delivery_type_id


class ProductOrderSchema(BaseModel):
    product: ProductSchema
    amount: int

    class Config:
        orm_mode = True


class OrderSchema(OrderBaseSchema, BaseSchema):
    user_id: int
    status: OrderStatus | None
    products: list[ProductOrderSchema] | None
    number: int | None

    created_at: datetime

    class Config:
        orm_mode = True


class ProductOrderInputSchema(BaseModel):
    id: int
    amount: int


class OrderCreateInputSchema(OrderBaseSchema):
    products: list['ProductOrderInputSchema']
    delivery_type_id: int


class OrderUpdateInputSchema(OrderBaseSchema):
    products: list['ProductOrderInputSchema'] | None
    status: OrderStatus | None
