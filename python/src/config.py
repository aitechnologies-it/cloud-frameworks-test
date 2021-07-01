import os
from distutils.util import strtobool
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False

    PROJECT_ID = os.environ.get('PROJECT_ID')
    FLASK_PORT = os.environ.get('FLASK_PORT', 8080)

    REQUIRE_AUTH = bool(strtobool(os.environ.get('REQUIRE_AUTH', 'False')))
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME', 'manzi')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD', 'cane')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_CONFIG = 'development'


class TestingConfig(Config):
    TESTING = True
    BASIC_AUTH_USERNAME = 'manzi'
    BASIC_AUTH_PASSWORD = 'cane'


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
