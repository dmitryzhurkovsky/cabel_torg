from pydantic import Field

from src.rest.schemas.base_schema import BaseSchema


class AttributeValueSchema(BaseSchema):
    id: int = Field(exclude=True)
    payload: str

    class Config:
        from_attributes = True


class AttributeNameSchema(BaseSchema):
    id: int = Field(exclude=True)
    payload: str

    class Config:
        from_attributes = True


class AttributeSchema(BaseSchema):
    id: int = Field(exclude=True)
    name: AttributeNameSchema
    value: AttributeValueSchema | None

    class Config:
        from_attributes = True
