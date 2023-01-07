from src.core.db.mixins.update_mixin import UpdateMixin
from src.core.db.mixins.delete_mixin import DeleteMixin
from src.core.db.mixins.create_mixin import CreateMixin
from src.core.db.mixins.list_mixin import ListMixin

from src.models.watchlist_model import WatchList


class WatchListManager(
    CreateMixin,
    DeleteMixin,
    UpdateMixin,
    ListMixin
):
    table = WatchList
