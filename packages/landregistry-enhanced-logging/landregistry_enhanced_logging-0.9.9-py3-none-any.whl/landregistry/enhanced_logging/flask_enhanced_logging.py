from logging.config import dictConfig
from typing import TYPE_CHECKING, Optional

from .filters import ContextualFilter
from .formatters import ContentSecurityPolicyFormatter, FlaskJsonFormatter
from .stubs import TraceID

if TYPE_CHECKING:
    from flask import Flask


# Doesn't inherit from EnhancedLogging because it's wildly different
class FlaskEnhancedLogging(object):
    def __init__(self, app: Optional["Flask"] = None) -> None:
        self.app = app
        self.tracer: TraceID
        if app is not None:
            self.init_app(app)

    def init_app(self, app: "Flask") -> None:
        self.tracer = TraceID()
        self.tracer.init_app(app)

        if not hasattr(app, "extensions"):  # pragma: no cover
            app.extensions = {}

        app.extensions["landregistry.enhanced_logging"] = {"extension": self}

        logconfig = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "simple": {"()": FlaskJsonFormatter},
                "content_security_policy": {"()": ContentSecurityPolicyFormatter},
            },
            "filters": {"contextual": {"()": ContextualFilter}},
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "simple",
                    "filters": ["contextual"],
                    "stream": "ext://sys.stdout",
                },
                "content_security_policy": {
                    "class": "logging.StreamHandler",
                    "formatter": "content_security_policy",
                    "filters": ["contextual"],
                    "stream": "ext://sys.stdout",
                },
            },
            "loggers": {
                "": {"handlers": ["console"], "level": app.config["FLASK_LOG_LEVEL"]},
                app.logger.name: {
                    "handlers": ["console"],
                    "level": app.config["FLASK_LOG_LEVEL"],
                    "propagate": 0,
                },
                "content_security_policy": {
                    "handlers": ["content_security_policy"],
                    "level": app.config["FLASK_LOG_LEVEL"],
                    "propagate": 0,
                },
            },
        }

        dictConfig(logconfig)
