"""App intance configs"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_url = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost/')
database_name = os.environ.get('DATABASE_NAME', 'cow')

# database_url = os.environ.get('DATABASE_URL', 'postgresql://password@localhost:5432/cow')


class BaseConfig:
    """Base configuration."""
    # Flask APP configs
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY", "\xe6.]`\x99\x07\x1ap\xff\xb7c\xf0\xea*\xba{")
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']
    DEBUG = False
    # SQLAlchemy configs
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Flask-RESTPlus Configs
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False

    PROPAGATE_EXCEPTIONS = True

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = database_url + database_name
    ENV = "development"


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = database_url + 'test_'+ database_name
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    ENV = "testing"


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = database_url

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
