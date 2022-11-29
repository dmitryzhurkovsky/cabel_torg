import asyncio
from asyncio import AbstractEventLoop
from typing import Generator, AsyncGenerator, Any

import pytest
import pytest_asyncio
from faker import Faker
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.app import app
from src.core.db.db import Base, engine, async_session
from src.core.managers.category_manager import CategoryManager
from src.core.managers.product_manager import ProductManager
from src.core.managers.user_manager import UserManager
from src.models import User, Product, Manufacturer, Category
from src.services.auth_service import AuthService

faker = Faker()


@pytest.fixture(scope='session')
def event_loop() -> AbstractEventLoop:
    """
    This should be here to escape the following exception:
    ScopeMismatch: You tried to access the function scoped fixture event_loop with a session scoped request object,
    involved factories:
    def session() -> sqlalchemy.ext.asyncio.session.AsyncSession
    """
    return asyncio.get_event_loop()


@pytest.fixture(scope='session')
async def session() -> AsyncSession:
    """A fixture that gives a session."""
    async with async_session() as sess:
        yield sess


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url=f"https:///api/v1") as client:
        yield client


@pytest_asyncio.fixture
async def patched_client(test_user):
    """The same as usual client but with user and bearer token."""
    async with AsyncClient(app=app, base_url=f"https:///api/v1") as client:
        token = await AuthService.create_token(user_id=test_user.id, token_type="access")
        client.headers["Authorization"] = f"Bearer {token}"
        client.user = test_user
        yield client




@pytest.fixture
def fake_user_data() -> dict:
    """Generate fake data for User."""
    return {
        # "id": 9999,
        "email": faker.email(),
        "password": faker.password(),
        "full_name": faker.first_name() + faker.last_name(),
        "phone_number": faker.phone_number(),
        "company_name": faker.company(),
        "unp": faker.pystr(),
        "legal_address": faker.address(),
        "IBAN": faker.iban(),
        "BIC": faker.pystr(),
        "serving_bank": faker.company(),
        "is_active": faker.boolean(),
        "is_admin": faker.boolean(),
    }


@pytest.fixture
def fake_product_data() -> dict:
    """Generate fake data for Product."""
    return {
        "vendor_code": faker.zipcode(),
        "name": faker.name(),
        "base_unit": faker.pystr(),
        "image_path": faker.file_path(),
        "tax": faker.pyint(),
        "description": faker.text(),
        "price": faker.pyfloat(),
    }


@pytest.fixture
def fake_category_data() -> dict:
    """Generate fake data for Category."""
    return {
        "name": faker.name()
    }


@pytest.fixture
async def test_user(
        session: AsyncSession,
        fake_user_data: dict,
) -> AsyncGenerator[User, None]:
    """Generate test user and after finished of the test delete him."""
    user = User(**fake_user_data)

    session.add(user)
    await session.commit()

    yield user

    await UserManager.delete(id=user.id, session=session)


@pytest.fixture
async def test_product(
        session: AsyncSession,
        fake_product_data: dict,
) -> AsyncGenerator[Product, None]:
    """Generate test product and after executing of test delete him."""
    product = Product(**fake_product_data)

    session.add(product)
    await session.commit()

    yield product

    await ProductManager.delete(id=product.id, session=session)


@pytest.fixture
async def test_category(
        session: AsyncSession,
        fake_category_data: dict,
) -> AsyncGenerator[Category, None]:
    """Generate test category and after executing of test delete him."""
    category = Category(**fake_category_data)

    session.add(category)
    await session.commit()

    yield category

    await CategoryManager.delete(id=category.id, session=session)
