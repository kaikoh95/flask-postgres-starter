import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class RedisConfig:
    """
    Redis configuration
    """

    CACHE_KEY_PREFIX = os.getenv("CACHE_KEY_PREFIX")
    CACHE_REDIS_HOST = os.getenv("CACHE_REDIS_HOST")
    CACHE_REDIS_PORT = os.getenv("CACHE_REDIS_PORT")
    CACHE_REDIS_DB = os.getenv("CACHE_REDIS_DB")
    CACHE_REDIS_PASSWORD = os.getenv("CACHE_REDIS_PASSWORD")
    CACHE_REDIS_URL = os.getenv("CACHE_REDIS_URL")
