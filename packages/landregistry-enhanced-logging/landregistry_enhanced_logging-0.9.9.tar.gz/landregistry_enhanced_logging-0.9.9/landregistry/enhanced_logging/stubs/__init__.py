# Conditional imports that will import things correctly if they're installed but will
# otherwise import different things that raise meaningful exceptions.
try:
    from landregistry.trace_id import TraceID
except ImportError:  # pragma: no cover
    from .flask import FlaskIsNotInstalled as TraceID  # noqa

try:
    from kombu.utils.debug import setup_logging as kombu_setup_logging  # type: ignore[import]
except ImportError:  # pragma: no cover
    from .kombu import kombu_is_not_installed as kombu_setup_logging  # noqa
