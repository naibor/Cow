def create_app(config_name):
    config_name = os.environ.get("APP_CONFIG", "production")
    APP = Flask(__name__, instance_relative_config=True)
    APP.config.from_object(app_config[config_name])
