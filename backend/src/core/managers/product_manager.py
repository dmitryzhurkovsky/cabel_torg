from src.core.db.mixins.list_mixin import ListMixin
from src.core.db.mixins.retrieve_mixin import RetrieveMixin
from src.models.product_models import Product


class ProductManager(ListMixin, RetrieveMixin):

    table = Product
