# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .short_url_search_result import ShortURLSearchResult

__all__ = ["URLSearchResponse"]


class URLSearchResponse(BaseModel):
    result: ShortURLSearchResult
