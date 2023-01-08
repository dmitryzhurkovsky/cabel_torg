from src.core.db.mixins.create_mixin import CreateMixin
from src.core.db.mixins.delete_mixin import DeleteMixin
from src.core.db.mixins.list_mixin import ListMixin
from src.core.db.mixins.update_mixin import UpdateMixin
from src.models.cart_model import Cart
from src.rest.schemas.cart_schema import (
    CartCreateSchema,
    CartSchema
)


class CartManager(
    CreateMixin,
    DeleteMixin,
    UpdateMixin,
    ListMixin
):
    table = Cart
    update_scheme = CartSchema
    create_scheme = CartCreateSchema
