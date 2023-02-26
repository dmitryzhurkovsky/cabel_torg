from pydantic import BaseModel, EmailStr

from src.rest.schemas.base_schema import BaseSchema


class FeedbackInputSchema(BaseModel):
    fullname: str
    email: EmailStr
    phone_number: str
    message: str


class FeedbackSchema(FeedbackInputSchema, BaseSchema):
    class Config:
        orm_mode = True
