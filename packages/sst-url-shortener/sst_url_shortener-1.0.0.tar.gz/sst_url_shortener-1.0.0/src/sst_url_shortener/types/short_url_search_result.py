# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ShortURLSearchResult", "URL"]


class URL(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    original_url: str = FieldInfo(alias="originalUrl")

    short_id: str = FieldInfo(alias="shortId")

    short_url: str = FieldInfo(alias="shortUrl")

    expired_at: Optional[datetime] = FieldInfo(alias="expiredAt", default=None)


class ShortURLSearchResult(BaseModel):
    cursor: Optional[str] = None

    urls: List[URL]
