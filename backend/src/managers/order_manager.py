from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.core.db.mixins.base_mixin import CreateBaseSchema, TableType
from src.managers.base_manager import CRUDManager
from src.models.order_model import Order, ProductOrder


class OrderManager(CRUDManager):
    table = Order

    preloaded_fields = (
        selectinload(Order.products).selectinload(ProductOrder.product),
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

        # Add ProductOrder models
        products_db = [
            ProductOrder(order_id=order.id, product_id=product.id, amount=product.amount)
            for product in products
        ]
        session.add_all(products_db)

        await session.commit()
        await session.refresh(order)

        return order
