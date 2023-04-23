import os
import pathlib

import jinja2
from dotenv import load_dotenv

load_dotenv('.env.dev')

# Service's settings
DEBUG = int(os.getenv('DEBUG', 0))
CORS_ALLOWED_HEADERS = os.environ.get('CORS_ALLOWED_HEADERS', '').split(',')
ORIGINS = os.environ.get('ORIGINS', '').split(',')
REDIS_URL = os.getenv('REDIS_URL')
IMAGES_PATH = os.getenv('IMAGES_PATH', '/images')  # it's used for uploading images.
STATIC_PATH = os.getenv('STATIC_PATH', '/static')  # It's used for generating templates and populate statics files.
SITE_HOST = os.getenv('SITE_HOST', 'localhost')  # it's used for creating links to sites.
TEMPLATES_PATH = pathlib.Path(__file__).parent.parent.joinpath('templates')
template_loader = jinja2.FileSystemLoader(TEMPLATES_PATH)
templates = jinja2.Environment(loader=template_loader)

# Database's settings
DB_NAME = os.getenv('DATABASE_NAME')
DB_USER = os.getenv('DATABASE_USER')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')
DB_HOST = os.getenv('DATABASE_HOST')
DB_PORT = os.getenv('DATABASE_PORT')
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# JWT settings
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRATION_TIME = 60 * 15  # 15 minutes
JWT_REFRESH_TOKEN_EXPIRATION_TIME = 60 * 60 * 24 * 7  # 7 days

# SMTP settings
SMTP_EMAIL_SENDER = os.getenv('SMTP_EMAIL_SENDER')
SMTP_HOST = os.getenv('SMTP_HOST')

# Parsers' settings
BOOKKEEPING_SHOULD_BE_PARSED = int(os.getenv('BOOKKEEPING_SHOULD_BE_PARSED', 0))
XML_BOOKKEEPING_FILE_PATH = os.getenv('XML_BOOKKEEPING_FILE_PATH')
PATH_TO_XML_FILE_WITH_PRICES = os.getenv('PATH_TO_XML_FILE_WITH_PRICES')
EXCLUDED_CATEGORIES = (
    'Архив',
    'Товары и услуги, вне основной номенклатуры',
    'Материалы/расход/организац.',
    'Топливо',
    'канцелярия',
)
DEFAULT_CATEGORIES_ORDER = {
    'Кабель и провод': 1,
    'Кабель оптический': 1000,
    'Кабель коаксиальный': 1100,
    'Кабель витая пара': 1200,
    'Кабель силовой': 1300,

    'Сетевое оборудование': 2,
    'Оборудование для телевидения': 2000,
    'Оборудование для оптических сетей': 2100,
    'Патч-корд СКС': 2200,
    'Оборудование для видеонаблюдения': 2300,
    'Оборудование RF сигнала': 2400,
    'Телефонное оборудование': 2500,
    'Коннектора, разъёмы, соединители': 2600,
    'Инженерная инфраструктура, СКС, ЦОД': 2700,

    'Материалы для монтажа кабеля': 3,
    'Источники бесперебойного питания ИБП (UPS), АКБ': 4
}
