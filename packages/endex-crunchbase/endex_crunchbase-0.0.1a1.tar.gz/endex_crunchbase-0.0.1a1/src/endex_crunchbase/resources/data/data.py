# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .entities import (
    EntitiesResource,
    AsyncEntitiesResource,
    EntitiesResourceWithRawResponse,
    AsyncEntitiesResourceWithRawResponse,
    EntitiesResourceWithStreamingResponse,
    AsyncEntitiesResourceWithStreamingResponse,
)
from .searches import (
    SearchesResource,
    AsyncSearchesResource,
    SearchesResourceWithRawResponse,
    AsyncSearchesResourceWithRawResponse,
    SearchesResourceWithStreamingResponse,
    AsyncSearchesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .entities.entities import EntitiesResource, AsyncEntitiesResource
from .searches.searches import SearchesResource, AsyncSearchesResource

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def entities(self) -> EntitiesResource:
        return EntitiesResource(self._client)

    @cached_property
    def searches(self) -> SearchesResource:
        return SearchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return DataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return DataResourceWithStreamingResponse(self)


class AsyncDataResource(AsyncAPIResource):
    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        return AsyncEntitiesResource(self._client)

    @cached_property
    def searches(self) -> AsyncSearchesResource:
        return AsyncSearchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncDataResourceWithStreamingResponse(self)


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

    @cached_property
    def entities(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self._data.entities)

    @cached_property
    def searches(self) -> SearchesResourceWithRawResponse:
        return SearchesResourceWithRawResponse(self._data.searches)


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self._data.entities)

    @cached_property
    def searches(self) -> AsyncSearchesResourceWithRawResponse:
        return AsyncSearchesResourceWithRawResponse(self._data.searches)


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

    @cached_property
    def entities(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self._data.entities)

    @cached_property
    def searches(self) -> SearchesResourceWithStreamingResponse:
        return SearchesResourceWithStreamingResponse(self._data.searches)


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self._data.entities)

    @cached_property
    def searches(self) -> AsyncSearchesResourceWithStreamingResponse:
        return AsyncSearchesResourceWithStreamingResponse(self._data.searches)
