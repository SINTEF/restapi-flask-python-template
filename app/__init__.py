"""
blueprint app
"""
from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore
from .dummyapp_v1_0 import routes as v1_0
from .dummyapp_v1_1 import routes as v1_1
from .admin import routes as admin_routes


def create_app(config=None):
    """
    Create default app
    """
    app = Flask(__name__)
    CORS(app)

    if config is None:
        app.config.from_object('app.config.Config')
    else:
        app.config.from_mapping(config)

    app.register_blueprint(v1_0.api, url_prefix="/api/dummy/v1_0")
    app.register_blueprint(v1_1.api, url_prefix="/api/dummy/v1_1")
    app.register_blueprint(admin_routes.api, url_prefix="/admin")
    return app
