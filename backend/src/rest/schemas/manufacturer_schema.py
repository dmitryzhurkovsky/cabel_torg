from src.rest.schemas.base_schema import BaseSchema


class ManufacturerSchema(BaseSchema):
    name: str

    class Config:
        from_attributes = True
