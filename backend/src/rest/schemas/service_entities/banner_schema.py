from pydantic import BaseModel

from src.rest.schemas.base_schema import BaseSchema


class BannerInputSchema(BaseModel):
    title: str | None = None
    subtitle: str | None = None
    text: str | None = None
    is_active: bool | None = None
    preview_text: str | None = None
    button_name: str | None = None
    button_link: str | None = None


class BannerSchema(BannerInputSchema, BaseSchema):
    image: str | None = None

    class Config:
        from_attributes = True
