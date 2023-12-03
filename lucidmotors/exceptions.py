"""Exception types for the Lucid Motors API."""

from dataclasses import dataclass
from typing import Optional
from grpc import StatusCode


@dataclass(frozen=True, repr=True)
class APIError(Exception):
    """
    Represents an error returned by the API
    """

    code: StatusCode
    message: Optional[str]
    debug_string: str

    def __str__(self) -> str:
        return f'{self.code}: {self.message}'
