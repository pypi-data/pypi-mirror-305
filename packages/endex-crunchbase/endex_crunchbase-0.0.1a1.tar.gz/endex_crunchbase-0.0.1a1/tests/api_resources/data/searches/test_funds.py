# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from endex_crunchbase import EndexCrunchbase, AsyncEndexCrunchbase
from endex_crunchbase.types.data.searches import FundCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: EndexCrunchbase) -> None:
        fund = client.data.searches.funds.create(
            field_ids=["string", "string", "string"],
            query=[
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
            ],
        )
        assert_matches_type(FundCreateResponse, fund, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: EndexCrunchbase) -> None:
        fund = client.data.searches.funds.create(
            field_ids=["string", "string", "string"],
            query=[
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                    "values": ["string", "string", "string"],
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                    "values": ["string", "string", "string"],
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                    "values": ["string", "string", "string"],
                },
            ],
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            order=[
                {
                    "field_id": "field_id",
                    "sort": "asc",
                    "nulls": "first",
                },
                {
                    "field_id": "field_id",
                    "sort": "asc",
                    "nulls": "first",
                },
                {
                    "field_id": "field_id",
                    "sort": "asc",
                    "nulls": "first",
                },
            ],
        )
        assert_matches_type(FundCreateResponse, fund, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: EndexCrunchbase) -> None:
        response = client.data.searches.funds.with_raw_response.create(
            field_ids=["string", "string", "string"],
            query=[
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = response.parse()
        assert_matches_type(FundCreateResponse, fund, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: EndexCrunchbase) -> None:
        with client.data.searches.funds.with_streaming_response.create(
            field_ids=["string", "string", "string"],
            query=[
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = response.parse()
            assert_matches_type(FundCreateResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFunds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEndexCrunchbase) -> None:
        fund = await async_client.data.searches.funds.create(
            field_ids=["string", "string", "string"],
            query=[
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
            ],
        )
        assert_matches_type(FundCreateResponse, fund, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        fund = await async_client.data.searches.funds.create(
            field_ids=["string", "string", "string"],
            query=[
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                    "values": ["string", "string", "string"],
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                    "values": ["string", "string", "string"],
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                    "values": ["string", "string", "string"],
                },
            ],
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            order=[
                {
                    "field_id": "field_id",
                    "sort": "asc",
                    "nulls": "first",
                },
                {
                    "field_id": "field_id",
                    "sort": "asc",
                    "nulls": "first",
                },
                {
                    "field_id": "field_id",
                    "sort": "asc",
                    "nulls": "first",
                },
            ],
        )
        assert_matches_type(FundCreateResponse, fund, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.data.searches.funds.with_raw_response.create(
            field_ids=["string", "string", "string"],
            query=[
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = await response.parse()
        assert_matches_type(FundCreateResponse, fund, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.data.searches.funds.with_streaming_response.create(
            field_ids=["string", "string", "string"],
            query=[
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
                {
                    "field_id": "field_id",
                    "operator_id": "blank",
                    "type": "predicate",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = await response.parse()
            assert_matches_type(FundCreateResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True
