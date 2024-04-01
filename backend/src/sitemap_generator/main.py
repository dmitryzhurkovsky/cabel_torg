import asyncio
from decimal import Decimal

from sqlalchemy import or_
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import settings
from src.core.db.db import async_session
from src.models import Category, Product, Article
from src.sitemap_generator.generator import SitemapGenerator, DynamicRoute
from src.sitemap_generator.repositories.sql_alchemy_repository import SQLAlchemyRepository


async def create_sitemap(db: AsyncSession):  # noqa
    category_repository = SQLAlchemyRepository(table=Category, db=db)
    category_repository.query_context.select_fields = (Category.site_link,)
    category_repository.query_context.filter_expressions = (
        Category.is_visible.is_not(False),
        Category.site_link.is_not(None)
    )

    product_repository = SQLAlchemyRepository(table=Product, db=db)
    product_repository.query_context.select_fields = (Product.vendor_code, Product.images)
    product_repository.query_context.filter_expressions = (
        Product.is_visible.is_not(False),
        or_(Product.price > Decimal(0), Product.is_price_on_request.is_(True))
    )

    article_repository = SQLAlchemyRepository(table=Article, db=db)
    article_repository.query_context.select_fields = (Article.id, Article.image)


    dynamic_routers = (
        DynamicRoute(site_name="category", db_repository=category_repository),
        DynamicRoute(site_name="card_product", db_repository=product_repository),
        DynamicRoute(site_name="new", db_repository=article_repository),
    )

    sitemap_generator = SitemapGenerator(
        site_name=settings.SITE_URL,
        absolute_path=settings.SITEMAP_PATH,
        static_routers=settings.STATIC_ROUTERS,
        dynamic_routers=dynamic_routers
    )

    sitemap = await sitemap_generator.generate_sitemap()
    sitemap_generator.output.write(sitemap)


async def main():
    async with async_session() as db:
        await create_sitemap(db=db)


if __name__ == "__main__":
    asyncio.run(main())
