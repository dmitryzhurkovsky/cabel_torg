from pydantic import BaseModel, validator

from src.core.exception.base_exception import BadRequestError
from src.rest.schemas.base_schema import BaseSchema


class QuickCategoryCreateSchema(BaseModel):
    categories: list[int]

    @validator('categories')
    def length_of_categories_lte_5_and_gte_1(cls, v):
        if len(v) != 4:
            raise BadRequestError(detail='You can set only 4 categories as quick categories.')
        return v


class CategoryUpdateSchema(BaseModel):
    discount: int


class CategorySchema(BaseSchema):
    name: str
    parent_category_id: int | None = None
    order: int | None = None
    discount: int | None = None

    site_link: str | None = None
    site_page_title: str | None = None
    site_page_description: str | None = None
    site_page_seo_description: str | None = None

    class Config:
        from_attributes = True
