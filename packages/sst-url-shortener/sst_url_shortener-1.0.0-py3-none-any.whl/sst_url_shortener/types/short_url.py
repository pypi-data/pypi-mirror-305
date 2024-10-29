# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ShortURL"]


class ShortURL(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    original_url: str = FieldInfo(alias="originalUrl")

    short_id: str = FieldInfo(alias="shortId")

    short_url: str = FieldInfo(alias="shortUrl")

    expired_at: Optional[datetime] = FieldInfo(alias="expiredAt", default=None)
