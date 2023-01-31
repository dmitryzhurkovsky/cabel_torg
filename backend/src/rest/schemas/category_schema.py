from pydantic import BaseModel

from src.rest.schemas.base_schema import BaseSchema


class CategoryUpdateSchema(BaseModel):
    discount: int


class CategorySchema(BaseSchema):
    name: str
    parent_category_id: int | None
    order: int | None
    discount: int | None

    class Config:
        orm_mode = True
