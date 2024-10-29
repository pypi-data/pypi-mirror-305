"""
CTX

Contextal command line tools and python library
"""

__version__ = "1.0.0"
__all__ = [
    "Platform",
    "QueryError",
    "ScenarioDuplicateNameError",
    "ScenarioReplacementError",
    "Config",
]

from .platform import (
    Platform,
    QueryError,
    ScenarioDuplicateNameError,
    ScenarioReplacementError,
)
from .config import Config
