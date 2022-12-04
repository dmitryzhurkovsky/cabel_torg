from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel


auth_schema = OAuth2PasswordBearer(
    tokenUrl='token',
)


class AuthenticationResponseSchema(BaseModel):
    access_token: str
    refresh_token: str


class RefreshTokenCreateSchema(BaseModel):
    owner_id: int
    refresh_token: str
