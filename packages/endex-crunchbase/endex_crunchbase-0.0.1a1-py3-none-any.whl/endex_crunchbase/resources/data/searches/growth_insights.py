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
from ....types.data.searches import growth_insight_create_params
from ....types.data.searches.growth_insight_create_response import GrowthInsightCreateResponse

__all__ = ["GrowthInsightsResource", "AsyncGrowthInsightsResource"]


class GrowthInsightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GrowthInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return GrowthInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GrowthInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return GrowthInsightsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        field_ids: List[str],
        query: Iterable[growth_insight_create_params.Query],
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Iterable[growth_insight_create_params.Order] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GrowthInsightCreateResponse:
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
            "/data/searches/growth_insights",
            body=maybe_transform(
                {
                    "field_ids": field_ids,
                    "query": query,
                    "after_id": after_id,
                    "before_id": before_id,
                    "limit": limit,
                    "order": order,
                },
                growth_insight_create_params.GrowthInsightCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrowthInsightCreateResponse,
        )


class AsyncGrowthInsightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGrowthInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGrowthInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGrowthInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncGrowthInsightsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        field_ids: List[str],
        query: Iterable[growth_insight_create_params.Query],
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Iterable[growth_insight_create_params.Order] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GrowthInsightCreateResponse:
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
            "/data/searches/growth_insights",
            body=await async_maybe_transform(
                {
                    "field_ids": field_ids,
                    "query": query,
                    "after_id": after_id,
                    "before_id": before_id,
                    "limit": limit,
                    "order": order,
                },
                growth_insight_create_params.GrowthInsightCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrowthInsightCreateResponse,
        )


class GrowthInsightsResourceWithRawResponse:
    def __init__(self, growth_insights: GrowthInsightsResource) -> None:
        self._growth_insights = growth_insights

        self.create = to_raw_response_wrapper(
            growth_insights.create,
        )


class AsyncGrowthInsightsResourceWithRawResponse:
    def __init__(self, growth_insights: AsyncGrowthInsightsResource) -> None:
        self._growth_insights = growth_insights

        self.create = async_to_raw_response_wrapper(
            growth_insights.create,
        )


class GrowthInsightsResourceWithStreamingResponse:
    def __init__(self, growth_insights: GrowthInsightsResource) -> None:
        self._growth_insights = growth_insights

        self.create = to_streamed_response_wrapper(
            growth_insights.create,
        )


class AsyncGrowthInsightsResourceWithStreamingResponse:
    def __init__(self, growth_insights: AsyncGrowthInsightsResource) -> None:
        self._growth_insights = growth_insights

        self.create = async_to_streamed_response_wrapper(
            growth_insights.create,
        )
