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
        from_attributes = True


class ProductSchema(BaseSchema):
    vendor_code: str | None = None
    name: str
    images: str | None = None
    tax: int | None = None
    description: str | None = None
    status: ProductStatus | None = None
    document_url: str | None = None

    is_new: bool | None = False
    is_popular: bool | None = False

    # price: Decimal | None  # without a tax. Don't use this field. Use price_with_tax instead.
    # price_with_discount: Decimal | None  # without a tax. Don't use this field. Use price_with_discount_and_tax

    price_with_tax: Decimal | float | int | None = None  # with a tax
    price_with_discount_and_tax: Decimal | float | int | None = None  # with a tax
    discount: Decimal | float | int | None = None
    actual_discount: Decimal | float | int | None = None
    is_price_on_request: bool | None = None

    count: Decimal | float | int | None = None
    weight: Decimal | float | int | None = None

    site_link: str | None = None
    site_page_title: str | None = None
    site_page_description: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    category: CategorySchema | None = None
    manufacturer: ManufacturerSchema | None = None
    base_unit: BaseUnitSchema | None = None
    attributes: List['AttributeSchema'] | list

    class Config:
        from_attributes = True


class ProductUpdateSchema(BaseModel):
    discount: int


class PaginatedProductSchema(BaseModel):
    limit: int
    offset: int
    total: int

    data: List['ProductSchema']
