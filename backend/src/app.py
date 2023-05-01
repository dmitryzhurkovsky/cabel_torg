import asyncio
import logging
import time

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware

from src.core import settings
from src.core.backends import BearerTokenAuthBackend
from src.core.db.db import engine
from src.parser.xml_bookkeeping_parser import (
    XMLParser,
    OffersParser
)
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


@app.on_event("startup")
async def startup():
    if settings.BOOKKEEPING_SHOULD_BE_PARSED:
        event_loop = asyncio.get_running_loop()

        async with AsyncSession(engine) as db:
            start_parsing = time.time()
            xml_parser = XMLParser(db=db)
            price_parser = OffersParser(db=db)

            await asyncio.wait([event_loop.create_task(xml_parser.parse_categories())])
            await asyncio.wait([event_loop.create_task(xml_parser.parse_attributes())])

            await event_loop.create_task(xml_parser.parse_products())
            await event_loop.create_task(xml_parser.set_is_visible_attribute())
            await event_loop.create_task(price_parser.parse_offers())
            logger.info(f'Parsing has been finished. It took {time.time() - start_parsing}')


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, log_level="debug", reload=True)
