from typing import Optional

from src.rest.schemas.base_schema import BaseSchema
from src.rest.schemas.category_schema import CategorySchema
from src.rest.schemas.manufacturer_schema import ManufacturerSchema


class ProductSchema(BaseSchema):
    vendor_code: str | None
    name: str
    category: Optional[CategorySchema]
    image: str | None
    manufacturer: Optional[ManufacturerSchema]
    tax: int | None
    description: str | None
    type: str | None

    class Config:
        orm_mode = True
