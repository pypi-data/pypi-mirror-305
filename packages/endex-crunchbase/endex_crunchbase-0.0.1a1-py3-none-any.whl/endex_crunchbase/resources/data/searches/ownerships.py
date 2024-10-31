# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.data.searches import ownership_create_params
from ....types.data.searches.ownership_create_response import OwnershipCreateResponse

__all__ = ["OwnershipsResource", "AsyncOwnershipsResource"]


class OwnershipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OwnershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return OwnershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OwnershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return OwnershipsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        field_ids: List[str],
        query: Iterable[ownership_create_params.Query],
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Iterable[ownership_create_params.Order] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OwnershipCreateResponse:
        """
        Can perform more complex filtering based on the query defined in the request
        body

        Args:
          query: Order in which the search results should be returned

          after_id: Used to paginate search results to the next page. after_id should be the uuid of
              the last item in the current page. May not be provided simultaneously with
              before_id.

          before_id: Used to paginate search results to the previous page. before_id should be the
              uuid of the first item in the current page. May not be provided simultaneously
              with after_id.

          limit: Number of rows to return. Default is 100, min is 1, max is 2000.

          order: Order in which the search results should be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/searches/ownerships",
            body=maybe_transform(
                {
                    "field_ids": field_ids,
                    "query": query,
                    "after_id": after_id,
                    "before_id": before_id,
                    "limit": limit,
                    "order": order,
                },
                ownership_create_params.OwnershipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnershipCreateResponse,
        )


class AsyncOwnershipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOwnershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOwnershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOwnershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncOwnershipsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        field_ids: List[str],
        query: Iterable[ownership_create_params.Query],
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Iterable[ownership_create_params.Order] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OwnershipCreateResponse:
        """
        Can perform more complex filtering based on the query defined in the request
        body

        Args:
          query: Order in which the search results should be returned

          after_id: Used to paginate search results to the next page. after_id should be the uuid of
              the last item in the current page. May not be provided simultaneously with
              before_id.

          before_id: Used to paginate search results to the previous page. before_id should be the
              uuid of the first item in the current page. May not be provided simultaneously
              with after_id.

          limit: Number of rows to return. Default is 100, min is 1, max is 2000.

          order: Order in which the search results should be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/searches/ownerships",
            body=await async_maybe_transform(
                {
                    "field_ids": field_ids,
                    "query": query,
                    "after_id": after_id,
                    "before_id": before_id,
                    "limit": limit,
                    "order": order,
                },
                ownership_create_params.OwnershipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnershipCreateResponse,
        )


class OwnershipsResourceWithRawResponse:
    def __init__(self, ownerships: OwnershipsResource) -> None:
        self._ownerships = ownerships

        self.create = to_raw_response_wrapper(
            ownerships.create,
        )


class AsyncOwnershipsResourceWithRawResponse:
    def __init__(self, ownerships: AsyncOwnershipsResource) -> None:
        self._ownerships = ownerships

        self.create = async_to_raw_response_wrapper(
            ownerships.create,
        )


class OwnershipsResourceWithStreamingResponse:
    def __init__(self, ownerships: OwnershipsResource) -> None:
        self._ownerships = ownerships

        self.create = to_streamed_response_wrapper(
            ownerships.create,
        )


class AsyncOwnershipsResourceWithStreamingResponse:
    def __init__(self, ownerships: AsyncOwnershipsResource) -> None:
        self._ownerships = ownerships

        self.create = async_to_streamed_response_wrapper(
            ownerships.create,
        )
