from pydantic import BaseModel

from src.rest.schemas.base_schema import BaseSchema


class AddressInputSchema(BaseModel):
    title: str | None
    payload: str | None
    vendor_info_id: int


class AddressSchema(AddressInputSchema, BaseSchema):
    class Config:
        orm_mode = True


class VendorInfoInputSchema(BaseModel):
    phone: str | None
    email: str | None

    director_fullname: str | None

    unp: str | None
    OKPO: str | None
    legal_address: str | None
    postal_address: str | None
    phone_and_fax: str | None

    serving_bank: str | None
    serving_bank_short: str | None
    IBAN: str | None
    RUR: str | None

    instagram_url: str | None
    facebook_url: str | None
    vk_url: str | None
    telegram_url: str | None
    twitter_url: str | None
    tiktok_url: str | None
    youtube_url: str | None


class VendorInfoSchema(VendorInfoInputSchema, BaseSchema):
    addresses: list['AddressSchema'] | None

    class Config:
        orm_mode = True
