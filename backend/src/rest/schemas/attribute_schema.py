from src.rest.schemas.base_schema import BaseSchema


class AttributeValueSchema(BaseSchema):
    payload: str

    class Config:
        orm_mode = True

        fields = {
            'id': {'exclude': True},
            'attribute': {'exclude': True}
        }


class AttributeNameSchema(BaseSchema):
    payload: str

    class Config:
        orm_mode = True

        fields = {
            'id': {'exclude': True},
            'attribute': {'exclude': True}
        }


class AttributeSchema(BaseSchema):
    value: AttributeValueSchema
    name: AttributeNameSchema

    class Config:
        orm_mode = True

        fields = {'id': {'exclude': True}}
