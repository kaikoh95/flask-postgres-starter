from app.helpers.exceptions_handlers import exception_handler
from app.services.test.api import TestApiWrapper


class TestApi:

    def __init__(self):
        self.client = TestApiWrapper()

    @staticmethod
    def __build_query_string(params):
        query = ""
        for key, value in params.items():
            query += f"{key}={value}&"
        if query[-1] == "&":
            query = query[:-1]
        return query

    def __get_response(self, path, params=None):
        if params:
            query = self.__build_query_string(params=params)
            path += f"?{query}"
        response = self.client.get(path=path)
        return response

    def get_test_status(self, test_id):
        path = f"/statuses/{test_id}"
        return self.__get_response(path=path)
