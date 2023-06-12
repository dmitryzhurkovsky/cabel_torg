from pydantic import BaseModel, EmailStr, validator

from src.rest.schemas.base_schema import BaseSchema


class UserBaseSchema(BaseModel):
    email: EmailStr | None
    password: str | None
    full_name: str | None
    phone_number: str | None
    company_name: str | None
    unp: str | None
    legal_address: str | None
    delivery_address: str | None
    IBAN: str | None
    BIC: str | None
    serving_bank: str | None
    is_admin: bool | None = False

    @validator('email')
    def transform_to_lowercase(cls, v: str):
        return v.lower()


class UserCreateSchema(UserBaseSchema):
    email: EmailStr
    password: str
    full_name: str
    phone_number: str
    company_name: str
    unp: str


class UserInputCreateSchema(UserCreateSchema):
    isGenerated: bool | None = False


class UserUpdateSchema(UserBaseSchema):
    pass


class UserSchema(UserBaseSchema, BaseSchema):
    class Config:
        orm_mode = True

        fields = {'password': {'exclude': True}}


class RecoveryPasswordSchema(BaseModel):
    email: EmailStr
