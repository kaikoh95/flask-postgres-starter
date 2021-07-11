import requests
from app.config.base import BaseConfig


class TestApiWrapper:

    def __init__(self):
        self.BASE_URI = BaseConfig.TEST_API

    def get(self, path):
        return self.__make_request("GET", path)

    def __execute_request(self, method, path, data=None):
        if data is None:
            data = {}
        url = f"{self.BASE_URI}{path}"
        conn = requests.request(method=method, url=url, data=data)
        return conn

    def __make_request(self, method, path, data=None):
        response = self.__execute_request(method, path, data)
        if not (response.status_code == requests.codes.ok and response.status_code == requests.codes.created):
            response.raise_for_status()
        try:
            result = response.json()
        except Exception as e:
            raise ValueError(f"No JSON object could be decoded {str(e)}")
        if type(result) is dict() and result.get("results"):
            result = result.get("results")

        return result
