# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from endex_crunchbase import EndexCrunchbase, AsyncEndexCrunchbase
from endex_crunchbase.types import (
    DeletedEntityListResponse,
    DeletedEntityRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeletedEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: EndexCrunchbase) -> None:
        deleted_entity = client.deleted_entities.retrieve(
            collection_id="collection_id",
        )
        assert_matches_type(DeletedEntityRetrieveResponse, deleted_entity, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: EndexCrunchbase) -> None:
        deleted_entity = client.deleted_entities.retrieve(
            collection_id="collection_id",
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            deleted_at_order="asc",
            limit=0,
        )
        assert_matches_type(DeletedEntityRetrieveResponse, deleted_entity, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: EndexCrunchbase) -> None:
        response = client.deleted_entities.with_raw_response.retrieve(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted_entity = response.parse()
        assert_matches_type(DeletedEntityRetrieveResponse, deleted_entity, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: EndexCrunchbase) -> None:
        with client.deleted_entities.with_streaming_response.retrieve(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted_entity = response.parse()
            assert_matches_type(DeletedEntityRetrieveResponse, deleted_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: EndexCrunchbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.deleted_entities.with_raw_response.retrieve(
                collection_id="",
            )

    @parametrize
    def test_method_list(self, client: EndexCrunchbase) -> None:
        deleted_entity = client.deleted_entities.list()
        assert_matches_type(DeletedEntityListResponse, deleted_entity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: EndexCrunchbase) -> None:
        deleted_entity = client.deleted_entities.list(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_ids="collection_ids",
            deleted_at_order="asc",
            limit=0,
        )
        assert_matches_type(DeletedEntityListResponse, deleted_entity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: EndexCrunchbase) -> None:
        response = client.deleted_entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted_entity = response.parse()
        assert_matches_type(DeletedEntityListResponse, deleted_entity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: EndexCrunchbase) -> None:
        with client.deleted_entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted_entity = response.parse()
            assert_matches_type(DeletedEntityListResponse, deleted_entity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeletedEntities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEndexCrunchbase) -> None:
        deleted_entity = await async_client.deleted_entities.retrieve(
            collection_id="collection_id",
        )
        assert_matches_type(DeletedEntityRetrieveResponse, deleted_entity, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        deleted_entity = await async_client.deleted_entities.retrieve(
            collection_id="collection_id",
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            deleted_at_order="asc",
            limit=0,
        )
        assert_matches_type(DeletedEntityRetrieveResponse, deleted_entity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.deleted_entities.with_raw_response.retrieve(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted_entity = await response.parse()
        assert_matches_type(DeletedEntityRetrieveResponse, deleted_entity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.deleted_entities.with_streaming_response.retrieve(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted_entity = await response.parse()
            assert_matches_type(DeletedEntityRetrieveResponse, deleted_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEndexCrunchbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.deleted_entities.with_raw_response.retrieve(
                collection_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEndexCrunchbase) -> None:
        deleted_entity = await async_client.deleted_entities.list()
        assert_matches_type(DeletedEntityListResponse, deleted_entity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEndexCrunchbase) -> None:
        deleted_entity = await async_client.deleted_entities.list(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_ids="collection_ids",
            deleted_at_order="asc",
            limit=0,
        )
        assert_matches_type(DeletedEntityListResponse, deleted_entity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEndexCrunchbase) -> None:
        response = await async_client.deleted_entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted_entity = await response.parse()
        assert_matches_type(DeletedEntityListResponse, deleted_entity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEndexCrunchbase) -> None:
        async with async_client.deleted_entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted_entity = await response.parse()
            assert_matches_type(DeletedEntityListResponse, deleted_entity, path=["response"])

        assert cast(Any, response.is_closed) is True
