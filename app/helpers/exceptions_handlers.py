from flask import current_app
from flask_restful import abort
from functools import wraps
from requests.exceptions import HTTPError
from http.client import BAD_REQUEST


def exception_handler(func):
    """
    Method decorator for handling exceptions
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ExceptionWithoutAbort as e:
            error = f"{str(e)} in {func.__qualname__}"
            current_app.logger.error(error)
        except HTTPError as e:
            code = BAD_REQUEST
            if e.response.status_code:
                code = e.response.status_code
            abort(code, error=str(e))
        except SaveToDbError as e:
            error = f"{str(e)} in {func.__qualname__}"
            current_app.logger.error(error)
            message = "Database Error: Error saving to db"
            if "unique constraint failed" in error.lower():
                message = "Database Error: Duplicated fields found when saving item to db"
            abort(BAD_REQUEST, error=f"{message} - {str(e)}")
        except Exception as e:
            error = f"Exception in {func.__qualname__} - {str(e)}"
            current_app.logger.error(error)
            abort(BAD_REQUEST, error=error)
    return wrapper


# Declare custom exception classes below
class ExceptionWithoutAbort(Exception):
    """Continue code when Exception is raised"""
    pass


class SaveToDbError(Exception):
    """Error when saving to db"""
    pass
