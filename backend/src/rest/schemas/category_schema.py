from typing import List

from src.rest.schemas.base_schema import BaseSchema


class CategoryWithNestedCategoriesSchema(BaseSchema):
    name: str
    subcategories: List['CategoryWithNestedCategoriesSchema']

    class Config:
        orm_mode = True


class CategorySchema(BaseSchema):
    name: str

    class Config:
        orm_mode = True
