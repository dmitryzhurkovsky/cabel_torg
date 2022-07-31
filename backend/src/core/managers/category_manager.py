from src.core.db.mixins.list_mixin import ListMixin
from src.core.db.mixins.retrieve_mixin import RetrieveMixin
from src.models.category_model import Category


class CategoryManager(ListMixin, RetrieveMixin):

    table = Category
