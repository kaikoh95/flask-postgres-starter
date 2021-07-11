from flask import Flask, request
from flask_restful_swagger_2 import Api
from flask_cors import CORS
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

VERSION = "v1"


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    api = Api(app)

    # Create an APISpec
    spec = APISpec(
        title="My Api Spec",
        version=VERSION,
        openapi_version="2.0.0",
        plugins=[MarshmallowPlugin()],
        info={
            "description": "Api services and usage guide",
        }
    )
    app.config.update({
        'APISPEC_SPEC': spec,
        'APISPEC_SWAGGER_URL': '/swagger',  # URI to access API Doc JSON
        'APISPEC_SWAGGER_UI_URL': '/swagger-ui'  # URI to access UI of API Doc
    })
    docs = FlaskApiSpec(app)

    # App environment config
    from app.config.base import BaseConfig
    from app.config.cache import CacheConfig
    from app.config.db import DbConfig
    from app.config.redis import RedisConfig

    app.config.from_object(BaseConfig)
    app.config.from_object(DbConfig)
    app.config.from_object(RedisConfig)
    app.config.from_object(CacheConfig)

    # Flask Caching
    from app.services.cache.cache import FlaskCache
    FlaskCache(app)

    # REST API Resource Views
    from app.test_example.views.test_objects_resource import TestObjectsResource
    from app.test_example.views.single_test_object_resource import SingleTestObjectResource

    api.add_resource(TestObjectsResource, '/test_example')
    api.add_resource(SingleTestObjectResource, '/test_example/<id>')

    # Register specs
    with app.test_request_context():
        docs.register(TestObjectsResource)
        docs.register(SingleTestObjectResource)

    # Default routes
    @app.route('/', methods=['GET'])
    def home():
        args = request.args
        out = {
            "message": "Welcome, you can view Swagger docs at /swagger-ui or /swagger."
        }
        if args:
            out = {**out, **args}
        return out, 200, {'Content-Type': 'application/json'}

    # Api Error Handlers
    from app.config.app_error_handlers import app_error_handlers
    app_error_handlers(app)

    return app
