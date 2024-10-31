# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import deleted_entity_list_params, deleted_entity_retrieve_params
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
from ..types.deleted_entity_list_response import DeletedEntityListResponse
from ..types.deleted_entity_retrieve_response import DeletedEntityRetrieveResponse

__all__ = ["DeletedEntitiesResource", "AsyncDeletedEntitiesResource"]


class DeletedEntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeletedEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return DeletedEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeletedEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return DeletedEntitiesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        collection_id: str,
        *,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        deleted_at_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedEntityRetrieveResponse:
        """
        Retrieve deleted entities.

        Args:
          after_id: Used to paginate search results to the next page. after_id should be the uuid of
              the last item in the current page. May not be provided simultaneously with
              before_id.

          before_id: Used to paginate search results to the previous page. before_id should be the
              uuid of the first item in the current page. May not be provided simultaneously
              with after_id

          deleted_at_order: Direction of sorting by deleted_at property

          limit: Number of results to retrieve; default = 10, max = 25

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._get(
            f"/data/deleted_entities/{collection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_id": after_id,
                        "before_id": before_id,
                        "deleted_at_order": deleted_at_order,
                        "limit": limit,
                    },
                    deleted_entity_retrieve_params.DeletedEntityRetrieveParams,
                ),
            ),
            cast_to=DeletedEntityRetrieveResponse,
        )

    def list(
        self,
        *,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        collection_ids: str | NotGiven = NOT_GIVEN,
        deleted_at_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedEntityListResponse:
        """
        Retrieve deleted entities.

        Args:
          after_id: Used to paginate search results to the next page. after_id should be the uuid of
              the last item in the current page. May not be provided simultaneously with
              before_id.

          before_id: Used to paginate search results to the previous page. before_id should be the
              uuid of the first item in the current page. May not be provided simultaneously
              with after_id

          collection_ids: Filter by collection id(s). Comma separated list of collection ids. E.g.
              organizations, people, funding_rounds, acquisitions, investments, events,
              press_references, funds, event_appearances, ipos, ownerships, categories,
              locations, jobs

          deleted_at_order: Direction of sorting by deleted_at property

          limit: Number of results to retrieve; default = 10, max = 25

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data/deleted_entities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_id": after_id,
                        "before_id": before_id,
                        "collection_ids": collection_ids,
                        "deleted_at_order": deleted_at_order,
                        "limit": limit,
                    },
                    deleted_entity_list_params.DeletedEntityListParams,
                ),
            ),
            cast_to=DeletedEntityListResponse,
        )


class AsyncDeletedEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeletedEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeletedEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeletedEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncDeletedEntitiesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        collection_id: str,
        *,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        deleted_at_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedEntityRetrieveResponse:
        """
        Retrieve deleted entities.

        Args:
          after_id: Used to paginate search results to the next page. after_id should be the uuid of
              the last item in the current page. May not be provided simultaneously with
              before_id.

          before_id: Used to paginate search results to the previous page. before_id should be the
              uuid of the first item in the current page. May not be provided simultaneously
              with after_id

          deleted_at_order: Direction of sorting by deleted_at property

          limit: Number of results to retrieve; default = 10, max = 25

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._get(
            f"/data/deleted_entities/{collection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_id": after_id,
                        "before_id": before_id,
                        "deleted_at_order": deleted_at_order,
                        "limit": limit,
                    },
                    deleted_entity_retrieve_params.DeletedEntityRetrieveParams,
                ),
            ),
            cast_to=DeletedEntityRetrieveResponse,
        )

    async def list(
        self,
        *,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        collection_ids: str | NotGiven = NOT_GIVEN,
        deleted_at_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedEntityListResponse:
        """
        Retrieve deleted entities.

        Args:
          after_id: Used to paginate search results to the next page. after_id should be the uuid of
              the last item in the current page. May not be provided simultaneously with
              before_id.

          before_id: Used to paginate search results to the previous page. before_id should be the
              uuid of the first item in the current page. May not be provided simultaneously
              with after_id

          collection_ids: Filter by collection id(s). Comma separated list of collection ids. E.g.
              organizations, people, funding_rounds, acquisitions, investments, events,
              press_references, funds, event_appearances, ipos, ownerships, categories,
              locations, jobs

          deleted_at_order: Direction of sorting by deleted_at property

          limit: Number of results to retrieve; default = 10, max = 25

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data/deleted_entities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_id": after_id,
                        "before_id": before_id,
                        "collection_ids": collection_ids,
                        "deleted_at_order": deleted_at_order,
                        "limit": limit,
                    },
                    deleted_entity_list_params.DeletedEntityListParams,
                ),
            ),
            cast_to=DeletedEntityListResponse,
        )


class DeletedEntitiesResourceWithRawResponse:
    def __init__(self, deleted_entities: DeletedEntitiesResource) -> None:
        self._deleted_entities = deleted_entities

        self.retrieve = to_raw_response_wrapper(
            deleted_entities.retrieve,
        )
        self.list = to_raw_response_wrapper(
            deleted_entities.list,
        )


class AsyncDeletedEntitiesResourceWithRawResponse:
    def __init__(self, deleted_entities: AsyncDeletedEntitiesResource) -> None:
        self._deleted_entities = deleted_entities

        self.retrieve = async_to_raw_response_wrapper(
            deleted_entities.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            deleted_entities.list,
        )


class DeletedEntitiesResourceWithStreamingResponse:
    def __init__(self, deleted_entities: DeletedEntitiesResource) -> None:
        self._deleted_entities = deleted_entities

        self.retrieve = to_streamed_response_wrapper(
            deleted_entities.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            deleted_entities.list,
        )


class AsyncDeletedEntitiesResourceWithStreamingResponse:
    def __init__(self, deleted_entities: AsyncDeletedEntitiesResource) -> None:
        self._deleted_entities = deleted_entities

        self.retrieve = async_to_streamed_response_wrapper(
            deleted_entities.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            deleted_entities.list,
        )
