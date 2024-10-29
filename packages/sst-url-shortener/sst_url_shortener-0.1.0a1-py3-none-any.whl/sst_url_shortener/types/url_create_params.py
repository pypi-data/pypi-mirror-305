# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["URLCreateParams"]


class URLCreateParams(TypedDict, total=False):
    original_url: Required[Annotated[str, PropertyInfo(alias="originalUrl")]]

    expired_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiredAt", format="iso8601")]
