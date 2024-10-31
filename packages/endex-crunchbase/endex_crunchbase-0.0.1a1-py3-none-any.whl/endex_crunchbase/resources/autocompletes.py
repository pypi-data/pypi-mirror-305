# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import autocomplete_list_params
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
from ..types.autocomplete_list_response import AutocompleteListResponse

__all__ = ["AutocompletesResource", "AsyncAutocompletesResource"]


class AutocompletesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutocompletesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AutocompletesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutocompletesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AutocompletesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        query: str,
        collection_ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutocompleteListResponse:
        """
        Suggests matching Identifier entities based on the query and entity_def_ids
        provided.

        Args:
          query: Value to perform the autocomplete search with.

          collection_ids: A comma separated list of collection ids to search against. Leaving this blank
              means it will search across all identifiers. Entity defs can be constrained to
              specific facets by providing them as facet collections. Relationship collections
              will resolve to their underlying entity def. \\CCollection ids are:
              acquisition_predictions, acquisitions, addresses, awards, categories,
              category_groups, closure_predictions, degrees, diversity_spotlights,
              event_appearances, events, funding_predictions, funding_rounds, funds,
              growth_insights, investments, investor_insights, ipo_predictions, ipos, jobs,
              key_employee_changes, layoffs, legal_proceedings, locations, organizations,
              ownerships, partnership_announcements, people, press_references, principals,
              product_launches, products

          limit: Number of results to retrieve; default = 10, max = 25

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data/autocompletes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "collection_ids": collection_ids,
                        "limit": limit,
                    },
                    autocomplete_list_params.AutocompleteListParams,
                ),
            ),
            cast_to=AutocompleteListResponse,
        )


class AsyncAutocompletesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutocompletesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutocompletesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutocompletesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncAutocompletesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        query: str,
        collection_ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutocompleteListResponse:
        """
        Suggests matching Identifier entities based on the query and entity_def_ids
        provided.

        Args:
          query: Value to perform the autocomplete search with.

          collection_ids: A comma separated list of collection ids to search against. Leaving this blank
              means it will search across all identifiers. Entity defs can be constrained to
              specific facets by providing them as facet collections. Relationship collections
              will resolve to their underlying entity def. \\CCollection ids are:
              acquisition_predictions, acquisitions, addresses, awards, categories,
              category_groups, closure_predictions, degrees, diversity_spotlights,
              event_appearances, events, funding_predictions, funding_rounds, funds,
              growth_insights, investments, investor_insights, ipo_predictions, ipos, jobs,
              key_employee_changes, layoffs, legal_proceedings, locations, organizations,
              ownerships, partnership_announcements, people, press_references, principals,
              product_launches, products

          limit: Number of results to retrieve; default = 10, max = 25

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data/autocompletes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "collection_ids": collection_ids,
                        "limit": limit,
                    },
                    autocomplete_list_params.AutocompleteListParams,
                ),
            ),
            cast_to=AutocompleteListResponse,
        )


class AutocompletesResourceWithRawResponse:
    def __init__(self, autocompletes: AutocompletesResource) -> None:
        self._autocompletes = autocompletes

        self.list = to_raw_response_wrapper(
            autocompletes.list,
        )


class AsyncAutocompletesResourceWithRawResponse:
    def __init__(self, autocompletes: AsyncAutocompletesResource) -> None:
        self._autocompletes = autocompletes

        self.list = async_to_raw_response_wrapper(
            autocompletes.list,
        )


class AutocompletesResourceWithStreamingResponse:
    def __init__(self, autocompletes: AutocompletesResource) -> None:
        self._autocompletes = autocompletes

        self.list = to_streamed_response_wrapper(
            autocompletes.list,
        )


class AsyncAutocompletesResourceWithStreamingResponse:
    def __init__(self, autocompletes: AsyncAutocompletesResource) -> None:
        self._autocompletes = autocompletes

        self.list = async_to_streamed_response_wrapper(
            autocompletes.list,
        )
