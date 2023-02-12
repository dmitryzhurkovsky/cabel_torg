from abc import ABC
from decimal import Decimal

from src.models import Product
from src.models.product_models import ProductStatus
from src.parser.mixins.base_mixin import BaseMixin
from src.parser.servers import database_service


class OfferMixin(BaseMixin, ABC):
    async def parse_offers(self):
        """Parse "Предложения" node and write then to a database."""
        offers = self.root_element[1][7]

        for offer in offers:
            product_bookkeeping_id = offer[0].text
            product_price = Decimal(offer[4][0][2].text).quantize(Decimal('1.00'))
            product_count = int(offer[5].text) if offer[5].text else 0

            product_db = await database_service.get_object(
                db=self.db, model=Product,
                fields={'bookkeeping_id': product_bookkeeping_id},
                prefetch_fields=(Product.attributes,)
            )

            product_db.price = product_price
            product_db.count = product_count
            if product_count > 0:
                product_db.status = ProductStatus.AVAILABLE.value
            elif product_count <= 0 and product_db.status != ProductStatus.ON_THE_WAY_TO_THE_WAREHOUSE:
                # We set up status of a product to ON_THE_WAY_TO_THE_WAREHOUSE during parsing products.
                product_db.status = ProductStatus.OUT_OF_STOCK.value

        await self.db.commit()
