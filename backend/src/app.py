import asyncio
import logging

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.cors import CORSMiddleware

from src.core import settings
from src.core.db.db import engine
from src.parser.xml_bookkeeping_parser import (
    XMLParser,
    PricesParser
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

from src.core.error_handlers import *  # noqa


@app.on_event("startup")
async def startup():
    if settings.BOOKKEEPING_SHOULD_BE_PARSED:
        event_loop = asyncio.get_running_loop()

        async with AsyncSession(engine) as db:
            xml_parser = XMLParser(db=db)
            price_parser = PricesParser(db=db)

            await asyncio.wait([event_loop.create_task(xml_parser.parse_categories())])
            await asyncio.wait([event_loop.create_task(xml_parser.parse_attributes())])

            await event_loop.create_task(xml_parser.parse_products())
            await event_loop.create_task(price_parser.parse_prices())
            logger.info("Parsing a file with products has been finished.")


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, log_level="debug", reload=True)
