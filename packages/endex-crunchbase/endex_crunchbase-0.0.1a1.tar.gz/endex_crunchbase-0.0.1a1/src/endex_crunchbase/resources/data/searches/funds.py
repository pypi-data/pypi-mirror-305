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
from ....types.data.searches import fund_create_params
from ....types.data.searches.fund_create_response import FundCreateResponse

__all__ = ["FundsResource", "AsyncFundsResource"]


class FundsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return FundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return FundsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        field_ids: List[str],
        query: Iterable[fund_create_params.Query],
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Iterable[fund_create_params.Order] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FundCreateResponse:
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
            "/data/searches/funds",
            body=maybe_transform(
                {
                    "field_ids": field_ids,
                    "query": query,
                    "after_id": after_id,
                    "before_id": before_id,
                    "limit": limit,
                    "order": order,
                },
                fund_create_params.FundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundCreateResponse,
        )


class AsyncFundsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncFundsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        field_ids: List[str],
        query: Iterable[fund_create_params.Query],
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Iterable[fund_create_params.Order] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FundCreateResponse:
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
            "/data/searches/funds",
            body=await async_maybe_transform(
                {
                    "field_ids": field_ids,
                    "query": query,
                    "after_id": after_id,
                    "before_id": before_id,
                    "limit": limit,
                    "order": order,
                },
                fund_create_params.FundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundCreateResponse,
        )


class FundsResourceWithRawResponse:
    def __init__(self, funds: FundsResource) -> None:
        self._funds = funds

        self.create = to_raw_response_wrapper(
            funds.create,
        )


class AsyncFundsResourceWithRawResponse:
    def __init__(self, funds: AsyncFundsResource) -> None:
        self._funds = funds

        self.create = async_to_raw_response_wrapper(
            funds.create,
        )


class FundsResourceWithStreamingResponse:
    def __init__(self, funds: FundsResource) -> None:
        self._funds = funds

        self.create = to_streamed_response_wrapper(
            funds.create,
        )


class AsyncFundsResourceWithStreamingResponse:
    def __init__(self, funds: AsyncFundsResource) -> None:
        self._funds = funds

        self.create = async_to_streamed_response_wrapper(
            funds.create,
        )
