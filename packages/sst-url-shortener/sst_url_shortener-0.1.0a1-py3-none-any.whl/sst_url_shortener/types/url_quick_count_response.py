# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .short_url_count_result import ShortURLCountResult

__all__ = ["URLQuickCountResponse"]


class URLQuickCountResponse(BaseModel):
    result: ShortURLCountResult
