"""
Main routes
"""
import logging
logger = logging.getLogger(__name__)

from . import main


@main.route('/', methods=['GET'])
def hello_world():
    logger.info("Responding to /")
    return 'Hello World!', 200


@main.route('/health', methods=['GET'])
def health():
    return "Healthy", 200
