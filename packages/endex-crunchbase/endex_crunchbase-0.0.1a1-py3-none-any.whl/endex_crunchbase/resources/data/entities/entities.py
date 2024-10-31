# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .degrees import (
    DegreesResource,
    AsyncDegreesResource,
    DegreesResourceWithRawResponse,
    AsyncDegreesResourceWithRawResponse,
    DegreesResourceWithStreamingResponse,
    AsyncDegreesResourceWithStreamingResponse,
)
from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from .jobs.jobs import JobsResource, AsyncJobsResource
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from .ownerships import (
    OwnershipsResource,
    AsyncOwnershipsResource,
    OwnershipsResourceWithRawResponse,
    AsyncOwnershipsResourceWithRawResponse,
    OwnershipsResourceWithStreamingResponse,
    AsyncOwnershipsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .category_groups import (
    CategoryGroupsResource,
    AsyncCategoryGroupsResource,
    CategoryGroupsResourceWithRawResponse,
    AsyncCategoryGroupsResourceWithRawResponse,
    CategoryGroupsResourceWithStreamingResponse,
    AsyncCategoryGroupsResourceWithStreamingResponse,
)
from .degrees.degrees import DegreesResource, AsyncDegreesResource
from .growth_insights import (
    GrowthInsightsResource,
    AsyncGrowthInsightsResource,
    GrowthInsightsResourceWithRawResponse,
    AsyncGrowthInsightsResourceWithRawResponse,
    GrowthInsightsResourceWithStreamingResponse,
    AsyncGrowthInsightsResourceWithStreamingResponse,
)
from .product_launches import (
    ProductLaunchesResource,
    AsyncProductLaunchesResource,
    ProductLaunchesResourceWithRawResponse,
    AsyncProductLaunchesResourceWithRawResponse,
    ProductLaunchesResourceWithStreamingResponse,
    AsyncProductLaunchesResourceWithStreamingResponse,
)
from .products.products import ProductsResource, AsyncProductsResource
from .closure_predictions import (
    ClosurePredictionsResource,
    AsyncClosurePredictionsResource,
    ClosurePredictionsResourceWithRawResponse,
    AsyncClosurePredictionsResourceWithRawResponse,
    ClosurePredictionsResourceWithStreamingResponse,
    AsyncClosurePredictionsResourceWithStreamingResponse,
)
from .funding_predictions import (
    FundingPredictionsResource,
    AsyncFundingPredictionsResource,
    FundingPredictionsResourceWithRawResponse,
    AsyncFundingPredictionsResourceWithRawResponse,
    FundingPredictionsResourceWithStreamingResponse,
    AsyncFundingPredictionsResourceWithStreamingResponse,
)
from .locations.locations import LocationsResource, AsyncLocationsResource
from .diversity_spotlights import (
    DiversitySpotlightsResource,
    AsyncDiversitySpotlightsResource,
    DiversitySpotlightsResourceWithRawResponse,
    AsyncDiversitySpotlightsResourceWithRawResponse,
    DiversitySpotlightsResourceWithStreamingResponse,
    AsyncDiversitySpotlightsResourceWithStreamingResponse,
)
from .categories.categories import CategoriesResource, AsyncCategoriesResource
from .ownerships.ownerships import OwnershipsResource, AsyncOwnershipsResource
from .category_groups.category_groups import CategoryGroupsResource, AsyncCategoryGroupsResource
from .growth_insights.growth_insights import GrowthInsightsResource, AsyncGrowthInsightsResource
from .product_launches.product_launches import ProductLaunchesResource, AsyncProductLaunchesResource
from .closure_predictions.closure_predictions import ClosurePredictionsResource, AsyncClosurePredictionsResource
from .funding_predictions.funding_predictions import FundingPredictionsResource, AsyncFundingPredictionsResource
from .diversity_spotlights.diversity_spotlights import DiversitySpotlightsResource, AsyncDiversitySpotlightsResource

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def ownerships(self) -> OwnershipsResource:
        return OwnershipsResource(self._client)

    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def category_groups(self) -> CategoryGroupsResource:
        return CategoryGroupsResource(self._client)

    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def closure_predictions(self) -> ClosurePredictionsResource:
        return ClosurePredictionsResource(self._client)

    @cached_property
    def degrees(self) -> DegreesResource:
        return DegreesResource(self._client)

    @cached_property
    def diversity_spotlights(self) -> DiversitySpotlightsResource:
        return DiversitySpotlightsResource(self._client)

    @cached_property
    def funding_predictions(self) -> FundingPredictionsResource:
        return FundingPredictionsResource(self._client)

    @cached_property
    def growth_insights(self) -> GrowthInsightsResource:
        return GrowthInsightsResource(self._client)

    @cached_property
    def products(self) -> ProductsResource:
        return ProductsResource(self._client)

    @cached_property
    def product_launches(self) -> ProductLaunchesResource:
        return ProductLaunchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def ownerships(self) -> AsyncOwnershipsResource:
        return AsyncOwnershipsResource(self._client)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def category_groups(self) -> AsyncCategoryGroupsResource:
        return AsyncCategoryGroupsResource(self._client)

    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def closure_predictions(self) -> AsyncClosurePredictionsResource:
        return AsyncClosurePredictionsResource(self._client)

    @cached_property
    def degrees(self) -> AsyncDegreesResource:
        return AsyncDegreesResource(self._client)

    @cached_property
    def diversity_spotlights(self) -> AsyncDiversitySpotlightsResource:
        return AsyncDiversitySpotlightsResource(self._client)

    @cached_property
    def funding_predictions(self) -> AsyncFundingPredictionsResource:
        return AsyncFundingPredictionsResource(self._client)

    @cached_property
    def growth_insights(self) -> AsyncGrowthInsightsResource:
        return AsyncGrowthInsightsResource(self._client)

    @cached_property
    def products(self) -> AsyncProductsResource:
        return AsyncProductsResource(self._client)

    @cached_property
    def product_launches(self) -> AsyncProductLaunchesResource:
        return AsyncProductLaunchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def ownerships(self) -> OwnershipsResourceWithRawResponse:
        return OwnershipsResourceWithRawResponse(self._entities.ownerships)

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._entities.categories)

    @cached_property
    def category_groups(self) -> CategoryGroupsResourceWithRawResponse:
        return CategoryGroupsResourceWithRawResponse(self._entities.category_groups)

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._entities.locations)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._entities.jobs)

    @cached_property
    def closure_predictions(self) -> ClosurePredictionsResourceWithRawResponse:
        return ClosurePredictionsResourceWithRawResponse(self._entities.closure_predictions)

    @cached_property
    def degrees(self) -> DegreesResourceWithRawResponse:
        return DegreesResourceWithRawResponse(self._entities.degrees)

    @cached_property
    def diversity_spotlights(self) -> DiversitySpotlightsResourceWithRawResponse:
        return DiversitySpotlightsResourceWithRawResponse(self._entities.diversity_spotlights)

    @cached_property
    def funding_predictions(self) -> FundingPredictionsResourceWithRawResponse:
        return FundingPredictionsResourceWithRawResponse(self._entities.funding_predictions)

    @cached_property
    def growth_insights(self) -> GrowthInsightsResourceWithRawResponse:
        return GrowthInsightsResourceWithRawResponse(self._entities.growth_insights)

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        return ProductsResourceWithRawResponse(self._entities.products)

    @cached_property
    def product_launches(self) -> ProductLaunchesResourceWithRawResponse:
        return ProductLaunchesResourceWithRawResponse(self._entities.product_launches)


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def ownerships(self) -> AsyncOwnershipsResourceWithRawResponse:
        return AsyncOwnershipsResourceWithRawResponse(self._entities.ownerships)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._entities.categories)

    @cached_property
    def category_groups(self) -> AsyncCategoryGroupsResourceWithRawResponse:
        return AsyncCategoryGroupsResourceWithRawResponse(self._entities.category_groups)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._entities.locations)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._entities.jobs)

    @cached_property
    def closure_predictions(self) -> AsyncClosurePredictionsResourceWithRawResponse:
        return AsyncClosurePredictionsResourceWithRawResponse(self._entities.closure_predictions)

    @cached_property
    def degrees(self) -> AsyncDegreesResourceWithRawResponse:
        return AsyncDegreesResourceWithRawResponse(self._entities.degrees)

    @cached_property
    def diversity_spotlights(self) -> AsyncDiversitySpotlightsResourceWithRawResponse:
        return AsyncDiversitySpotlightsResourceWithRawResponse(self._entities.diversity_spotlights)

    @cached_property
    def funding_predictions(self) -> AsyncFundingPredictionsResourceWithRawResponse:
        return AsyncFundingPredictionsResourceWithRawResponse(self._entities.funding_predictions)

    @cached_property
    def growth_insights(self) -> AsyncGrowthInsightsResourceWithRawResponse:
        return AsyncGrowthInsightsResourceWithRawResponse(self._entities.growth_insights)

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        return AsyncProductsResourceWithRawResponse(self._entities.products)

    @cached_property
    def product_launches(self) -> AsyncProductLaunchesResourceWithRawResponse:
        return AsyncProductLaunchesResourceWithRawResponse(self._entities.product_launches)


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def ownerships(self) -> OwnershipsResourceWithStreamingResponse:
        return OwnershipsResourceWithStreamingResponse(self._entities.ownerships)

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._entities.categories)

    @cached_property
    def category_groups(self) -> CategoryGroupsResourceWithStreamingResponse:
        return CategoryGroupsResourceWithStreamingResponse(self._entities.category_groups)

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._entities.locations)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._entities.jobs)

    @cached_property
    def closure_predictions(self) -> ClosurePredictionsResourceWithStreamingResponse:
        return ClosurePredictionsResourceWithStreamingResponse(self._entities.closure_predictions)

    @cached_property
    def degrees(self) -> DegreesResourceWithStreamingResponse:
        return DegreesResourceWithStreamingResponse(self._entities.degrees)

    @cached_property
    def diversity_spotlights(self) -> DiversitySpotlightsResourceWithStreamingResponse:
        return DiversitySpotlightsResourceWithStreamingResponse(self._entities.diversity_spotlights)

    @cached_property
    def funding_predictions(self) -> FundingPredictionsResourceWithStreamingResponse:
        return FundingPredictionsResourceWithStreamingResponse(self._entities.funding_predictions)

    @cached_property
    def growth_insights(self) -> GrowthInsightsResourceWithStreamingResponse:
        return GrowthInsightsResourceWithStreamingResponse(self._entities.growth_insights)

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        return ProductsResourceWithStreamingResponse(self._entities.products)

    @cached_property
    def product_launches(self) -> ProductLaunchesResourceWithStreamingResponse:
        return ProductLaunchesResourceWithStreamingResponse(self._entities.product_launches)


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def ownerships(self) -> AsyncOwnershipsResourceWithStreamingResponse:
        return AsyncOwnershipsResourceWithStreamingResponse(self._entities.ownerships)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._entities.categories)

    @cached_property
    def category_groups(self) -> AsyncCategoryGroupsResourceWithStreamingResponse:
        return AsyncCategoryGroupsResourceWithStreamingResponse(self._entities.category_groups)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._entities.locations)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._entities.jobs)

    @cached_property
    def closure_predictions(self) -> AsyncClosurePredictionsResourceWithStreamingResponse:
        return AsyncClosurePredictionsResourceWithStreamingResponse(self._entities.closure_predictions)

    @cached_property
    def degrees(self) -> AsyncDegreesResourceWithStreamingResponse:
        return AsyncDegreesResourceWithStreamingResponse(self._entities.degrees)

    @cached_property
    def diversity_spotlights(self) -> AsyncDiversitySpotlightsResourceWithStreamingResponse:
        return AsyncDiversitySpotlightsResourceWithStreamingResponse(self._entities.diversity_spotlights)

    @cached_property
    def funding_predictions(self) -> AsyncFundingPredictionsResourceWithStreamingResponse:
        return AsyncFundingPredictionsResourceWithStreamingResponse(self._entities.funding_predictions)

    @cached_property
    def growth_insights(self) -> AsyncGrowthInsightsResourceWithStreamingResponse:
        return AsyncGrowthInsightsResourceWithStreamingResponse(self._entities.growth_insights)

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        return AsyncProductsResourceWithStreamingResponse(self._entities.products)

    @cached_property
    def product_launches(self) -> AsyncProductLaunchesResourceWithStreamingResponse:
        return AsyncProductLaunchesResourceWithStreamingResponse(self._entities.product_launches)
