try:
    import flask
except ImportError:  # pragma: no cover
    flask = None  # type: ignore[assignment]

import logging


class ContextualFilter(logging.Filter):
    def filter(self, log_record: logging.LogRecord) -> bool:
        """Provide some extra variables to be placed into the log message"""

        # If we have an app context (because we're servicing an http request) then get the trace id
        if flask and flask.ctx.has_app_context():
            extension = flask.current_app.extensions["landregistry.enhanced_logging"]["extension"]
            log_record.trace_id = extension.tracer.current_trace_id
        else:
            log_record.trace_id = "N/A"
        return True
