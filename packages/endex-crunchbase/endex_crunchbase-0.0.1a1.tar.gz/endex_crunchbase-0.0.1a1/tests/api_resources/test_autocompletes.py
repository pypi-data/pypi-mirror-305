# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from endex_crunchbase import EndexCrunchbase, AsyncEndexCrunchbase
from endex_crunchbase.types import AutocompleteListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutocompletes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: EndexCrunchbase) -> None:
        autocomplete = client.autocompletes.list(
            query="query",
        )
        assert_matches_type(AutocompleteListResponse, autocomplete, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: EndexCrunchbase) -> None:
        autocomplete = client.autocompletes.list(
            query="query",
            collection_ids="collection_ids",
            limit=0,
        )
        assert_matches_type(AutocompleteListResponse, autocomplete, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: EndexCrunchbase) -> None:
        response = client.autocompletes.with_raw_response.list(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListResponse, autocomplete, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: EndexCrunchbase) -> None:
        with client.autocompletes.with_streaming_response.list(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutocompletes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncEndexCrunchbase) -> None:
        autocomplete = await async_client.autocompletes.list(
            query="query",
        )
        assert_matches_type(AutocompleteListResponse, autocomplete, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        autocomplete = await async_client.autocompletes.list(
            query="query",
            collection_ids="collection_ids",
            limit=0,
        )
        assert_matches_type(AutocompleteListResponse, autocomplete, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.autocompletes.with_raw_response.list(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListResponse, autocomplete, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.autocompletes.with_streaming_response.list(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True
