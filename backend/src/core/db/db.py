from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from src.core import settings

engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
