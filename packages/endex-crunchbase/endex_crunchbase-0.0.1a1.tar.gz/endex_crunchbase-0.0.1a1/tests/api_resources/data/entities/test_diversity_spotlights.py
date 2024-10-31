# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from endex_crunchbase import EndexCrunchbase, AsyncEndexCrunchbase
from endex_crunchbase.types.data.entities import DiversitySpotlightRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiversitySpotlights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: EndexCrunchbase) -> None:
        diversity_spotlight = client.data.entities.diversity_spotlights.retrieve(
            entity_id="entity_id",
        )
        assert_matches_type(DiversitySpotlightRetrieveResponse, diversity_spotlight, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: EndexCrunchbase) -> None:
        diversity_spotlight = client.data.entities.diversity_spotlights.retrieve(
            entity_id="entity_id",
            card_ids="card_ids",
            field_ids="field_ids",
        )
        assert_matches_type(DiversitySpotlightRetrieveResponse, diversity_spotlight, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: EndexCrunchbase) -> None:
        response = client.data.entities.diversity_spotlights.with_raw_response.retrieve(
            entity_id="entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diversity_spotlight = response.parse()
        assert_matches_type(DiversitySpotlightRetrieveResponse, diversity_spotlight, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: EndexCrunchbase) -> None:
        with client.data.entities.diversity_spotlights.with_streaming_response.retrieve(
            entity_id="entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diversity_spotlight = response.parse()
            assert_matches_type(DiversitySpotlightRetrieveResponse, diversity_spotlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: EndexCrunchbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.data.entities.diversity_spotlights.with_raw_response.retrieve(
                entity_id="",
            )


class TestAsyncDiversitySpotlights:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEndexCrunchbase) -> None:
        diversity_spotlight = await async_client.data.entities.diversity_spotlights.retrieve(
            entity_id="entity_id",
        )
        assert_matches_type(DiversitySpotlightRetrieveResponse, diversity_spotlight, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        diversity_spotlight = await async_client.data.entities.diversity_spotlights.retrieve(
            entity_id="entity_id",
            card_ids="card_ids",
            field_ids="field_ids",
        )
        assert_matches_type(DiversitySpotlightRetrieveResponse, diversity_spotlight, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.data.entities.diversity_spotlights.with_raw_response.retrieve(
            entity_id="entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diversity_spotlight = await response.parse()
        assert_matches_type(DiversitySpotlightRetrieveResponse, diversity_spotlight, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.data.entities.diversity_spotlights.with_streaming_response.retrieve(
            entity_id="entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diversity_spotlight = await response.parse()
            assert_matches_type(DiversitySpotlightRetrieveResponse, diversity_spotlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEndexCrunchbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.data.entities.diversity_spotlights.with_raw_response.retrieve(
                entity_id="",
            )
