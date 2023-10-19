from src.rest.schemas.base_schema import BaseSchema


class BaseUnitSchema(BaseSchema):
    code: str | None = None
    full_name: str | None = None
    international_abbreviated: str | None = None

    class Config:
        from_attributes = True
