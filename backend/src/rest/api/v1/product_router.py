from decimal import Decimal

from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.enums import ProductTypeFilterEnum, ProductOrderFilterEnum
from src.rest.managers.product_manager import ProductManager
from src.rest.permissions import is_admin_permission
from src.rest.schemas.product_schema import (
    ProductSchema,
    PaginatedProductSchema,
    ProductUpdateSchema
)

product_router = APIRouter(tags=['products'], prefix='/products')


@product_router.get(
    '/',
    response_model=PaginatedProductSchema,
)
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
        price_gte: Decimal | None = Query(default=None, description='Start value in range of price'),
        price_lte: Decimal | None = Query(default=None, description='End value in range of price'),
        type_of_product: ProductTypeFilterEnum | None = Query(
            default=None,
            description='The last parameter in the lef column/This parameter set that products will be downloaded'
        ),
        q: str | None = Query(
            default=None,
            description='Search by product\'s name, description, vendor code or category\'s name of products'
        ),
        ordering: ProductOrderFilterEnum = Query(default=None),
        offset: int = 0, limit: int = Query(default=12, lte=100),
        session: AsyncSession = Depends(get_session)
) -> PaginatedProductSchema:
    products = await ProductManager.filter_list(
        filters=request.query_params,
        session=session,
        offset=offset,
        limit=limit
    )
    count_of_products = await ProductManager.get_count_of_products(
        filters=request.query_params,
        session=session
    )

    return PaginatedProductSchema(
        data=products,
        limit=limit,
        offset=offset,
        total=count_of_products
    )  # todo it better


@product_router.get(
    '/{product_id:path}',
    response_model=ProductSchema,
)
async def get_product(product_id: int | str, session: AsyncSession = Depends(get_session)):
    return await ProductManager.retrieve(
        id=product_id,
        vendor_code=product_id,
        use_or_condition=True,
        session=session,
    )


@product_router.patch(
    '/{product_id}',
    response_model=ProductSchema,
    dependencies=[Depends(is_admin_permission)]
)
async def update_product(
        product_id: int,
        product_info: ProductUpdateSchema,
        session: AsyncSession = Depends(get_session)
):
    return await ProductManager.update_discount(
        pk=product_id,
        session=session,
        input_data=product_info
    )
