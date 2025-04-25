from sqlalchemy import select, update, BooleanClauseList, BinaryExpression
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin
from src.models.abstract_model import BaseModel
from src.parser.main import parser_logger
from src.parser.utils import    fields_were_updated


async def get_object(
        db: AsyncSession,
        model,
        fields: dict | BooleanClauseList,
        prefetch_fields: tuple = None,
) -> BaseModel | None:
    """Get an object from a database."""
    options = BaseMixin.init_preloaded_fields(preloaded_fields=prefetch_fields)

    query = select(model).options(*options)
    if isinstance(fields, dict):
        query = query.filter_by(**fields)
    elif isinstance(fields, (BooleanClauseList, BinaryExpression)):
        query = query.filter(fields)

    query_result = await db.execute(query)
    return query_result.scalar_one_or_none()


async def create_object(
        db: AsyncSession,
        model,
        fields: dict,
        refresh: bool = True
) -> tuple[BaseModel | None, bool]:
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
        parser_logger.info(f'An exception happened during adding of record to database: {e}\n')
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
        prefetch_fields: tuple | None = None,
        update: bool = False,
        refresh: bool = True,
        pk_field: str = 'bookkeeping_id',
        custom_filters: tuple = None
) -> tuple[BaseModel, bool]:
    """
    Get the instance from the database and update all fields except id and accounting id and return the instance
    as the first argument and a boolean of whether the instance was created in the second argument.

    Args:
        db: an async session of db.
        model: is used to tell parser what model is used to create/update instances.
        fields: fields are used to create or update the instance.
        prefetch_fields: fields that should be preloaded to prevent await IO error when we try to get an attribute
         of related model.
        update: is used to tell parser whether we should update the instance or only create or get it.
        refresh: is used to tell SqlAlchemy whether we should update session.
         For example if we need to get id of instances.
        pk_field: is used to connect instance in db with instance in 1C bookkeeping.
        custom_filters: is used to filter by custom fields. For example: we want to have a few OR conditions and so on.

    Returns: A tuple where the first argument is instance and the second one is bool whether it was created.
    """
    # Get filter fields
    if custom_filters is not None:
        filter_by_fields = custom_filters
    else:
        value_of_pk_field = fields.get(pk_field)
        filter_by_fields = {pk_field: value_of_pk_field} if value_of_pk_field else fields

    print(fields.get('vendor_code'))
    # Hit a database to get an instance
    instance = await get_object(db=db, model=model, fields=filter_by_fields, prefetch_fields=prefetch_fields)
    if instance:
        if update and fields_were_updated(fields=fields, instance=instance):
            await update_object(db=db, model=model, instance=instance, fields=fields)

        return instance, False

    # The instance doesn't exist, try to create it
    instance, created = await create_object(db=db, model=model, fields=fields, refresh=refresh)
    if created:
        return instance, True

    # The instance is already created, try to get the object from the database and update fields again.
    instance = await get_object(db=db, model=model, fields=filter_by_fields, prefetch_fields=prefetch_fields)
    if update and fields_were_updated(fields=fields, instance=instance):
        await update_object(db=db, model=model, instance=instance, fields=fields)

    return instance, False
