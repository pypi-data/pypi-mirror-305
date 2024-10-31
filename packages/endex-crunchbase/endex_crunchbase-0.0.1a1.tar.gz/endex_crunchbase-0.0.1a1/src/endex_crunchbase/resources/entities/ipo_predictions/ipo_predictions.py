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
from ....types.entities import ipo_prediction_retrieve_params
from ....types.entities.ipo_prediction_retrieve_response import IpoPredictionRetrieveResponse

__all__ = ["IpoPredictionsResource", "AsyncIpoPredictionsResource"]


class IpoPredictionsResource(SyncAPIResource):
    @cached_property
    def cards(self) -> CardsResource:
        return CardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> IpoPredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return IpoPredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IpoPredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return IpoPredictionsResourceWithStreamingResponse(self)

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
    ) -> IpoPredictionRetrieveResponse:
        """
        Lookup an IpoPrediction

        Args:
          card_ids: Cards to include on the resulting entity - array of card_id strings in JSON
              encoded as string Card Ids for IpoPrediction: [fields]

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
            f"/data/entities/ipo_predictions/{entity_id}",
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
                    ipo_prediction_retrieve_params.IpoPredictionRetrieveParams,
                ),
            ),
            cast_to=IpoPredictionRetrieveResponse,
        )


class AsyncIpoPredictionsResource(AsyncAPIResource):
    @cached_property
    def cards(self) -> AsyncCardsResource:
        return AsyncCardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIpoPredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIpoPredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIpoPredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncIpoPredictionsResourceWithStreamingResponse(self)

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
    ) -> IpoPredictionRetrieveResponse:
        """
        Lookup an IpoPrediction

        Args:
          card_ids: Cards to include on the resulting entity - array of card_id strings in JSON
              encoded as string Card Ids for IpoPrediction: [fields]

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
            f"/data/entities/ipo_predictions/{entity_id}",
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
                    ipo_prediction_retrieve_params.IpoPredictionRetrieveParams,
                ),
            ),
            cast_to=IpoPredictionRetrieveResponse,
        )


class IpoPredictionsResourceWithRawResponse:
    def __init__(self, ipo_predictions: IpoPredictionsResource) -> None:
        self._ipo_predictions = ipo_predictions

        self.retrieve = to_raw_response_wrapper(
            ipo_predictions.retrieve,
        )

    @cached_property
    def cards(self) -> CardsResourceWithRawResponse:
        return CardsResourceWithRawResponse(self._ipo_predictions.cards)


class AsyncIpoPredictionsResourceWithRawResponse:
    def __init__(self, ipo_predictions: AsyncIpoPredictionsResource) -> None:
        self._ipo_predictions = ipo_predictions

        self.retrieve = async_to_raw_response_wrapper(
            ipo_predictions.retrieve,
        )

    @cached_property
    def cards(self) -> AsyncCardsResourceWithRawResponse:
        return AsyncCardsResourceWithRawResponse(self._ipo_predictions.cards)


class IpoPredictionsResourceWithStreamingResponse:
    def __init__(self, ipo_predictions: IpoPredictionsResource) -> None:
        self._ipo_predictions = ipo_predictions

        self.retrieve = to_streamed_response_wrapper(
            ipo_predictions.retrieve,
        )

    @cached_property
    def cards(self) -> CardsResourceWithStreamingResponse:
        return CardsResourceWithStreamingResponse(self._ipo_predictions.cards)


class AsyncIpoPredictionsResourceWithStreamingResponse:
    def __init__(self, ipo_predictions: AsyncIpoPredictionsResource) -> None:
        self._ipo_predictions = ipo_predictions

        self.retrieve = async_to_streamed_response_wrapper(
            ipo_predictions.retrieve,
        )

    @cached_property
    def cards(self) -> AsyncCardsResourceWithStreamingResponse:
        return AsyncCardsResourceWithStreamingResponse(self._ipo_predictions.cards)
