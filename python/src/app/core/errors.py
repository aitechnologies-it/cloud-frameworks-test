"""
Routes for error handling.
"""
from flask import jsonify

from . import main
from .log import logger


@main.app_errorhandler(500)
def server_error(e):
    """500 handler"""
    logger().info(f'Ready for Response. 500: {e}')
    return jsonify(
        status="SERVER_INTERNAL_ERROR",
        message="An internal error occurred. Try again later or contact us."
    ), 500


@main.app_errorhandler(404)
def not_found(e):
    """Credentials not found: 404"""
    logger().info(f'Ready for Response. 404: {e}')
    return jsonify(
        status="NOT_FOUND",
        message="{}".format(e)
    ), 404


@main.app_errorhandler(400)
def invalid_argument(e):
    """Bad Request"""
    logger().info(f'Ready for Response. 400: {e}')
    return jsonify(
        status="BAD_REQUEST",
        message="{}".format(e)
    ), 400
