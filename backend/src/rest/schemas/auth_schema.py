from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

auth_schema = OAuth2PasswordBearer(
    tokenUrl='token',
)


class AuthenticationResponseSchema(BaseModel):
    access_token: str
    refresh_token: str


class UpdateRefreshTokenSchema(BaseModel):
    refresh_token: str
