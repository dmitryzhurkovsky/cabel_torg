from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

auth_schema = OAuth2PasswordBearer(
    tokenUrl='token',
)


class AuthenticationResponseSchema(BaseModel):
    access_token: str
