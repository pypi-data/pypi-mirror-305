# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["URLSearchParams"]


class URLSearchParams(TypedDict, total=False):
    cursor: str

    expired_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="expiredAtLTE", format="iso8601")]

    limit: float

    original_url_begins_with: Annotated[str, PropertyInfo(alias="originalUrlBeginsWith")]
