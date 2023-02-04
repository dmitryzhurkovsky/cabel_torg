from abc import ABC
from decimal import Decimal

from src.models import Product
from src.parser import database_services
from src.parser.mixins.base_mixin import BaseMixin


class PriceMixin(BaseMixin, ABC):
    async def parse_prices(self):
        """Parse "Предложения" node and write then to a database."""
        prices = self.root_element[1][7]

        for price in prices:
            product_bookkeeping_id = price[0].text
            product_price = Decimal(price[4][0][2].text)

            product_db = await database_services.get_object(
                db=self.db, model=Product,
                fields={'bookkeeping_id': product_bookkeeping_id},
                prefetch_fields=(Product.attributes,)
            )
            product_db.price = product_price

        await self.db.commit()
