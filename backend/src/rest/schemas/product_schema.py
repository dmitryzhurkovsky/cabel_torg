from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel

from src.models.product_model import ProductStatus
from src.rest.schemas.attribute_schema import AttributeSchema
from src.rest.schemas.base_schema import BaseSchema
from src.rest.schemas.base_unit_schema import BaseUnitSchema
from src.rest.schemas.category_schema import CategorySchema
from src.rest.schemas.manufacturer_schema import ManufacturerSchema


class ProductRequestCallSchema(BaseSchema):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductSchema(BaseSchema):
    vendor_code: str | None
    name: str
    images: str | None
    tax: int | None
    description: str | None
    status: ProductStatus | None

    price: Decimal | None
    discount: int | None
    price_with_discount: Decimal | None
    count: int | None
    weight: Decimal | None

    created_at: datetime | None
    updated_at: datetime | None

    category: CategorySchema | None
    manufacturer: ManufacturerSchema | None
    base_unit: BaseUnitSchema | None
    attributes: List['AttributeSchema'] | list

    class Config:
        orm_mode = True


class ProductUpdateSchema(BaseModel):
    discount: int


class PaginatedProductSchema(BaseModel):
    limit: int
    offset: int
    total: int

    data: List['ProductSchema']
