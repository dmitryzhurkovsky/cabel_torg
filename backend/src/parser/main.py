import asyncio
import os
import time
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from src.core import settings
from src.core.db.db import async_session
from src.log import create_logger
from src.models import ParserInfo
from src.parser.servers import database_service
from src.parser.utils import set_permissions_recursive
from src.parser.xml_bookkeeping_parser import XMLParser, OffersParser
from src.services.email_service import EmailService

parser_logger = create_logger(log_file_name='parser')

bookkeeping_last_modified_time = None
offers_last_modified_time = None


class BookkeepingContextManager:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def __aenter__(self):
        fields = {
            'id': 1,
            'started_at': datetime.now(),
        }

        if bookkeeping_last_modified_time and offers_last_modified_time:
            last_modified_time = max(bookkeeping_last_modified_time, offers_last_modified_time)  # noqa
            fields['files_were_updated_at'] = datetime.fromtimestamp(last_modified_time)

        await database_service.update_or_create_object(
            model=ParserInfo,
            fields=fields,
            pk_field='id',
            db=self.db,
            update=True
        )

    async def __aexit__(self, exc_type, exc_value, traceback):
        fields = {
            'id': 1,
            'finished_at': None
        }

        if exc_type is not None:
            fields['is_failed'] = True
            fields['exception'] = str(exc_value)
        else:
            fields['finished_at'] = datetime.now()

        if bookkeeping_last_modified_time and offers_last_modified_time:
            last_modified_time = max(bookkeeping_last_modified_time, offers_last_modified_time)  # noqa
            fields['files_were_updated_at'] = datetime.fromtimestamp(last_modified_time)

        await database_service.update_or_create_object(
            model=ParserInfo,
            fields=fields,
            pk_field='id',
            db=self.db,
            update=True
        )


def parsing_files_are_changed() -> bool:
    """
    Check a hash of files that should be parsed to recognize whether they are changed.
    We do it to decrease overhead to database and server's resources.
    """
    bookkeeping_file_modified_time = os.path.getmtime(filename=settings.BOOKKEEPING_FILE_PATH)
    file_with_offers_modified_time = os.path.getmtime(filename=settings.FILE_WITH_PRICES_PATH)

    if (
            bookkeeping_file_modified_time != bookkeeping_last_modified_time or
            file_with_offers_modified_time != offers_last_modified_time
    ):
        return True

    return False


async def parse_bookkeeping_file():
    global bookkeeping_last_modified_time, offers_last_modified_time

    async with async_session() as db:
        async with BookkeepingContextManager(db=db):
            try:
                xml_parser = XMLParser(db=db)
                price_parser = OffersParser(db=db)

                await asyncio.wait([event_loop.create_task(xml_parser.parse_categories())])
                await asyncio.wait([event_loop.create_task(xml_parser.delete_old_categories())])
                await asyncio.wait([event_loop.create_task(xml_parser.parse_attributes())])

                await event_loop.create_task(xml_parser.parse_products())
                await event_loop.create_task(xml_parser.set_is_visible_attribute())
                await event_loop.create_task(xml_parser.delete_old_products())
                await event_loop.create_task(price_parser.parse_offers())
            except Exception as e:
                parser_logger.info(f'Exception has happened:\n{e}\n')
                EmailService.send_email(
                    message=f'Exception is {e}.',
                    subject='SITE: cabel-trog.by. ERROR: Parsing has failed.',
                    send_to_service=True
                )
                time.sleep(60 * 60 * 24)  # notify service personal each 24 hours about errors.
            else:
                bookkeeping_last_modified_time = os.path.getmtime(filename=settings.BOOKKEEPING_FILE_PATH)
                offers_last_modified_time = os.path.getmtime(filename=settings.FILE_WITH_PRICES_PATH)
                set_permissions_recursive(path=settings.IMAGES_PATH, mode=0o777)
                set_permissions_recursive(path=settings.DOCUMENTS_PATH, mode=0o777)


if __name__ == '__main__':
    if settings.LAUNCH_PARSER_EACH_N_MINUTES == 0:
        exit()

    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

    while True:
        if parsing_files_are_changed():
            event_loop.run_until_complete(parse_bookkeeping_file())
        else:
            time.sleep(settings.LAUNCH_PARSER_EACH_N_MINUTES)
