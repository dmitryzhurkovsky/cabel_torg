import asyncio

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.cors import CORSMiddleware

from build.xml_bookkeeping_parser import XMLParser
from src.core.db.db import init_db, engine
from src.rest.api.router import base_router

app = FastAPI()
app.include_router(base_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await init_db()

    event_loop = asyncio.get_running_loop()

    async with AsyncSession(engine) as db:
        parser = XMLParser(db=db)

        await asyncio.wait([event_loop.create_task(parser.parse_categories())])

        await event_loop.create_task(parser.parse_goods())


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8001, log_level="debug", reload=True)
