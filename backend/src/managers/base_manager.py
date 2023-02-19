from src.core.db.mixins.create_mixin import CreateMixin
from src.core.db.mixins.delete_mixin import DeleteMixin
from src.core.db.mixins.list_mixin import ListMixin
from src.core.db.mixins.retrieve_mixin import RetrieveMixin
from src.core.db.mixins.update_mixin import UpdateMixin


class CRUDManager(
    ListMixin,
    RetrieveMixin,
    CreateMixin,
    UpdateMixin,
    DeleteMixin
):
    pass
