from pydantic import BaseModel

from src.rest.schemas.base_schema import BaseSchema


class PartnerInputSchema(BaseModel):
    image: str


class PartnerSchema(PartnerInputSchema, BaseSchema):
    class Config:
        orm_mode = True
