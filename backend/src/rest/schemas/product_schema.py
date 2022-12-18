from src.rest.schemas.base_schema import BaseSchema
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

    class Config:
        orm_mode = True
