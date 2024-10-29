# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import (
    url_create_params,
    url_search_params,
    url_from_short_id_params,
    url_from_original_url_params,
    url_delete_by_short_id_params,
    url_delete_by_original_url_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.url_create_response import URLCreateResponse
from ..types.url_search_response import URLSearchResponse
from ..types.url_slow_count_response import URLSlowCountResponse
from ..types.url_quick_count_response import URLQuickCountResponse
from ..types.url_from_short_id_response import URLFromShortIDResponse
from ..types.url_from_original_url_response import URLFromOriginalURLResponse

__all__ = ["URLsResource", "AsyncURLsResource"]


class URLsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Dizzzmas/sst-url-shortener-python-sdk#accessing-raw-response-data-eg-headers
        """
        return URLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Dizzzmas/sst-url-shortener-python-sdk#with_streaming_response
        """
        return URLsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        original_url: str,
        expired_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLCreateResponse:
        """
        Create a new short url

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/urls/create",
            body=maybe_transform(
                {
                    "original_url": original_url,
                    "expired_at": expired_at,
                },
                url_create_params.URLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLCreateResponse,
        )

    def delete_by_original_url(
        self,
        *,
        original_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a short url by original url

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/urls/delete-by-original-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"original_url": original_url}, url_delete_by_original_url_params.URLDeleteByOriginalURLParams
                ),
            ),
            cast_to=object,
        )

    def delete_by_short_id(
        self,
        *,
        short_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a short url by short id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/urls/delete-by-short-id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"short_id": short_id}, url_delete_by_short_id_params.URLDeleteByShortIDParams),
            ),
            cast_to=object,
        )

    def from_original_url(
        self,
        *,
        original_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLFromOriginalURLResponse:
        """
        Get the short url from the original url

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/urls/from-original-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"original_url": original_url}, url_from_original_url_params.URLFromOriginalURLParams
                ),
            ),
            cast_to=URLFromOriginalURLResponse,
        )

    def from_short_id(
        self,
        *,
        short_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLFromShortIDResponse:
        """
        Get the short url from the short id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/urls/from-short-id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"short_id": short_id}, url_from_short_id_params.URLFromShortIDParams),
            ),
            cast_to=URLFromShortIDResponse,
        )

    def quick_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLQuickCountResponse:
        """Get approximate count of short urls in the DB. Updated every 6 hours."""
        return self._get(
            "/urls/quick-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLQuickCountResponse,
        )

    def search(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        expired_at_lte: Union[str, datetime] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        original_url_begins_with: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLSearchResponse:
        """
        Paginated search of short urls

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/urls/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "expired_at_lte": expired_at_lte,
                        "limit": limit,
                        "original_url_begins_with": original_url_begins_with,
                    },
                    url_search_params.URLSearchParams,
                ),
            ),
            cast_to=URLSearchResponse,
        )

    def slow_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLSlowCountResponse:
        """Scan through the entire table to get real-time count of items"""
        return self._get(
            "/urls/slow-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLSlowCountResponse,
        )


class AsyncURLsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Dizzzmas/sst-url-shortener-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncURLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Dizzzmas/sst-url-shortener-python-sdk#with_streaming_response
        """
        return AsyncURLsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        original_url: str,
        expired_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLCreateResponse:
        """
        Create a new short url

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/urls/create",
            body=await async_maybe_transform(
                {
                    "original_url": original_url,
                    "expired_at": expired_at,
                },
                url_create_params.URLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLCreateResponse,
        )

    async def delete_by_original_url(
        self,
        *,
        original_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a short url by original url

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/urls/delete-by-original-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"original_url": original_url}, url_delete_by_original_url_params.URLDeleteByOriginalURLParams
                ),
            ),
            cast_to=object,
        )

    async def delete_by_short_id(
        self,
        *,
        short_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a short url by short id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/urls/delete-by-short-id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"short_id": short_id}, url_delete_by_short_id_params.URLDeleteByShortIDParams
                ),
            ),
            cast_to=object,
        )

    async def from_original_url(
        self,
        *,
        original_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLFromOriginalURLResponse:
        """
        Get the short url from the original url

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/urls/from-original-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"original_url": original_url}, url_from_original_url_params.URLFromOriginalURLParams
                ),
            ),
            cast_to=URLFromOriginalURLResponse,
        )

    async def from_short_id(
        self,
        *,
        short_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLFromShortIDResponse:
        """
        Get the short url from the short id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/urls/from-short-id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"short_id": short_id}, url_from_short_id_params.URLFromShortIDParams
                ),
            ),
            cast_to=URLFromShortIDResponse,
        )

    async def quick_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLQuickCountResponse:
        """Get approximate count of short urls in the DB. Updated every 6 hours."""
        return await self._get(
            "/urls/quick-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLQuickCountResponse,
        )

    async def search(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        expired_at_lte: Union[str, datetime] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        original_url_begins_with: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLSearchResponse:
        """
        Paginated search of short urls

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/urls/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "expired_at_lte": expired_at_lte,
                        "limit": limit,
                        "original_url_begins_with": original_url_begins_with,
                    },
                    url_search_params.URLSearchParams,
                ),
            ),
            cast_to=URLSearchResponse,
        )

    async def slow_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLSlowCountResponse:
        """Scan through the entire table to get real-time count of items"""
        return await self._get(
            "/urls/slow-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLSlowCountResponse,
        )


class URLsResourceWithRawResponse:
    def __init__(self, urls: URLsResource) -> None:
        self._urls = urls

        self.create = to_raw_response_wrapper(
            urls.create,
        )
        self.delete_by_original_url = to_raw_response_wrapper(
            urls.delete_by_original_url,
        )
        self.delete_by_short_id = to_raw_response_wrapper(
            urls.delete_by_short_id,
        )
        self.from_original_url = to_raw_response_wrapper(
            urls.from_original_url,
        )
        self.from_short_id = to_raw_response_wrapper(
            urls.from_short_id,
        )
        self.quick_count = to_raw_response_wrapper(
            urls.quick_count,
        )
        self.search = to_raw_response_wrapper(
            urls.search,
        )
        self.slow_count = to_raw_response_wrapper(
            urls.slow_count,
        )


class AsyncURLsResourceWithRawResponse:
    def __init__(self, urls: AsyncURLsResource) -> None:
        self._urls = urls

        self.create = async_to_raw_response_wrapper(
            urls.create,
        )
        self.delete_by_original_url = async_to_raw_response_wrapper(
            urls.delete_by_original_url,
        )
        self.delete_by_short_id = async_to_raw_response_wrapper(
            urls.delete_by_short_id,
        )
        self.from_original_url = async_to_raw_response_wrapper(
            urls.from_original_url,
        )
        self.from_short_id = async_to_raw_response_wrapper(
            urls.from_short_id,
        )
        self.quick_count = async_to_raw_response_wrapper(
            urls.quick_count,
        )
        self.search = async_to_raw_response_wrapper(
            urls.search,
        )
        self.slow_count = async_to_raw_response_wrapper(
            urls.slow_count,
        )


class URLsResourceWithStreamingResponse:
    def __init__(self, urls: URLsResource) -> None:
        self._urls = urls

        self.create = to_streamed_response_wrapper(
            urls.create,
        )
        self.delete_by_original_url = to_streamed_response_wrapper(
            urls.delete_by_original_url,
        )
        self.delete_by_short_id = to_streamed_response_wrapper(
            urls.delete_by_short_id,
        )
        self.from_original_url = to_streamed_response_wrapper(
            urls.from_original_url,
        )
        self.from_short_id = to_streamed_response_wrapper(
            urls.from_short_id,
        )
        self.quick_count = to_streamed_response_wrapper(
            urls.quick_count,
        )
        self.search = to_streamed_response_wrapper(
            urls.search,
        )
        self.slow_count = to_streamed_response_wrapper(
            urls.slow_count,
        )


class AsyncURLsResourceWithStreamingResponse:
    def __init__(self, urls: AsyncURLsResource) -> None:
        self._urls = urls

        self.create = async_to_streamed_response_wrapper(
            urls.create,
        )
        self.delete_by_original_url = async_to_streamed_response_wrapper(
            urls.delete_by_original_url,
        )
        self.delete_by_short_id = async_to_streamed_response_wrapper(
            urls.delete_by_short_id,
        )
        self.from_original_url = async_to_streamed_response_wrapper(
            urls.from_original_url,
        )
        self.from_short_id = async_to_streamed_response_wrapper(
            urls.from_short_id,
        )
        self.quick_count = async_to_streamed_response_wrapper(
            urls.quick_count,
        )
        self.search = async_to_streamed_response_wrapper(
            urls.search,
        )
        self.slow_count = async_to_streamed_response_wrapper(
            urls.slow_count,
        )
