import logging
from logging.config import dictConfig
from typing import Any

from .formatters import JsonFormatter


class EnhancedLogging(object):
    def __init__(self, app_module_name: str = "server") -> None:
        # Let's get the app's base package name so we can set the correct formatter, filter and logger names
        self._app_module_name = app_module_name

    def init(self, app_log_level: str) -> None:
        self._log_level = app_log_level
        logconfig = self._create_logconfig()

        # Set up the loggers fomatters and handlers from the LOGCONFIG dict
        dictConfig(logconfig)

    def _create_logconfig(self) -> dict[str, Any]:
        return {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {"simple": {"()": JsonFormatter}},
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "simple",
                    "stream": "ext://sys.stdout",
                }
            },
            "loggers": {
                self._app_module_name: {"handlers": ["console"], "level": self._log_level},
            },
        }

    @property
    def logger(self) -> logging.Logger:
        return self.get_logger()

    def get_logger(self) -> logging.Logger:
        return logging.getLogger(self._app_module_name)
