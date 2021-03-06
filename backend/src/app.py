import asyncio

import uvicorn
from build.xml_bookkeeping_parser import XMLParser
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.cors import CORSMiddleware

from src.core import settings
from src.core.db.db import engine
from src.rest.api.router import base_router

app = FastAPI()
app.include_router(base_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=settings.CORS_ALLOWED_HEADERS,
)


from src.core.error_handlers import *  # noqa


@app.on_event("startup")
async def startup():
    event_loop = asyncio.get_running_loop()

    async with AsyncSession(engine) as db:
        parser = XMLParser(db=db)

        await asyncio.wait([event_loop.create_task(parser.parse_categories())])

        await event_loop.create_task(parser.parse_goods())


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8001, log_level="debug", reload=True)
