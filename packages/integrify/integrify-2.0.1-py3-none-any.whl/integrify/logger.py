import logging
from functools import partial
from typing import Callable

try:
    import logfire  # type: ignore[import-not-found]
except ModuleNotFoundError:
    logfire = None

try:
    import loguru  # type: ignore[import-not-found]
except ModuleNotFoundError:
    loguru = None


LOGGER: Callable = logging.getLogger
LOGURU: Callable = loguru and partial(loguru.logger.bind)
LOGFIRE: Callable = logfire and partial(logfire.with_tags)


LOGGER_FUNCTION = LOGGER
