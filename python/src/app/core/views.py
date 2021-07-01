"""
Main routes
"""
import uuid

from flask import request, current_app, jsonify

from . import main
from .basic_auth import basic_auth
from .log import logger
from .utils import parse_json, validate_json, version


@main.route('/', methods=['GET'])
def hello_world():
    """Route for checking whether the service is alive."""
    logger().debug(f'Headers: {request.headers}.')
    msg = f'Service alive. Version: {version()}.'
    return jsonify(
        status='OK',
        message=msg
    ), 200


@main.route('/health', methods=['GET'])
def health():
    return current_app.service.health()


@main.route('/env', methods=['GET'])
def env():
    return current_app.service.health()


@main.route('/query', methods=['POST'])
@basic_auth
def query():
    sid = str(uuid.uuid4())
    logger().set_sid(sid)

    with validate_json():
        _ = parse_json(request.json)

    logger().info('/query')

    res = current_app.service.query()

    logger().info('Ready for Response. 200.')

    return res, 200
