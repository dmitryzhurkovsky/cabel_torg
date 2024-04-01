import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Iterable
from xml.dom import minidom

from src.core import settings
from src.sitemap_generator.file_managers.base_manager import FileManager
from src.sitemap_generator.file_managers.text_file_manager import TextFileManager
from src.sitemap_generator.repositories.abstract_repository import Repository


@dataclass
class DynamicRoute:
    site_name: str
    db_repository: Repository


@dataclass
class SiteMapObject:
    page_url: str
    images: Iterable | None = tuple()


class SitemapGenerator:
    def __init__(
            self,
            site_name: str,
            absolute_path: str = "sitemap.xml",
            static_routers: Iterable = None,
            dynamic_routers: Iterable[DynamicRoute] = None,
            schema_version: str = "0.9",
    ):
        self.site_name = site_name if site_name.startswith("https://") else f"https://{site_name}"
        self.static_routes = static_routers or []
        self.dynamic_routes = dynamic_routers or []
        self.schema_version = schema_version

        self.output: FileManager = TextFileManager(filename=absolute_path)

    def create_root_element(self) -> ET.Element:
        root_element = ET.Element("urlset")
        root_element.set("xmlns", f"https://www.sitemaps.org/schemas/sitemap/{self.schema_version}")
        root_element.set(
            "xmlns:image", f"http://www.google.com/schemas/sitemap-image/{self.schema_version}"
        )
        return root_element

    def create_page(self, page_url: str, parent_element: ET.Element) -> ET.Element:
        url_element = ET.SubElement(parent_element, "url")
        loc = ET.SubElement(url_element, "loc")
        loc.text = f"{self.site_name}/{page_url}"
        return url_element

    @staticmethod
    def attach_image_to_page(image_url: str, parent_element: ET.Element) -> None:
        image_element = ET.SubElement(parent_element, "image:image")
        loc = ET.SubElement(image_element, "image:loc")
        loc.text = image_url

    async def generate_sitemap(self) -> str:
        root_element = self.create_root_element()

        for page_url in self.static_routes:
            self.create_page(page_url=page_url, parent_element=root_element)

        for route in self.dynamic_routes:
            dynamic_page_attributes = await self.get_dynamic_page_attributes(route)

            for payload in dynamic_page_attributes:
                page = self.create_page(page_url=payload.page_url, parent_element=root_element)
                if payload.images:
                    for image in payload.images:
                        self.attach_image_to_page(image_url=image, parent_element=page)

        return minidom.parseString(ET.tostring(root_element)).toprettyxml(indent="  ")

    @staticmethod
    async def get_dynamic_page_attributes(route: DynamicRoute):
        result = []

        records = await route.db_repository.get_all_records()
        for record in records:
            site_map_object = SiteMapObject(page_url=f"{route.site_name}/{record[0]}")
            if hasattr(record, "images"):
                site_map_object.images = [
                    f"{settings.SITE_URL}/site_media/images{image}" for image in record.images.split(',')
                ] if record.images else None
            elif hasattr(record, "image"):
                site_map_object.images = [
                    f"{settings.SITE_URL}/site_media/images{record.image}"
                ] if record.image else None

            result.append(site_map_object)

        return result
