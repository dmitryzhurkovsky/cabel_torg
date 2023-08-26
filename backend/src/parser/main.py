import asyncio
import os
import time
from datetime import datetime

from sqlalchemy.exc import PendingRollbackError
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


class BookkeepingLoggerContextManager:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def __aenter__(self):
        global bookkeeping_last_modified_time, offers_last_modified_time

        bookkeeping_last_modified_time = os.path.getmtime(filename=settings.BOOKKEEPING_FILE_PATH)
        offers_last_modified_time = os.path.getmtime(filename=settings.FILE_WITH_PRICES_PATH)
        files_were_updated_at = datetime.fromtimestamp(max(bookkeeping_last_modified_time, offers_last_modified_time))

        await database_service.update_or_create_object(
            model=ParserInfo,
            fields={
                'id': 1,
                'started_at': datetime.now(),
                'files_were_updated_at': files_were_updated_at
            },
            pk_field='id',
            db=self.db,
            update=True
        )

    async def __aexit__(self, exc_type, exc_value, traceback):
        global bookkeeping_last_modified_time, offers_last_modified_time

        fields = {'id': 1}

        if exc_type:
            fields['finished_at'] = None  # noqa
            fields['is_failed'] = True
            fields['exception'] = str(exc_value)

            parser_logger.info(f'Exception has happened:\n{exc_value}\n')
            EmailService.send_email(
                message=f'Exception is {exc_value}.',
                subject='SITE: cabel-trog.by. ERROR: Parsing has failed.',
                send_to_service=True
            )
        else:
            fields['finished_at'] = datetime.now()

        await database_service.update_or_create_object(
            model=ParserInfo,
            fields=fields,
            pk_field='id',
            db=self.db,
            update=True
        )

        if exc_type is PendingRollbackError:
            # PendingRollbackError is raised some time and to fix it's enough to restart parser or wait a little.
            # We also need to reset modification time variables to force the parser to start parssing again.
            time.sleep(60 * 10)
            bookkeeping_last_modified_time = None
            offers_last_modified_time = None
        elif exc_type:
            # If there is a critical bug, we will sent messages to service staff rather than restart and
            # make a pause in parsing rather than start it each 3 minutes.
            time.sleep(60 * 60 * 24)


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
    async with async_session() as db:
        async with BookkeepingLoggerContextManager(db=db):
            xml_parser = XMLParser(db=db)
            price_parser = OffersParser(db=db)

            await asyncio.wait([event_loop.create_task(xml_parser.parse_categories())])
            await asyncio.wait([event_loop.create_task(xml_parser.delete_old_categories())])
            await asyncio.wait([event_loop.create_task(xml_parser.parse_attributes())])

            await event_loop.create_task(xml_parser.parse_products())
            await event_loop.create_task(xml_parser.set_is_visible_attribute())
            await event_loop.create_task(xml_parser.delete_old_products())
            await event_loop.create_task(price_parser.parse_offers())

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
