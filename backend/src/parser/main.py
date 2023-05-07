import asyncio
import os
import time

from sqlalchemy.ext.asyncio import AsyncSession

from src.app import logger
from src.core import settings
from src.core.db.db import engine
from src.parser.xml_bookkeeping_parser import XMLParser, OffersParser

last_modified_time = None


async def parse_bookkeeping_file():
    event_loop = asyncio.get_running_loop()

    async with AsyncSession(engine) as db:
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
    global last_modified_time

    bookkeeping_file_modified_time = os.path.getmtime(filename=settings.BOOKKEEPING_FILE_PATH)
    file_with_prices_modified_time = os.path.getmtime(filename=settings.FILE_WITH_PRICES_PATH)

    if (
        bookkeeping_file_modified_time != last_modified_time or
        file_with_prices_modified_time != last_modified_time
    ):
        last_modified_time = bookkeeping_file_modified_time if (
                bookkeeping_file_modified_time > file_with_prices_modified_time
        ) else file_with_prices_modified_time
        return True

    return False


async def main():
    while True:
        if parsing_files_are_changed():
            await parse_bookkeeping_file()
        else:
            await asyncio.sleep(settings.LAUNCH_PARSER_EACH_N_MINUTES)


asyncio.run(main())
