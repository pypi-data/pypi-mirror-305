# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.entities.layoffs import card_retrieve_params
from ....types.entities.layoffs.card_retrieve_response import CardRetrieveResponse

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return CardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return CardsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        card_id: str,
        *,
        entity_id: str,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        card_field_ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardRetrieveResponse:
        """
        The following cards are available: [fields]

        Args:
          after_id: Lookup uuid of the last item in the previous page (not required for first page).
              Used to iterate a card's results starting at the beginning of the ordered set
              and moving forward. Suitable for implementing "next page" functionality. May not
              be provided simultaneously with before_id.

          before_id: Lookup uuid of the first item in the previous page (not required for first
              page). Used to iterate a card's results starting at the end of the ordered set
              and moving backward. Suitable for implementing "previous page" functionality.
              May not be provided simultaneously with after_id.

          card_field_ids: Card fields to include on the specified card - array of field_id strings in JSON
              encoded as string

          limit: Number of rows to return. Default is 100, min is 1, max is 100.

          order: Field name with order direction (asc/desc)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            f"/data/entities/layoffs/{entity_id}/cards/{card_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_id": after_id,
                        "before_id": before_id,
                        "card_field_ids": card_field_ids,
                        "limit": limit,
                        "order": order,
                    },
                    card_retrieve_params.CardRetrieveParams,
                ),
            ),
            cast_to=CardRetrieveResponse,
        )


class AsyncCardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncCardsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        card_id: str,
        *,
        entity_id: str,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        card_field_ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardRetrieveResponse:
        """
        The following cards are available: [fields]

        Args:
          after_id: Lookup uuid of the last item in the previous page (not required for first page).
              Used to iterate a card's results starting at the beginning of the ordered set
              and moving forward. Suitable for implementing "next page" functionality. May not
              be provided simultaneously with before_id.

          before_id: Lookup uuid of the first item in the previous page (not required for first
              page). Used to iterate a card's results starting at the end of the ordered set
              and moving backward. Suitable for implementing "previous page" functionality.
              May not be provided simultaneously with after_id.

          card_field_ids: Card fields to include on the specified card - array of field_id strings in JSON
              encoded as string

          limit: Number of rows to return. Default is 100, min is 1, max is 100.

          order: Field name with order direction (asc/desc)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            f"/data/entities/layoffs/{entity_id}/cards/{card_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_id": after_id,
                        "before_id": before_id,
                        "card_field_ids": card_field_ids,
                        "limit": limit,
                        "order": order,
                    },
                    card_retrieve_params.CardRetrieveParams,
                ),
            ),
            cast_to=CardRetrieveResponse,
        )


class CardsResourceWithRawResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.retrieve = to_raw_response_wrapper(
            cards.retrieve,
        )


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.retrieve = async_to_raw_response_wrapper(
            cards.retrieve,
        )


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.retrieve = to_streamed_response_wrapper(
            cards.retrieve,
        )


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.retrieve = async_to_streamed_response_wrapper(
            cards.retrieve,
        )
