from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


async def get_or_create(
        db: AsyncSession,
        model,
        fields: dict,
        prefetch_fields: tuple = None,
        refresh: bool = True
):
    """
    Return an instance with the first argument,
    and whether instance was created or not in the second argument.
    """
    options = BaseMixin.init_preloaded_fields(prefetch_fields=prefetch_fields)

    bookkeeping_id = fields.get('bookkeeping_id')
    filter_by_fields = {'bookkeeping_id': bookkeeping_id} if bookkeeping_id else fields

    result = await db.execute(
        select(model).
        filter_by(**filter_by_fields).
        options(*options)
    )
    instance = result.scalar_one_or_none()

    if instance:
        return instance, False

    instance = model(**fields)
    try:
        db.add(instance)
        await db.commit()
        if refresh:
            await db.refresh(instance)
    except Exception as e:
        print(f'During adding of record to database exception happened: {e}')  # todo add it to a logger
        await db.rollback()
        result = await db.execute(
            select(model).
            filter_by(**filter_by_fields).
            options(*options)
        )
        instance = result.first()
        return instance, False
    else:
        return instance, True


async def get(db: AsyncSession, model, fields: dict, prefetch_fields: tuple = None):
    options = BaseMixin.init_preloaded_fields(prefetch_fields=prefetch_fields)

    result = await db.execute(
        select(model).
        filter_by(**fields).
        options(*options)
    )
    return result.scalar_one_or_none()
