# -*- coding: utf-8 -*-

# import multiprocessing
import os

from distutils.util import strtobool


bind = os.getenv('GUNICORN_BIND', '0.0.0.0:8080')

workers = int(os.getenv('GUNICORN_WORKERS', 1))
threads = int(os.getenv('GUNICORN_THREADS', 250))

reload = bool(strtobool(os.getenv('GUNICORN_RELOAD', 'false')))
