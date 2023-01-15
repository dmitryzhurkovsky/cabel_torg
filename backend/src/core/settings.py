import os

from dotenv import load_dotenv

load_dotenv('.env.dev')

DEBUG = int(os.getenv('DEBUG', 0))
BOOKKEEPING_SHOULD_BE_PARSED = int(os.getenv('DEBUG', 0))

DB_NAME = os.getenv('DATABASE_NAME')
DB_USER = os.getenv('DATABASE_USER')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')
DB_HOST = os.getenv('DATABASE_HOST')
DB_PORT = os.getenv('DATABASE_PORT')
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRATION_TIME = 60 * 15  # 15 minutes
JWT_REFRESH_TOKEN_EXPIRATION_TIME = 60 * 60 * 24 * 7  # 7 days

XML_BOOKKEEPING_FILE_PATH = os.getenv('XML_BOOKKEEPING_FILE_PATH')
PATH_TO_XML_FILE_WITH_PRICES = os.getenv('PATH_TO_XML_FILE_WITH_PRICES')

CORS_ALLOWED_HEADERS = os.environ.get('CORS_ALLOWED_HEADERS', '').split(',')
ORIGINS = os.environ.get('ORIGINS', '').split(',')

REDIS_URL = os.getenv('REDIS_URL')
