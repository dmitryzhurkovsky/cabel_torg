from typing import List

from src.rest.schemas.base_schema import BaseSchema


class CategoryWithNestedCategoriesSchema(BaseSchema):
    name: str
    parent_category_id: int | None
    subcategories: List['CategoryWithNestedCategoriesSchema']

    class Config:
        orm_mode = True


class CategorySchema(BaseSchema):
    name: str
    parent_category_id: int | None
    order: int | None

    class Config:
        orm_mode = True
