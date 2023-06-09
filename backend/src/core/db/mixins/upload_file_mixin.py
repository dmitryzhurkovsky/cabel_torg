import os
from pathlib import Path

import aiofiles
from fastapi import UploadFile

from src.core import settings
from src.core.db.mixins.base_mixin import BaseMixin


class FileMixin(BaseMixin):
    @classmethod
    async def upload_file(cls, pk: int, input_file: UploadFile, custom_folder_path: str = None) -> str:
        """Upload a file on a disk and return file's path."""
        file_extension = input_file.filename.split('.')[-1]
        file_name = f'{custom_folder_path if custom_folder_path else cls.table.__tablename__}/{pk}.{file_extension}'
        file_name_with_path = f'{settings.IMAGES_PATH}/{file_name}'
        os.makedirs(os.path.dirname(file_name_with_path), exist_ok=True)

        async with aiofiles.open(file_name_with_path, 'wb') as output_file:
            content = await input_file.read()
            await output_file.write(content)

        return file_name

    @classmethod
    def delete_file(cls, file_name: str):
        """Delete a file from a disk."""
        file = Path(f'{settings.IMAGES_PATH}/{file_name}')
        file.unlink(missing_ok=True)
