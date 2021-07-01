__version__ = "0.1"

import os
from flask import Flask
from flask_cors import CORS

from config import config
from .core import utils
from .core.log import logger, use_json_logger
from .core.service import Service

if use_json_logger():
    import stacklogging
    log_fun = stacklogging.getLogger("jsonLogger")
else:
    from logging.config import dictConfig
    dictConfig({
        'version': 1,
        "disable_existing_loggers": True,
        'formatters': {'default': {
            'format': '%(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })


def create_app():
    app = Flask(__name__)
    app.version = __version__
    app.config.from_object(config[os.environ.get('FLASK_CONFIG') or 'default'])
    # config[config_name].init_app(app)
    app.config['PROPAGATE_EXCEPTIONS'] = False

    with app.app_context():
        logger().info(f"Running create_app. App version: {__version__}")
        logger().debug(f"ENVIRON: {os.environ}")
        logger().debug(f"CONFIG: {app.config}")
        CORS(app, supports_credentials=True)

        app.service = Service()
        logger().info("Initialized Service.")

        from .core import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
