"""Lucid user account / profile information."""

from typing import Optional
from pydantic import BaseModel, Field, validator

class User(BaseModel):
    """The logged-in Lucid user's profile information"""

    email: str
    username: str
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    locale: Optional[str]
    photo_url: Optional[str] = Field(alias='photoUrl')

    @validator("locale", pre=True)
    def locale_none_to_empty(cls, v: object) -> object:
        if v is None:
            return ""
        return v

    @validator("photo_url", pre=True)
    def photo_url_none_to_empty(cls, v: object) -> object:
        if v is None:
            return ""
        return v
