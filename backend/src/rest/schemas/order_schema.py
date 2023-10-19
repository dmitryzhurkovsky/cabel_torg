from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, EmailStr

from src.models.order_model import OrderStatus
from src.rest.schemas.base_schema import BaseSchema
from src.rest.schemas.product_schema import ProductSchema


class OrderBaseSchema(BaseModel):
    # requisites
    promo_code: str | None = None
    company_name: str | None = None
    unp: str | None = None
    legal_address: str | None = None
    IBAN: str | None = None
    BIC: str | None = None
    serving_bank: str | None = None

    # contact information
    full_name: str | None = None
    phone_number: str | None = None
    email: EmailStr | None = None

    # delivery information
    city: str | None = None
    street: str | None = None
    house: str | None = None
    flat: str | None = None
    delivery_type_id: int | None = None
    # todo check delivery_type_id


class ProductOrderSchema(BaseModel):
    product: ProductSchema
    amount: int

    class Config:
        from_attributes = True


class OrderSchema(OrderBaseSchema, BaseSchema):
    user_id: int
    status: OrderStatus | None = None
    products: list[ProductOrderSchema] | None = None
    number: int | None = None

    created_at: datetime
    total_price: Decimal

    class Config:
        from_attributes = True


class ProductOrderInputSchema(BaseModel):
    id: int
    amount: int


class OrderCreateInputSchema(OrderBaseSchema):
    products: list['ProductOrderInputSchema']
    delivery_type_id: int


class OrderUpdateInputSchema(OrderBaseSchema):
    products: list['ProductOrderInputSchema'] | None = None
    status: OrderStatus | None = None
