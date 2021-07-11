from app.test_example.helpers.test_common_helpers import TestCommonHelpers
from app.test_example.schemas.test_schemas import TestObjectRequestSchema, TestObjectSchema
from app.helpers.common_helpers import process_request_body
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from app.services.cache.cache import cache


class TestObjectsResource(MethodResource):
    """Example methods for reading/creating endpoint."""

    @doc(description='Gets all in the database.', tags=['Test'])
    @marshal_with(TestObjectSchema(many=True), description="A list of Test.", code=200)
    @cache.cached(key_prefix='get_all_test_objects')
    def get(self, **kwargs):
        tests = TestCommonHelpers.get_all_test_objects()
        return TestObjectSchema(many=True).dump(tests), 200

    @doc(description='Creates a Test object and saves it in the database.', tags=['Test'])
    @use_kwargs(TestObjectRequestSchema, location="json", description="Accepts unique object number and object ID strings.")
    @marshal_with(TestObjectSchema, description="A Test object.", code=200)
    def post(self, **kwargs):
        payload = process_request_body(schema=TestObjectRequestSchema())
        test = TestCommonHelpers().construct_test_object(**payload).serialize()
        return TestObjectSchema().dump(test), 200
