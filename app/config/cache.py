import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class CacheConfig:
    """
    Cache configuration
    """

    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 30
