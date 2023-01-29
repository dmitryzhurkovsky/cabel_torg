from pydantic import BaseModel

from src.rest.schemas.base_schema import BaseSchema


class ArticleInputSchema(BaseModel):
    title: str
    content: str


class ArticleSchema(ArticleInputSchema, BaseSchema):
    class Config:
        orm_mode = True
