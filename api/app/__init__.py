"""Main APP module"""
import os
from flask import Flask, make_response, jsonify, redirect
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# local import
from config import app_config
# initialize sql-alchemy
db = SQLAlchemy()
# Get the instance config to use
config_name = os.environ.get("APP_CONFIG", "development")
APP = Flask(__name__, instance_relative_config=True)
APP.config.from_object(app_config[config_name])
APP.config['PROPAGATE_EXCEPTIONS'] = True
jwt_manager = JWTManager()
jwt_manager.init_app(APP)
# Application =Api(APP)
# jwt_manager._set_error_handler_callbacks(Application)


jwt_manager._set_error_handler_callbacks(APP)

# overide 404 error handler
@APP.errorhandler(404)
def resource_not_found(error):
    """
    This will be response returned if the user attempts to access
    a non-existent resource or url.
    """

    response_payload = dict(
        message="The requested URL was not found on the server. " + \
                "If you entered the URL manually please check your spelling and try again."
    )
    return make_response(jsonify(response_payload), 404)

@APP.route('/', methods=['GET'])
def redirect_to_docs():
    """
    Redirects root to API docs
    """
    return redirect('/api/v1/docs')

db.init_app(APP)

# Import and add namespaces for the endpoints
from . restplus import API
from app.endpoints.auth import auth_ns
from app.endpoints.milking import milk_ns, all_ns
from app.endpoints.cow_construction import cow_ns
API.add_namespace(auth_ns)
API.add_namespace(milk_ns)
API.add_namespace(all_ns)
API.add_namespace(cow_ns)
API.init_app(APP)
CORS(APP)





