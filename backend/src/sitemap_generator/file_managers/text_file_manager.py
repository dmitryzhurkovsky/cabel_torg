from pathlib import Path

from src.sitemap_generator.file_managers.base_manager import AbstractFileManager


class TextFileManager(AbstractFileManager):
    def __init__(self, filename: str):
        self.path = Path(filename)

    def write(self, data: str):
        self.path.write_text(data)
