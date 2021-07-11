from datetime import datetime
from app.config.db import db
from app.helpers.common_helpers import convert_to_camel_case
from app.helpers.exceptions_handlers import exception_handler, SaveToDbError


class TestModel(db.Model):
    __tablename__ = "test"

    id = db.Column(db.String(255), primary_key=True, nullable=False)
    object_id = db.Column(db.String(255), unique=True, nullable=False)
    object_number = db.Column(db.String(255), unique=True, nullable=False)
    object_status = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)

    # audit purposes
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)

    def serialize(self):
        """Converts model into readable format in camel case"""
        data = {
            "id": self.id,
            "object_id": self.object_id,
            "object_number": self.object_number,
            "object_status": self.object_status,
            "last_location": {
                "lat": self.lat,
                "long": self.long,
            }
        }
        return convert_to_camel_case(data)

    @exception_handler
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            raise SaveToDbError(e)
        return self
