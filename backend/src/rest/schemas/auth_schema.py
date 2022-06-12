from pydantic import BaseModel


class RefreshTokenBaseSchema(BaseModel):
    refresh_token: str


class AccessTokenBaseSchema(BaseModel):
    access_token: str


class AuthenticationResponseSchema(BaseModel):
    access_token: str
    refresh_token: str


class RefreshTokenCreateSchema(BaseModel):
    owner_id: int
    refresh_token: str



