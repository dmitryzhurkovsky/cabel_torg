from src.core.db.mixins.create_mixin import CreateMixin
from src.core.db.mixins.delete_mixin import DeleteMixin
from src.core.db.mixins.list_mixin import ListMixin
from src.core.db.mixins.update_mixin import UpdateMixin
from src.models.cart_model import Cart
from src.rest.schemas.cart_schema import (
    CartCreateInputSchema,
    CartSchema
)


class CartManager(
    CreateMixin,
    DeleteMixin,
    UpdateMixin,
    ListMixin
):
    table = Cart
    preloaded_fields = (
        Cart.product,
    )

    update_scheme = CartSchema
    create_scheme = CartCreateInputSchema
