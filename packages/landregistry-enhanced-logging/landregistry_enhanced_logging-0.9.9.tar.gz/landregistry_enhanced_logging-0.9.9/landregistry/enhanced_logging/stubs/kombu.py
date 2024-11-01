from typing import Any

from .exceptions import NotInstalledError


def kombu_is_not_installed(*args: tuple[Any], **kwargs: dict[str, Any]) -> None:  # pragma: no cover
    raise NotInstalledError("Kombu is required for this logger.")
