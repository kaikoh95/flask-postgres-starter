import uuid

from app.test_example.models.test_model import TestModel
from app.test_example.models.services import TestApi
from app.helpers.common_helpers import convert_to_snake_case
from app.helpers.exceptions_handlers import exception_handler


class TestCommonHelpers:
    def __init__(self):
        self.client = TestApi()

    @staticmethod
    def get_all_test_objects():
        return [test_object.serialize() for test_object in TestModel.query.all()]

    def construct_test_object(self, **kwargs):
        """Creates a Test object from given details"""
        object_status = self.latest_test_object_status(object_id=kwargs.get("object_id"))
        object_data = self.construct_test_object_data(object_status=object_status, **kwargs)

        test_object = TestModel.query.filter_by(id=kwargs.get("id")).scalar() or TestModel(**object_data)
        if test_object:
            for key, value in object_data.items():
                setattr(test_object, key, value)
        return test_object.save()

    @staticmethod
    def construct_test_object_data(object_status, **kwargs):
        object_data = {
            "object_status": "Healthy" if object_status.get("healthy", False) is True else "Broken",
            "long": float(object_status.get("long") or object_status.get("lng")),
            "lat": float(object_status.get("lat")),
            "object_id": kwargs.get("object_id"),
            "object_number": kwargs.get("object_number"),
            "id": kwargs.get("id") or str(uuid.uuid4()),
        }
        return object_data

    @exception_handler
    def latest_test_object_status(self, object_id):
        """Fetches object status and locations from External API"""
        object_statuses = self.client.get_test_status(object_id)
        object_statuses = convert_to_snake_case(object_statuses)
        object_status = sorted(object_statuses, key=lambda x: x["timestamp"], reverse=True)[0]

        return object_status
