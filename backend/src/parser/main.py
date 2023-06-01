import asyncio
import os
import time

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.app import logger
from src.core import settings
from src.core.db.db import engine
from src.parser.xml_bookkeeping_parser import XMLParser, OffersParser

parser_async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

bookkeeping_last_modified_time = None
offers_last_modified_time = None


async def parse_bookkeeping_file():
    event_loop = asyncio.get_running_loop()

    async with parser_async_session() as db:
        start_parsing = time.time()
        xml_parser = XMLParser(db=db)
        price_parser = OffersParser(db=db)

        await asyncio.wait([event_loop.create_task(xml_parser.parse_categories())])
        await asyncio.wait([event_loop.create_task(xml_parser.parse_attributes())])

        await event_loop.create_task(xml_parser.parse_products())
        await event_loop.create_task(xml_parser.set_is_visible_attribute())
        await event_loop.create_task(price_parser.parse_offers())
        logger.info(f'Parsing has been finished. It took {time.time() - start_parsing}')


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
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

    while True:
        if parsing_files_are_changed():
            # todo add logs
            event_loop.run_until_complete(parse_bookkeeping_file())
            bookkeeping_last_modified_time = os.path.getmtime(filename=settings.BOOKKEEPING_FILE_PATH)
            offers_last_modified_time = os.path.getmtime(filename=settings.FILE_WITH_PRICES_PATH)
        else:
            time.sleep(settings.LAUNCH_PARSER_EACH_N_MINUTES)
