__version__ = "0.1"

import os
from flask import Flask
from flask_cors import CORS
import logging
logger = logging.getLogger(__name__)

from logging.config import dictConfig
dictConfig({
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        'json': {
            'format': '%(message)s %(lineno)d %(filename)s %(levelname)s %(asctime)s',
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter'
        }
    },
    "handlers": {
        "json": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            'stream': 'ext://sys.stdout',
        }
    },
    "loggers": {
        "": {
            "handlers": ["json"],
            "level": 'INFO'
        }
    }
})

from config import config


def create_app():
    app = Flask(__name__)
    app.version = __version__
    app.config.from_object(config[os.environ.get('FLASK_CONFIG') or 'default'])
    app.config['PROPAGATE_EXCEPTIONS'] = False

    with app.app_context():
        logger.info(f"Running create_app. App version: {__version__}")
        logger.debug(f"ENVIRON: {os.environ}")
        logger.debug(f"CONFIG: {app.config}")
        CORS(app, supports_credentials=True)

        from .core import main as main_blueprint
        app.register_blueprint(main_blueprint)

        logger.info("Initialized Service.")

    return app
