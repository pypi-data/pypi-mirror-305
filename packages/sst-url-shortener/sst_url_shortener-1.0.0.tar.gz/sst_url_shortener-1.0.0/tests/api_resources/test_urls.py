# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sst_url_shortener import SstURLShortener, AsyncSstURLShortener
from sst_url_shortener.types import (
    URLCreateResponse,
    URLSearchResponse,
    URLSlowCountResponse,
    URLQuickCountResponse,
    URLFromShortIDResponse,
    URLFromOriginalURLResponse,
)
from sst_url_shortener._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SstURLShortener) -> None:
        url = client.urls.create(
            original_url="https://example.com",
        )
        assert_matches_type(URLCreateResponse, url, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SstURLShortener) -> None:
        url = client.urls.create(
            original_url="https://example.com",
            expired_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(URLCreateResponse, url, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SstURLShortener) -> None:
        response = client.urls.with_raw_response.create(
            original_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(URLCreateResponse, url, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SstURLShortener) -> None:
        with client.urls.with_streaming_response.create(
            original_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(URLCreateResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_by_original_url(self, client: SstURLShortener) -> None:
        url = client.urls.delete_by_original_url(
            original_url="https://example.com",
        )
        assert_matches_type(object, url, path=["response"])

    @parametrize
    def test_raw_response_delete_by_original_url(self, client: SstURLShortener) -> None:
        response = client.urls.with_raw_response.delete_by_original_url(
            original_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(object, url, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_original_url(self, client: SstURLShortener) -> None:
        with client.urls.with_streaming_response.delete_by_original_url(
            original_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(object, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_by_short_id(self, client: SstURLShortener) -> None:
        url = client.urls.delete_by_short_id(
            short_id="shortId",
        )
        assert_matches_type(object, url, path=["response"])

    @parametrize
    def test_raw_response_delete_by_short_id(self, client: SstURLShortener) -> None:
        response = client.urls.with_raw_response.delete_by_short_id(
            short_id="shortId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(object, url, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_short_id(self, client: SstURLShortener) -> None:
        with client.urls.with_streaming_response.delete_by_short_id(
            short_id="shortId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(object, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_from_original_url(self, client: SstURLShortener) -> None:
        url = client.urls.from_original_url(
            original_url="https://example.com",
        )
        assert_matches_type(URLFromOriginalURLResponse, url, path=["response"])

    @parametrize
    def test_raw_response_from_original_url(self, client: SstURLShortener) -> None:
        response = client.urls.with_raw_response.from_original_url(
            original_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(URLFromOriginalURLResponse, url, path=["response"])

    @parametrize
    def test_streaming_response_from_original_url(self, client: SstURLShortener) -> None:
        with client.urls.with_streaming_response.from_original_url(
            original_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(URLFromOriginalURLResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_from_short_id(self, client: SstURLShortener) -> None:
        url = client.urls.from_short_id(
            short_id="xxx",
        )
        assert_matches_type(URLFromShortIDResponse, url, path=["response"])

    @parametrize
    def test_raw_response_from_short_id(self, client: SstURLShortener) -> None:
        response = client.urls.with_raw_response.from_short_id(
            short_id="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(URLFromShortIDResponse, url, path=["response"])

    @parametrize
    def test_streaming_response_from_short_id(self, client: SstURLShortener) -> None:
        with client.urls.with_streaming_response.from_short_id(
            short_id="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(URLFromShortIDResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_quick_count(self, client: SstURLShortener) -> None:
        url = client.urls.quick_count()
        assert_matches_type(URLQuickCountResponse, url, path=["response"])

    @parametrize
    def test_raw_response_quick_count(self, client: SstURLShortener) -> None:
        response = client.urls.with_raw_response.quick_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(URLQuickCountResponse, url, path=["response"])

    @parametrize
    def test_streaming_response_quick_count(self, client: SstURLShortener) -> None:
        with client.urls.with_streaming_response.quick_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(URLQuickCountResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: SstURLShortener) -> None:
        url = client.urls.search()
        assert_matches_type(URLSearchResponse, url, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: SstURLShortener) -> None:
        url = client.urls.search(
            cursor="cursor",
            expired_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            original_url_begins_with="originalUrlBeginsWith",
        )
        assert_matches_type(URLSearchResponse, url, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: SstURLShortener) -> None:
        response = client.urls.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(URLSearchResponse, url, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: SstURLShortener) -> None:
        with client.urls.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(URLSearchResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_slow_count(self, client: SstURLShortener) -> None:
        url = client.urls.slow_count()
        assert_matches_type(URLSlowCountResponse, url, path=["response"])

    @parametrize
    def test_raw_response_slow_count(self, client: SstURLShortener) -> None:
        response = client.urls.with_raw_response.slow_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(URLSlowCountResponse, url, path=["response"])

    @parametrize
    def test_streaming_response_slow_count(self, client: SstURLShortener) -> None:
        with client.urls.with_streaming_response.slow_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(URLSlowCountResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncURLs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.create(
            original_url="https://example.com",
        )
        assert_matches_type(URLCreateResponse, url, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.create(
            original_url="https://example.com",
            expired_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(URLCreateResponse, url, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSstURLShortener) -> None:
        response = await async_client.urls.with_raw_response.create(
            original_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(URLCreateResponse, url, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSstURLShortener) -> None:
        async with async_client.urls.with_streaming_response.create(
            original_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(URLCreateResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_by_original_url(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.delete_by_original_url(
            original_url="https://example.com",
        )
        assert_matches_type(object, url, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_original_url(self, async_client: AsyncSstURLShortener) -> None:
        response = await async_client.urls.with_raw_response.delete_by_original_url(
            original_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(object, url, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_original_url(self, async_client: AsyncSstURLShortener) -> None:
        async with async_client.urls.with_streaming_response.delete_by_original_url(
            original_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(object, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_by_short_id(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.delete_by_short_id(
            short_id="shortId",
        )
        assert_matches_type(object, url, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_short_id(self, async_client: AsyncSstURLShortener) -> None:
        response = await async_client.urls.with_raw_response.delete_by_short_id(
            short_id="shortId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(object, url, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_short_id(self, async_client: AsyncSstURLShortener) -> None:
        async with async_client.urls.with_streaming_response.delete_by_short_id(
            short_id="shortId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(object, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_from_original_url(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.from_original_url(
            original_url="https://example.com",
        )
        assert_matches_type(URLFromOriginalURLResponse, url, path=["response"])

    @parametrize
    async def test_raw_response_from_original_url(self, async_client: AsyncSstURLShortener) -> None:
        response = await async_client.urls.with_raw_response.from_original_url(
            original_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(URLFromOriginalURLResponse, url, path=["response"])

    @parametrize
    async def test_streaming_response_from_original_url(self, async_client: AsyncSstURLShortener) -> None:
        async with async_client.urls.with_streaming_response.from_original_url(
            original_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(URLFromOriginalURLResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_from_short_id(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.from_short_id(
            short_id="xxx",
        )
        assert_matches_type(URLFromShortIDResponse, url, path=["response"])

    @parametrize
    async def test_raw_response_from_short_id(self, async_client: AsyncSstURLShortener) -> None:
        response = await async_client.urls.with_raw_response.from_short_id(
            short_id="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(URLFromShortIDResponse, url, path=["response"])

    @parametrize
    async def test_streaming_response_from_short_id(self, async_client: AsyncSstURLShortener) -> None:
        async with async_client.urls.with_streaming_response.from_short_id(
            short_id="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(URLFromShortIDResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_quick_count(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.quick_count()
        assert_matches_type(URLQuickCountResponse, url, path=["response"])

    @parametrize
    async def test_raw_response_quick_count(self, async_client: AsyncSstURLShortener) -> None:
        response = await async_client.urls.with_raw_response.quick_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(URLQuickCountResponse, url, path=["response"])

    @parametrize
    async def test_streaming_response_quick_count(self, async_client: AsyncSstURLShortener) -> None:
        async with async_client.urls.with_streaming_response.quick_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(URLQuickCountResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.search()
        assert_matches_type(URLSearchResponse, url, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.search(
            cursor="cursor",
            expired_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            original_url_begins_with="originalUrlBeginsWith",
        )
        assert_matches_type(URLSearchResponse, url, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncSstURLShortener) -> None:
        response = await async_client.urls.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(URLSearchResponse, url, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncSstURLShortener) -> None:
        async with async_client.urls.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(URLSearchResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_slow_count(self, async_client: AsyncSstURLShortener) -> None:
        url = await async_client.urls.slow_count()
        assert_matches_type(URLSlowCountResponse, url, path=["response"])

    @parametrize
    async def test_raw_response_slow_count(self, async_client: AsyncSstURLShortener) -> None:
        response = await async_client.urls.with_raw_response.slow_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(URLSlowCountResponse, url, path=["response"])

    @parametrize
    async def test_streaming_response_slow_count(self, async_client: AsyncSstURLShortener) -> None:
        async with async_client.urls.with_streaming_response.slow_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(URLSlowCountResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True
