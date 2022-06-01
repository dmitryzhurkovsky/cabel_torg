import os
from dotenv import load_dotenv

load_dotenv('.env.dev')

DEBUG = int(os.getenv('DEBUG', 0))

DB_NAME = os.getenv('DATABASE_NAME')
DB_USER = os.getenv('DATABASE_USER')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')
DB_HOST = os.getenv('DATABASE_HOST')
DB_PORT = os.getenv('DATABASE_PORT')
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

XML_BOOKKEEPING_FILE_PATH = os.getenv('XML_BOOKKEEPING_FILE_PATH')
