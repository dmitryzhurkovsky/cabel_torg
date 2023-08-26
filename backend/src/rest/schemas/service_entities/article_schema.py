from datetime import datetime

from pydantic import BaseModel

from src.rest.schemas.base_schema import BaseSchema


class ArticleInputSchema(BaseModel):
    title: str
    content: str
    preview_text: str


class ArticleSchema(ArticleInputSchema, BaseSchema):
    image: str | None
    created_at: datetime | None

    class Config:
        from_attributes = True
