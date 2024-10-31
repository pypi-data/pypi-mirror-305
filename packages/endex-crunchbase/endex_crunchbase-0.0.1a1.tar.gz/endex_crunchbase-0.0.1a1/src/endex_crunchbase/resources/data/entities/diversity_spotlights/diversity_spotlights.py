# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .cards import (
    CardsResource,
    AsyncCardsResource,
    CardsResourceWithRawResponse,
    AsyncCardsResourceWithRawResponse,
    CardsResourceWithStreamingResponse,
    AsyncCardsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.data.entities import diversity_spotlight_retrieve_params
from .....types.data.entities.diversity_spotlight_retrieve_response import DiversitySpotlightRetrieveResponse

__all__ = ["DiversitySpotlightsResource", "AsyncDiversitySpotlightsResource"]


class DiversitySpotlightsResource(SyncAPIResource):
    @cached_property
    def cards(self) -> CardsResource:
        return CardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DiversitySpotlightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return DiversitySpotlightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiversitySpotlightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return DiversitySpotlightsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        entity_id: str,
        *,
        card_ids: str | NotGiven = NOT_GIVEN,
        field_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiversitySpotlightRetrieveResponse:
        """
        Lookup a DiversitySpotlight

        Args:
          card_ids: Cards to include on the resulting entity - array of card_id strings in JSON
              encoded as string Card Ids for DiversitySpotlight: [fields]

          field_ids: Fields to include on the resulting entity - either an array of field_id strings
              in JSON or a comma-separated list encoded as string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/data/entities/diversity_spotlights/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "card_ids": card_ids,
                        "field_ids": field_ids,
                    },
                    diversity_spotlight_retrieve_params.DiversitySpotlightRetrieveParams,
                ),
            ),
            cast_to=DiversitySpotlightRetrieveResponse,
        )


class AsyncDiversitySpotlightsResource(AsyncAPIResource):
    @cached_property
    def cards(self) -> AsyncCardsResource:
        return AsyncCardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiversitySpotlightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDiversitySpotlightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiversitySpotlightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncDiversitySpotlightsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        entity_id: str,
        *,
        card_ids: str | NotGiven = NOT_GIVEN,
        field_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiversitySpotlightRetrieveResponse:
        """
        Lookup a DiversitySpotlight

        Args:
          card_ids: Cards to include on the resulting entity - array of card_id strings in JSON
              encoded as string Card Ids for DiversitySpotlight: [fields]

          field_ids: Fields to include on the resulting entity - either an array of field_id strings
              in JSON or a comma-separated list encoded as string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/data/entities/diversity_spotlights/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "card_ids": card_ids,
                        "field_ids": field_ids,
                    },
                    diversity_spotlight_retrieve_params.DiversitySpotlightRetrieveParams,
                ),
            ),
            cast_to=DiversitySpotlightRetrieveResponse,
        )


class DiversitySpotlightsResourceWithRawResponse:
    def __init__(self, diversity_spotlights: DiversitySpotlightsResource) -> None:
        self._diversity_spotlights = diversity_spotlights

        self.retrieve = to_raw_response_wrapper(
            diversity_spotlights.retrieve,
        )

    @cached_property
    def cards(self) -> CardsResourceWithRawResponse:
        return CardsResourceWithRawResponse(self._diversity_spotlights.cards)


class AsyncDiversitySpotlightsResourceWithRawResponse:
    def __init__(self, diversity_spotlights: AsyncDiversitySpotlightsResource) -> None:
        self._diversity_spotlights = diversity_spotlights

        self.retrieve = async_to_raw_response_wrapper(
            diversity_spotlights.retrieve,
        )

    @cached_property
    def cards(self) -> AsyncCardsResourceWithRawResponse:
        return AsyncCardsResourceWithRawResponse(self._diversity_spotlights.cards)


class DiversitySpotlightsResourceWithStreamingResponse:
    def __init__(self, diversity_spotlights: DiversitySpotlightsResource) -> None:
        self._diversity_spotlights = diversity_spotlights

        self.retrieve = to_streamed_response_wrapper(
            diversity_spotlights.retrieve,
        )

    @cached_property
    def cards(self) -> CardsResourceWithStreamingResponse:
        return CardsResourceWithStreamingResponse(self._diversity_spotlights.cards)


class AsyncDiversitySpotlightsResourceWithStreamingResponse:
    def __init__(self, diversity_spotlights: AsyncDiversitySpotlightsResource) -> None:
        self._diversity_spotlights = diversity_spotlights

        self.retrieve = async_to_streamed_response_wrapper(
            diversity_spotlights.retrieve,
        )

    @cached_property
    def cards(self) -> AsyncCardsResourceWithStreamingResponse:
        return AsyncCardsResourceWithStreamingResponse(self._diversity_spotlights.cards)
