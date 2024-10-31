# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ipos import (
    IposResource,
    AsyncIposResource,
    IposResourceWithRawResponse,
    AsyncIposResourceWithRawResponse,
    IposResourceWithStreamingResponse,
    AsyncIposResourceWithStreamingResponse,
)
from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .funds import (
    FundsResource,
    AsyncFundsResource,
    FundsResourceWithRawResponse,
    AsyncFundsResourceWithRawResponse,
    FundsResourceWithStreamingResponse,
    AsyncFundsResourceWithStreamingResponse,
)
from .awards import (
    AwardsResource,
    AsyncAwardsResource,
    AwardsResourceWithRawResponse,
    AsyncAwardsResourceWithRawResponse,
    AwardsResourceWithStreamingResponse,
    AsyncAwardsResourceWithStreamingResponse,
)
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .people import (
    PeopleResource,
    AsyncPeopleResource,
    PeopleResourceWithRawResponse,
    AsyncPeopleResourceWithRawResponse,
    PeopleResourceWithStreamingResponse,
    AsyncPeopleResourceWithStreamingResponse,
)
from .degrees import (
    DegreesResource,
    AsyncDegreesResource,
    DegreesResourceWithRawResponse,
    AsyncDegreesResourceWithRawResponse,
    DegreesResourceWithStreamingResponse,
    AsyncDegreesResourceWithStreamingResponse,
)
from .layoffs import (
    LayoffsResource,
    AsyncLayoffsResource,
    LayoffsResourceWithRawResponse,
    AsyncLayoffsResourceWithRawResponse,
    LayoffsResourceWithStreamingResponse,
    AsyncLayoffsResourceWithStreamingResponse,
)
from .addresses import (
    AddressesResource,
    AsyncAddressesResource,
    AddressesResourceWithRawResponse,
    AsyncAddressesResourceWithRawResponse,
    AddressesResourceWithStreamingResponse,
    AsyncAddressesResourceWithStreamingResponse,
)
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
from .investments import (
    InvestmentsResource,
    AsyncInvestmentsResource,
    InvestmentsResourceWithRawResponse,
    AsyncInvestmentsResourceWithRawResponse,
    InvestmentsResourceWithStreamingResponse,
    AsyncInvestmentsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .acquisitions import (
    AcquisitionsResource,
    AsyncAcquisitionsResource,
    AcquisitionsResourceWithRawResponse,
    AsyncAcquisitionsResourceWithRawResponse,
    AcquisitionsResourceWithStreamingResponse,
    AsyncAcquisitionsResourceWithStreamingResponse,
)
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from .funding_rounds import (
    FundingRoundsResource,
    AsyncFundingRoundsResource,
    FundingRoundsResourceWithRawResponse,
    AsyncFundingRoundsResourceWithRawResponse,
    FundingRoundsResourceWithStreamingResponse,
    AsyncFundingRoundsResourceWithStreamingResponse,
)
from .category_groups import (
    CategoryGroupsResource,
    AsyncCategoryGroupsResource,
    CategoryGroupsResourceWithRawResponse,
    AsyncCategoryGroupsResourceWithRawResponse,
    CategoryGroupsResourceWithStreamingResponse,
    AsyncCategoryGroupsResourceWithStreamingResponse,
)
from .growth_insights import (
    GrowthInsightsResource,
    AsyncGrowthInsightsResource,
    GrowthInsightsResourceWithRawResponse,
    AsyncGrowthInsightsResourceWithRawResponse,
    GrowthInsightsResourceWithStreamingResponse,
    AsyncGrowthInsightsResourceWithStreamingResponse,
)
from .ipo_predictions import (
    IpoPredictionsResource,
    AsyncIpoPredictionsResource,
    IpoPredictionsResourceWithRawResponse,
    AsyncIpoPredictionsResourceWithRawResponse,
    IpoPredictionsResourceWithStreamingResponse,
    AsyncIpoPredictionsResourceWithStreamingResponse,
)
from .press_references import (
    PressReferencesResource,
    AsyncPressReferencesResource,
    PressReferencesResourceWithRawResponse,
    AsyncPressReferencesResourceWithRawResponse,
    PressReferencesResourceWithStreamingResponse,
    AsyncPressReferencesResourceWithStreamingResponse,
)
from .event_appearances import (
    EventAppearancesResource,
    AsyncEventAppearancesResource,
    EventAppearancesResourceWithRawResponse,
    AsyncEventAppearancesResourceWithRawResponse,
    EventAppearancesResourceWithStreamingResponse,
    AsyncEventAppearancesResourceWithStreamingResponse,
)
from .investor_insights import (
    InvestorInsightsResource,
    AsyncInvestorInsightsResource,
    InvestorInsightsResourceWithRawResponse,
    AsyncInvestorInsightsResourceWithRawResponse,
    InvestorInsightsResourceWithStreamingResponse,
    AsyncInvestorInsightsResourceWithStreamingResponse,
)
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
from .diversity_spotlights import (
    DiversitySpotlightsResource,
    AsyncDiversitySpotlightsResource,
    DiversitySpotlightsResourceWithRawResponse,
    AsyncDiversitySpotlightsResourceWithRawResponse,
    DiversitySpotlightsResourceWithStreamingResponse,
    AsyncDiversitySpotlightsResourceWithStreamingResponse,
)
from .key_employee_changes import (
    KeyEmployeeChangesResource,
    AsyncKeyEmployeeChangesResource,
    KeyEmployeeChangesResourceWithRawResponse,
    AsyncKeyEmployeeChangesResourceWithRawResponse,
    KeyEmployeeChangesResourceWithStreamingResponse,
    AsyncKeyEmployeeChangesResourceWithStreamingResponse,
)
from .acquisition_predictions import (
    AcquisitionPredictionsResource,
    AsyncAcquisitionPredictionsResource,
    AcquisitionPredictionsResourceWithRawResponse,
    AsyncAcquisitionPredictionsResourceWithRawResponse,
    AcquisitionPredictionsResourceWithStreamingResponse,
    AsyncAcquisitionPredictionsResourceWithStreamingResponse,
)

__all__ = ["SearchesResource", "AsyncSearchesResource"]


class SearchesResource(SyncAPIResource):
    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def people(self) -> PeopleResource:
        return PeopleResource(self._client)

    @cached_property
    def funding_rounds(self) -> FundingRoundsResource:
        return FundingRoundsResource(self._client)

    @cached_property
    def acquisitions(self) -> AcquisitionsResource:
        return AcquisitionsResource(self._client)

    @cached_property
    def investments(self) -> InvestmentsResource:
        return InvestmentsResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def press_references(self) -> PressReferencesResource:
        return PressReferencesResource(self._client)

    @cached_property
    def funds(self) -> FundsResource:
        return FundsResource(self._client)

    @cached_property
    def event_appearances(self) -> EventAppearancesResource:
        return EventAppearancesResource(self._client)

    @cached_property
    def ipos(self) -> IposResource:
        return IposResource(self._client)

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
    def key_employee_changes(self) -> KeyEmployeeChangesResource:
        return KeyEmployeeChangesResource(self._client)

    @cached_property
    def layoffs(self) -> LayoffsResource:
        return LayoffsResource(self._client)

    @cached_property
    def acquisition_predictions(self) -> AcquisitionPredictionsResource:
        return AcquisitionPredictionsResource(self._client)

    @cached_property
    def addresses(self) -> AddressesResource:
        return AddressesResource(self._client)

    @cached_property
    def awards(self) -> AwardsResource:
        return AwardsResource(self._client)

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
    def investor_insights(self) -> InvestorInsightsResource:
        return InvestorInsightsResource(self._client)

    @cached_property
    def ipo_predictions(self) -> IpoPredictionsResource:
        return IpoPredictionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return SearchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return SearchesResourceWithStreamingResponse(self)


class AsyncSearchesResource(AsyncAPIResource):
    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def people(self) -> AsyncPeopleResource:
        return AsyncPeopleResource(self._client)

    @cached_property
    def funding_rounds(self) -> AsyncFundingRoundsResource:
        return AsyncFundingRoundsResource(self._client)

    @cached_property
    def acquisitions(self) -> AsyncAcquisitionsResource:
        return AsyncAcquisitionsResource(self._client)

    @cached_property
    def investments(self) -> AsyncInvestmentsResource:
        return AsyncInvestmentsResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def press_references(self) -> AsyncPressReferencesResource:
        return AsyncPressReferencesResource(self._client)

    @cached_property
    def funds(self) -> AsyncFundsResource:
        return AsyncFundsResource(self._client)

    @cached_property
    def event_appearances(self) -> AsyncEventAppearancesResource:
        return AsyncEventAppearancesResource(self._client)

    @cached_property
    def ipos(self) -> AsyncIposResource:
        return AsyncIposResource(self._client)

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
    def key_employee_changes(self) -> AsyncKeyEmployeeChangesResource:
        return AsyncKeyEmployeeChangesResource(self._client)

    @cached_property
    def layoffs(self) -> AsyncLayoffsResource:
        return AsyncLayoffsResource(self._client)

    @cached_property
    def acquisition_predictions(self) -> AsyncAcquisitionPredictionsResource:
        return AsyncAcquisitionPredictionsResource(self._client)

    @cached_property
    def addresses(self) -> AsyncAddressesResource:
        return AsyncAddressesResource(self._client)

    @cached_property
    def awards(self) -> AsyncAwardsResource:
        return AsyncAwardsResource(self._client)

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
    def investor_insights(self) -> AsyncInvestorInsightsResource:
        return AsyncInvestorInsightsResource(self._client)

    @cached_property
    def ipo_predictions(self) -> AsyncIpoPredictionsResource:
        return AsyncIpoPredictionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EndexAI/endex-crunchbase-python#with_streaming_response
        """
        return AsyncSearchesResourceWithStreamingResponse(self)


class SearchesResourceWithRawResponse:
    def __init__(self, searches: SearchesResource) -> None:
        self._searches = searches

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._searches.organizations)

    @cached_property
    def people(self) -> PeopleResourceWithRawResponse:
        return PeopleResourceWithRawResponse(self._searches.people)

    @cached_property
    def funding_rounds(self) -> FundingRoundsResourceWithRawResponse:
        return FundingRoundsResourceWithRawResponse(self._searches.funding_rounds)

    @cached_property
    def acquisitions(self) -> AcquisitionsResourceWithRawResponse:
        return AcquisitionsResourceWithRawResponse(self._searches.acquisitions)

    @cached_property
    def investments(self) -> InvestmentsResourceWithRawResponse:
        return InvestmentsResourceWithRawResponse(self._searches.investments)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._searches.events)

    @cached_property
    def press_references(self) -> PressReferencesResourceWithRawResponse:
        return PressReferencesResourceWithRawResponse(self._searches.press_references)

    @cached_property
    def funds(self) -> FundsResourceWithRawResponse:
        return FundsResourceWithRawResponse(self._searches.funds)

    @cached_property
    def event_appearances(self) -> EventAppearancesResourceWithRawResponse:
        return EventAppearancesResourceWithRawResponse(self._searches.event_appearances)

    @cached_property
    def ipos(self) -> IposResourceWithRawResponse:
        return IposResourceWithRawResponse(self._searches.ipos)

    @cached_property
    def ownerships(self) -> OwnershipsResourceWithRawResponse:
        return OwnershipsResourceWithRawResponse(self._searches.ownerships)

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._searches.categories)

    @cached_property
    def category_groups(self) -> CategoryGroupsResourceWithRawResponse:
        return CategoryGroupsResourceWithRawResponse(self._searches.category_groups)

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._searches.locations)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._searches.jobs)

    @cached_property
    def key_employee_changes(self) -> KeyEmployeeChangesResourceWithRawResponse:
        return KeyEmployeeChangesResourceWithRawResponse(self._searches.key_employee_changes)

    @cached_property
    def layoffs(self) -> LayoffsResourceWithRawResponse:
        return LayoffsResourceWithRawResponse(self._searches.layoffs)

    @cached_property
    def acquisition_predictions(self) -> AcquisitionPredictionsResourceWithRawResponse:
        return AcquisitionPredictionsResourceWithRawResponse(self._searches.acquisition_predictions)

    @cached_property
    def addresses(self) -> AddressesResourceWithRawResponse:
        return AddressesResourceWithRawResponse(self._searches.addresses)

    @cached_property
    def awards(self) -> AwardsResourceWithRawResponse:
        return AwardsResourceWithRawResponse(self._searches.awards)

    @cached_property
    def closure_predictions(self) -> ClosurePredictionsResourceWithRawResponse:
        return ClosurePredictionsResourceWithRawResponse(self._searches.closure_predictions)

    @cached_property
    def degrees(self) -> DegreesResourceWithRawResponse:
        return DegreesResourceWithRawResponse(self._searches.degrees)

    @cached_property
    def diversity_spotlights(self) -> DiversitySpotlightsResourceWithRawResponse:
        return DiversitySpotlightsResourceWithRawResponse(self._searches.diversity_spotlights)

    @cached_property
    def funding_predictions(self) -> FundingPredictionsResourceWithRawResponse:
        return FundingPredictionsResourceWithRawResponse(self._searches.funding_predictions)

    @cached_property
    def growth_insights(self) -> GrowthInsightsResourceWithRawResponse:
        return GrowthInsightsResourceWithRawResponse(self._searches.growth_insights)

    @cached_property
    def investor_insights(self) -> InvestorInsightsResourceWithRawResponse:
        return InvestorInsightsResourceWithRawResponse(self._searches.investor_insights)

    @cached_property
    def ipo_predictions(self) -> IpoPredictionsResourceWithRawResponse:
        return IpoPredictionsResourceWithRawResponse(self._searches.ipo_predictions)


class AsyncSearchesResourceWithRawResponse:
    def __init__(self, searches: AsyncSearchesResource) -> None:
        self._searches = searches

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._searches.organizations)

    @cached_property
    def people(self) -> AsyncPeopleResourceWithRawResponse:
        return AsyncPeopleResourceWithRawResponse(self._searches.people)

    @cached_property
    def funding_rounds(self) -> AsyncFundingRoundsResourceWithRawResponse:
        return AsyncFundingRoundsResourceWithRawResponse(self._searches.funding_rounds)

    @cached_property
    def acquisitions(self) -> AsyncAcquisitionsResourceWithRawResponse:
        return AsyncAcquisitionsResourceWithRawResponse(self._searches.acquisitions)

    @cached_property
    def investments(self) -> AsyncInvestmentsResourceWithRawResponse:
        return AsyncInvestmentsResourceWithRawResponse(self._searches.investments)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._searches.events)

    @cached_property
    def press_references(self) -> AsyncPressReferencesResourceWithRawResponse:
        return AsyncPressReferencesResourceWithRawResponse(self._searches.press_references)

    @cached_property
    def funds(self) -> AsyncFundsResourceWithRawResponse:
        return AsyncFundsResourceWithRawResponse(self._searches.funds)

    @cached_property
    def event_appearances(self) -> AsyncEventAppearancesResourceWithRawResponse:
        return AsyncEventAppearancesResourceWithRawResponse(self._searches.event_appearances)

    @cached_property
    def ipos(self) -> AsyncIposResourceWithRawResponse:
        return AsyncIposResourceWithRawResponse(self._searches.ipos)

    @cached_property
    def ownerships(self) -> AsyncOwnershipsResourceWithRawResponse:
        return AsyncOwnershipsResourceWithRawResponse(self._searches.ownerships)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._searches.categories)

    @cached_property
    def category_groups(self) -> AsyncCategoryGroupsResourceWithRawResponse:
        return AsyncCategoryGroupsResourceWithRawResponse(self._searches.category_groups)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._searches.locations)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._searches.jobs)

    @cached_property
    def key_employee_changes(self) -> AsyncKeyEmployeeChangesResourceWithRawResponse:
        return AsyncKeyEmployeeChangesResourceWithRawResponse(self._searches.key_employee_changes)

    @cached_property
    def layoffs(self) -> AsyncLayoffsResourceWithRawResponse:
        return AsyncLayoffsResourceWithRawResponse(self._searches.layoffs)

    @cached_property
    def acquisition_predictions(self) -> AsyncAcquisitionPredictionsResourceWithRawResponse:
        return AsyncAcquisitionPredictionsResourceWithRawResponse(self._searches.acquisition_predictions)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithRawResponse:
        return AsyncAddressesResourceWithRawResponse(self._searches.addresses)

    @cached_property
    def awards(self) -> AsyncAwardsResourceWithRawResponse:
        return AsyncAwardsResourceWithRawResponse(self._searches.awards)

    @cached_property
    def closure_predictions(self) -> AsyncClosurePredictionsResourceWithRawResponse:
        return AsyncClosurePredictionsResourceWithRawResponse(self._searches.closure_predictions)

    @cached_property
    def degrees(self) -> AsyncDegreesResourceWithRawResponse:
        return AsyncDegreesResourceWithRawResponse(self._searches.degrees)

    @cached_property
    def diversity_spotlights(self) -> AsyncDiversitySpotlightsResourceWithRawResponse:
        return AsyncDiversitySpotlightsResourceWithRawResponse(self._searches.diversity_spotlights)

    @cached_property
    def funding_predictions(self) -> AsyncFundingPredictionsResourceWithRawResponse:
        return AsyncFundingPredictionsResourceWithRawResponse(self._searches.funding_predictions)

    @cached_property
    def growth_insights(self) -> AsyncGrowthInsightsResourceWithRawResponse:
        return AsyncGrowthInsightsResourceWithRawResponse(self._searches.growth_insights)

    @cached_property
    def investor_insights(self) -> AsyncInvestorInsightsResourceWithRawResponse:
        return AsyncInvestorInsightsResourceWithRawResponse(self._searches.investor_insights)

    @cached_property
    def ipo_predictions(self) -> AsyncIpoPredictionsResourceWithRawResponse:
        return AsyncIpoPredictionsResourceWithRawResponse(self._searches.ipo_predictions)


class SearchesResourceWithStreamingResponse:
    def __init__(self, searches: SearchesResource) -> None:
        self._searches = searches

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._searches.organizations)

    @cached_property
    def people(self) -> PeopleResourceWithStreamingResponse:
        return PeopleResourceWithStreamingResponse(self._searches.people)

    @cached_property
    def funding_rounds(self) -> FundingRoundsResourceWithStreamingResponse:
        return FundingRoundsResourceWithStreamingResponse(self._searches.funding_rounds)

    @cached_property
    def acquisitions(self) -> AcquisitionsResourceWithStreamingResponse:
        return AcquisitionsResourceWithStreamingResponse(self._searches.acquisitions)

    @cached_property
    def investments(self) -> InvestmentsResourceWithStreamingResponse:
        return InvestmentsResourceWithStreamingResponse(self._searches.investments)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._searches.events)

    @cached_property
    def press_references(self) -> PressReferencesResourceWithStreamingResponse:
        return PressReferencesResourceWithStreamingResponse(self._searches.press_references)

    @cached_property
    def funds(self) -> FundsResourceWithStreamingResponse:
        return FundsResourceWithStreamingResponse(self._searches.funds)

    @cached_property
    def event_appearances(self) -> EventAppearancesResourceWithStreamingResponse:
        return EventAppearancesResourceWithStreamingResponse(self._searches.event_appearances)

    @cached_property
    def ipos(self) -> IposResourceWithStreamingResponse:
        return IposResourceWithStreamingResponse(self._searches.ipos)

    @cached_property
    def ownerships(self) -> OwnershipsResourceWithStreamingResponse:
        return OwnershipsResourceWithStreamingResponse(self._searches.ownerships)

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._searches.categories)

    @cached_property
    def category_groups(self) -> CategoryGroupsResourceWithStreamingResponse:
        return CategoryGroupsResourceWithStreamingResponse(self._searches.category_groups)

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._searches.locations)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._searches.jobs)

    @cached_property
    def key_employee_changes(self) -> KeyEmployeeChangesResourceWithStreamingResponse:
        return KeyEmployeeChangesResourceWithStreamingResponse(self._searches.key_employee_changes)

    @cached_property
    def layoffs(self) -> LayoffsResourceWithStreamingResponse:
        return LayoffsResourceWithStreamingResponse(self._searches.layoffs)

    @cached_property
    def acquisition_predictions(self) -> AcquisitionPredictionsResourceWithStreamingResponse:
        return AcquisitionPredictionsResourceWithStreamingResponse(self._searches.acquisition_predictions)

    @cached_property
    def addresses(self) -> AddressesResourceWithStreamingResponse:
        return AddressesResourceWithStreamingResponse(self._searches.addresses)

    @cached_property
    def awards(self) -> AwardsResourceWithStreamingResponse:
        return AwardsResourceWithStreamingResponse(self._searches.awards)

    @cached_property
    def closure_predictions(self) -> ClosurePredictionsResourceWithStreamingResponse:
        return ClosurePredictionsResourceWithStreamingResponse(self._searches.closure_predictions)

    @cached_property
    def degrees(self) -> DegreesResourceWithStreamingResponse:
        return DegreesResourceWithStreamingResponse(self._searches.degrees)

    @cached_property
    def diversity_spotlights(self) -> DiversitySpotlightsResourceWithStreamingResponse:
        return DiversitySpotlightsResourceWithStreamingResponse(self._searches.diversity_spotlights)

    @cached_property
    def funding_predictions(self) -> FundingPredictionsResourceWithStreamingResponse:
        return FundingPredictionsResourceWithStreamingResponse(self._searches.funding_predictions)

    @cached_property
    def growth_insights(self) -> GrowthInsightsResourceWithStreamingResponse:
        return GrowthInsightsResourceWithStreamingResponse(self._searches.growth_insights)

    @cached_property
    def investor_insights(self) -> InvestorInsightsResourceWithStreamingResponse:
        return InvestorInsightsResourceWithStreamingResponse(self._searches.investor_insights)

    @cached_property
    def ipo_predictions(self) -> IpoPredictionsResourceWithStreamingResponse:
        return IpoPredictionsResourceWithStreamingResponse(self._searches.ipo_predictions)


class AsyncSearchesResourceWithStreamingResponse:
    def __init__(self, searches: AsyncSearchesResource) -> None:
        self._searches = searches

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._searches.organizations)

    @cached_property
    def people(self) -> AsyncPeopleResourceWithStreamingResponse:
        return AsyncPeopleResourceWithStreamingResponse(self._searches.people)

    @cached_property
    def funding_rounds(self) -> AsyncFundingRoundsResourceWithStreamingResponse:
        return AsyncFundingRoundsResourceWithStreamingResponse(self._searches.funding_rounds)

    @cached_property
    def acquisitions(self) -> AsyncAcquisitionsResourceWithStreamingResponse:
        return AsyncAcquisitionsResourceWithStreamingResponse(self._searches.acquisitions)

    @cached_property
    def investments(self) -> AsyncInvestmentsResourceWithStreamingResponse:
        return AsyncInvestmentsResourceWithStreamingResponse(self._searches.investments)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._searches.events)

    @cached_property
    def press_references(self) -> AsyncPressReferencesResourceWithStreamingResponse:
        return AsyncPressReferencesResourceWithStreamingResponse(self._searches.press_references)

    @cached_property
    def funds(self) -> AsyncFundsResourceWithStreamingResponse:
        return AsyncFundsResourceWithStreamingResponse(self._searches.funds)

    @cached_property
    def event_appearances(self) -> AsyncEventAppearancesResourceWithStreamingResponse:
        return AsyncEventAppearancesResourceWithStreamingResponse(self._searches.event_appearances)

    @cached_property
    def ipos(self) -> AsyncIposResourceWithStreamingResponse:
        return AsyncIposResourceWithStreamingResponse(self._searches.ipos)

    @cached_property
    def ownerships(self) -> AsyncOwnershipsResourceWithStreamingResponse:
        return AsyncOwnershipsResourceWithStreamingResponse(self._searches.ownerships)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._searches.categories)

    @cached_property
    def category_groups(self) -> AsyncCategoryGroupsResourceWithStreamingResponse:
        return AsyncCategoryGroupsResourceWithStreamingResponse(self._searches.category_groups)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._searches.locations)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._searches.jobs)

    @cached_property
    def key_employee_changes(self) -> AsyncKeyEmployeeChangesResourceWithStreamingResponse:
        return AsyncKeyEmployeeChangesResourceWithStreamingResponse(self._searches.key_employee_changes)

    @cached_property
    def layoffs(self) -> AsyncLayoffsResourceWithStreamingResponse:
        return AsyncLayoffsResourceWithStreamingResponse(self._searches.layoffs)

    @cached_property
    def acquisition_predictions(self) -> AsyncAcquisitionPredictionsResourceWithStreamingResponse:
        return AsyncAcquisitionPredictionsResourceWithStreamingResponse(self._searches.acquisition_predictions)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithStreamingResponse:
        return AsyncAddressesResourceWithStreamingResponse(self._searches.addresses)

    @cached_property
    def awards(self) -> AsyncAwardsResourceWithStreamingResponse:
        return AsyncAwardsResourceWithStreamingResponse(self._searches.awards)

    @cached_property
    def closure_predictions(self) -> AsyncClosurePredictionsResourceWithStreamingResponse:
        return AsyncClosurePredictionsResourceWithStreamingResponse(self._searches.closure_predictions)

    @cached_property
    def degrees(self) -> AsyncDegreesResourceWithStreamingResponse:
        return AsyncDegreesResourceWithStreamingResponse(self._searches.degrees)

    @cached_property
    def diversity_spotlights(self) -> AsyncDiversitySpotlightsResourceWithStreamingResponse:
        return AsyncDiversitySpotlightsResourceWithStreamingResponse(self._searches.diversity_spotlights)

    @cached_property
    def funding_predictions(self) -> AsyncFundingPredictionsResourceWithStreamingResponse:
        return AsyncFundingPredictionsResourceWithStreamingResponse(self._searches.funding_predictions)

    @cached_property
    def growth_insights(self) -> AsyncGrowthInsightsResourceWithStreamingResponse:
        return AsyncGrowthInsightsResourceWithStreamingResponse(self._searches.growth_insights)

    @cached_property
    def investor_insights(self) -> AsyncInvestorInsightsResourceWithStreamingResponse:
        return AsyncInvestorInsightsResourceWithStreamingResponse(self._searches.investor_insights)

    @cached_property
    def ipo_predictions(self) -> AsyncIpoPredictionsResourceWithStreamingResponse:
        return AsyncIpoPredictionsResourceWithStreamingResponse(self._searches.ipo_predictions)
