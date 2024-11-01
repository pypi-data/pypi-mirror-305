import collections
import json
import logging
import traceback
from typing import Any, Optional


class JsonFormatter(logging.Formatter):
    def build_log_entry(
        self, record: logging.LogRecord, trace_id: str, exception: Optional[list[str]]
    ) -> collections.OrderedDict[str, Any]:
        # Timestamp must be first (webops request)
        return collections.OrderedDict(
            [
                ("timestamp", self.formatTime(record)),
                ("level", record.levelname),
                ("traceid", trace_id),
                ("message", super().format(record)),
                ("exception", exception),
            ]
        )

    def format(self, record: logging.LogRecord) -> str:
        if hasattr(record, "trace_id"):
            trace_id = record.trace_id
        else:
            trace_id = "N/A"

        if record.exc_info:
            exc = traceback.format_exception(*record.exc_info)
        else:
            exc = None

        log_entry = self.build_log_entry(record, trace_id, exc)
        return json.dumps(log_entry)


class FlaskJsonFormatter(JsonFormatter):
    def build_log_entry(
        self, record: logging.LogRecord, trace_id: str, exception: Optional[list[str]]
    ) -> collections.OrderedDict:
        record_message = record.msg % record.args if record.args else record.msg
        return collections.OrderedDict(
            [
                ("timestamp", self.formatTime(record)),
                ("level", record.levelname),
                ("traceid", trace_id),
                ("message", record_message),
                ("exception", exception),
            ]
        )


class ContentSecurityPolicyFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        # Timestamp must be first (webops request)
        record_message = record.msg % record.args if record.args else record.msg
        log_entry = collections.OrderedDict(
            [
                ("timestamp", self.formatTime(record)),
                ("level", record.levelname),
                ("traceid", record.trace_id),  # type: ignore[attr-defined]
                ("message", record_message),
                (
                    "content_security_policy_report",
                    record.content_security_policy_report,  # type: ignore[attr-defined]
                ),
            ]
        )

        return json.dumps(log_entry)
