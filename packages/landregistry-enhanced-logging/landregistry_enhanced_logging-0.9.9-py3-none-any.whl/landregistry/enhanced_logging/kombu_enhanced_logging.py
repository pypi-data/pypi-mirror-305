import logging
from logging.config import dictConfig

from .enhanced_logging import EnhancedLogging
from .stubs import kombu_setup_logging


class KombuEnhancedLogging(EnhancedLogging):
    def __init__(self, app_module_name: str = "server") -> None:
        super().__init__(app_module_name)

    def init(self, app_log_level: str, kombu_log_level: str) -> None:  # type: ignore[override]
        kombu_setup_logging(loglevel=kombu_log_level)
        self._log_level = app_log_level
        logconfig = self._create_logconfig()

        logconfig["loggers"]["amqp"] = {"handlers": ["console"], "level": kombu_log_level}
        dictConfig(logconfig)

    def get_logger(self) -> logging.Logger:
        return logging.getLogger(self._app_module_name)
