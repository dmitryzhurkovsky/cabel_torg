import json

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.managers.watch_list_manager import WatchListManager
from src.models import Product


async def test_add_to_watchlist(
        patched_client: AsyncClient,
        session: AsyncSession,
        test_product: Product
):
    response = await patched_client.post('/watch_lists', data=json.dumps({  # noqa
        "product_id": test_product.id
    }))
    assert response.status_code == status.HTTP_201_CREATED

    response = await patched_client.delete(f'/watch_lists/{test_product.id}')
    assert response.status_code == status.HTTP_204_NO_CONTENT
