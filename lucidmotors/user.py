"""Lucid user account / profile information."""

from typing import Optional
from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    """The logged-in Lucid user's profile information"""

    email: str
    username: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    locale: Optional[str]
    photo_url: Optional[str] = Field(alias="photoUrl")

    @field_validator("locale")
    def locale_none_to_empty(cls, v: object) -> object:
        if v is None:
            return ""
        return v

    @field_validator("photo_url")
    def photo_url_none_to_empty(cls, v: object) -> object:
        if v is None:
            return ""
        return v
