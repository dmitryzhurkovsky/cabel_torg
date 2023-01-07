from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.enums import ProductTypeFilter
from src.core.managers.product_manager import ProductManager
from src.rest.schemas.product_schema import ProductSchema

product_router = APIRouter(tags=['products'])


@product_router.get('/products', response_model=list[ProductSchema])
async def get_products(
        request: Request,
        category_id: int | None = Query(None, description=(
                '1 Type of equipment(The first filter in the left column), '
                '2 Category(The second filter in the left column) '
                '3 Subcategory(The filter above products) are the same model. '
                'For correct filtering it\'s required pass the follow the sequence. '
                'Explanation: If user choose "Category" and them "Subcategory" endpoint expects '
                'to get a "subcategory" instead of a category'
        )),
        price_gte: int | None = Query(default=None, description='Start value in range of price'),
        price_lte: int | None = Query(default=None, description='End value in range of price'),
        type_of_product: ProductTypeFilter = Query(
            default=ProductTypeFilter.ALL.value,
            description='The last parameter in the lef column/This parameter set that products will be downloaded'
        ),
        q: str | None = Query(default=None, description='Search by name of products'),
        offset: int = 0, limit: int = Query(default=12, lte=100),
        session: AsyncSession = Depends(get_session)
):
    return await ProductManager.filter_list(
        filter_fields=request.query_params,
        session=session,
        prefetch_fields=(
            ProductManager.table.manufacturer,
            ProductManager.table.category,
            ProductManager.table.attributes,
        ),
        offset=offset,
        limit=limit
    )


@product_router.get('/products/{product_id}', response_model=ProductSchema)
async def get_product(product_id: int, session: AsyncSession = Depends(get_session)):
    return await ProductManager.retrieve(
        id=product_id,
        session=session,
        prefetch_fields=(
            ProductManager.table.manufacturer,
            ProductManager.table.category,
            ProductManager.table.attributes,
        )
    )
