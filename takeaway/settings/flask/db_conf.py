db_conf = """

from flask import current_app
from extensions.extensions import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from sqlalchemy.orm import relationship
Integer, Column, String, DateTime, Boolean, Date, relationship, ForeignKey =  db.Integer, db.Column, db.String,  db.DateTime, db.Boolean, db.Date, db.relationship, db.ForeignKey


class Operation:

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=db.func.now())
    updated_at = Column(DateTime(timezone=True),default=datetime.utcnow,onupdate=datetime.utcnow,server_default=db.func.now())


class Model(db.Model, Operation):

    __abstract__= True

    def save_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as err:
            current_app.logger.error(err)
            return False

    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self
        except Exception as err:
            current_app.logger.error(err)
            return False

    def update_db(self, **kwargs):
        try:
            for key, val in kwargs.items():
                setattr(self, key, val)
            self.save_db()
        except Exception as err:
            current_app.logger.error(err)
            return False

"""