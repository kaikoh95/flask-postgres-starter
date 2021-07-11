import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """
    Base application configuration
    """
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    DEBUG = os.getenv("DEBUG", False)
    TESTING = os.getenv("TESTING", False)
    
    ENV = os.getenv("ENV")
    FLASK_ENV = os.getenv("FLASK_ENV")
    
    TEST_API = os.getenv("TEST_API")
