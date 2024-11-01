from .exceptions import NotInstalledError


class FlaskIsNotInstalled(object):  # pragma: no cover
    def __init__(self) -> None:
        raise NotInstalledError("Flask is required for this logger.")
