from pydantic import BaseModel, validator

from src.rest.schemas.base_schema import BaseSchema


class AddressInputSchema(BaseModel):
    title: str | None = None
    payload: str | None = None
    vendor_info_id: int | None = 1

    @validator('vendor_info_id')
    def product_id_is_required_for_goods_receipt(cls, v):
        return 1


class AddressSchema(AddressInputSchema, BaseSchema):
    class Config:
        from_attributes = True


class VendorInfoInputSchema(BaseModel):
    phone: str | None = None
    email: str | None = None
    logo: str | None = None
    price_document: str | None = None

    director_fullname: str | None = None

    unp: str | None = None
    OKPO: str | None = None
    legal_address: str | None = None
    postal_address: str | None = None
    phone_and_fax: str | None = None

    serving_bank: str | None = None
    serving_bank_short: str | None = None
    IBAN: str | None = None
    RUR: str | None = None

    instagram_url: str | None = None
    facebook_url: str | None = None
    vk_url: str | None = None
    telegram_url: str | None = None
    twitter_url: str | None = None
    tiktok_url: str | None = None
    youtube_url: str | None = None


class VendorInfoSchema(VendorInfoInputSchema, BaseSchema):
    addresses: list['AddressSchema'] | None = None

    class Config:
        from_attributes = True
