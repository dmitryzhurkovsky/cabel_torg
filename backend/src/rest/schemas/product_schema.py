from decimal import Decimal
from typing import List

from pydantic import BaseModel

from src.rest.schemas.attribute_schema import AttributeSchema
from src.rest.schemas.base_schema import BaseSchema
from src.rest.schemas.base_unit_schema import BaseUnitSchema
from src.rest.schemas.category_schema import CategorySchema
from src.rest.schemas.manufacturer_schema import ManufacturerSchema


class ProductSchema(BaseSchema):
    vendor_code: str | None
    name: str
    category: CategorySchema | None
    images: str | None
    manufacturer: ManufacturerSchema | None
    tax: int | None
    description: str | None
    type: str | None
    base_unit: BaseUnitSchema | None
    attributes: List['AttributeSchema'] | list
    price: Decimal | None

    class Config:
        orm_mode = True


class ProductInCartSchema(BaseSchema):
    vendor_code: str | None
    name: str

    class Config:
        orm_mode = True


class ProductInWatchListSchema(BaseSchema):
    vendor_code: str | None
    name: str

    class Config:
        orm_mode = True


class PaginatedProductSchema(BaseModel):
    limit: int
    offset: int
    total: int

    data: List['ProductSchema']
