from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.managers.product_manager import ProductManager
from src.rest.schemas.product_schema import ProductSchema

product_router = APIRouter(tags=['products'])


@product_router.get('/products/', response_model=list[ProductSchema])
async def get_products(session: AsyncSession = Depends(get_session)):
    products = await ProductManager.list(
        session=session,
        prefetch_fields=(
            ProductManager.table.manufacturer,
            ProductManager.table.category
        )
    )

    return products


@product_router.get('/products/{product_id}', response_model=ProductSchema)
async def get_product(product_id: int, session: AsyncSession = Depends(get_session)):
    product = await ProductManager.retrieve(
        id=product_id,
        session=session,
        prefetch_fields=(
            ProductManager.table.manufacturer,
            ProductManager.table.category
        )
    )

    return product
