flask_setting = """
from flask_env import MetaFlaskEnv
import os


class BaseSettings(metaclass=MetaFlaskEnv):
    
    DEBUG = True

    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

"""

prod_settings = """
from settings.settings import BaseSettings
import os

class ProdSettings(BaseSettings):

    DEBUG=False
    SQLALCHEMY_ECHO=False

    DB_NAME = os.getenv("DB_NAME","postgres")
    DB_PORT = os.getenv("DB_PORT",5432)
    DB_HOST = os.getenv("DB_HOST","127.0.0.1")
    DB_PASSWORD = os.getenv("DB_PASSWORD","")
    DB_USER = os.getenv("DB_USER","postgres")

    SQLALCHEMY_DATABASE_URI = f"DB_DRIVER://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
"""

dev_settings = """
from settings.settings import BaseSettings
from datetime import timedelta
import os

class DevelopSettings(BaseSettings):
    
    DEBUG=True
    ENV="development"
    SQLALCHEMY_DATABASE_URI = "DB_DRIVER:///DB_NAME"
    JWT_SECRET_KEY = os.urandom(32)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=3)

"""

test_settings = """

import os
from settings.settings import BaseSettings

class TestSettings(BaseSettings):
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False


    DB_NAME = os.getenv("DB_NAME", "unittest_db")
    DB_PORT = os.getenv("DB_PORT", 5432)
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_USER = os.getenv("DB_USER", "postgres")

    SQLALCHEMY_DATABASE_URI = (
        f"DB_DRIVER://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

"""