from src.rest.schemas.base_schema import BaseSchema


class BaseUnitSchema(BaseSchema):
    code: str | None
    full_name: str | None
    international_abbreviated: str | None

    class Config:
        from_attributes = True
