# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .short_url import ShortURL

__all__ = ["URLFromShortIDResponse"]


class URLFromShortIDResponse(BaseModel):
    result: ShortURL
