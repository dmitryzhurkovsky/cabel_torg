from sqlalchemy import select, update
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


async def get_object(
        db: AsyncSession,
        model,
        fields: dict,
        prefetch_fields: tuple = None,
):
    """Get an object from a database."""
    options = BaseMixin.init_preloaded_fields(prefetch_fields=prefetch_fields)

    query_result = await db.execute(
        select(model).
        filter_by(**fields).
        options(*options)
    )
    return query_result.scalar_one_or_none()


async def create_object(
        db: AsyncSession,
        model,
        fields: dict,
        refresh: bool = True
):
    """Create an object in a database."""
    try:
        # Try to create an instance
        instance = model(**fields)
        db.add(instance)
        await db.commit()
        if refresh:
            await db.refresh(instance)

        return instance, True
    except Exception as e:
        # Rollback if there is any problem
        print(f'During adding of record to database exception happened: {e}')  # todo add it to a logger
        await db.rollback()

        return None, False


async def update_object(
        db: AsyncSession,
        model,
        instance,
        fields: dict,
        refresh: bool = True
):
    """Update an object in a database."""
    # Update the instance
    await db.execute(
        update(model).
        where(model.id == instance.id).
        values(**fields)
    )
    await db.commit()
    if refresh:
        await db.refresh(instance)


async def update_or_create_object(
        db: AsyncSession,
        model,
        fields: dict,
        prefetch_fields: tuple = None,
        update: bool = False,
        refresh: bool = True
):
    """
    Get the instance from the database and update all fields except id and accounting id and return the instance
    as the first argument and a boolean of whether the instance was created in the second argument.
    """
    # Get filter fields
    bookkeeping_id = fields.pop('bookkeeping_id', None)
    filter_by_fields = {'bookkeeping_id': bookkeeping_id} if bookkeeping_id else fields

    # Hit a database to get an instance
    instance = await get_object(db=db, model=model, fields=filter_by_fields, prefetch_fields=prefetch_fields)
    if instance:
        if update:
            await update_object(db=db, model=model, instance=instance, fields=fields)
        return instance, False

    # The instance doesn't exist, try to create it
    instance, created = await create_object(db=db, model=model, fields=fields, refresh=refresh)
    if created:
        return instance, True

    # The instance is already created, try to get the object from the database and update fields again..
    instance = await get_object(db=db, model=model, fields=filter_by_fields, prefetch_fields=prefetch_fields)
    if update:
        await update_object(db=db, model=model, instance=instance, fields=fields)

    return instance, False
