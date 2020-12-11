flask_extension = """
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import validate,fields,validates_schema
from flask_migrate import Migrate
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager

pwd_context = CryptContext(schemes="sha256_crypt")
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()


"""

