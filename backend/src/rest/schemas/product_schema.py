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
    vendor_code: str | None
    name: str
    images: str | None
    tax: int | None
    description: str | None
    status: ProductStatus | None
    document_url: str | None

    is_new: bool | None
    is_popular: bool | None


    # price: Decimal | None  # without a tax. Don't use this field. Use price_with_tax instead.
    # price_with_discount: Decimal | None  # without a tax. Don't use this field. Use price_with_discount_and_tax

    price_with_tax: Decimal | None  # with a tax
    price_with_discount_and_tax: Decimal | None  # with a tax
    discount: int | None
    actual_discount: Decimal | None
    is_price_on_request: bool | None

    count: int | None
    weight: Decimal | None

    site_link: str | None
    site_page_title: str | None
    site_page_description: str | None
    created_at: datetime | None
    updated_at: datetime | None

    category: CategorySchema | None
    manufacturer: ManufacturerSchema | None
    base_unit: BaseUnitSchema | None
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
