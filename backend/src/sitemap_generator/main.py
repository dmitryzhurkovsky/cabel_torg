import asyncio
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable
from xml.dom import minidom

from sqlalchemy import or_

from src.core.db.db import async_session
from src.models import Category, Product, Article
from src.sitemap_generator.file_managers.base_manager import FileManager
from src.sitemap_generator.file_managers.text_file_manager import TextFileManager
from src.sitemap_generator.repositories.abstract_repository import Repository
from src.sitemap_generator.repositories.sql_alchemy_repository import SQLAlchemyRepository


@dataclass
class DynamicRoute:
    site_name: str
    db_repository: Repository


class SitemapGenerator:
    def __init__(
            self,
            site_name: str,
            static_routers: Iterable = None,
            dynamic_routers: Iterable[DynamicRoute] = None,
            schema_version: str = "0.9",
    ):
        self.site_name = site_name if site_name.startswith("https://") else f"https://{site_name}"
        self.static_routes = static_routers or []
        self.dynamic_routes = dynamic_routers or []
        self.schema_version = schema_version

        self.output: FileManager = TextFileManager(filename="sitemap.xml")

    def create_root_element(self) -> ET.Element:
        root_element = ET.Element("urlset")
        root_element.set("xmlns", f"https://www.sitemaps.org/schemas/sitemap/{self.schema_version}")
        return root_element

    def create_page(self, page: str, parent_element: ET.Element) -> ET.Element:
        url_element = ET.SubElement(parent_element, "url")
        loc = ET.SubElement(url_element, "loc")
        loc.text = f"{self.site_name}/{page}"
        return parent_element

    async def generate_sitemap(self) -> str:
        root_element = self.create_root_element()

        for page in self.static_routes:
            self.create_page(page=page, parent_element=root_element)

        for route in self.dynamic_routes:
            dynamic_pages = await self.get_dynamic_pages(route)
            for page in dynamic_pages:
                self.create_page(page=page, parent_element=root_element)

        return minidom.parseString(ET.tostring(root_element)).toprettyxml(indent="  ")

    @staticmethod
    async def get_dynamic_pages(route: DynamicRoute):
        slug_fields = await route.db_repository.get_all_records()
        return [f"{route.site_name}/{slug_filed}" for slug_filed in slug_fields]


async def create_sitemap():
    async with async_session() as db:
        static_routers = ("how_to_work", "shipping", "wholesale", "warranty", "offer", "about", "contacts", "new")

        category_repository = SQLAlchemyRepository(table=Category, db=db)
        category_repository.query_context.select_fields = (Category.site_link,)
        category_repository.query_context.filter_expressions = (
            Category.is_visible.is_not(False),
            Category.site_link.is_not(None)
        )

        product_repository = SQLAlchemyRepository(table=Product, db=db)
        product_repository.query_context.select_fields = (Product.vendor_code,)
        product_repository.query_context.filter_expressions = (
            Product.is_visible.is_not(False),
            or_(
                Product.price > Decimal(0),
                Product.is_price_on_request.is_(True)
            )
        )

        article_repository = SQLAlchemyRepository(table=Article, db=db)
        article_repository.query_context.select_fields = (Article.id,)

        dynamic_routers = (
            DynamicRoute(site_name="category", db_repository=category_repository),
            DynamicRoute(site_name="card_product", db_repository=product_repository),
            DynamicRoute(site_name="new", db_repository=article_repository),
        )

        sitemap_generator = SitemapGenerator(
            site_name="cabel-torg.by",
            static_routers=static_routers,
            dynamic_routers=dynamic_routers
        )

        sitemap = await sitemap_generator.generate_sitemap()
        sitemap_generator.output.write(sitemap)


if __name__ == "__main__":
    asyncio.run(create_sitemap())
