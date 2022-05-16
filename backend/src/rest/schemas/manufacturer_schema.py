from src.rest.schemas.base_schema import BaseSchema


class ManufacturerSchema(BaseSchema):
    name: str

    class Config:
        orm_mode = True
