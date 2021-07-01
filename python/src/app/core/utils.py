import contextlib
import sys
import traceback

from flask import current_app

from .log import logger


@contextlib.contextmanager
def validate_json():
    try:
        yield
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)  # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        logger().error(f'ERROR: parsing json request body on line {line} in statement `{text}`')
        raise JSONSchemaValidatorException(f"Error parsing json request body. Statement: `{text}`")


def parse_json(data_json):
    return None


class JSONSchemaValidatorException(Exception):
    pass


def version():
    return {
        "version": current_app.version,
        "service": current_app.service.get_version()
    }
