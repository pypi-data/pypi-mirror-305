"""lion-core."""

import logging

from .log_manager import LogManager
from .setting import Settings
from .version import __version__

__all__ = [
    "Settings",
    "LogManager",
    "__version__",
]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
