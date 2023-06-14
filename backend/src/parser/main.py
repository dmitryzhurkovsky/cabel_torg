import asyncio
import os
import time

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.core import settings
from src.core.db.db import engine
from src.log import create_logger
from src.parser.utils import set_permissions_recursive
from src.parser.xml_bookkeeping_parser import XMLParser, OffersParser
from src.services.email_service import EmailService

parser_async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
parser_logger = create_logger(log_file_name='parser')

bookkeeping_last_modified_time = None
offers_last_modified_time = None


async def parse_bookkeeping_file():
    event_loop = asyncio.get_running_loop()

    async with parser_async_session() as db:
        xml_parser = XMLParser(db=db)
        price_parser = OffersParser(db=db)

        await asyncio.wait([event_loop.create_task(xml_parser.parse_categories())])
        await asyncio.wait([event_loop.create_task(xml_parser.delete_old_categories())])
        await asyncio.wait([event_loop.create_task(xml_parser.parse_attributes())])

        await event_loop.create_task(xml_parser.parse_products())
        await event_loop.create_task(xml_parser.set_is_visible_attribute())
        await event_loop.create_task(xml_parser.delete_old_products())
        await event_loop.create_task(price_parser.parse_offers())


def parsing_files_are_changed() -> bool:
    """
    Check a hash of files that should be parsed to recognize whether they are changed.
    We do it to decrease overhead to database and server's resources.
    """
    global bookkeeping_last_modified_time, offers_last_modified_time

    bookkeeping_file_modified_time = os.path.getmtime(filename=settings.BOOKKEEPING_FILE_PATH)
    file_with_offers_modified_time = os.path.getmtime(filename=settings.FILE_WITH_PRICES_PATH)

    if (
            bookkeeping_file_modified_time != bookkeeping_last_modified_time or
            file_with_offers_modified_time != offers_last_modified_time
    ):
        return True

    return False


if __name__ == '__main__':
    if settings.LAUNCH_PARSER_EACH_N_MINUTES == 0:
        exit()

    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

    while True:
        if parsing_files_are_changed():
            start_parsing = time.time()
            try:
                event_loop.run_until_complete(parse_bookkeeping_file())
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

        else:
            time.sleep(settings.LAUNCH_PARSER_EACH_N_MINUTES)
