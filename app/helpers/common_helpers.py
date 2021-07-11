import json
from flask_restful import request
from flask import current_app
from app.helpers.exceptions_handlers import exception_handler
from app.helpers.string_converters import to_snake_case, to_camel_case


@exception_handler
def process_request_body(schema=None):
    request_body = request.get_data()
    if not request_body:
        raise Exception("JSON Body missing in request")
    request_body = json.loads(request_body)
    if schema:
        return convert_to_snake_case(validate_request_body(request_body, schema))
    return convert_to_snake_case(request_body)  # make json object more pythonic


def validate_request_body(request_body, schema):
    errors = schema.validate(request_body)
    if errors:
        current_app.logger.error(str(errors))
        raise Exception(f"Request failed validation - {str(errors)}")
    return schema.load(request_body, partial=True)


def convert_to_snake_case(iterable):
    converted = {}
    if type(iterable) is list:
        converted = []
        for item in iterable:
            converted.append(convert_to_snake_case(item))
    elif type(iterable) is dict:
        for key, value in iterable.items():
            if isinstance(value, dict):
                value = convert_to_snake_case(value)
            converted[to_snake_case(key)] = value
    return converted


def convert_to_camel_case(iterable):
    converted = {}
    if type(iterable) is list:
        converted = []
        for item in iterable:
            converted.append(convert_to_camel_case(item))
    elif type(iterable) is dict:
        for key, value in iterable.items():
            if isinstance(value, dict):
                value = convert_to_camel_case(value)
            converted[to_camel_case(key)] = value
    return converted
