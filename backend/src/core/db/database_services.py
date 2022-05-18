from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession


async def get_or_create(db: AsyncSession, model, fields: dict):
    """
    Return an instance with the first argument,
    and whether instance was created or not in the second argument.
    """
    result = await db.execute(
        select(model).
        filter_by(**fields)
    )
    instance = result.scalar_one_or_none()

    if instance:
        return instance, False

    instance = model(**fields)
    try:
        db.add(instance)
        await db.commit()
    except Exception as e:  # Set exception for you base.
        print(f'During adding of record to database exception happened: {e}')
        await db.rollback()
        result = await db.execute(
            select(model).
            filter_by(**fields)
        )
        instance = result.first()
        return instance, False
    else:
        return instance, True


async def get(db: AsyncSession, model, fields: dict):
    result = await db.execute(
        select(model).
        filter_by(**fields)
    )
    return result.scalar_one_or_none()
