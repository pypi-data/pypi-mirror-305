# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from endex_crunchbase import EndexCrunchbase, AsyncEndexCrunchbase
from endex_crunchbase.types import (
    SearchProductsResponse,
    SearchPrincipalsResponse,
    SearchProductLaunchesResponse,
    SearchLegalProceedingsResponse,
    SearchPartnershipAnnouncementsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_legal_proceedings(self, client: EndexCrunchbase) -> None:
        search = client.searches.legal_proceedings(
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
        assert_matches_type(SearchLegalProceedingsResponse, search, path=["response"])

    @parametrize
    def test_method_legal_proceedings_with_all_params(self, client: EndexCrunchbase) -> None:
        search = client.searches.legal_proceedings(
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
        assert_matches_type(SearchLegalProceedingsResponse, search, path=["response"])

    @parametrize
    def test_raw_response_legal_proceedings(self, client: EndexCrunchbase) -> None:
        response = client.searches.with_raw_response.legal_proceedings(
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
        search = response.parse()
        assert_matches_type(SearchLegalProceedingsResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_legal_proceedings(self, client: EndexCrunchbase) -> None:
        with client.searches.with_streaming_response.legal_proceedings(
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

            search = response.parse()
            assert_matches_type(SearchLegalProceedingsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_partnership_announcements(self, client: EndexCrunchbase) -> None:
        search = client.searches.partnership_announcements(
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
        assert_matches_type(SearchPartnershipAnnouncementsResponse, search, path=["response"])

    @parametrize
    def test_method_partnership_announcements_with_all_params(self, client: EndexCrunchbase) -> None:
        search = client.searches.partnership_announcements(
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
        assert_matches_type(SearchPartnershipAnnouncementsResponse, search, path=["response"])

    @parametrize
    def test_raw_response_partnership_announcements(self, client: EndexCrunchbase) -> None:
        response = client.searches.with_raw_response.partnership_announcements(
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
        search = response.parse()
        assert_matches_type(SearchPartnershipAnnouncementsResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_partnership_announcements(self, client: EndexCrunchbase) -> None:
        with client.searches.with_streaming_response.partnership_announcements(
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

            search = response.parse()
            assert_matches_type(SearchPartnershipAnnouncementsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_principals(self, client: EndexCrunchbase) -> None:
        search = client.searches.principals(
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
        assert_matches_type(SearchPrincipalsResponse, search, path=["response"])

    @parametrize
    def test_method_principals_with_all_params(self, client: EndexCrunchbase) -> None:
        search = client.searches.principals(
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
        assert_matches_type(SearchPrincipalsResponse, search, path=["response"])

    @parametrize
    def test_raw_response_principals(self, client: EndexCrunchbase) -> None:
        response = client.searches.with_raw_response.principals(
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
        search = response.parse()
        assert_matches_type(SearchPrincipalsResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_principals(self, client: EndexCrunchbase) -> None:
        with client.searches.with_streaming_response.principals(
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

            search = response.parse()
            assert_matches_type(SearchPrincipalsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_product_launches(self, client: EndexCrunchbase) -> None:
        search = client.searches.product_launches(
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
        assert_matches_type(SearchProductLaunchesResponse, search, path=["response"])

    @parametrize
    def test_method_product_launches_with_all_params(self, client: EndexCrunchbase) -> None:
        search = client.searches.product_launches(
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
        assert_matches_type(SearchProductLaunchesResponse, search, path=["response"])

    @parametrize
    def test_raw_response_product_launches(self, client: EndexCrunchbase) -> None:
        response = client.searches.with_raw_response.product_launches(
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
        search = response.parse()
        assert_matches_type(SearchProductLaunchesResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_product_launches(self, client: EndexCrunchbase) -> None:
        with client.searches.with_streaming_response.product_launches(
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

            search = response.parse()
            assert_matches_type(SearchProductLaunchesResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_products(self, client: EndexCrunchbase) -> None:
        search = client.searches.products(
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
        assert_matches_type(SearchProductsResponse, search, path=["response"])

    @parametrize
    def test_method_products_with_all_params(self, client: EndexCrunchbase) -> None:
        search = client.searches.products(
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
        assert_matches_type(SearchProductsResponse, search, path=["response"])

    @parametrize
    def test_raw_response_products(self, client: EndexCrunchbase) -> None:
        response = client.searches.with_raw_response.products(
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
        search = response.parse()
        assert_matches_type(SearchProductsResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_products(self, client: EndexCrunchbase) -> None:
        with client.searches.with_streaming_response.products(
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

            search = response.parse()
            assert_matches_type(SearchProductsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearches:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_legal_proceedings(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.legal_proceedings(
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
        assert_matches_type(SearchLegalProceedingsResponse, search, path=["response"])

    @parametrize
    async def test_method_legal_proceedings_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.legal_proceedings(
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
        assert_matches_type(SearchLegalProceedingsResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_legal_proceedings(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.searches.with_raw_response.legal_proceedings(
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
        search = await response.parse()
        assert_matches_type(SearchLegalProceedingsResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_legal_proceedings(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.searches.with_streaming_response.legal_proceedings(
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

            search = await response.parse()
            assert_matches_type(SearchLegalProceedingsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_partnership_announcements(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.partnership_announcements(
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
        assert_matches_type(SearchPartnershipAnnouncementsResponse, search, path=["response"])

    @parametrize
    async def test_method_partnership_announcements_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.partnership_announcements(
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
        assert_matches_type(SearchPartnershipAnnouncementsResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_partnership_announcements(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.searches.with_raw_response.partnership_announcements(
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
        search = await response.parse()
        assert_matches_type(SearchPartnershipAnnouncementsResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_partnership_announcements(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.searches.with_streaming_response.partnership_announcements(
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

            search = await response.parse()
            assert_matches_type(SearchPartnershipAnnouncementsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_principals(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.principals(
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
        assert_matches_type(SearchPrincipalsResponse, search, path=["response"])

    @parametrize
    async def test_method_principals_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.principals(
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
        assert_matches_type(SearchPrincipalsResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_principals(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.searches.with_raw_response.principals(
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
        search = await response.parse()
        assert_matches_type(SearchPrincipalsResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_principals(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.searches.with_streaming_response.principals(
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

            search = await response.parse()
            assert_matches_type(SearchPrincipalsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_product_launches(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.product_launches(
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
        assert_matches_type(SearchProductLaunchesResponse, search, path=["response"])

    @parametrize
    async def test_method_product_launches_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.product_launches(
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
        assert_matches_type(SearchProductLaunchesResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_product_launches(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.searches.with_raw_response.product_launches(
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
        search = await response.parse()
        assert_matches_type(SearchProductLaunchesResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_product_launches(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.searches.with_streaming_response.product_launches(
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

            search = await response.parse()
            assert_matches_type(SearchProductLaunchesResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_products(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.products(
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
        assert_matches_type(SearchProductsResponse, search, path=["response"])

    @parametrize
    async def test_method_products_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        search = await async_client.searches.products(
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
        assert_matches_type(SearchProductsResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_products(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.searches.with_raw_response.products(
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
        search = await response.parse()
        assert_matches_type(SearchProductsResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_products(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.searches.with_streaming_response.products(
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

            search = await response.parse()
            assert_matches_type(SearchProductsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
