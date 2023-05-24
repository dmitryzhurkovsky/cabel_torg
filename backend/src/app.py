import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware

from src.core import settings
from src.core.backends import BearerTokenAuthBackend
from src.rest.api.router import base_router

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(base_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=("*",),
    allow_headers=settings.CORS_ALLOWED_HEADERS,
)
app.add_middleware(
    AuthenticationMiddleware,
    backend=BearerTokenAuthBackend()
)

from src.core.error_handlers import *  # noqa

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, log_level="debug", reload=True)
