# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.entities import principal_retrieve_params
from ...types.entities.principal_retrieve_response import PrincipalRetrieveResponse

__all__ = ["PrincipalsResource", "AsyncPrincipalsResource"]


class PrincipalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrincipalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return PrincipalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrincipalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return PrincipalsResourceWithStreamingResponse(self)

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
    ) -> PrincipalRetrieveResponse:
        """
        Lookup a Principal

        Args:
          card_ids: Principal entity doesn't have any cards

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
            f"/data/entities/principals/{entity_id}",
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
                    principal_retrieve_params.PrincipalRetrieveParams,
                ),
            ),
            cast_to=PrincipalRetrieveResponse,
        )


class AsyncPrincipalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrincipalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrincipalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrincipalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncPrincipalsResourceWithStreamingResponse(self)

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
    ) -> PrincipalRetrieveResponse:
        """
        Lookup a Principal

        Args:
          card_ids: Principal entity doesn't have any cards

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
            f"/data/entities/principals/{entity_id}",
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
                    principal_retrieve_params.PrincipalRetrieveParams,
                ),
            ),
            cast_to=PrincipalRetrieveResponse,
        )


class PrincipalsResourceWithRawResponse:
    def __init__(self, principals: PrincipalsResource) -> None:
        self._principals = principals

        self.retrieve = to_raw_response_wrapper(
            principals.retrieve,
        )


class AsyncPrincipalsResourceWithRawResponse:
    def __init__(self, principals: AsyncPrincipalsResource) -> None:
        self._principals = principals

        self.retrieve = async_to_raw_response_wrapper(
            principals.retrieve,
        )


class PrincipalsResourceWithStreamingResponse:
    def __init__(self, principals: PrincipalsResource) -> None:
        self._principals = principals

        self.retrieve = to_streamed_response_wrapper(
            principals.retrieve,
        )


class AsyncPrincipalsResourceWithStreamingResponse:
    def __init__(self, principals: AsyncPrincipalsResource) -> None:
        self._principals = principals

        self.retrieve = async_to_streamed_response_wrapper(
            principals.retrieve,
        )
