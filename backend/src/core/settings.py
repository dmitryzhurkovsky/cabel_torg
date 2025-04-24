import os
import pathlib

import jinja2
from dotenv import load_dotenv

load_dotenv('.env')

# Service's settings
DEBUG = int(os.getenv('DEBUG', 0))
CORS_ALLOWED_HEADERS = os.environ.get('CORS_ALLOWED_HEADERS', '').split(',')
ORIGINS = os.environ.get('ORIGINS', '').split(',')
REDIS_URL = os.getenv('REDIS_URL')  # deprecated
DATA_PATH = os.getenv('DATA_PATH')
IMAGES_PATH = f'{DATA_PATH}/site_media/images'  # it's used for uploading images.
DOCUMENTS_PATH = f'{DATA_PATH}/site_media/documents'  # it's used for uploading documents.
LOGS_PATH = f'{DATA_PATH}/logs'  # it's used as a folder for logs.
DOCUMENTS_URL = os.getenv('DOCUMENTS_URL', '/site_media/documents')  # It's used for generating
STATIC_URL = os.getenv('STATIC_URL', '/static')  # It's used for generating templates and populate statics files.
SITE_HOST = os.getenv('SITE_HOST', 'localhost')  # it's used for creating links to sites.
TEMPLATES_PATH = pathlib.Path(__file__).parent.parent.joinpath('templates')
template_loader = jinja2.FileSystemLoader(TEMPLATES_PATH)
templates = jinja2.Environment(loader=template_loader)
ADMINISTRATOR_EMAIL = os.getenv('ADMINISTRATOR_EMAIL', 'admin@admin.com')  # it's admin
SERVICE_EMAIL = os.getenv('SERVICE_EMAIL', 'service@service.com')  # it's admin
DEFAULT_TAX = int(os.getenv('DEFAULT_TAX')) if os.getenv('DEFAULT_TAX') else 20

# Database's settings
DB_NAME = os.getenv('DATABASE_NAME')
DB_USER = os.getenv('DATABASE_USER')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')
DB_HOST = os.getenv('DATABASE_HOST')
DB_PORT = os.getenv('DATABASE_PORT')
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# JWT settings
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_TYPE = 'Bearer'
JWT_ACCESS_TOKEN_EXPIRATION_TIME = 60 * 15  # 15 minutes
JWT_REFRESH_TOKEN_EXPIRATION_TIME = 60 * 60 * 24 * 7  # 7 days

# SMTP settings
SMTP_EMAIL_SENDER = os.getenv('SMTP_EMAIL_SENDER')
SMTP_HOST = os.getenv('SMTP_HOST')

# Parsers' settings
LAUNCH_PARSER_EACH_N_MINUTES = int(os.getenv('LAUNCH_PARSER_EACH_N_MINUTES', 0)) * 60
BOOKKEEPING_FILE_PATH = os.getenv('BOOKKEEPING_FILE_PATH')
FILE_WITH_PRICES_PATH = os.getenv('FILE_WITH_PRICES_PATH')
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
    'Телефонное оборудование': 2400,
    'Коннектора, разъёмы, соединители': 2500,
    'Инженерная инфраструктура, СКС, ЦОД': 2600,

    'Материалы для монтажа кабеля': 3,
    'Оборудование RF сигнала': 4
}

# Sitemap generator
SITEMAP_STATIC_ROUTERS = os.getenv(
    "SITEMAP_STATIC_ROUTERS",
    (
        "how_to_work",
        "shipping",
        "wholesale",
        "warranty",
        "offer",
        "about",
        "contacts",
        "new"
    )
)
SITE_URL = os.getenv("SITE_URL", "https://cabel-torg.by")
SITEMAP_PATH = os.getenv("SITEMAP_PATH", f"{DATA_PATH}/site_media/sitemap.xml")
SITEMAP_SCHEMA_VERSION = os.getenv("SITEMAP_SCHEMA_VERSION", "0.9")
