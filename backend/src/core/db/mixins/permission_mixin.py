from sqlalchemy import and_, select
from sqlalchemy.sql.expression import exists
from starlette.requests import Request

from src.core.db.db import async_session
from src.core.exception.base_exception import ForbiddenError


class PermissionMixin:
    table = None

    @classmethod
    async def check_object_permission(cls, request: Request) -> bool:
        if request.user.is_admin:
            return True

        if not request.user:
            return False

        object_id = int(next(iter(request.path_params.values())))
        async with async_session() as session:
            query_result = await session.execute(
                select(
                    exists(
                        select(cls.table.user_id, cls.table.id).
                        where(and_(
                            cls.table.user_id == request.user.id,
                            cls.table.id == object_id
                        ))
                    )
                )
            )
        has_permission = query_result.scalar()

        if not has_permission:
            raise ForbiddenError
