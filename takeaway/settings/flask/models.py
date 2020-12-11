flask_model ='''
from extensions.extension import db
from sqlalchemy.sql import func
from sqlalchemy.exc import InvalidRequestError,IntegrityError
from extensions.db_conf import (
    Model,
    DateTime,
    Integer,
    String,
    Column,
    Boolean,
    Date,
    relationship,
    ForeignKey,
)

'''