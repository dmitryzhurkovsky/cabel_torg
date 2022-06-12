from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    email: EmailStr | None
    full_name: str | None
    phone_number: str | None
    company_name: str | None
    unp: str | None
    legal_address: str | None
    IBAN: str | None
    BIC: str | None
    serving_bank: str | None


class UserCreateSchema(UserBaseSchema):
    email: str
    password: str


class UserUpdateSchema(UserBaseSchema):
    password: str | None


class UserInDBBaseSchema(UserBaseSchema):
    id: int | None

    class Config:
        orm_mode = True
