from starlette.config import Config
from starlette.datastructures import Secret,URL
from core.settings.settings import BaseConfig


class DevSettings(BaseConfig):

    """ Configuration class for site development environment """

    config = Config()

    DB_USER = config("DB_USER", cast=str, default="postgres")
    DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default="postgres")
    DB_HOST = config("DB_HOST", cast=str, default="db")
    DB_PORT = config("DB_PORT", cast=str, default="5432")
    DB_NAME = config("DB_NAME", cast=str, default="postgres")
    
    DEBUG = config("DEBUG", cast=bool, default=True)
    
    DATABASE_URL = config(
        "DATABASE_URL",
        default="asyncpg:///fastapitest",
    )