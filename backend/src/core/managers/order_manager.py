from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.core.db.mixins.base_mixin import CreateBaseSchema, TableType
from src.core.db.mixins.create_mixin import CreateMixin
from src.core.db.mixins.delete_mixin import DeleteMixin
from src.core.db.mixins.list_mixin import ListMixin
from src.core.db.mixins.update_mixin import UpdateMixin
from src.models.order_model import Order, ProductOrder


class OrderManager(
    CreateMixin,
    DeleteMixin,
    UpdateMixin,
    ListMixin
):
    table = Order

    @classmethod
    async def list(
            cls,
            session: AsyncSession,
            prefetch_fields: tuple = None,
            filter_fields: dict = {},  # noqa
            search_fields: tuple = (),
            order_fields: tuple = (),
            custom_options: tuple = (),
            offset: int = 0,
            limit: int = 100,
    ) -> list:
        """Get list of objects"""
        custom_options = (selectinload(Order.products).selectinload(ProductOrder.product),)
        return await super().list(
            session=session,
            prefetch_fields=prefetch_fields,
            filter_fields=filter_fields,
            search_fields=search_fields,
            order_fields=order_fields,
            custom_options=custom_options,
            offset=offset,
            limit=limit
        )

    @classmethod
    async def create(
            cls,
            input_data: CreateBaseSchema | dict,
            session: AsyncSession,
    ) -> TableType:
        products = input_data.pop('products')

        order = cls.table(  # noqa
            **(input_data if isinstance(input_data, dict) else input_data.__dict__)
        )
        session.add(order)
        await session.flush()

        products_db = [
            ProductOrder(order_id=order.id, product_id=product.id, amount=product.amount)
            for product in products
        ]
        session.add_all(products_db)
        await session.commit()
        await session.refresh(order)

        return order
