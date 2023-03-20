from pydantic import BaseModel

from src.rest.schemas.base_schema import BaseSchema


class BannerInputSchema(BaseModel):
    title: str | None
    subtitle: str | None
    text: str | None
    is_active: bool | None


class BannerSchema(BannerInputSchema, BaseSchema):
    image: str | None
    preview_text: str

    class Config:
        orm_mode = True
