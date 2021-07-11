from app.test_example.helpers.test_common_helpers import TestCommonHelpers
from app.test_example.schemas.test_schemas import TestObjectRequestSchema, TestObjectSchema
from app.helpers.common_helpers import process_request_body
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


class SingleTestObjectResource(MethodResource):
    """Contains methods for reading/updating/deleting a Test object."""

    @doc(description='Updates a Test object and saves it in the database. '
                     'This creates a Test object if not already exists.',
         tags=['Test'])
    @use_kwargs(TestObjectRequestSchema, location="json", description="Accepts unique object number and object ID strings.")
    @marshal_with(TestObjectSchema, description="A Test object.", code=200)
    def put(self, **kwargs):
        payload = {
            **process_request_body(TestObjectRequestSchema()),
            "id": kwargs.get("id")
        }
        test_object = TestCommonHelpers().construct_test_object(**payload).serialize()
        return TestObjectSchema().dump(test_object), 200
