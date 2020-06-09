devsetting = '''

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
        default="DB_DRIVER:///DB_NAME",
    )   
'''

prodsettings = '''
from starlette.config import Config
from starlette.datastructures import Secret,URL
from core.settings.settings import BaseConfig
import os

class ProdSettings(BaseConfig):

    """ Configuration class for site development environment """

    config = Config()

    DB_USER = config("DB_USER", cast=str, default="postgres")
    DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default="postgres")
    DB_HOST = config("DB_HOST", cast=str, default="db")
    DB_PORT = config("DB_PORT", cast=str, default="5432")
    DB_NAME = config("DB_NAME", cast=str, default="postgres")
    INCLUDE_SCHEMA=config("INCLUDE_SCHEMA", cast=bool, default=False)
    SSL_CERT_FILE = config("SSL_PATH",default="/etc/.cert/ca-certificate.crt")
    
    DATABASE_URL = config(
        "DATABASE_URL",
        default=f"DB_DRIVER://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    )

'''

setting = '''
from starlette.config import Config
from starlette.datastructures import Secret
import os

project_name="test"


class BaseConfig:

    """
    Base configuration class. Subclasses should include configurations for
    testing, development and production environments
    """
    config = Config()

    INCLUDE_SCHEMA=config("INCLUDE_SCHEMA", cast=bool, default=True)

    SECRET_KEY = config("SECRET_KEY",default=os.urandom(32))
    SQLALCHEMY_ECHO = config("SQLALCHEMY_ECHO",cast=bool,default=False)
    SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS",cast=bool,default=False)

    LOGGER_NAME = "%s_log" % project_name
    LOG_FILENAME = "/var/tmp/app.%s.log" % project_name

    CORS_ORIGINS = config("CORS_HOSTS",default="*")



    DEBUG = config("DEBUG", cast=bool, default=False)
    TESTING = config("TESTING", cast=bool, default=False)


'''
