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
from .layoffs import (
    LayoffsResource,
    AsyncLayoffsResource,
    LayoffsResourceWithRawResponse,
    AsyncLayoffsResourceWithRawResponse,
    LayoffsResourceWithStreamingResponse,
    AsyncLayoffsResourceWithStreamingResponse,
)
from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .addresses import (
    AddressesResource,
    AsyncAddressesResource,
    AddressesResourceWithRawResponse,
    AsyncAddressesResourceWithRawResponse,
    AddressesResourceWithStreamingResponse,
    AsyncAddressesResourceWithStreamingResponse,
)
from .ipos.ipos import IposResource, AsyncIposResource
from .principals import (
    PrincipalsResource,
    AsyncPrincipalsResource,
    PrincipalsResourceWithRawResponse,
    AsyncPrincipalsResourceWithRawResponse,
    PrincipalsResourceWithStreamingResponse,
    AsyncPrincipalsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .funds.funds import FundsResource, AsyncFundsResource
from .investments import (
    InvestmentsResource,
    AsyncInvestmentsResource,
    InvestmentsResourceWithRawResponse,
    AsyncInvestmentsResourceWithRawResponse,
    InvestmentsResourceWithStreamingResponse,
    AsyncInvestmentsResourceWithStreamingResponse,
)
from .acquisitions import (
    AcquisitionsResource,
    AsyncAcquisitionsResource,
    AcquisitionsResourceWithRawResponse,
    AsyncAcquisitionsResourceWithRawResponse,
    AcquisitionsResourceWithStreamingResponse,
    AsyncAcquisitionsResourceWithStreamingResponse,
)
from .awards.awards import AwardsResource, AsyncAwardsResource
from .events.events import EventsResource, AsyncEventsResource
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from .people.people import PeopleResource, AsyncPeopleResource
from .funding_rounds import (
    FundingRoundsResource,
    AsyncFundingRoundsResource,
    FundingRoundsResourceWithRawResponse,
    AsyncFundingRoundsResourceWithRawResponse,
    FundingRoundsResourceWithStreamingResponse,
    AsyncFundingRoundsResourceWithStreamingResponse,
)
from .ipo_predictions import (
    IpoPredictionsResource,
    AsyncIpoPredictionsResource,
    IpoPredictionsResourceWithRawResponse,
    AsyncIpoPredictionsResourceWithRawResponse,
    IpoPredictionsResourceWithStreamingResponse,
    AsyncIpoPredictionsResourceWithStreamingResponse,
)
from .layoffs.layoffs import LayoffsResource, AsyncLayoffsResource
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
from .legal_proceedings import (
    LegalProceedingsResource,
    AsyncLegalProceedingsResource,
    LegalProceedingsResourceWithRawResponse,
    AsyncLegalProceedingsResourceWithRawResponse,
    LegalProceedingsResourceWithStreamingResponse,
    AsyncLegalProceedingsResourceWithStreamingResponse,
)
from .addresses.addresses import AddressesResource, AsyncAddressesResource
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
from .investments.investments import InvestmentsResource, AsyncInvestmentsResource
from .acquisitions.acquisitions import AcquisitionsResource, AsyncAcquisitionsResource
from .partnership_announcements import (
    PartnershipAnnouncementsResource,
    AsyncPartnershipAnnouncementsResource,
    PartnershipAnnouncementsResourceWithRawResponse,
    AsyncPartnershipAnnouncementsResourceWithRawResponse,
    PartnershipAnnouncementsResourceWithStreamingResponse,
    AsyncPartnershipAnnouncementsResourceWithStreamingResponse,
)
from .organizations.organizations import OrganizationsResource, AsyncOrganizationsResource
from .funding_rounds.funding_rounds import FundingRoundsResource, AsyncFundingRoundsResource
from .ipo_predictions.ipo_predictions import IpoPredictionsResource, AsyncIpoPredictionsResource
from .press_references.press_references import PressReferencesResource, AsyncPressReferencesResource
from .event_appearances.event_appearances import EventAppearancesResource, AsyncEventAppearancesResource
from .investor_insights.investor_insights import InvestorInsightsResource, AsyncInvestorInsightsResource
from .legal_proceedings.legal_proceedings import LegalProceedingsResource, AsyncLegalProceedingsResource
from .key_employee_changes.key_employee_changes import KeyEmployeeChangesResource, AsyncKeyEmployeeChangesResource
from .acquisition_predictions.acquisition_predictions import (
    AcquisitionPredictionsResource,
    AsyncAcquisitionPredictionsResource,
)
from .partnership_announcements.partnership_announcements import (
    PartnershipAnnouncementsResource,
    AsyncPartnershipAnnouncementsResource,
)

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
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
    def investor_insights(self) -> InvestorInsightsResource:
        return InvestorInsightsResource(self._client)

    @cached_property
    def ipo_predictions(self) -> IpoPredictionsResource:
        return IpoPredictionsResource(self._client)

    @cached_property
    def legal_proceedings(self) -> LegalProceedingsResource:
        return LegalProceedingsResource(self._client)

    @cached_property
    def partnership_announcements(self) -> PartnershipAnnouncementsResource:
        return PartnershipAnnouncementsResource(self._client)

    @cached_property
    def principals(self) -> PrincipalsResource:
        return PrincipalsResource(self._client)

    @cached_property
    def products(self) -> ProductsResource:
        return ProductsResource(self._client)

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
    def investor_insights(self) -> AsyncInvestorInsightsResource:
        return AsyncInvestorInsightsResource(self._client)

    @cached_property
    def ipo_predictions(self) -> AsyncIpoPredictionsResource:
        return AsyncIpoPredictionsResource(self._client)

    @cached_property
    def legal_proceedings(self) -> AsyncLegalProceedingsResource:
        return AsyncLegalProceedingsResource(self._client)

    @cached_property
    def partnership_announcements(self) -> AsyncPartnershipAnnouncementsResource:
        return AsyncPartnershipAnnouncementsResource(self._client)

    @cached_property
    def principals(self) -> AsyncPrincipalsResource:
        return AsyncPrincipalsResource(self._client)

    @cached_property
    def products(self) -> AsyncProductsResource:
        return AsyncProductsResource(self._client)

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
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._entities.organizations)

    @cached_property
    def people(self) -> PeopleResourceWithRawResponse:
        return PeopleResourceWithRawResponse(self._entities.people)

    @cached_property
    def funding_rounds(self) -> FundingRoundsResourceWithRawResponse:
        return FundingRoundsResourceWithRawResponse(self._entities.funding_rounds)

    @cached_property
    def acquisitions(self) -> AcquisitionsResourceWithRawResponse:
        return AcquisitionsResourceWithRawResponse(self._entities.acquisitions)

    @cached_property
    def investments(self) -> InvestmentsResourceWithRawResponse:
        return InvestmentsResourceWithRawResponse(self._entities.investments)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._entities.events)

    @cached_property
    def press_references(self) -> PressReferencesResourceWithRawResponse:
        return PressReferencesResourceWithRawResponse(self._entities.press_references)

    @cached_property
    def funds(self) -> FundsResourceWithRawResponse:
        return FundsResourceWithRawResponse(self._entities.funds)

    @cached_property
    def event_appearances(self) -> EventAppearancesResourceWithRawResponse:
        return EventAppearancesResourceWithRawResponse(self._entities.event_appearances)

    @cached_property
    def ipos(self) -> IposResourceWithRawResponse:
        return IposResourceWithRawResponse(self._entities.ipos)

    @cached_property
    def key_employee_changes(self) -> KeyEmployeeChangesResourceWithRawResponse:
        return KeyEmployeeChangesResourceWithRawResponse(self._entities.key_employee_changes)

    @cached_property
    def layoffs(self) -> LayoffsResourceWithRawResponse:
        return LayoffsResourceWithRawResponse(self._entities.layoffs)

    @cached_property
    def acquisition_predictions(self) -> AcquisitionPredictionsResourceWithRawResponse:
        return AcquisitionPredictionsResourceWithRawResponse(self._entities.acquisition_predictions)

    @cached_property
    def addresses(self) -> AddressesResourceWithRawResponse:
        return AddressesResourceWithRawResponse(self._entities.addresses)

    @cached_property
    def awards(self) -> AwardsResourceWithRawResponse:
        return AwardsResourceWithRawResponse(self._entities.awards)

    @cached_property
    def investor_insights(self) -> InvestorInsightsResourceWithRawResponse:
        return InvestorInsightsResourceWithRawResponse(self._entities.investor_insights)

    @cached_property
    def ipo_predictions(self) -> IpoPredictionsResourceWithRawResponse:
        return IpoPredictionsResourceWithRawResponse(self._entities.ipo_predictions)

    @cached_property
    def legal_proceedings(self) -> LegalProceedingsResourceWithRawResponse:
        return LegalProceedingsResourceWithRawResponse(self._entities.legal_proceedings)

    @cached_property
    def partnership_announcements(self) -> PartnershipAnnouncementsResourceWithRawResponse:
        return PartnershipAnnouncementsResourceWithRawResponse(self._entities.partnership_announcements)

    @cached_property
    def principals(self) -> PrincipalsResourceWithRawResponse:
        return PrincipalsResourceWithRawResponse(self._entities.principals)

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        return ProductsResourceWithRawResponse(self._entities.products)


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._entities.organizations)

    @cached_property
    def people(self) -> AsyncPeopleResourceWithRawResponse:
        return AsyncPeopleResourceWithRawResponse(self._entities.people)

    @cached_property
    def funding_rounds(self) -> AsyncFundingRoundsResourceWithRawResponse:
        return AsyncFundingRoundsResourceWithRawResponse(self._entities.funding_rounds)

    @cached_property
    def acquisitions(self) -> AsyncAcquisitionsResourceWithRawResponse:
        return AsyncAcquisitionsResourceWithRawResponse(self._entities.acquisitions)

    @cached_property
    def investments(self) -> AsyncInvestmentsResourceWithRawResponse:
        return AsyncInvestmentsResourceWithRawResponse(self._entities.investments)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._entities.events)

    @cached_property
    def press_references(self) -> AsyncPressReferencesResourceWithRawResponse:
        return AsyncPressReferencesResourceWithRawResponse(self._entities.press_references)

    @cached_property
    def funds(self) -> AsyncFundsResourceWithRawResponse:
        return AsyncFundsResourceWithRawResponse(self._entities.funds)

    @cached_property
    def event_appearances(self) -> AsyncEventAppearancesResourceWithRawResponse:
        return AsyncEventAppearancesResourceWithRawResponse(self._entities.event_appearances)

    @cached_property
    def ipos(self) -> AsyncIposResourceWithRawResponse:
        return AsyncIposResourceWithRawResponse(self._entities.ipos)

    @cached_property
    def key_employee_changes(self) -> AsyncKeyEmployeeChangesResourceWithRawResponse:
        return AsyncKeyEmployeeChangesResourceWithRawResponse(self._entities.key_employee_changes)

    @cached_property
    def layoffs(self) -> AsyncLayoffsResourceWithRawResponse:
        return AsyncLayoffsResourceWithRawResponse(self._entities.layoffs)

    @cached_property
    def acquisition_predictions(self) -> AsyncAcquisitionPredictionsResourceWithRawResponse:
        return AsyncAcquisitionPredictionsResourceWithRawResponse(self._entities.acquisition_predictions)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithRawResponse:
        return AsyncAddressesResourceWithRawResponse(self._entities.addresses)

    @cached_property
    def awards(self) -> AsyncAwardsResourceWithRawResponse:
        return AsyncAwardsResourceWithRawResponse(self._entities.awards)

    @cached_property
    def investor_insights(self) -> AsyncInvestorInsightsResourceWithRawResponse:
        return AsyncInvestorInsightsResourceWithRawResponse(self._entities.investor_insights)

    @cached_property
    def ipo_predictions(self) -> AsyncIpoPredictionsResourceWithRawResponse:
        return AsyncIpoPredictionsResourceWithRawResponse(self._entities.ipo_predictions)

    @cached_property
    def legal_proceedings(self) -> AsyncLegalProceedingsResourceWithRawResponse:
        return AsyncLegalProceedingsResourceWithRawResponse(self._entities.legal_proceedings)

    @cached_property
    def partnership_announcements(self) -> AsyncPartnershipAnnouncementsResourceWithRawResponse:
        return AsyncPartnershipAnnouncementsResourceWithRawResponse(self._entities.partnership_announcements)

    @cached_property
    def principals(self) -> AsyncPrincipalsResourceWithRawResponse:
        return AsyncPrincipalsResourceWithRawResponse(self._entities.principals)

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        return AsyncProductsResourceWithRawResponse(self._entities.products)


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._entities.organizations)

    @cached_property
    def people(self) -> PeopleResourceWithStreamingResponse:
        return PeopleResourceWithStreamingResponse(self._entities.people)

    @cached_property
    def funding_rounds(self) -> FundingRoundsResourceWithStreamingResponse:
        return FundingRoundsResourceWithStreamingResponse(self._entities.funding_rounds)

    @cached_property
    def acquisitions(self) -> AcquisitionsResourceWithStreamingResponse:
        return AcquisitionsResourceWithStreamingResponse(self._entities.acquisitions)

    @cached_property
    def investments(self) -> InvestmentsResourceWithStreamingResponse:
        return InvestmentsResourceWithStreamingResponse(self._entities.investments)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._entities.events)

    @cached_property
    def press_references(self) -> PressReferencesResourceWithStreamingResponse:
        return PressReferencesResourceWithStreamingResponse(self._entities.press_references)

    @cached_property
    def funds(self) -> FundsResourceWithStreamingResponse:
        return FundsResourceWithStreamingResponse(self._entities.funds)

    @cached_property
    def event_appearances(self) -> EventAppearancesResourceWithStreamingResponse:
        return EventAppearancesResourceWithStreamingResponse(self._entities.event_appearances)

    @cached_property
    def ipos(self) -> IposResourceWithStreamingResponse:
        return IposResourceWithStreamingResponse(self._entities.ipos)

    @cached_property
    def key_employee_changes(self) -> KeyEmployeeChangesResourceWithStreamingResponse:
        return KeyEmployeeChangesResourceWithStreamingResponse(self._entities.key_employee_changes)

    @cached_property
    def layoffs(self) -> LayoffsResourceWithStreamingResponse:
        return LayoffsResourceWithStreamingResponse(self._entities.layoffs)

    @cached_property
    def acquisition_predictions(self) -> AcquisitionPredictionsResourceWithStreamingResponse:
        return AcquisitionPredictionsResourceWithStreamingResponse(self._entities.acquisition_predictions)

    @cached_property
    def addresses(self) -> AddressesResourceWithStreamingResponse:
        return AddressesResourceWithStreamingResponse(self._entities.addresses)

    @cached_property
    def awards(self) -> AwardsResourceWithStreamingResponse:
        return AwardsResourceWithStreamingResponse(self._entities.awards)

    @cached_property
    def investor_insights(self) -> InvestorInsightsResourceWithStreamingResponse:
        return InvestorInsightsResourceWithStreamingResponse(self._entities.investor_insights)

    @cached_property
    def ipo_predictions(self) -> IpoPredictionsResourceWithStreamingResponse:
        return IpoPredictionsResourceWithStreamingResponse(self._entities.ipo_predictions)

    @cached_property
    def legal_proceedings(self) -> LegalProceedingsResourceWithStreamingResponse:
        return LegalProceedingsResourceWithStreamingResponse(self._entities.legal_proceedings)

    @cached_property
    def partnership_announcements(self) -> PartnershipAnnouncementsResourceWithStreamingResponse:
        return PartnershipAnnouncementsResourceWithStreamingResponse(self._entities.partnership_announcements)

    @cached_property
    def principals(self) -> PrincipalsResourceWithStreamingResponse:
        return PrincipalsResourceWithStreamingResponse(self._entities.principals)

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        return ProductsResourceWithStreamingResponse(self._entities.products)


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._entities.organizations)

    @cached_property
    def people(self) -> AsyncPeopleResourceWithStreamingResponse:
        return AsyncPeopleResourceWithStreamingResponse(self._entities.people)

    @cached_property
    def funding_rounds(self) -> AsyncFundingRoundsResourceWithStreamingResponse:
        return AsyncFundingRoundsResourceWithStreamingResponse(self._entities.funding_rounds)

    @cached_property
    def acquisitions(self) -> AsyncAcquisitionsResourceWithStreamingResponse:
        return AsyncAcquisitionsResourceWithStreamingResponse(self._entities.acquisitions)

    @cached_property
    def investments(self) -> AsyncInvestmentsResourceWithStreamingResponse:
        return AsyncInvestmentsResourceWithStreamingResponse(self._entities.investments)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._entities.events)

    @cached_property
    def press_references(self) -> AsyncPressReferencesResourceWithStreamingResponse:
        return AsyncPressReferencesResourceWithStreamingResponse(self._entities.press_references)

    @cached_property
    def funds(self) -> AsyncFundsResourceWithStreamingResponse:
        return AsyncFundsResourceWithStreamingResponse(self._entities.funds)

    @cached_property
    def event_appearances(self) -> AsyncEventAppearancesResourceWithStreamingResponse:
        return AsyncEventAppearancesResourceWithStreamingResponse(self._entities.event_appearances)

    @cached_property
    def ipos(self) -> AsyncIposResourceWithStreamingResponse:
        return AsyncIposResourceWithStreamingResponse(self._entities.ipos)

    @cached_property
    def key_employee_changes(self) -> AsyncKeyEmployeeChangesResourceWithStreamingResponse:
        return AsyncKeyEmployeeChangesResourceWithStreamingResponse(self._entities.key_employee_changes)

    @cached_property
    def layoffs(self) -> AsyncLayoffsResourceWithStreamingResponse:
        return AsyncLayoffsResourceWithStreamingResponse(self._entities.layoffs)

    @cached_property
    def acquisition_predictions(self) -> AsyncAcquisitionPredictionsResourceWithStreamingResponse:
        return AsyncAcquisitionPredictionsResourceWithStreamingResponse(self._entities.acquisition_predictions)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithStreamingResponse:
        return AsyncAddressesResourceWithStreamingResponse(self._entities.addresses)

    @cached_property
    def awards(self) -> AsyncAwardsResourceWithStreamingResponse:
        return AsyncAwardsResourceWithStreamingResponse(self._entities.awards)

    @cached_property
    def investor_insights(self) -> AsyncInvestorInsightsResourceWithStreamingResponse:
        return AsyncInvestorInsightsResourceWithStreamingResponse(self._entities.investor_insights)

    @cached_property
    def ipo_predictions(self) -> AsyncIpoPredictionsResourceWithStreamingResponse:
        return AsyncIpoPredictionsResourceWithStreamingResponse(self._entities.ipo_predictions)

    @cached_property
    def legal_proceedings(self) -> AsyncLegalProceedingsResourceWithStreamingResponse:
        return AsyncLegalProceedingsResourceWithStreamingResponse(self._entities.legal_proceedings)

    @cached_property
    def partnership_announcements(self) -> AsyncPartnershipAnnouncementsResourceWithStreamingResponse:
        return AsyncPartnershipAnnouncementsResourceWithStreamingResponse(self._entities.partnership_announcements)

    @cached_property
    def principals(self) -> AsyncPrincipalsResourceWithStreamingResponse:
        return AsyncPrincipalsResourceWithStreamingResponse(self._entities.principals)

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        return AsyncProductsResourceWithStreamingResponse(self._entities.products)
