import os
import time
import threading
import logging

from flask import current_app, g


class TimeTracker:
    def __init__(self):
        self.start = self._now()
        self.end = self.start
        self._from_beginning = 0
        self._from_last_round = 0

    def update(self):
        now = self._now()
        self._from_beginning = now - self.start
        self._from_last_round = now - self.end
        self.end = now

    def from_last_round(self, update=False):
        if update:
            self.update()
        return self._from_last_round

    def from_beginning(self, update=False):
        if update:
            self.update()
        return self._from_beginning

    @staticmethod
    def _now():
        return int(time.time() * 1000)


level2severity = {
    "DEFAULT": 0,
    "DEBUG": 100,
    "INFO": 200,
    "NOTICE": 300,
    "WARNING": 400,
    "ERROR": 500,
    "CRITICAL": 600,
    "ALERT": 700,
    "EMERGENCY": 800
}


def use_json_logger():
    return os.environ.get('FLASK_CONFIG', '') == "production"


class Logger:
    def __init__(self):
        self.actor = 'api'
        self.session_id = '00000000-0000-0000-0000-000000000000'
        self.time_tracker = TimeTracker()
        if use_json_logger():
            self.logger = logging.getLogger("jsonLogger")
        else:
            self.logger = current_app.logger

    def set_sid(self, session_id):
        self.session_id = session_id if session_id else self.session_id

    def set_actor(self, actor):
        self.actor = actor

    def reset_actor(self):
        self.actor = 'api'

    def info(self, msg):
        level = "INFO"
        timenow = self.time_tracker.from_beginning(update=True)
        self.logger.info(
            msg=self._format_msg(msg, timenow, level=level),
            extra=self._get_extra(timenow)
        )

    def error(self, msg):
        level = "ERROR"
        timenow = self.time_tracker.from_beginning(update=True)
        self.logger.error(
            msg=self._format_msg(msg, timenow, level=level),
            extra=self._get_extra(timenow)
        )

    def critical(self, msg):
        level = "CRITICAL"
        timenow = self.time_tracker.from_beginning(update=True)
        self.logger.critical(
            msg=self._format_msg(msg, timenow, level=level),
            extra=self._get_extra(timenow)
        )

    def debug(self, msg):
        level = "DEBUG"
        timenow = self.time_tracker.from_beginning(update=True)
        self.logger.info(
            msg=self._format_msg(msg, timenow, level=level),
            extra=self._get_extra(timenow)
        )

    def warning(self, msg):
        level = "WARNING"
        timenow = self.time_tracker.from_beginning(update=True)
        self.logger.warning(
            msg=self._format_msg(msg, timenow, level=level),
            extra=self._get_extra(timenow)
        )

    def _format_msg(self, text, timenow, level="default"):
        thread_name = self._format_thread_name(threading.currentThread().getName())
        level_text = "" if use_json_logger() else level+" "
        return f"{self.session_id[-12:]} {thread_name} {timenow:4} {level_text}| {text}"

    def _get_extra(self, timenow):
        return {
            "thread_name": threading.currentThread().getName(),
            "correlation_id": self.session_id,
            "time": timenow
        }

    @staticmethod
    def _format_thread_name(text):
        if text == "MainThread":
            return "MainThread"
        elif "ThreadPoolExecutor" in text:
            return "PoolEx" + text[-4:].replace('-', '')
        elif "Thread-" in text:
            return "Thread" + text[-2:].replace('-', '')
        else:
            return text[-4:]

    def _make_extra(self, **kwargs):
        obj = {
            'session_id': self.session_id,
        }
        obj.update({k: v for k, v in kwargs.items()})

        return obj


def logger():
    if 'my_logger' not in g:
        g.my_logger = Logger()
    return g.my_logger
