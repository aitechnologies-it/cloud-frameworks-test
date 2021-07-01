"""
Our own implementation of a basic authentication plugin for flask.

Expects `BASIC_AUTH_USERNAME` and `BASIC_AUTH_PASSWORD` flask app config variables to have the correct credentials.

Examples
--------
To add authentication to an endpoint, just add `@basic_auth`:
```
@main.route('/', methods=['GET'])
@basic_auth
def hello_world():
    ...
```
"""
from functools import wraps

from flask import request, current_app, Response


def basic_auth(view_func):
    """Flask annotation basic auth

    Parameters
    ----------
    view_func
        Not to be provided by the user.
    """
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if _authenticate():
            return view_func(*args, **kwargs)
        else:
            return Response(
                status=401,
                headers={'WWW-Authenticate': 'Basic realm=""'}
            )
    return wrapper


def _authenticate():
    auth = request.authorization
    return (
        auth and auth.type == 'basic' and
        _check_credentials(auth.username, auth.password)
    )


def _check_credentials(username, password):
    if current_app.config['REQUIRE_AUTH']:
        correct_username = current_app.config['BASIC_AUTH_USERNAME']
        correct_password = current_app.config['BASIC_AUTH_PASSWORD']
        return username == correct_username and password == correct_password
    else:
        current_app.logger.info("Allowing unauthenticated API call.")
        return True
