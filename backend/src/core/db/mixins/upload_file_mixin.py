import os

import aiofiles
from fastapi import UploadFile

from src.core import settings
from src.core.db.mixins.base_mixin import BaseMixin


class FileMixin(BaseMixin):
    @classmethod
    async def upload_file(cls, pk: int, input_file: UploadFile) -> str:
        """Upload a file on a disk and return file's path."""
        file_name = f'{cls.table.__tablename__}/{pk}.{input_file}'
        file_name_with_path = f'{settings.IMAGES_PATH}/{file_name}'
        os.makedirs(os.path.dirname(file_name_with_path), exist_ok=True)

        async with aiofiles.open(file_name_with_path, 'wb') as output_file:
            content = await input_file.read()
            await output_file.write(content)

        return file_name

    @classmethod
    def delete_file(cls, pk: int):
        """Delete a file from a disk."""
        file_name = f'{settings.IMAGES_PATH}/{cls.table.__tablename__}/{pk}'
        file_name_with_path = f'{settings.IMAGES_PATH}/{file_name}'
        os.remove(file_name_with_path)
