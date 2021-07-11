from flask_caching import Cache

cache = Cache()


class FlaskCache:
    """
    Contains caching methods for specific caching
    """

    def __init__(self, app):
        cache.init_app(app)
        self.cache = cache

    def save_cache(self, key, data):
        return self.cache.set(key, data)

    def has_cache(self, key):
        return self.get_specific_cache(key) is not None

    def get_specific_cache(self, key):
        return self.cache.get(key)

    def clear_specific_cache(self, key):
        return self.cache.delete(key)

    def clear_cache(self):
        return self.cache.clear()

