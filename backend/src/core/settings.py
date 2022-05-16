
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    DB_NAME: str = 'cabel_torg_dev'
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'postgres'
    DB_HOST: str = 'localhost'
    DB_PORT: str = '5432'

    XML_BOOKKEEPING_FILE_PATH: str = '/test_1.xml'

    @property
    def database_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    class Config:
        # env_file = '../.env.prod'
        env_file = '.env.dev'


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
