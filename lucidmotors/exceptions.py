"""Exception types for the Lucid Motors API."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, repr=True)
class APIError(Exception):
    """
    Represents an error returned by the API
    """
    http_status: int
    code: Optional[int]
    message: Optional[str]
