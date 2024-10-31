# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "OrganizationRetrieveResponse",
    "Cards",
    "CardsAcquireeAcquisition",
    "CardsAcquireeAcquisitionIdentifier",
    "CardsAcquireeAcquisitionAcquireeCategory",
    "CardsAcquireeAcquisitionAcquireeFundingTotal",
    "CardsAcquireeAcquisitionAcquireeIdentifier",
    "CardsAcquireeAcquisitionAcquireeLocation",
    "CardsAcquireeAcquisitionAcquirerCategory",
    "CardsAcquireeAcquisitionAcquirerFundingTotal",
    "CardsAcquireeAcquisitionAcquirerIdentifier",
    "CardsAcquireeAcquisitionAcquirerLocation",
    "CardsAcquireeAcquisitionAnnouncedOn",
    "CardsAcquireeAcquisitionCompletedOn",
    "CardsAcquireeAcquisitionPrice",
    "CardsAcquirerAcquisition",
    "CardsAcquirerAcquisitionIdentifier",
    "CardsAcquirerAcquisitionAcquireeCategory",
    "CardsAcquirerAcquisitionAcquireeFundingTotal",
    "CardsAcquirerAcquisitionAcquireeIdentifier",
    "CardsAcquirerAcquisitionAcquireeLocation",
    "CardsAcquirerAcquisitionAcquirerCategory",
    "CardsAcquirerAcquisitionAcquirerFundingTotal",
    "CardsAcquirerAcquisitionAcquirerIdentifier",
    "CardsAcquirerAcquisitionAcquirerLocation",
    "CardsAcquirerAcquisitionAnnouncedOn",
    "CardsAcquirerAcquisitionCompletedOn",
    "CardsAcquirerAcquisitionPrice",
    "CardsAcquisitionPrediction",
    "CardsAcquisitionPredictionIdentifier",
    "CardsAcquisitionPredictionExampleAcquisition",
    "CardsAcquisitionPredictionGrowthInsight",
    "CardsAcquisitionPredictionKeyLeadershipHire",
    "CardsAcquisitionPredictionOrganization",
    "CardsAcquisitionPredictionPartnershipAnnouncement",
    "CardsAcquisitionPredictionRunwaySpeculation",
    "CardsChildOrganization",
    "CardsChildOrganizationIdentifier",
    "CardsChildOrganizationAcquirerIdentifier",
    "CardsChildOrganizationCategory",
    "CardsChildOrganizationCategoryGroup",
    "CardsChildOrganizationClosedOn",
    "CardsChildOrganizationDelistedOn",
    "CardsChildOrganizationDiversitySpotlight",
    "CardsChildOrganizationEquityFundingTotal",
    "CardsChildOrganizationExitedOn",
    "CardsChildOrganizationFacebook",
    "CardsChildOrganizationFoundedOn",
    "CardsChildOrganizationFounderIdentifier",
    "CardsChildOrganizationFundingTotal",
    "CardsChildOrganizationFundsTotal",
    "CardsChildOrganizationInvestorIdentifier",
    "CardsChildOrganizationLastEquityFundingTotal",
    "CardsChildOrganizationLastFundingTotal",
    "CardsChildOrganizationLinkedin",
    "CardsChildOrganizationLocationGroupIdentifier",
    "CardsChildOrganizationLocationIdentifier",
    "CardsChildOrganizationOwnerIdentifier",
    "CardsChildOrganizationStockSymbol",
    "CardsChildOrganizationTwitter",
    "CardsChildOrganizationValuation",
    "CardsChildOrganizationWebsite",
    "CardsChildOwnership",
    "CardsChildOwnershipIdentifier",
    "CardsChildOwnershipOwneeIdentifier",
    "CardsChildOwnershipOwnerIdentifier",
    "CardsClosurePrediction",
    "CardsClosurePredictionIdentifier",
    "CardsClosurePredictionAddress",
    "CardsClosurePredictionAward",
    "CardsClosurePredictionGrowthInsight",
    "CardsClosurePredictionKeyEmployeeChange",
    "CardsClosurePredictionLayoff",
    "CardsClosurePredictionLegalProceeding",
    "CardsClosurePredictionOrganization",
    "CardsClosurePredictionPartnershipAnnouncement",
    "CardsClosurePredictionProductLaunch",
    "CardsEventAppearance",
    "CardsEventAppearanceIdentifier",
    "CardsEventAppearanceEventIdentifier",
    "CardsEventAppearanceEventLocationIdentifier",
    "CardsEventAppearanceParticipantIdentifier",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsAcquirerIdentifier",
    "CardsFieldsCategory",
    "CardsFieldsCategoryGroup",
    "CardsFieldsClosedOn",
    "CardsFieldsDelistedOn",
    "CardsFieldsDiversitySpotlight",
    "CardsFieldsEquityFundingTotal",
    "CardsFieldsExitedOn",
    "CardsFieldsFacebook",
    "CardsFieldsFoundedOn",
    "CardsFieldsFounderIdentifier",
    "CardsFieldsFundingTotal",
    "CardsFieldsFundsTotal",
    "CardsFieldsInvestorIdentifier",
    "CardsFieldsLastEquityFundingTotal",
    "CardsFieldsLastFundingTotal",
    "CardsFieldsLinkedin",
    "CardsFieldsLocationGroupIdentifier",
    "CardsFieldsLocationIdentifier",
    "CardsFieldsOwnerIdentifier",
    "CardsFieldsStockSymbol",
    "CardsFieldsTwitter",
    "CardsFieldsValuation",
    "CardsFieldsWebsite",
    "CardsFounder",
    "CardsFounderIdentifier",
    "CardsFounderFacebook",
    "CardsFounderLinkedin",
    "CardsFounderLocationGroupIdentifier",
    "CardsFounderLocationIdentifier",
    "CardsFounderPrimaryOrganization",
    "CardsFounderTwitter",
    "CardsFounderWebsite",
    "CardsFundingPrediction",
    "CardsFundingPredictionIdentifier",
    "CardsFundingPredictionExampleFundingRound",
    "CardsFundingPredictionGrowthInsight",
    "CardsFundingPredictionKeyLeadershipHire",
    "CardsFundingPredictionOrganization",
    "CardsFundingPredictionPartnershipAnnouncement",
    "CardsFundingPredictionProductLaunch",
    "CardsFundingPredictionRunwaySpeculation",
    "CardsGrowthInsight",
    "CardsGrowthInsightIdentifier",
    "CardsGrowthInsightOrganization",
    "CardsHeadquartersAddress",
    "CardsHeadquartersAddressIdentifier",
    "CardsHeadquartersAddressHeadquarteredOrganizationIdentifier",
    "CardsHeadquartersAddressLocationIdentifier",
    "CardsHeadquartersAddressOrganization",
    "CardsInvestorInsight",
    "CardsInvestorInsightIdentifier",
    "CardsInvestorInsightCategory",
    "CardsInvestorInsightDiversityInvestment",
    "CardsInvestorInsightLocation",
    "CardsInvestorInsightMedianInvestmentSize",
    "CardsInvestorInsightOrganization",
    "CardsInvestor",
    "CardsInvestorIdentifier",
    "CardsInvestorCategory",
    "CardsInvestorCategoryGroup",
    "CardsInvestorClosedOn",
    "CardsInvestorDelistedOn",
    "CardsInvestorDiversitySpotlight",
    "CardsInvestorEquityFundingTotal",
    "CardsInvestorExitedOn",
    "CardsInvestorFacebook",
    "CardsInvestorFoundedOn",
    "CardsInvestorFounderIdentifier",
    "CardsInvestorFundingTotal",
    "CardsInvestorInvestorIdentifier",
    "CardsInvestorLastEquityFundingTotal",
    "CardsInvestorLastFundingTotal",
    "CardsInvestorLinkedin",
    "CardsInvestorLocationGroupIdentifier",
    "CardsInvestorLocationIdentifier",
    "CardsInvestorPrimaryOrganization",
    "CardsInvestorStockSymbol",
    "CardsInvestorTwitter",
    "CardsInvestorWebsite",
    "CardsIpoPrediction",
    "CardsIpoPredictionIdentifier",
    "CardsIpoPredictionExampleFundingRound",
    "CardsIpoPredictionExampleIpo",
    "CardsIpoPredictionGrowthInsight",
    "CardsIpoPredictionKeyLeadershipHire",
    "CardsIpoPredictionOrganization",
    "CardsIpo",
    "CardsIpoIdentifier",
    "CardsIpoAmountRaised",
    "CardsIpoDelistedOn",
    "CardsIpoOrganizationIdentifier",
    "CardsIpoSharePrice",
    "CardsIpoValuation",
    "CardsJob",
    "CardsJobIdentifier",
    "CardsJobEndedOn",
    "CardsJobOrganizationIdentifier",
    "CardsJobPersonIdentifier",
    "CardsJobStartedOn",
    "CardsKeyEmployeeChange",
    "CardsKeyEmployeeChangeIdentifier",
    "CardsKeyEmployeeChangeOrganizationIdentifier",
    "CardsLayoff",
    "CardsLayoffIdentifier",
    "CardsLayoffOrganizationIdentifier",
    "CardsParentOrganization",
    "CardsParentOrganizationIdentifier",
    "CardsParentOrganizationAcquirerIdentifier",
    "CardsParentOrganizationCategory",
    "CardsParentOrganizationCategoryGroup",
    "CardsParentOrganizationClosedOn",
    "CardsParentOrganizationDelistedOn",
    "CardsParentOrganizationDiversitySpotlight",
    "CardsParentOrganizationEquityFundingTotal",
    "CardsParentOrganizationExitedOn",
    "CardsParentOrganizationFacebook",
    "CardsParentOrganizationFoundedOn",
    "CardsParentOrganizationFounderIdentifier",
    "CardsParentOrganizationFundingTotal",
    "CardsParentOrganizationFundsTotal",
    "CardsParentOrganizationInvestorIdentifier",
    "CardsParentOrganizationLastEquityFundingTotal",
    "CardsParentOrganizationLastFundingTotal",
    "CardsParentOrganizationLinkedin",
    "CardsParentOrganizationLocationGroupIdentifier",
    "CardsParentOrganizationLocationIdentifier",
    "CardsParentOrganizationOwnerIdentifier",
    "CardsParentOrganizationStockSymbol",
    "CardsParentOrganizationTwitter",
    "CardsParentOrganizationValuation",
    "CardsParentOrganizationWebsite",
    "CardsParentOwnership",
    "CardsParentOwnershipIdentifier",
    "CardsParentOwnershipOwneeIdentifier",
    "CardsParentOwnershipOwnerIdentifier",
    "CardsParticipatedFundingRound",
    "CardsParticipatedFundingRoundIdentifier",
    "CardsParticipatedFundingRoundClosedOn",
    "CardsParticipatedFundingRoundFundedOrganizationCategory",
    "CardsParticipatedFundingRoundFundedOrganizationDiversitySpotlight",
    "CardsParticipatedFundingRoundFundedOrganizationFundingTotal",
    "CardsParticipatedFundingRoundFundedOrganizationIdentifier",
    "CardsParticipatedFundingRoundFundedOrganizationLocation",
    "CardsParticipatedFundingRoundInvestorIdentifier",
    "CardsParticipatedFundingRoundLeadInvestorIdentifier",
    "CardsParticipatedFundingRoundMoneyRaised",
    "CardsParticipatedFundingRoundPostMoneyValuation",
    "CardsParticipatedFundingRoundPreMoneyValuation",
    "CardsParticipatedFundingRoundTargetMoneyRaised",
    "CardsParticipatedFund",
    "CardsParticipatedFundIdentifier",
    "CardsParticipatedFundInvestorIdentifier",
    "CardsParticipatedFundMoneyRaised",
    "CardsParticipatedFundOwnerIdentifier",
    "CardsParticipatedFundStartedOn",
    "CardsParticipatedInvestment",
    "CardsParticipatedInvestmentIdentifier",
    "CardsParticipatedInvestmentFundingRoundIdentifier",
    "CardsParticipatedInvestmentFundingRoundMoneyRaised",
    "CardsParticipatedInvestmentInvestorIdentifier",
    "CardsParticipatedInvestmentMoneyInvested",
    "CardsParticipatedInvestmentOrganizationDiversitySpotlight",
    "CardsParticipatedInvestmentOrganizationIdentifier",
    "CardsParticipatedInvestmentPartnerIdentifier",
    "CardsPressReference",
    "CardsPressReferenceIdentifier",
    "CardsPressReferenceActivityEntity",
    "CardsPressReferenceURL",
    "CardsProduct",
    "CardsProductIdentifier",
    "CardsProductOrganization",
    "CardsRaisedFundingRound",
    "CardsRaisedFundingRoundIdentifier",
    "CardsRaisedFundingRoundClosedOn",
    "CardsRaisedFundingRoundFundedOrganizationCategory",
    "CardsRaisedFundingRoundFundedOrganizationDiversitySpotlight",
    "CardsRaisedFundingRoundFundedOrganizationFundingTotal",
    "CardsRaisedFundingRoundFundedOrganizationIdentifier",
    "CardsRaisedFundingRoundFundedOrganizationLocation",
    "CardsRaisedFundingRoundInvestorIdentifier",
    "CardsRaisedFundingRoundLeadInvestorIdentifier",
    "CardsRaisedFundingRoundMoneyRaised",
    "CardsRaisedFundingRoundPostMoneyValuation",
    "CardsRaisedFundingRoundPreMoneyValuation",
    "CardsRaisedFundingRoundTargetMoneyRaised",
    "CardsRaisedFund",
    "CardsRaisedFundIdentifier",
    "CardsRaisedFundInvestorIdentifier",
    "CardsRaisedFundMoneyRaised",
    "CardsRaisedFundOwnerIdentifier",
    "CardsRaisedFundStartedOn",
    "CardsRaisedInvestment",
    "CardsRaisedInvestmentIdentifier",
    "CardsRaisedInvestmentFundingRoundIdentifier",
    "CardsRaisedInvestmentFundingRoundMoneyRaised",
    "CardsRaisedInvestmentInvestorIdentifier",
    "CardsRaisedInvestmentMoneyInvested",
    "CardsRaisedInvestmentOrganizationDiversitySpotlight",
    "CardsRaisedInvestmentOrganizationIdentifier",
    "CardsRaisedInvestmentPartnerIdentifier",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesAcquirerIdentifier",
    "PropertiesCategory",
    "PropertiesCategoryGroup",
    "PropertiesClosedOn",
    "PropertiesDelistedOn",
    "PropertiesDiversitySpotlight",
    "PropertiesEquityFundingTotal",
    "PropertiesExitedOn",
    "PropertiesFacebook",
    "PropertiesFoundedOn",
    "PropertiesFounderIdentifier",
    "PropertiesFundingTotal",
    "PropertiesFundsTotal",
    "PropertiesInvestorIdentifier",
    "PropertiesLastEquityFundingTotal",
    "PropertiesLastFundingTotal",
    "PropertiesLinkedin",
    "PropertiesLocationGroupIdentifier",
    "PropertiesLocationIdentifier",
    "PropertiesOwnerIdentifier",
    "PropertiesStockSymbol",
    "PropertiesTwitter",
    "PropertiesValuation",
    "PropertiesWebsite",
]


class CardsAcquireeAcquisitionIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquireeAcquisitionAcquireeCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquireeAcquisitionAcquireeFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsAcquireeAcquisitionAcquireeIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquireeAcquisitionAcquireeLocation(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsAcquireeAcquisitionAcquirerCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquireeAcquisitionAcquirerFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsAcquireeAcquisitionAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquireeAcquisitionAcquirerLocation(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsAcquireeAcquisitionAnnouncedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsAcquireeAcquisitionCompletedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsAcquireeAcquisitionPrice(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsAcquireeAcquisition(BaseModel):
    identifier: CardsAcquireeAcquisitionIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquiree_categories: Optional[List[CardsAcquireeAcquisitionAcquireeCategory]] = None
    """Keyword, sector, or industry"""

    acquiree_funding_total: Optional[CardsAcquireeAcquisitionAcquireeFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    acquiree_identifier: Optional[CardsAcquireeAcquisitionAcquireeIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquiree_last_funding_type: Optional[str] = None
    """Last funding round type (e.g. Series A, Seed, Private Equity)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    acquiree_locations: Optional[List[CardsAcquireeAcquisitionAcquireeLocation]] = None
    """Where the acquired organization is headquartered"""

    acquiree_num_funding_rounds: Optional[float] = None
    """Acquired organization's total number of funding rounds"""

    acquiree_revenue_range: Optional[str] = None
    """Estimated revenue range for acquired organization

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    acquiree_short_description: Optional[str] = None
    """Text of acquired organization's description, industries, and industry groups"""

    acquirer_categories: Optional[List[CardsAcquireeAcquisitionAcquirerCategory]] = None
    """Keyword, sector, or industry"""

    acquirer_funding_stage: Optional[str] = None
    """Acquiring organization's most recent funding status

    - early_stage_venture - Early Stage Venture
    - ipo - IPO
    - late_stage_venture - Late Stage Venture
    - m_and_a - M&A
    - private_equity - Private Equity
    - seed - Seed
    """

    acquirer_funding_total: Optional[CardsAcquireeAcquisitionAcquirerFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    acquirer_identifier: Optional[CardsAcquireeAcquisitionAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_locations: Optional[List[CardsAcquireeAcquisitionAcquirerLocation]] = None
    """Where the organization is headquartered"""

    acquirer_num_funding_rounds: Optional[float] = None
    """Acquiring organization's total number of funding rounds"""

    acquirer_revenue_range: Optional[str] = None
    """Estimated revenue range for acquiring organization

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    acquirer_short_description: Optional[str] = None
    """Text of acquiring organization's description, industries, and industry groups"""

    acquisition_type: Optional[str] = None
    """Type of acquisition

    - acquihire - Acquihire
    - acquisition - Acquisition
    - lbo - Leveraged Buyout
    - management_buyout - Management Buyout
    - merge - Merger
    """

    announced_on: Optional[CardsAcquireeAcquisitionAnnouncedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    completed_on: Optional[CardsAcquireeAcquisitionCompletedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    created_at: Optional[datetime] = None

    disposition_of_acquired: Optional[str] = None
    """How is the acquired Organization structured after the acquisition

    - combined - Combined
    - division - Division
    - product - Product
    - separate_entity - Separate Entity
    - subsidiary - Subsidiary
    """

    entity_def_id: Optional[str] = None
    """- acquisition - Acquisition"""

    permalink: Optional[str] = None

    price: Optional[CardsAcquireeAcquisitionPrice] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_acquisition: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Acquisitions"""

    short_description: Optional[str] = None
    """Short description of the Acquisition"""

    status: Optional[str] = None
    """Status of the acquisition

    - complete - Complete
    - pending - Pending
    """

    terms: Optional[str] = None
    """Terms of the acquisition

    - cash - Cash
    - cash_and_stock - Cash & Stock
    - stock - Stock
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsAcquirerAcquisitionIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquirerAcquisitionAcquireeCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquirerAcquisitionAcquireeFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsAcquirerAcquisitionAcquireeIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquirerAcquisitionAcquireeLocation(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsAcquirerAcquisitionAcquirerCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquirerAcquisitionAcquirerFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsAcquirerAcquisitionAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquirerAcquisitionAcquirerLocation(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsAcquirerAcquisitionAnnouncedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsAcquirerAcquisitionCompletedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsAcquirerAcquisitionPrice(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsAcquirerAcquisition(BaseModel):
    identifier: CardsAcquirerAcquisitionIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquiree_categories: Optional[List[CardsAcquirerAcquisitionAcquireeCategory]] = None
    """Keyword, sector, or industry"""

    acquiree_funding_total: Optional[CardsAcquirerAcquisitionAcquireeFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    acquiree_identifier: Optional[CardsAcquirerAcquisitionAcquireeIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquiree_last_funding_type: Optional[str] = None
    """Last funding round type (e.g. Series A, Seed, Private Equity)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    acquiree_locations: Optional[List[CardsAcquirerAcquisitionAcquireeLocation]] = None
    """Where the acquired organization is headquartered"""

    acquiree_num_funding_rounds: Optional[float] = None
    """Acquired organization's total number of funding rounds"""

    acquiree_revenue_range: Optional[str] = None
    """Estimated revenue range for acquired organization

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    acquiree_short_description: Optional[str] = None
    """Text of acquired organization's description, industries, and industry groups"""

    acquirer_categories: Optional[List[CardsAcquirerAcquisitionAcquirerCategory]] = None
    """Keyword, sector, or industry"""

    acquirer_funding_stage: Optional[str] = None
    """Acquiring organization's most recent funding status

    - early_stage_venture - Early Stage Venture
    - ipo - IPO
    - late_stage_venture - Late Stage Venture
    - m_and_a - M&A
    - private_equity - Private Equity
    - seed - Seed
    """

    acquirer_funding_total: Optional[CardsAcquirerAcquisitionAcquirerFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    acquirer_identifier: Optional[CardsAcquirerAcquisitionAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_locations: Optional[List[CardsAcquirerAcquisitionAcquirerLocation]] = None
    """Where the organization is headquartered"""

    acquirer_num_funding_rounds: Optional[float] = None
    """Acquiring organization's total number of funding rounds"""

    acquirer_revenue_range: Optional[str] = None
    """Estimated revenue range for acquiring organization

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    acquirer_short_description: Optional[str] = None
    """Text of acquiring organization's description, industries, and industry groups"""

    acquisition_type: Optional[str] = None
    """Type of acquisition

    - acquihire - Acquihire
    - acquisition - Acquisition
    - lbo - Leveraged Buyout
    - management_buyout - Management Buyout
    - merge - Merger
    """

    announced_on: Optional[CardsAcquirerAcquisitionAnnouncedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    completed_on: Optional[CardsAcquirerAcquisitionCompletedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    created_at: Optional[datetime] = None

    disposition_of_acquired: Optional[str] = None
    """How is the acquired Organization structured after the acquisition

    - combined - Combined
    - division - Division
    - product - Product
    - separate_entity - Separate Entity
    - subsidiary - Subsidiary
    """

    entity_def_id: Optional[str] = None
    """- acquisition - Acquisition"""

    permalink: Optional[str] = None

    price: Optional[CardsAcquirerAcquisitionPrice] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_acquisition: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Acquisitions"""

    short_description: Optional[str] = None
    """Short description of the Acquisition"""

    status: Optional[str] = None
    """Status of the acquisition

    - complete - Complete
    - pending - Pending
    """

    terms: Optional[str] = None
    """Terms of the acquisition

    - cash - Cash
    - cash_and_stock - Cash & Stock
    - stock - Stock
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsAcquisitionPredictionIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquisitionPredictionExampleAcquisition(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquisitionPredictionGrowthInsight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquisitionPredictionKeyLeadershipHire(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquisitionPredictionOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquisitionPredictionPartnershipAnnouncement(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquisitionPredictionRunwaySpeculation(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAcquisitionPrediction(BaseModel):
    identifier: CardsAcquisitionPredictionIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None
    """Time of Creation"""

    entity_def_id: Optional[str] = None
    """Entity Def Type

    - acquisition_prediction - Acquisition Prediction
    """

    example_acquisition: Optional[CardsAcquisitionPredictionExampleAcquisition] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this Acquisition Prediction was generated"""

    growth_insight: Optional[CardsAcquisitionPredictionGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_leadership_hire: Optional[CardsAcquisitionPredictionKeyLeadershipHire] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    organization: Optional[CardsAcquisitionPredictionOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partnership_announcement: Optional[CardsAcquisitionPredictionPartnershipAnnouncement] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    probability_score: Optional[float] = None
    """The predicted probability that this Organization will be acquired"""

    runway_speculation: Optional[CardsAcquisitionPredictionRunwaySpeculation] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Time of Update"""

    uuid: Optional[str] = None
    """UUID"""


class CardsChildOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsChildOrganizationDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsChildOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsChildOrganizationExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsChildOrganizationFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsChildOrganizationFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsChildOrganizationFundsTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsChildOrganizationInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationLastEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsChildOrganizationLastFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsChildOrganizationLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationLocationGroupIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsChildOrganizationLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsChildOrganizationOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganizationValuation(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsChildOrganizationWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsChildOrganization(BaseModel):
    identifier: CardsChildOrganizationIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_identifier: Optional[CardsChildOrganizationAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None
    """Alternate or previous names for the organization"""

    categories: Optional[List[CardsChildOrganizationCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsChildOrganizationCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsChildOrganizationClosedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    company_type: Optional[str] = None
    """Whether an Organization is for profit or non-profit

    - for_profit - For Profit
    - non_profit - Non-profit
    """

    contact_email: Optional[str] = None
    """General contact email for the organization"""

    created_at: Optional[datetime] = None

    delisted_on: Optional[CardsChildOrganizationDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    demo_days: Optional[bool] = None
    """Whether an accelerator hosts any demo days"""

    description: Optional[str] = None
    """Organization Description, Industries, Industry Groups"""

    diversity_spotlights: Optional[List[CardsChildOrganizationDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    entity_def_id: Optional[str] = None
    """- organization - Organization"""

    equity_funding_total: Optional[CardsChildOrganizationEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsChildOrganizationExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsChildOrganizationFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    founded_on: Optional[CardsChildOrganizationFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsChildOrganizationFounderIdentifier]] = None
    """Founders of the organization"""

    funding_stage: Optional[str] = None
    """This field describes an organization's most recent funding status (e.g.

    Early Stage Venture, Late Stage Venture, M&A)

    - early_stage_venture - Early Stage Venture
    - ipo - IPO
    - late_stage_venture - Late Stage Venture
    - m_and_a - M&A
    - private_equity - Private Equity
    - seed - Seed
    """

    funding_total: Optional[CardsChildOrganizationFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funds_total: Optional[CardsChildOrganizationFundsTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    growth_insight_confidence: Optional[str] = None
    """Confidence level associated with this company's growth status

    - c100_unknown - Unknown
    - c200_low - Low
    - c300_medium - Medium
    - c400_high - High
    """

    growth_insight_direction: Optional[str] = None
    """
    - c100_uncertain - Uncertain
    - c200_declining - Not Growing
    - c300_stable - Stable
    - c400_growing - Growing
    """

    hub_tags: Optional[List[str]] = None
    """
    Tags are labels assigned to organizations, which identify their belonging to a
    group with that shared label
    """

    image_id: Optional[str] = None
    """The profile image of the organization on Crunchbase"""

    image_url: Optional[str] = None
    """The url of the profile image"""

    investor_identifiers: Optional[List[CardsChildOrganizationInvestorIdentifier]] = None
    """
    The top 5 investors with investments in this company, ordered by Crunchbase Rank
    """

    investor_stage: Optional[List[str]] = None
    """This describes the stage of investments made by this organization (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    investor_type: Optional[List[str]] = None
    """This describes the type of investor this organization is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    ipo_status: Optional[str] = None
    """The current public status of the Organization

    - delisted - Delisted
    - private - Private
    - public - Public
    """

    last_equity_funding_total: Optional[CardsChildOrganizationLastEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_equity_funding_type: Optional[str] = None
    """The most recent Funding Round excluding debt

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_funding_at: Optional[date] = None
    """Date of most recent Funding Round"""

    last_funding_total: Optional[CardsChildOrganizationLastFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_funding_type: Optional[str] = None
    """Last funding round type (e.g. Seed, Series A, Private Equity)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_key_employee_change_date: Optional[date] = None
    """See companies that have hired executives (VP and above) in a certain date range"""

    last_layoff_date: Optional[date] = None
    """Date of last layoff event"""

    layout_id: Optional[str] = None
    """This is the auto-generated layout for the profile

    - investor - Investor Layout
    - school - School Layout
    """

    legal_name: Optional[str] = None
    """The legal name of the organization"""

    linkedin: Optional[CardsChildOrganizationLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    listed_stock_symbol: Optional[str] = None
    """Stock ticker symbol (e.g. AAPL, FB, TWTR)"""

    location_group_identifiers: Optional[List[CardsChildOrganizationLocationGroupIdentifier]] = None
    """Where the organization is headquartered (e.g.

    San Francisco Bay Area, Silicon Valley)
    """

    location_identifiers: Optional[List[CardsChildOrganizationLocationIdentifier]] = None
    """Where the organization is headquartered"""

    name: Optional[str] = None

    num_acquisitions: Optional[float] = None
    """Total number of Acquisitions"""

    num_alumni: Optional[float] = None
    """Total number of alumni"""

    num_articles: Optional[float] = None
    """Number of news articles that reference the Organization"""

    num_current_advisor_positions: Optional[float] = None
    """
    Total number of board member and advisor profiles an organization has on
    Crunchbase
    """

    num_current_positions: Optional[float] = None
    """Total number of employee profiles an organization has on Crunchbase"""

    num_diversity_spotlight_investments: Optional[float] = None
    """Total number of diversity investments made by an investor"""

    num_employees_enum: Optional[str] = None
    """Total number of employees

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_enrollments: Optional[str] = None
    """Total number of Enrollments

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_event_appearances: Optional[float] = None
    """Total number of events an Organization appeared in"""

    num_exits: Optional[float] = None
    """Total number of Exits"""

    num_exits_ipo: Optional[float] = None
    """Total number of Exits (IPO)"""

    num_founder_alumni: Optional[float] = None
    """Total number of Alumni that are Founders"""

    num_founders: Optional[float] = None
    """Total number of Founders"""

    num_funding_rounds: Optional[float] = None
    """Total number of Funding Rounds"""

    num_funds: Optional[float] = None
    """Total number of Funds raised"""

    num_investments: Optional[float] = None
    """Total number of Investments made"""

    num_investors: Optional[float] = None
    """Total number of investment firms and individual investors"""

    num_lead_investments: Optional[float] = None
    """Total number of Lead Investments made"""

    num_lead_investors: Optional[float] = None
    """Total number of lead investment firms and individual investors"""

    num_past_positions: Optional[float] = None
    """Total number of past employee profiles of an organization"""

    num_portfolio_organizations: Optional[float] = None
    """Total number of portfolio organizations"""

    num_sub_organizations: Optional[float] = None
    """Total number of sub-organizations that belongs to a parent Organization"""

    operating_status: Optional[str] = None
    """Operating Status of Organization e.g. Active, Closed

    - active - Active
    - closed - Closed
    """

    owner_identifier: Optional[CardsChildOrganizationOwnerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    phone_number: Optional[str] = None
    """Organization's general phone number"""

    program_application_deadline: Optional[date] = None
    """The deadline for applying to the Accelerator Program"""

    program_duration: Optional[float] = None
    """The duration of the Acceleration Program in number of weeks"""

    program_type: Optional[str] = None
    """The type of Accelerator Program (e.g. On-Site, Online)

    - on_site - On-Site
    - online - Online
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_delta_d30: Optional[float] = None
    """Movement in Rank over the last 30 days using a score from -10 to 10"""

    rank_delta_d7: Optional[float] = None
    """Movement in Rank over the last 7 days using a score from -10 to 10"""

    rank_delta_d90: Optional[float] = None
    """Movement in Rank over the last 90 days using a score from -10 to 10"""

    rank_org: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Organizations"""

    revenue_range: Optional[str] = None
    """Estimated revenue range for organization

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    school_method: Optional[str] = None
    """The type of School Method (e.g. On Campus, Online)

    - on_compus - On Campus
    - online - Online
    - online_and_on_campus - Online and On Campus
    """

    school_program: Optional[str] = None
    """The type of School Program (e.g. Bootcamp, Four Year University)

    - bootcamp - Bootcamp
    - community_college - Community College
    - four_year_university - Four Year University
    - graduate_university - Graduate University
    - high_school - High School
    - trade_school - Trade School
    - two_year_university - Two Year University
    """

    school_type: Optional[str] = None
    """The type of school

    - for_profit_private - Private
    - non_profit_private - Private (Non-Profit)
    - public - Public
    """

    short_description: Optional[str] = None
    """Text of Organization Description, Industries, and Industry Groups"""

    status: Optional[str] = None
    """Status of Organization e.g. Operating, Closed, Acquired, IPO

    - closed - Closed
    - ipo - IPO
    - operating - Operating
    - was_acquired - Was Acquired
    """

    stock_exchange_symbol: Optional[str] = None
    """Stock exchange where the Organization is listed e.g. NYSE, NASDAQ

    - adx - ADX - Abu Dhabi Securities Exchange
    - afx - AFX - Afghanistan Stock Exchange
    - altx - ALTX - ALTX East Africa Exchange
    - amex - AMEX - American Stock Exchange
    - ams - AMS - Euronext Amsterdam
    - amx - AMX - Armenia Securities Exchange
    - asce - ASCE - Abuja Securities and Commodities Exchange
    - asx - ASX - Australian Securities Exchange
    - ath - ATH - Athens Stock Exchange
    - bcba - BCBA - Buenos Aires Stock Exchange
    - bdp - BDP - Budapest Stock Exchange
    - belex - BELEX - Belgrade Stock Exchange
    - ber - BER - Berliner Börse
    - bfb - BFB - Baku Stock Exchange
    - bit - BIT - Italian Stock Exchange
    - bkk - BKK - Thailand Stock Exchange
    - blse - BLSE - Banja Luka Stock Exchange
    - bme - BME - Madrid Stock Exchange
    - bmv - BMV - Mexican Stock Exchange
    - bom - BOM - Bombay Stock Exchange
    - brvm - BRVM - Regional Securities Exchange SA
    - bse - BSE - Bulgarian Stock Exchange
    - bse_lb - BSE - Beirut Stock Exchange
    - bsse - BSSE - Bratislava Stock Exchange
    - bsx - BSX - Bermuda Stock Exchange
    - bvb - BVB - Bucharest Stock Exchange
    - bvc - BVC - Colombian Stock Exchange
    - bvfb - BVFB - Belarusian Currency and Stock Exchange
    - bvm - BVM - Montevideo Stock Exchange
    - bvmf - B3 - Brazil Stock Exchange and OTC Market
    - bvmt - BVMT - Tunis Stock Exchange
    - bx - BX - Berne Stock Exchange
    - cas - CAS - Casablanca Stock Exchange
    - cise - CISE - Channel Islands Stock Exchange
    - cnsx - CNSX - Canadian National Stock Exchange
    - col - COL - Colombo Stock Exchange
    - cph - CPH - Copenhagen Stock Exchange
    - cse - CSE - Canadian Securities Exchange
    - cse_cy - CSE - Cyprus Stock Exchange
    - csx - CSX - Cambodia Securities Exchange
    - cve - TSX-V - Toronto TSX Venture Exchange
    - dfm - DFM - Dubai Financial Market
    - dse - DSE - Dhaka Stock Exchange
    - dsx - DSX - Douala Stock Exchange
    - dus - DUS - Börse Düsseldorf
    - ebr - EBR - Euronext Brussels
    - egx - EGX - Egypt Stock Exchange
    - eli - ELI - Euronext Lisbon
    - epa - EPA - Euronext Paris
    - etr - ETR - Deutsche Börse XETRA
    - eurex - EUREX - Eurex Exchange
    - fra - FRA - Frankfurt Stock Exchange
    - fwb - FWB - Börse Frankfurt Stock Exchange
    - gha - GHA - Ghana Stock Exchange
    - gsx - GSX - Georgian Stock Exchange
    - gsx_gi - GSX - Gibraltar Stock Exchange
    - hel - HEL - Helsinki Stock Exchange
    - hkg - HKG - Hong Kong Stock Exchange
    - hnx - HNX - Hanoi Stock Exchange
    - hose - HOSE - Ho Chi Minh Stock Exchange
    - ice - ICE - Iceland Stock Exchange
    - idx - IDX - Indonesia Stock Exchange
    - iex - IEX - Investors Exchange
    - ifb - IFB - Iran Fara Bourse
    - ime - IME - Iran Mercantile Exchange
    - irenex - IRENEX - Iran Energy Exchange
    - ise - ISE - Irish Stock Exchange
    - ist - IST - Istanbul Stock Exchange
    - isx - ISX - Iraq Stock Exchange
    - jp - JP - Japan Exchange
    - jsc - JSC - Belarusian Currency and Stock Exchange
    - jse - JSE - Johannesburg Stock Exchange
    - jse_jam - JSE - Jamaica Stock Exchange
    - kase - KASE - Kazakhstan Stock Exchange
    - klse - KLSE - Malaysia Stock Exchange
    - kosdaq - KOSDAQ - Korean Securities Dealers Automated Quotations
    - krx - KRX - Korea Stock Exchange
    - kse - KSE - Kuwait Stock Exchange
    - lje - LJE - Ljubljana Stock Exchange
    - lse - LSE - London Stock Exchange
    - lsm - LSM - Libyan Stock Market
    - lsx - LSX - Lao Securities Exchange
    - luse - LuSE - Lusaka Securities Exchange
    - luxse - LuxSE - Luxembourg Stock Exchange
    - mal - MAL - Malta Stock Exchange
    - mcx - MCX - Multi Commodity Exchange of India
    - meff - MEFF - Mercado Spanish Financial Futures Market
    - mnse - MNSE - Montenegro Stock Exchange
    - moex - MOEX - Moscow Exchange
    - mse - MSE - Metropolitan Stock Exchange
    - mse_md - MSE - Moldova Stock Exchange
    - mse_mk - MSE - Macedonian Stock Exchange
    - msei - MSEI - Metropolitan Stock Exchange of India
    - msm - MSM - Muscat Securities Market
    - mun - MUN - Börse München
    - nasdaq - NASDAQ
    - nbo - NSE - Nairobi Securities Exchange
    - neeq - NEEQ - National Equities Exchange and Quotations
    - nepse - NEPSE - Nepal Stock Exchange
    - nex - NEX - NEX Exchange
    - ngm - NGM - Nordic Growth Market Exchange
    - nig - NIG - Nigerian Stock Exchange
    - notc - NOTC - Norwegian OTC
    - npex - NPEX - NPEX Stock Exchange
    - nse - NSE - National Stock Exchange of India
    - nsx - NSX - National Stock Exchange of Australia
    - nyse - NYSE - New York Stock Exchange
    - nysearca - NYSEARCA - NYSE Arca
    - nysemkt - NYSEAMERICAN - NYSE American
    - nze - NZE - New Zealand Stock Exchange
    - ose - OSE - Oslo Stock Exchange
    - otcbb - OTCBB - FINRA OTC Bulletin Board
    - otcpink - OTC Pink
    - otcqb - OTCQB
    - otcqx - OTCQX
    - pdex - PDEx - Philippine Dealing Exchange
    - pex - PEX - Palestine Exchange
    - pfts - PFTS - PFTS Ukraine Stock Exchange
    - pomsox - POMSoX - Port Moresby Stock Exchange
    - prg - PRA - Prague Stock Exchange
    - pse - PSE - Philippine Stock Exchange
    - psx - PSX - Pakistan Stock Exchange
    - qse - QSE - Qatar Stock Exchange
    - rfb - RFB - Riga Stock Exchange
    - rse - RSE - Rwanda Stock Exchange
    - rsebl - RSEBL - Royal Securities Exchange of Bhutan
    - sase - SASE - Sarajevo Stock Exchange
    - sbx - SBX - BX Swiss
    - sehk - SEHK - The Stock Exchange of Hong Kong
    - sem - SEM - Stock Exchange of Mauritius
    - sgbv - SGBV - Algiers Stock Exchange
    - sgx - SGX - Singapore Stock Exchange
    - six - SIX - SIX Swiss Exchange
    - spbex - SPBEX - Saint Petersburg Stock Exchange
    - spse - SPSE - South Pacific Stock Exchange
    - sse - SSE - Shanghai Stock Exchange
    - ssx - SSX - Sydney Stock Exchange
    - sto - STO - Stockholm Stock Exchange
    - stu - STU - Börse Stuttgart
    - swx - SWX - SIX Swiss Exchange
    - szse - SZSE - Shenzhen Stock Exchange
    - tadawul - Tadawul - Saudi Stock Exchange
    - tal - TSE - Tallinn Stock Exchange
    - tfex - TFEX - Thailand Futures Exchange
    - tise - TISE - The International Stock Exchange
    - tlv - TLV - Tel Aviv Stock Exchange
    - tpe - TWSE - Taiwan Stock Exchange
    - tse_al - TSE - Tirana Stock Exchange
    - tse_ir - TSE - Tehran Stock Exchange
    - tsec - TWO - Taiwan OTC Exchange
    - tsx - TSX - Toronto Stock Exchange
    - ttse - TTSE - Trinidad and Tobago Stock Exchange
    - tyo - TYO - Tokyo Stock Exchange
    - use - USE - Uganda Securities Exchange
    - ux - UX - Ukrainian Exchange
    - vie - VIE - Vienna Stock Exchange
    - vmf - VMF - Faroese Securities Market
    - vse - VSE - Vancouver Stock Exchange
    - wse - WSE - Warsaw Stock Exchange
    - ysx - YSX - Yangon Stock Exchange
    - zamace - ZAMACE - Zambian Commodity Exchange
    - zse - ZSE - Zimbabwe Stock Exchange
    - zse_hr - ZSE - Zagreb Stock Exchange
    """

    stock_symbol: Optional[CardsChildOrganizationStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsChildOrganizationTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    valuation: Optional[CardsChildOrganizationValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    valuation_date: Optional[date] = None
    """Date of latest post money valuation"""

    website: Optional[CardsChildOrganizationWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class CardsChildOwnershipIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOwnershipOwneeIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOwnershipOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsChildOwnership(BaseModel):
    identifier: CardsChildOwnershipIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- ownership - Ownership"""

    name: Optional[str] = None

    ownee_identifier: Optional[CardsChildOwnershipOwneeIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    owner_identifier: Optional[CardsChildOwnershipOwnerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    ownership_type: Optional[str] = None
    """
    This is the relationship defining how a sub-organization is related to a parent
    organization

    - affiliated_company - Affiliated Company
    - division - Division
    - investment_arm - Investment Arm
    - joint_venture - Joint Venture
    - subsidiary - Subsidiary
    """

    permalink: Optional[str] = None

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsClosurePredictionIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePredictionAddress(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePredictionAward(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePredictionGrowthInsight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePredictionKeyEmployeeChange(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePredictionLayoff(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePredictionLegalProceeding(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePredictionOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePredictionPartnershipAnnouncement(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePredictionProductLaunch(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsClosurePrediction(BaseModel):
    identifier: CardsClosurePredictionIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    address: Optional[CardsClosurePredictionAddress] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    award: Optional[CardsClosurePredictionAward] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- closure_prediction - Closure Prediction"""

    generated_on: Optional[date] = None

    growth_insight: Optional[CardsClosurePredictionGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_employee_change: Optional[CardsClosurePredictionKeyEmployeeChange] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    layoff: Optional[CardsClosurePredictionLayoff] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    legal_proceeding: Optional[CardsClosurePredictionLegalProceeding] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    media_sentiment: Optional[str] = None
    """
    - c100_evidence_absent - No Increased Negative Media Coverage
    - c200_evidence_present - Increased Negative Media Coverage
    """

    organization: Optional[CardsClosurePredictionOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partnership_announcement: Optional[CardsClosurePredictionPartnershipAnnouncement] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    probability_score: Optional[float] = None

    probability_tier: Optional[str] = None
    """
    - p100_positive_high - Very Likely
    - p200_positive_low - Likely
    - p300_neutral - Unsure
    - p400_negative_low - Unlikely
    - p500_negative_high - Very Unlikely
    """

    product_launch: Optional[CardsClosurePredictionProductLaunch] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsEventAppearanceIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsEventAppearanceEventIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsEventAppearanceEventLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsEventAppearanceParticipantIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsEventAppearance(BaseModel):
    identifier: CardsEventAppearanceIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    appearance_type: Optional[str] = None
    """Describe how an Organization or a Person is participating in an Event (e.g.

    Speaker, Sponsor, etc.)

    - contestant - Contestant
    - exhibitor - Exhibitor
    - organizer - Organizer
    - speaker - Speaker
    - sponsor - Sponsor
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- event_appearance - Event Appearance"""

    event_identifier: Optional[CardsEventAppearanceEventIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    event_location_identifiers: Optional[List[CardsEventAppearanceEventLocationIdentifier]] = None
    """Location of the Event (e.g. Japan, San Francisco, Europe, Asia)"""

    event_starts_on: Optional[date] = None
    """Start date of the Event"""

    name: Optional[str] = None

    participant_identifier: Optional[CardsEventAppearanceParticipantIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    short_description: Optional[str] = None
    """
    A short description of how a person or an organization is participant in an
    Event
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsFieldsIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsFieldsDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsFieldsDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsFieldsExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsFieldsFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsFieldsFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsFieldsFundsTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsFieldsInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsLastEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsFieldsLastFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsFieldsLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsLocationGroupIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsFieldsLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsFieldsOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsValuation(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsFieldsWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFields(BaseModel):
    identifier: CardsFieldsIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_identifier: Optional[CardsFieldsAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None
    """Alternate or previous names for the organization"""

    categories: Optional[List[CardsFieldsCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsFieldsCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsFieldsClosedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    company_type: Optional[str] = None
    """Whether an Organization is for profit or non-profit

    - for_profit - For Profit
    - non_profit - Non-profit
    """

    contact_email: Optional[str] = None
    """General contact email for the organization"""

    created_at: Optional[datetime] = None

    delisted_on: Optional[CardsFieldsDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    demo_days: Optional[bool] = None
    """Whether an accelerator hosts any demo days"""

    description: Optional[str] = None
    """Organization Description, Industries, Industry Groups"""

    diversity_spotlights: Optional[List[CardsFieldsDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    entity_def_id: Optional[str] = None
    """- organization - Organization"""

    equity_funding_total: Optional[CardsFieldsEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsFieldsExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsFieldsFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    founded_on: Optional[CardsFieldsFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsFieldsFounderIdentifier]] = None
    """Founders of the organization"""

    funding_stage: Optional[str] = None
    """This field describes an organization's most recent funding status (e.g.

    Early Stage Venture, Late Stage Venture, M&A)

    - early_stage_venture - Early Stage Venture
    - ipo - IPO
    - late_stage_venture - Late Stage Venture
    - m_and_a - M&A
    - private_equity - Private Equity
    - seed - Seed
    """

    funding_total: Optional[CardsFieldsFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funds_total: Optional[CardsFieldsFundsTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    growth_insight_confidence: Optional[str] = None
    """Confidence level associated with this company's growth status

    - c100_unknown - Unknown
    - c200_low - Low
    - c300_medium - Medium
    - c400_high - High
    """

    growth_insight_direction: Optional[str] = None
    """
    - c100_uncertain - Uncertain
    - c200_declining - Not Growing
    - c300_stable - Stable
    - c400_growing - Growing
    """

    hub_tags: Optional[List[str]] = None
    """
    Tags are labels assigned to organizations, which identify their belonging to a
    group with that shared label
    """

    image_id: Optional[str] = None
    """The profile image of the organization on Crunchbase"""

    image_url: Optional[str] = None
    """The url of the profile image"""

    investor_identifiers: Optional[List[CardsFieldsInvestorIdentifier]] = None
    """
    The top 5 investors with investments in this company, ordered by Crunchbase Rank
    """

    investor_stage: Optional[List[str]] = None
    """This describes the stage of investments made by this organization (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    investor_type: Optional[List[str]] = None
    """This describes the type of investor this organization is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    ipo_status: Optional[str] = None
    """The current public status of the Organization

    - delisted - Delisted
    - private - Private
    - public - Public
    """

    last_equity_funding_total: Optional[CardsFieldsLastEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_equity_funding_type: Optional[str] = None
    """The most recent Funding Round excluding debt

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_funding_at: Optional[date] = None
    """Date of most recent Funding Round"""

    last_funding_total: Optional[CardsFieldsLastFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_funding_type: Optional[str] = None
    """Last funding round type (e.g. Seed, Series A, Private Equity)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_key_employee_change_date: Optional[date] = None
    """See companies that have hired executives (VP and above) in a certain date range"""

    last_layoff_date: Optional[date] = None
    """Date of last layoff event"""

    layout_id: Optional[str] = None
    """This is the auto-generated layout for the profile

    - investor - Investor Layout
    - school - School Layout
    """

    legal_name: Optional[str] = None
    """The legal name of the organization"""

    linkedin: Optional[CardsFieldsLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    listed_stock_symbol: Optional[str] = None
    """Stock ticker symbol (e.g. AAPL, FB, TWTR)"""

    location_group_identifiers: Optional[List[CardsFieldsLocationGroupIdentifier]] = None
    """Where the organization is headquartered (e.g.

    San Francisco Bay Area, Silicon Valley)
    """

    location_identifiers: Optional[List[CardsFieldsLocationIdentifier]] = None
    """Where the organization is headquartered"""

    name: Optional[str] = None

    num_acquisitions: Optional[float] = None
    """Total number of Acquisitions"""

    num_alumni: Optional[float] = None
    """Total number of alumni"""

    num_articles: Optional[float] = None
    """Number of news articles that reference the Organization"""

    num_current_advisor_positions: Optional[float] = None
    """
    Total number of board member and advisor profiles an organization has on
    Crunchbase
    """

    num_current_positions: Optional[float] = None
    """Total number of employee profiles an organization has on Crunchbase"""

    num_diversity_spotlight_investments: Optional[float] = None
    """Total number of diversity investments made by an investor"""

    num_employees_enum: Optional[str] = None
    """Total number of employees

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_enrollments: Optional[str] = None
    """Total number of Enrollments

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_event_appearances: Optional[float] = None
    """Total number of events an Organization appeared in"""

    num_exits: Optional[float] = None
    """Total number of Exits"""

    num_exits_ipo: Optional[float] = None
    """Total number of Exits (IPO)"""

    num_founder_alumni: Optional[float] = None
    """Total number of Alumni that are Founders"""

    num_founders: Optional[float] = None
    """Total number of Founders"""

    num_funding_rounds: Optional[float] = None
    """Total number of Funding Rounds"""

    num_funds: Optional[float] = None
    """Total number of Funds raised"""

    num_investments: Optional[float] = None
    """Total number of Investments made"""

    num_investors: Optional[float] = None
    """Total number of investment firms and individual investors"""

    num_lead_investments: Optional[float] = None
    """Total number of Lead Investments made"""

    num_lead_investors: Optional[float] = None
    """Total number of lead investment firms and individual investors"""

    num_past_positions: Optional[float] = None
    """Total number of past employee profiles of an organization"""

    num_portfolio_organizations: Optional[float] = None
    """Total number of portfolio organizations"""

    num_sub_organizations: Optional[float] = None
    """Total number of sub-organizations that belongs to a parent Organization"""

    operating_status: Optional[str] = None
    """Operating Status of Organization e.g. Active, Closed

    - active - Active
    - closed - Closed
    """

    owner_identifier: Optional[CardsFieldsOwnerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    phone_number: Optional[str] = None
    """Organization's general phone number"""

    program_application_deadline: Optional[date] = None
    """The deadline for applying to the Accelerator Program"""

    program_duration: Optional[float] = None
    """The duration of the Acceleration Program in number of weeks"""

    program_type: Optional[str] = None
    """The type of Accelerator Program (e.g. On-Site, Online)

    - on_site - On-Site
    - online - Online
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_delta_d30: Optional[float] = None
    """Movement in Rank over the last 30 days using a score from -10 to 10"""

    rank_delta_d7: Optional[float] = None
    """Movement in Rank over the last 7 days using a score from -10 to 10"""

    rank_delta_d90: Optional[float] = None
    """Movement in Rank over the last 90 days using a score from -10 to 10"""

    rank_org: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Organizations"""

    revenue_range: Optional[str] = None
    """Estimated revenue range for organization

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    school_method: Optional[str] = None
    """The type of School Method (e.g. On Campus, Online)

    - on_compus - On Campus
    - online - Online
    - online_and_on_campus - Online and On Campus
    """

    school_program: Optional[str] = None
    """The type of School Program (e.g. Bootcamp, Four Year University)

    - bootcamp - Bootcamp
    - community_college - Community College
    - four_year_university - Four Year University
    - graduate_university - Graduate University
    - high_school - High School
    - trade_school - Trade School
    - two_year_university - Two Year University
    """

    school_type: Optional[str] = None
    """The type of school

    - for_profit_private - Private
    - non_profit_private - Private (Non-Profit)
    - public - Public
    """

    short_description: Optional[str] = None
    """Text of Organization Description, Industries, and Industry Groups"""

    status: Optional[str] = None
    """Status of Organization e.g. Operating, Closed, Acquired, IPO

    - closed - Closed
    - ipo - IPO
    - operating - Operating
    - was_acquired - Was Acquired
    """

    stock_exchange_symbol: Optional[str] = None
    """Stock exchange where the Organization is listed e.g. NYSE, NASDAQ

    - adx - ADX - Abu Dhabi Securities Exchange
    - afx - AFX - Afghanistan Stock Exchange
    - altx - ALTX - ALTX East Africa Exchange
    - amex - AMEX - American Stock Exchange
    - ams - AMS - Euronext Amsterdam
    - amx - AMX - Armenia Securities Exchange
    - asce - ASCE - Abuja Securities and Commodities Exchange
    - asx - ASX - Australian Securities Exchange
    - ath - ATH - Athens Stock Exchange
    - bcba - BCBA - Buenos Aires Stock Exchange
    - bdp - BDP - Budapest Stock Exchange
    - belex - BELEX - Belgrade Stock Exchange
    - ber - BER - Berliner Börse
    - bfb - BFB - Baku Stock Exchange
    - bit - BIT - Italian Stock Exchange
    - bkk - BKK - Thailand Stock Exchange
    - blse - BLSE - Banja Luka Stock Exchange
    - bme - BME - Madrid Stock Exchange
    - bmv - BMV - Mexican Stock Exchange
    - bom - BOM - Bombay Stock Exchange
    - brvm - BRVM - Regional Securities Exchange SA
    - bse - BSE - Bulgarian Stock Exchange
    - bse_lb - BSE - Beirut Stock Exchange
    - bsse - BSSE - Bratislava Stock Exchange
    - bsx - BSX - Bermuda Stock Exchange
    - bvb - BVB - Bucharest Stock Exchange
    - bvc - BVC - Colombian Stock Exchange
    - bvfb - BVFB - Belarusian Currency and Stock Exchange
    - bvm - BVM - Montevideo Stock Exchange
    - bvmf - B3 - Brazil Stock Exchange and OTC Market
    - bvmt - BVMT - Tunis Stock Exchange
    - bx - BX - Berne Stock Exchange
    - cas - CAS - Casablanca Stock Exchange
    - cise - CISE - Channel Islands Stock Exchange
    - cnsx - CNSX - Canadian National Stock Exchange
    - col - COL - Colombo Stock Exchange
    - cph - CPH - Copenhagen Stock Exchange
    - cse - CSE - Canadian Securities Exchange
    - cse_cy - CSE - Cyprus Stock Exchange
    - csx - CSX - Cambodia Securities Exchange
    - cve - TSX-V - Toronto TSX Venture Exchange
    - dfm - DFM - Dubai Financial Market
    - dse - DSE - Dhaka Stock Exchange
    - dsx - DSX - Douala Stock Exchange
    - dus - DUS - Börse Düsseldorf
    - ebr - EBR - Euronext Brussels
    - egx - EGX - Egypt Stock Exchange
    - eli - ELI - Euronext Lisbon
    - epa - EPA - Euronext Paris
    - etr - ETR - Deutsche Börse XETRA
    - eurex - EUREX - Eurex Exchange
    - fra - FRA - Frankfurt Stock Exchange
    - fwb - FWB - Börse Frankfurt Stock Exchange
    - gha - GHA - Ghana Stock Exchange
    - gsx - GSX - Georgian Stock Exchange
    - gsx_gi - GSX - Gibraltar Stock Exchange
    - hel - HEL - Helsinki Stock Exchange
    - hkg - HKG - Hong Kong Stock Exchange
    - hnx - HNX - Hanoi Stock Exchange
    - hose - HOSE - Ho Chi Minh Stock Exchange
    - ice - ICE - Iceland Stock Exchange
    - idx - IDX - Indonesia Stock Exchange
    - iex - IEX - Investors Exchange
    - ifb - IFB - Iran Fara Bourse
    - ime - IME - Iran Mercantile Exchange
    - irenex - IRENEX - Iran Energy Exchange
    - ise - ISE - Irish Stock Exchange
    - ist - IST - Istanbul Stock Exchange
    - isx - ISX - Iraq Stock Exchange
    - jp - JP - Japan Exchange
    - jsc - JSC - Belarusian Currency and Stock Exchange
    - jse - JSE - Johannesburg Stock Exchange
    - jse_jam - JSE - Jamaica Stock Exchange
    - kase - KASE - Kazakhstan Stock Exchange
    - klse - KLSE - Malaysia Stock Exchange
    - kosdaq - KOSDAQ - Korean Securities Dealers Automated Quotations
    - krx - KRX - Korea Stock Exchange
    - kse - KSE - Kuwait Stock Exchange
    - lje - LJE - Ljubljana Stock Exchange
    - lse - LSE - London Stock Exchange
    - lsm - LSM - Libyan Stock Market
    - lsx - LSX - Lao Securities Exchange
    - luse - LuSE - Lusaka Securities Exchange
    - luxse - LuxSE - Luxembourg Stock Exchange
    - mal - MAL - Malta Stock Exchange
    - mcx - MCX - Multi Commodity Exchange of India
    - meff - MEFF - Mercado Spanish Financial Futures Market
    - mnse - MNSE - Montenegro Stock Exchange
    - moex - MOEX - Moscow Exchange
    - mse - MSE - Metropolitan Stock Exchange
    - mse_md - MSE - Moldova Stock Exchange
    - mse_mk - MSE - Macedonian Stock Exchange
    - msei - MSEI - Metropolitan Stock Exchange of India
    - msm - MSM - Muscat Securities Market
    - mun - MUN - Börse München
    - nasdaq - NASDAQ
    - nbo - NSE - Nairobi Securities Exchange
    - neeq - NEEQ - National Equities Exchange and Quotations
    - nepse - NEPSE - Nepal Stock Exchange
    - nex - NEX - NEX Exchange
    - ngm - NGM - Nordic Growth Market Exchange
    - nig - NIG - Nigerian Stock Exchange
    - notc - NOTC - Norwegian OTC
    - npex - NPEX - NPEX Stock Exchange
    - nse - NSE - National Stock Exchange of India
    - nsx - NSX - National Stock Exchange of Australia
    - nyse - NYSE - New York Stock Exchange
    - nysearca - NYSEARCA - NYSE Arca
    - nysemkt - NYSEAMERICAN - NYSE American
    - nze - NZE - New Zealand Stock Exchange
    - ose - OSE - Oslo Stock Exchange
    - otcbb - OTCBB - FINRA OTC Bulletin Board
    - otcpink - OTC Pink
    - otcqb - OTCQB
    - otcqx - OTCQX
    - pdex - PDEx - Philippine Dealing Exchange
    - pex - PEX - Palestine Exchange
    - pfts - PFTS - PFTS Ukraine Stock Exchange
    - pomsox - POMSoX - Port Moresby Stock Exchange
    - prg - PRA - Prague Stock Exchange
    - pse - PSE - Philippine Stock Exchange
    - psx - PSX - Pakistan Stock Exchange
    - qse - QSE - Qatar Stock Exchange
    - rfb - RFB - Riga Stock Exchange
    - rse - RSE - Rwanda Stock Exchange
    - rsebl - RSEBL - Royal Securities Exchange of Bhutan
    - sase - SASE - Sarajevo Stock Exchange
    - sbx - SBX - BX Swiss
    - sehk - SEHK - The Stock Exchange of Hong Kong
    - sem - SEM - Stock Exchange of Mauritius
    - sgbv - SGBV - Algiers Stock Exchange
    - sgx - SGX - Singapore Stock Exchange
    - six - SIX - SIX Swiss Exchange
    - spbex - SPBEX - Saint Petersburg Stock Exchange
    - spse - SPSE - South Pacific Stock Exchange
    - sse - SSE - Shanghai Stock Exchange
    - ssx - SSX - Sydney Stock Exchange
    - sto - STO - Stockholm Stock Exchange
    - stu - STU - Börse Stuttgart
    - swx - SWX - SIX Swiss Exchange
    - szse - SZSE - Shenzhen Stock Exchange
    - tadawul - Tadawul - Saudi Stock Exchange
    - tal - TSE - Tallinn Stock Exchange
    - tfex - TFEX - Thailand Futures Exchange
    - tise - TISE - The International Stock Exchange
    - tlv - TLV - Tel Aviv Stock Exchange
    - tpe - TWSE - Taiwan Stock Exchange
    - tse_al - TSE - Tirana Stock Exchange
    - tse_ir - TSE - Tehran Stock Exchange
    - tsec - TWO - Taiwan OTC Exchange
    - tsx - TSX - Toronto Stock Exchange
    - ttse - TTSE - Trinidad and Tobago Stock Exchange
    - tyo - TYO - Tokyo Stock Exchange
    - use - USE - Uganda Securities Exchange
    - ux - UX - Ukrainian Exchange
    - vie - VIE - Vienna Stock Exchange
    - vmf - VMF - Faroese Securities Market
    - vse - VSE - Vancouver Stock Exchange
    - wse - WSE - Warsaw Stock Exchange
    - ysx - YSX - Yangon Stock Exchange
    - zamace - ZAMACE - Zambian Commodity Exchange
    - zse - ZSE - Zimbabwe Stock Exchange
    - zse_hr - ZSE - Zagreb Stock Exchange
    """

    stock_symbol: Optional[CardsFieldsStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsFieldsTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    valuation: Optional[CardsFieldsValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    valuation_date: Optional[date] = None
    """Date of latest post money valuation"""

    website: Optional[CardsFieldsWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class CardsFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFounderFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFounderLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFounderLocationGroupIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsFounderLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsFounderPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFounderTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFounderWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFounder(BaseModel):
    identifier: CardsFounderIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None
    """Alternate or previous names for the individual"""

    born_on: Optional[date] = None
    """The birthdate of the person"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Text from a Person's biography"""

    died_on: Optional[date] = None
    """The date when a person died"""

    entity_def_id: Optional[str] = None
    """- person - Person"""

    facebook: Optional[CardsFounderFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    first_name: Optional[str] = None
    """First name of a Person"""

    gender: Optional[str] = None
    """A Person's gender

    - agender - Agender
    - androgyne - Androgyne
    - androgynous - Androgynous
    - bigender - Bigender
    - female - Female
    - ftm - Female to Male (FTM)
    - gender_fluid - Gender Fluid
    - gender_nonconforming - Gender Nonconforming
    - gender_questioning - Gender Questioning
    - gender_variant - Gender Variant
    - genderqueer - Genderqueer
    - male - Male
    - mtf - Male to Female (MTF)
    - neutrois - Neutrois
    - non_binary - Non-Binary
    - not_provided - Prefer not to identify
    - other - Other
    - pangender - Pangender
    - transfeminine - Transfeminine
    - transgender_female - Transgender Female
    - transgender_male - Transgender Male
    - transgender_man - Transgender Man
    - transgender_person - Transgender Person
    - transgender_woman - Transgender Woman
    - transmasculine - Transmasculine
    - transsexual_female - Transsexual Female
    - transsexual_male - Transsexual Male
    - transsexual_man - Transsexual Man
    - transsexual_person - Transsexual Person
    - transsexual_woman - Transsexual Woman
    - two_spirit - Two-Spirit
    """

    image_id: Optional[str] = None
    """The profile image of the person on Crunchbase"""

    image_url: Optional[str] = None
    """The url of the profile image"""

    investor_stage: Optional[List[str]] = None
    """This describes the stage of investor this person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    investor_type: Optional[List[str]] = None
    """This describes the type of investor the person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    last_name: Optional[str] = None
    """Last name of a Person"""

    layout_id: Optional[str] = None
    """This is the auto-generated layout for the profile

    - investor - Investor Layout
    """

    linkedin: Optional[CardsFounderLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[CardsFounderLocationGroupIdentifier]] = None
    """Where the person is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[CardsFounderLocationIdentifier]] = None
    """Where the person is located (e.g. Europe, Menlo Park, China)"""

    middle_name: Optional[str] = None
    """Middle name of a Person"""

    name: Optional[str] = None
    """Full name of a Person"""

    num_articles: Optional[float] = None
    """Number of news articles that reference the Person"""

    num_current_advisor_jobs: Optional[float] = None
    """Total number of current Advisors and Board roles the person has"""

    num_current_jobs: Optional[float] = None
    """Total number of current Jobs the person has"""

    num_diversity_spotlight_investments: Optional[float] = None
    """Total number of diversity investments made by an investor"""

    num_event_appearances: Optional[float] = None
    """Total number of events the individual appeared in"""

    num_exits: Optional[float] = None
    """Total number of Exits"""

    num_exits_ipo: Optional[float] = None
    """Total number of Exits (IPO)"""

    num_founded_organizations: Optional[float] = None
    """Number of Organizations that the person founded"""

    num_investments: Optional[float] = None
    """Number of Investments the Individual has participated in"""

    num_jobs: Optional[float] = None

    num_lead_investments: Optional[float] = None
    """Number of Investments led by the Individual"""

    num_partner_investments: Optional[float] = None
    """Number of Investments the Individual has partnered in"""

    num_past_advisor_jobs: Optional[float] = None
    """Total number of past Board and Advisor roles the person has"""

    num_past_jobs: Optional[float] = None
    """Total number of past Jobs the person has"""

    num_portfolio_organizations: Optional[float] = None
    """Number of portfolio companies associated to the Person"""

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    primary_job_title: Optional[str] = None
    """The person's primary job title"""

    primary_organization: Optional[CardsFounderPrimaryOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_delta_d30: Optional[float] = None
    """Movement in Rank over the last 30 days using a score from -10 to 10"""

    rank_delta_d7: Optional[float] = None
    """Movement in Rank over the last 7 days using a score from -10 to 10"""

    rank_delta_d90: Optional[float] = None
    """Movement in Rank over the last 90 days using a score from -10 to 10"""

    rank_person: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active People"""

    short_description: Optional[str] = None
    """Text of Person Description, Industries, and Industry Groups"""

    twitter: Optional[CardsFounderTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[CardsFounderWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to a Person's website"""


class CardsFundingPredictionIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFundingPredictionExampleFundingRound(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFundingPredictionGrowthInsight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFundingPredictionKeyLeadershipHire(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFundingPredictionOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFundingPredictionPartnershipAnnouncement(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFundingPredictionProductLaunch(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFundingPredictionRunwaySpeculation(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFundingPrediction(BaseModel):
    identifier: CardsFundingPredictionIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None
    """Time of Creation"""

    entity_def_id: Optional[str] = None
    """Entity Def Type

    - funding_prediction - Funding Prediction
    """

    example_funding_round: Optional[CardsFundingPredictionExampleFundingRound] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this Funding Prediction was generated"""

    growth_insight: Optional[CardsFundingPredictionGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_leadership_hire: Optional[CardsFundingPredictionKeyLeadershipHire] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    organization: Optional[CardsFundingPredictionOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partnership_announcement: Optional[CardsFundingPredictionPartnershipAnnouncement] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    probability_score: Optional[float] = None
    """The predicted probability that this Organization will receive funding"""

    probability_score_timeseries: Optional[str] = None
    """
    JSON object showing the probabilities for when the funding round is expected to
    occur. 4 scores indicate the probability of the funding round occurring in 0-5
    months, 6-11 months, 12-24 months, and 24+ months relative to the generated_on
    date.
    """

    product_launch: Optional[CardsFundingPredictionProductLaunch] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    runway_speculation: Optional[CardsFundingPredictionRunwaySpeculation] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    unicorn_status: Optional[str] = None
    """Achieved unicorn status in the last 12 months

    - c100_evidence_absent - Has Not Recently Achieved Unicorn Status
    - c200_evidence_present - Has Recently Achieved Unicorn Status
    """

    updated_at: Optional[datetime] = None
    """Time of Update"""

    uuid: Optional[str] = None
    """UUID"""


class CardsGrowthInsightIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsGrowthInsightOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsGrowthInsight(BaseModel):
    identifier: CardsGrowthInsightIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    customers: Optional[str] = None
    """Fluctuations in the number of customers or users

    - c100_worsening - Customer Decline
    - c200_improving - Customer Growth
    """

    description: Optional[str] = None
    """A concise text statement highlighting the company's growth trajectory"""

    engagement: Optional[str] = None
    """
    Changes in product engagement levels, including increases or decreases in
    website traffic, app downloads, and user activity

    - c100_worsening - Product Usage Decline
    - c200_improving - Product Usage Growth
    """

    entity_def_id: Optional[str] = None
    """Growth Insight

    - growth_insight - Growth Insight
    """

    finance: Optional[str] = None
    """
    Changes in key financial metrics including revenue, sales, earnings, profit
    margins, dividends, return on investment, stock performance, and commercial
    contracts

    - c100_worsening - Financial Decline
    - c200_improving - Financial Growth
    """

    funding_raised: Optional[str] = None
    """
    Activities related to financial investments, including receiving funding or
    making strategic investments into other organizations

    - c100_worsening - Has Not Recently Raised Funding
    - c200_improving - Recently Raised Funding
    """

    generated_on: Optional[date] = None
    """Date on which this insight was generated"""

    growth_confidence: Optional[str] = None
    """Assessment of the reliability and accuracy of the provided data

    - c100_unknown - Unknown
    - c200_low - Low
    - c300_medium - Medium
    - c400_high - High
    """

    growth_direction: Optional[str] = None
    """Direction of the company's growth trajectory

    - c100_uncertain - Uncertain
    - c200_declining - Not Growing
    - c300_stable - Stable
    - c400_growing - Growing
    """

    headcount: Optional[str] = None
    """
    Variations in employee numbers, including hiring sprees, layoffs, workforce
    expansions, and reductions

    - c100_worsening - Headcount Reduction
    - c200_improving - Headcount Growth
    """

    market_share: Optional[str] = None
    """
    Changes in the company’s market share, including growth through new market
    entries and decline due to market exits

    - c100_worsening - Market Share Decline
    - c200_improving - Market Share Expansion
    """

    mergers_acquisitions: Optional[str] = None
    """Business consolidations involving mergers, acquisitions, or divestitures

    - c100_worsening - No Merger or Acquisition
    - c200_improving - Merger or Acquisition
    """

    operations: Optional[str] = None
    """
    Modifications in operational footprints, including acquisitions or reductions of
    facilities, and regional expansions or contractions

    - c100_worsening - Operations Contraction
    - c200_improving - Operations Expansion
    """

    organization: Optional[CardsGrowthInsightOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    outbound_investment: Optional[str] = None
    """Records the company's financial investments into external entities or projects

    - c100_worsening - No Strategic Investment
    - c200_improving - Strategic Investment
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsHeadquartersAddressIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsHeadquartersAddressHeadquarteredOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsHeadquartersAddressLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsHeadquartersAddressOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsHeadquartersAddress(BaseModel):
    identifier: CardsHeadquartersAddressIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    country_code: Optional[str] = None
    """Country Code"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- address - Address"""

    headquartered_organization_identifier: Optional[CardsHeadquartersAddressHeadquarteredOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    location_identifiers: Optional[List[CardsHeadquartersAddressLocationIdentifier]] = None
    """What city the address is located in (e.g. San Francisco, London, Kiev)."""

    name: Optional[str] = None
    """Descriptive name of the Address (e.g. Headquarters, London Office)"""

    opening_date: Optional[date] = None
    """Date this location opened"""

    opening_description: Optional[str] = None
    """Summary of context regarding opening of this address"""

    organization: Optional[CardsHeadquartersAddressOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    postal_code: Optional[str] = None
    """The postal code of the address"""

    region_code: Optional[str] = None
    """Region Code"""

    street_1: Optional[str] = None
    """The street address of the location"""

    street_2: Optional[str] = None
    """The street address of the location"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsInvestorInsightIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorInsightCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorInsightDiversityInvestment(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorInsightLocation(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsInvestorInsightMedianInvestmentSize(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsInvestorInsightOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorInsight(BaseModel):
    identifier: CardsInvestorInsightIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    associated_investments_since: Optional[date] = None
    """Associated investments since"""

    categories: Optional[List[CardsInvestorInsightCategory]] = None
    """Investment categories"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """A concise text statement highlighting the investor insight"""

    diversity_investments: Optional[List[CardsInvestorInsightDiversityInvestment]] = None
    """Diversity investments"""

    entity_def_id: Optional[str] = None
    """Investor Insight

    - investor_insight - Investor Insight
    """

    exit_success_rate: Optional[float] = None
    """Exit success rate"""

    generated_on: Optional[date] = None
    """Date on which this insight was generated"""

    investment_types: Optional[List[str]] = None
    """Investment types"""

    lead_investor_rate: Optional[float] = None
    """Lead investor rate"""

    locations: Optional[List[CardsInvestorInsightLocation]] = None
    """Investment locations"""

    median_investment_size: Optional[CardsInvestorInsightMedianInvestmentSize] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    organization: Optional[CardsInvestorInsightOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    stages: Optional[List[str]] = None
    """Investment stages"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsInvestorDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsInvestorDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsInvestorExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsInvestorFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsInvestorFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsInvestorInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorLastEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsInvestorLastFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsInvestorLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorLocationGroupIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsInvestorLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsInvestorPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsInvestorWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsInvestor(BaseModel):
    identifier: CardsInvestorIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None

    born_on: Optional[date] = None

    categories: Optional[List[CardsInvestorCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsInvestorCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsInvestorClosedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    company_type: Optional[str] = None
    """Whether an Organization is for profit or non-profit

    - for_profit - For Profit
    - non_profit - Non-profit
    """

    contact_email: Optional[str] = None
    """General contact email for the organization or person"""

    created_at: Optional[datetime] = None

    delisted_on: Optional[CardsInvestorDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    description: Optional[str] = None
    """Organization or Person Description, Industries, Industry Groups"""

    died_on: Optional[date] = None

    diversity_spotlights: Optional[List[CardsInvestorDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    entity_def_id: Optional[str] = None
    """
    - organization - Organization
    - person - Person
    """

    equity_funding_total: Optional[CardsInvestorEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsInvestorExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsInvestorFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    first_name: Optional[str] = None
    """First name of a Person"""

    founded_on: Optional[CardsInvestorFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsInvestorFounderIdentifier]] = None
    """Founders of the organization"""

    funding_stage: Optional[str] = None
    """This field describes an organization's most recent funding status (e.g.

    Early Stage Venture, Late Stage Venture, M&A)

    - early_stage_venture - Early Stage Venture
    - ipo - IPO
    - late_stage_venture - Late Stage Venture
    - m_and_a - M&A
    - private_equity - Private Equity
    - seed - Seed
    """

    funding_total: Optional[CardsInvestorFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    gender: Optional[str] = None
    """A Person's gender

    - agender - Agender
    - androgyne - Androgyne
    - androgynous - Androgynous
    - bigender - Bigender
    - female - Female
    - ftm - Female to Male (FTM)
    - gender_fluid - Gender Fluid
    - gender_nonconforming - Gender Nonconforming
    - gender_questioning - Gender Questioning
    - gender_variant - Gender Variant
    - genderqueer - Genderqueer
    - male - Male
    - mtf - Male to Female (MTF)
    - neutrois - Neutrois
    - non_binary - Non-Binary
    - not_provided - Prefer not to identify
    - other - Other
    - pangender - Pangender
    - transfeminine - Transfeminine
    - transgender_female - Transgender Female
    - transgender_male - Transgender Male
    - transgender_man - Transgender Man
    - transgender_person - Transgender Person
    - transgender_woman - Transgender Woman
    - transmasculine - Transmasculine
    - transsexual_female - Transsexual Female
    - transsexual_male - Transsexual Male
    - transsexual_man - Transsexual Man
    - transsexual_person - Transsexual Person
    - transsexual_woman - Transsexual Woman
    - two_spirit - Two-Spirit
    """

    hub_tags: Optional[List[str]] = None
    """Tags representing special attributes of organizations that are used in Hubs"""

    image_id: Optional[str] = None

    image_url: Optional[str] = None
    """The url of the profile image"""

    investor_identifiers: Optional[List[CardsInvestorInvestorIdentifier]] = None
    """
    The top 5 investors with investments in this company, ordered by Crunchbase Rank
    """

    investor_stage: Optional[List[str]] = None
    """This describes the stage of investor this organization or person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    investor_type: Optional[List[str]] = None
    """This describes the type of investor this organization or person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    ipo_status: Optional[str] = None
    """The current public status of the Organization

    - delisted - Delisted
    - private - Private
    - public - Public
    """

    last_equity_funding_total: Optional[CardsInvestorLastEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_equity_funding_type: Optional[str] = None
    """The most recent Funding Round excluding debt

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_funding_at: Optional[date] = None
    """Date of most recent Funding Round"""

    last_funding_total: Optional[CardsInvestorLastFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_funding_type: Optional[str] = None
    """Last funding round type (e.g. Series A, Seed, Private Equity)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_name: Optional[str] = None
    """Last name of a Person"""

    layout_id: Optional[str] = None

    linkedin: Optional[CardsInvestorLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[CardsInvestorLocationGroupIdentifier]] = None
    """Where the principal is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[CardsInvestorLocationIdentifier]] = None
    """Where the organization is headquartered"""

    name: Optional[str] = None

    num_alumni: Optional[float] = None
    """Total number of alumni"""

    num_articles: Optional[float] = None
    """Number of news articles that reference the Organization"""

    num_diversity_spotlight_investments: Optional[float] = None
    """Total number of diversity investments made by an investor"""

    num_employees_enum: Optional[str] = None
    """Total number of Employees

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_enrollments: Optional[str] = None
    """Total number of Enrollments

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_event_appearances: Optional[float] = None
    """Total number of events An Organization or Person appeared in"""

    num_exits: Optional[float] = None
    """Total number of Exits"""

    num_exits_ipo: Optional[float] = None
    """Total number of Exits (IPO)"""

    num_founded_organizations: Optional[float] = None
    """Number of Organizations that the Person founded"""

    num_founders: Optional[float] = None
    """Total number of Founders"""

    num_funding_rounds: Optional[float] = None
    """Total number of Funding Rounds"""

    num_funds: Optional[float] = None

    num_investments: Optional[float] = None
    """Total number of Investments made"""

    num_investors: Optional[float] = None
    """Total number of investment firms and individual investors"""

    num_jobs: Optional[float] = None

    num_lead_investments: Optional[float] = None
    """Number of Investments led by the Person"""

    num_lead_investors: Optional[float] = None
    """Total number of lead investment firms and individual investors"""

    num_partner_investments: Optional[float] = None
    """Number of Investments the Individual has partnered in"""

    num_portfolio_organizations: Optional[float] = None
    """Total number of portfolio organizations"""

    operating_status: Optional[str] = None
    """Operating Status of Organization e.g. Active, Closed

    - active - Active
    - closed - Closed
    """

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None

    phone_number: Optional[str] = None
    """General phone number of the organization or person"""

    primary_job_title: Optional[str] = None
    """The person's primary job title (e.g. CEO, Chief Architect, Product Manager)"""

    primary_organization: Optional[CardsInvestorPrimaryOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    program_application_deadline: Optional[date] = None
    """The deadline for applying to the Accelerator Program"""

    program_duration: Optional[float] = None
    """The duration of the Acceleration Program in number of weeks"""

    program_type: Optional[str] = None
    """The type of Accelerator Program (e.g. On-Site, Online)

    - on_site - On-Site
    - online - Online
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_delta_d30: Optional[float] = None
    """Movement in Rank over the last 30 days using a score from -10 to 10"""

    rank_delta_d7: Optional[float] = None
    """Movement in Rank over the last 7 days using a score from -10 to 10"""

    rank_delta_d90: Optional[float] = None
    """Movement in Rank over the last 90 days using a score from -10 to 10"""

    revenue_range: Optional[str] = None
    """Estimated Revenue Range for Organizations

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    school_method: Optional[str] = None
    """The type of School Method (e.g. On Campus, Online)

    - on_compus - On Campus
    - online - Online
    - online_and_on_campus - Online and On Campus
    """

    school_program: Optional[str] = None
    """The type of School Program (e.g. Bootcamp, Four Year University)

    - bootcamp - Bootcamp
    - community_college - Community College
    - four_year_university - Four Year University
    - graduate_university - Graduate University
    - high_school - High School
    - trade_school - Trade School
    - two_year_university - Two Year University
    """

    school_type: Optional[str] = None
    """The type of School (e.g. Public, Private)

    - for_profit_private - Private
    - non_profit_private - Private (Non-Profit)
    - public - Public
    """

    short_description: Optional[str] = None
    """Text of Organization or Person Description, Industries, and Industry Groups"""

    status: Optional[str] = None
    """Status of Organization e.g. Operating, Closed, Acquired, IPO

    - closed - Closed
    - ipo - IPO
    - operating - Operating
    - was_acquired - Was Acquired
    """

    stock_exchange_symbol: Optional[str] = None
    """Stock exchange where the Organization is listed e.g. NYSE, NASDAQ

    - adx - ADX - Abu Dhabi Securities Exchange
    - afx - AFX - Afghanistan Stock Exchange
    - altx - ALTX - ALTX East Africa Exchange
    - amex - AMEX - American Stock Exchange
    - ams - AMS - Euronext Amsterdam
    - amx - AMX - Armenia Securities Exchange
    - asce - ASCE - Abuja Securities and Commodities Exchange
    - asx - ASX - Australian Securities Exchange
    - ath - ATH - Athens Stock Exchange
    - bcba - BCBA - Buenos Aires Stock Exchange
    - bdp - BDP - Budapest Stock Exchange
    - belex - BELEX - Belgrade Stock Exchange
    - ber - BER - Berliner Börse
    - bfb - BFB - Baku Stock Exchange
    - bit - BIT - Italian Stock Exchange
    - bkk - BKK - Thailand Stock Exchange
    - blse - BLSE - Banja Luka Stock Exchange
    - bme - BME - Madrid Stock Exchange
    - bmv - BMV - Mexican Stock Exchange
    - bom - BOM - Bombay Stock Exchange
    - brvm - BRVM - Regional Securities Exchange SA
    - bse - BSE - Bulgarian Stock Exchange
    - bse_lb - BSE - Beirut Stock Exchange
    - bsse - BSSE - Bratislava Stock Exchange
    - bsx - BSX - Bermuda Stock Exchange
    - bvb - BVB - Bucharest Stock Exchange
    - bvc - BVC - Colombian Stock Exchange
    - bvfb - BVFB - Belarusian Currency and Stock Exchange
    - bvm - BVM - Montevideo Stock Exchange
    - bvmf - B3 - Brazil Stock Exchange and OTC Market
    - bvmt - BVMT - Tunis Stock Exchange
    - bx - BX - Berne Stock Exchange
    - cas - CAS - Casablanca Stock Exchange
    - cise - CISE - Channel Islands Stock Exchange
    - cnsx - CNSX - Canadian National Stock Exchange
    - col - COL - Colombo Stock Exchange
    - cph - CPH - Copenhagen Stock Exchange
    - cse - CSE - Canadian Securities Exchange
    - cse_cy - CSE - Cyprus Stock Exchange
    - csx - CSX - Cambodia Securities Exchange
    - cve - TSX-V - Toronto TSX Venture Exchange
    - dfm - DFM - Dubai Financial Market
    - dse - DSE - Dhaka Stock Exchange
    - dsx - DSX - Douala Stock Exchange
    - dus - DUS - Börse Düsseldorf
    - ebr - EBR - Euronext Brussels
    - egx - EGX - Egypt Stock Exchange
    - eli - ELI - Euronext Lisbon
    - epa - EPA - Euronext Paris
    - etr - ETR - Deutsche Börse XETRA
    - eurex - EUREX - Eurex Exchange
    - fra - FRA - Frankfurt Stock Exchange
    - fwb - FWB - Börse Frankfurt Stock Exchange
    - gha - GHA - Ghana Stock Exchange
    - gsx - GSX - Georgian Stock Exchange
    - gsx_gi - GSX - Gibraltar Stock Exchange
    - hel - HEL - Helsinki Stock Exchange
    - hkg - HKG - Hong Kong Stock Exchange
    - hnx - HNX - Hanoi Stock Exchange
    - hose - HOSE - Ho Chi Minh Stock Exchange
    - ice - ICE - Iceland Stock Exchange
    - idx - IDX - Indonesia Stock Exchange
    - iex - IEX - Investors Exchange
    - ifb - IFB - Iran Fara Bourse
    - ime - IME - Iran Mercantile Exchange
    - irenex - IRENEX - Iran Energy Exchange
    - ise - ISE - Irish Stock Exchange
    - ist - IST - Istanbul Stock Exchange
    - isx - ISX - Iraq Stock Exchange
    - jp - JP - Japan Exchange
    - jsc - JSC - Belarusian Currency and Stock Exchange
    - jse - JSE - Johannesburg Stock Exchange
    - jse_jam - JSE - Jamaica Stock Exchange
    - kase - KASE - Kazakhstan Stock Exchange
    - klse - KLSE - Malaysia Stock Exchange
    - kosdaq - KOSDAQ - Korean Securities Dealers Automated Quotations
    - krx - KRX - Korea Stock Exchange
    - kse - KSE - Kuwait Stock Exchange
    - lje - LJE - Ljubljana Stock Exchange
    - lse - LSE - London Stock Exchange
    - lsm - LSM - Libyan Stock Market
    - lsx - LSX - Lao Securities Exchange
    - luse - LuSE - Lusaka Securities Exchange
    - luxse - LuxSE - Luxembourg Stock Exchange
    - mal - MAL - Malta Stock Exchange
    - mcx - MCX - Multi Commodity Exchange of India
    - meff - MEFF - Mercado Spanish Financial Futures Market
    - mnse - MNSE - Montenegro Stock Exchange
    - moex - MOEX - Moscow Exchange
    - mse - MSE - Metropolitan Stock Exchange
    - mse_md - MSE - Moldova Stock Exchange
    - mse_mk - MSE - Macedonian Stock Exchange
    - msei - MSEI - Metropolitan Stock Exchange of India
    - msm - MSM - Muscat Securities Market
    - mun - MUN - Börse München
    - nasdaq - NASDAQ
    - nbo - NSE - Nairobi Securities Exchange
    - neeq - NEEQ - National Equities Exchange and Quotations
    - nepse - NEPSE - Nepal Stock Exchange
    - nex - NEX - NEX Exchange
    - ngm - NGM - Nordic Growth Market Exchange
    - nig - NIG - Nigerian Stock Exchange
    - notc - NOTC - Norwegian OTC
    - npex - NPEX - NPEX Stock Exchange
    - nse - NSE - National Stock Exchange of India
    - nsx - NSX - National Stock Exchange of Australia
    - nyse - NYSE - New York Stock Exchange
    - nysearca - NYSEARCA - NYSE Arca
    - nysemkt - NYSEAMERICAN - NYSE American
    - nze - NZE - New Zealand Stock Exchange
    - ose - OSE - Oslo Stock Exchange
    - otcbb - OTCBB - FINRA OTC Bulletin Board
    - otcpink - OTC Pink
    - otcqb - OTCQB
    - otcqx - OTCQX
    - pdex - PDEx - Philippine Dealing Exchange
    - pex - PEX - Palestine Exchange
    - pfts - PFTS - PFTS Ukraine Stock Exchange
    - pomsox - POMSoX - Port Moresby Stock Exchange
    - prg - PRA - Prague Stock Exchange
    - pse - PSE - Philippine Stock Exchange
    - psx - PSX - Pakistan Stock Exchange
    - qse - QSE - Qatar Stock Exchange
    - rfb - RFB - Riga Stock Exchange
    - rse - RSE - Rwanda Stock Exchange
    - rsebl - RSEBL - Royal Securities Exchange of Bhutan
    - sase - SASE - Sarajevo Stock Exchange
    - sbx - SBX - BX Swiss
    - sehk - SEHK - The Stock Exchange of Hong Kong
    - sem - SEM - Stock Exchange of Mauritius
    - sgbv - SGBV - Algiers Stock Exchange
    - sgx - SGX - Singapore Stock Exchange
    - six - SIX - SIX Swiss Exchange
    - spbex - SPBEX - Saint Petersburg Stock Exchange
    - spse - SPSE - South Pacific Stock Exchange
    - sse - SSE - Shanghai Stock Exchange
    - ssx - SSX - Sydney Stock Exchange
    - sto - STO - Stockholm Stock Exchange
    - stu - STU - Börse Stuttgart
    - swx - SWX - SIX Swiss Exchange
    - szse - SZSE - Shenzhen Stock Exchange
    - tadawul - Tadawul - Saudi Stock Exchange
    - tal - TSE - Tallinn Stock Exchange
    - tfex - TFEX - Thailand Futures Exchange
    - tise - TISE - The International Stock Exchange
    - tlv - TLV - Tel Aviv Stock Exchange
    - tpe - TWSE - Taiwan Stock Exchange
    - tse_al - TSE - Tirana Stock Exchange
    - tse_ir - TSE - Tehran Stock Exchange
    - tsec - TWO - Taiwan OTC Exchange
    - tsx - TSX - Toronto Stock Exchange
    - ttse - TTSE - Trinidad and Tobago Stock Exchange
    - tyo - TYO - Tokyo Stock Exchange
    - use - USE - Uganda Securities Exchange
    - ux - UX - Ukrainian Exchange
    - vie - VIE - Vienna Stock Exchange
    - vmf - VMF - Faroese Securities Market
    - vse - VSE - Vancouver Stock Exchange
    - wse - WSE - Warsaw Stock Exchange
    - ysx - YSX - Yangon Stock Exchange
    - zamace - ZAMACE - Zambian Commodity Exchange
    - zse - ZSE - Zimbabwe Stock Exchange
    - zse_hr - ZSE - Zagreb Stock Exchange
    """

    stock_symbol: Optional[CardsInvestorStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsInvestorTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[CardsInvestorWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class CardsIpoPredictionIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsIpoPredictionExampleFundingRound(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsIpoPredictionExampleIpo(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsIpoPredictionGrowthInsight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsIpoPredictionKeyLeadershipHire(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsIpoPredictionOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsIpoPrediction(BaseModel):
    identifier: CardsIpoPredictionIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None
    """Time of Creation"""

    entity_def_id: Optional[str] = None
    """Entity Def Type

    - ipo_prediction - IPO Prediction
    """

    example_funding_round: Optional[CardsIpoPredictionExampleFundingRound] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    example_ipo: Optional[CardsIpoPredictionExampleIpo] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this IPO Prediction was generated"""

    growth_insight: Optional[CardsIpoPredictionGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_leadership_hire: Optional[CardsIpoPredictionKeyLeadershipHire] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    media_sentiment: Optional[str] = None
    """
    A sudden increase in media coverage with positive sentiment in the last 12
    months

    - c100_evidence_absent - No Increased Positive Media Coverage
    - c200_evidence_present - Increased Positive Media Coverage
    """

    organization: Optional[CardsIpoPredictionOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    probability_score: Optional[float] = None
    """The predicted probability that this Organization will IPO"""

    probability_tier: Optional[str] = None
    """
    The predicted probability of an IPO for this organization is divided into
    distinct tiers that quantify the likelihood of this event.

    - p100_positive_high - Very Likely
    - p200_positive_low - Likely
    - p300_neutral - Unsure
    - p400_negative_low - Unlikely
    - p500_negative_high - Very Unlikely
    """

    unicorn_status: Optional[str] = None
    """Achieved unicorn status in the last 12 months

    - c100_evidence_absent - Has Not Recently Achieved Unicorn Status
    - c200_evidence_present - Has Recently Achieved Unicorn Status
    """

    updated_at: Optional[datetime] = None
    """Time of Update"""

    uuid: Optional[str] = None
    """UUID"""


class CardsIpoIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsIpoAmountRaised(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsIpoDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsIpoOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsIpoSharePrice(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsIpoValuation(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsIpo(BaseModel):
    identifier: CardsIpoIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    amount_raised: Optional[CardsIpoAmountRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    created_at: Optional[datetime] = None

    delisted_on: Optional[CardsIpoDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    entity_def_id: Optional[str] = None
    """- ipo - Ipo"""

    image_id: Optional[str] = None

    organization_identifier: Optional[CardsIpoOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_ipo: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active IPOs"""

    share_price: Optional[CardsIpoSharePrice] = None
    """A field containing decimal data that represents some amount of money"""

    shares_outstanding: Optional[float] = None
    """Number of shares that were outstanding at the time of IPO"""

    shares_sold: Optional[float] = None
    """Number of shares sold at the time of IPO"""

    short_description: Optional[str] = None

    stock_exchange_symbol: Optional[str] = None
    """Stock exchange where the Organization is listed (e.g. NYSE, NASDAQ)

    - adx - ADX - Abu Dhabi Securities Exchange
    - afx - AFX - Afghanistan Stock Exchange
    - altx - ALTX - ALTX East Africa Exchange
    - amex - AMEX - American Stock Exchange
    - ams - AMS - Euronext Amsterdam
    - amx - AMX - Armenia Securities Exchange
    - asce - ASCE - Abuja Securities and Commodities Exchange
    - asx - ASX - Australian Securities Exchange
    - ath - ATH - Athens Stock Exchange
    - bcba - BCBA - Buenos Aires Stock Exchange
    - bdp - BDP - Budapest Stock Exchange
    - belex - BELEX - Belgrade Stock Exchange
    - ber - BER - Berliner Börse
    - bfb - BFB - Baku Stock Exchange
    - bit - BIT - Italian Stock Exchange
    - bkk - BKK - Thailand Stock Exchange
    - blse - BLSE - Banja Luka Stock Exchange
    - bme - BME - Madrid Stock Exchange
    - bmv - BMV - Mexican Stock Exchange
    - bom - BOM - Bombay Stock Exchange
    - brvm - BRVM - Regional Securities Exchange SA
    - bse - BSE - Bulgarian Stock Exchange
    - bse_lb - BSE - Beirut Stock Exchange
    - bsse - BSSE - Bratislava Stock Exchange
    - bsx - BSX - Bermuda Stock Exchange
    - bvb - BVB - Bucharest Stock Exchange
    - bvc - BVC - Colombian Stock Exchange
    - bvfb - BVFB - Belarusian Currency and Stock Exchange
    - bvm - BVM - Montevideo Stock Exchange
    - bvmf - B3 - Brazil Stock Exchange and OTC Market
    - bvmt - BVMT - Tunis Stock Exchange
    - bx - BX - Berne Stock Exchange
    - cas - CAS - Casablanca Stock Exchange
    - cise - CISE - Channel Islands Stock Exchange
    - cnsx - CNSX - Canadian National Stock Exchange
    - col - COL - Colombo Stock Exchange
    - cph - CPH - Copenhagen Stock Exchange
    - cse - CSE - Canadian Securities Exchange
    - cse_cy - CSE - Cyprus Stock Exchange
    - csx - CSX - Cambodia Securities Exchange
    - cve - TSX-V - Toronto TSX Venture Exchange
    - dfm - DFM - Dubai Financial Market
    - dse - DSE - Dhaka Stock Exchange
    - dsx - DSX - Douala Stock Exchange
    - dus - DUS - Börse Düsseldorf
    - ebr - EBR - Euronext Brussels
    - egx - EGX - Egypt Stock Exchange
    - eli - ELI - Euronext Lisbon
    - epa - EPA - Euronext Paris
    - etr - ETR - Deutsche Börse XETRA
    - eurex - EUREX - Eurex Exchange
    - fra - FRA - Frankfurt Stock Exchange
    - fwb - FWB - Börse Frankfurt Stock Exchange
    - gha - GHA - Ghana Stock Exchange
    - gsx - GSX - Georgian Stock Exchange
    - gsx_gi - GSX - Gibraltar Stock Exchange
    - hel - HEL - Helsinki Stock Exchange
    - hkg - HKG - Hong Kong Stock Exchange
    - hnx - HNX - Hanoi Stock Exchange
    - hose - HOSE - Ho Chi Minh Stock Exchange
    - ice - ICE - Iceland Stock Exchange
    - idx - IDX - Indonesia Stock Exchange
    - iex - IEX - Investors Exchange
    - ifb - IFB - Iran Fara Bourse
    - ime - IME - Iran Mercantile Exchange
    - irenex - IRENEX - Iran Energy Exchange
    - ise - ISE - Irish Stock Exchange
    - ist - IST - Istanbul Stock Exchange
    - isx - ISX - Iraq Stock Exchange
    - jp - JP - Japan Exchange
    - jsc - JSC - Belarusian Currency and Stock Exchange
    - jse - JSE - Johannesburg Stock Exchange
    - jse_jam - JSE - Jamaica Stock Exchange
    - kase - KASE - Kazakhstan Stock Exchange
    - klse - KLSE - Malaysia Stock Exchange
    - kosdaq - KOSDAQ - Korean Securities Dealers Automated Quotations
    - krx - KRX - Korea Stock Exchange
    - kse - KSE - Kuwait Stock Exchange
    - lje - LJE - Ljubljana Stock Exchange
    - lse - LSE - London Stock Exchange
    - lsm - LSM - Libyan Stock Market
    - lsx - LSX - Lao Securities Exchange
    - luse - LuSE - Lusaka Securities Exchange
    - luxse - LuxSE - Luxembourg Stock Exchange
    - mal - MAL - Malta Stock Exchange
    - mcx - MCX - Multi Commodity Exchange of India
    - meff - MEFF - Mercado Spanish Financial Futures Market
    - mnse - MNSE - Montenegro Stock Exchange
    - moex - MOEX - Moscow Exchange
    - mse - MSE - Metropolitan Stock Exchange
    - mse_md - MSE - Moldova Stock Exchange
    - mse_mk - MSE - Macedonian Stock Exchange
    - msei - MSEI - Metropolitan Stock Exchange of India
    - msm - MSM - Muscat Securities Market
    - mun - MUN - Börse München
    - nasdaq - NASDAQ
    - nbo - NSE - Nairobi Securities Exchange
    - neeq - NEEQ - National Equities Exchange and Quotations
    - nepse - NEPSE - Nepal Stock Exchange
    - nex - NEX - NEX Exchange
    - ngm - NGM - Nordic Growth Market Exchange
    - nig - NIG - Nigerian Stock Exchange
    - notc - NOTC - Norwegian OTC
    - npex - NPEX - NPEX Stock Exchange
    - nse - NSE - National Stock Exchange of India
    - nsx - NSX - National Stock Exchange of Australia
    - nyse - NYSE - New York Stock Exchange
    - nysearca - NYSEARCA - NYSE Arca
    - nysemkt - NYSEAMERICAN - NYSE American
    - nze - NZE - New Zealand Stock Exchange
    - ose - OSE - Oslo Stock Exchange
    - otcbb - OTCBB - FINRA OTC Bulletin Board
    - otcpink - OTC Pink
    - otcqb - OTCQB
    - otcqx - OTCQX
    - pdex - PDEx - Philippine Dealing Exchange
    - pex - PEX - Palestine Exchange
    - pfts - PFTS - PFTS Ukraine Stock Exchange
    - pomsox - POMSoX - Port Moresby Stock Exchange
    - prg - PRA - Prague Stock Exchange
    - pse - PSE - Philippine Stock Exchange
    - psx - PSX - Pakistan Stock Exchange
    - qse - QSE - Qatar Stock Exchange
    - rfb - RFB - Riga Stock Exchange
    - rse - RSE - Rwanda Stock Exchange
    - rsebl - RSEBL - Royal Securities Exchange of Bhutan
    - sase - SASE - Sarajevo Stock Exchange
    - sbx - SBX - BX Swiss
    - sehk - SEHK - The Stock Exchange of Hong Kong
    - sem - SEM - Stock Exchange of Mauritius
    - sgbv - SGBV - Algiers Stock Exchange
    - sgx - SGX - Singapore Stock Exchange
    - six - SIX - SIX Swiss Exchange
    - spbex - SPBEX - Saint Petersburg Stock Exchange
    - spse - SPSE - South Pacific Stock Exchange
    - sse - SSE - Shanghai Stock Exchange
    - ssx - SSX - Sydney Stock Exchange
    - sto - STO - Stockholm Stock Exchange
    - stu - STU - Börse Stuttgart
    - swx - SWX - SIX Swiss Exchange
    - szse - SZSE - Shenzhen Stock Exchange
    - tadawul - Tadawul - Saudi Stock Exchange
    - tal - TSE - Tallinn Stock Exchange
    - tfex - TFEX - Thailand Futures Exchange
    - tise - TISE - The International Stock Exchange
    - tlv - TLV - Tel Aviv Stock Exchange
    - tpe - TWSE - Taiwan Stock Exchange
    - tse_al - TSE - Tirana Stock Exchange
    - tse_ir - TSE - Tehran Stock Exchange
    - tsec - TWO - Taiwan OTC Exchange
    - tsx - TSX - Toronto Stock Exchange
    - ttse - TTSE - Trinidad and Tobago Stock Exchange
    - tyo - TYO - Tokyo Stock Exchange
    - use - USE - Uganda Securities Exchange
    - ux - UX - Ukrainian Exchange
    - vie - VIE - Vienna Stock Exchange
    - vmf - VMF - Faroese Securities Market
    - vse - VSE - Vancouver Stock Exchange
    - wse - WSE - Warsaw Stock Exchange
    - ysx - YSX - Yangon Stock Exchange
    - zamace - ZAMACE - Zambian Commodity Exchange
    - zse - ZSE - Zimbabwe Stock Exchange
    - zse_hr - ZSE - Zagreb Stock Exchange
    """

    stock_full_symbol: Optional[str] = None

    stock_symbol: Optional[str] = None
    """Stock ticker symbol (e.g. AAPL, FB, TWTR)"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    valuation: Optional[CardsIpoValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    went_public_on: Optional[date] = None
    """Date the Organization went public"""


class CardsJobIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsJobEndedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsJobOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsJobPersonIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsJobStartedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsJob(BaseModel):
    identifier: CardsJobIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    employee_featured_order: Optional[float] = None
    """These are the featured employees of an organization"""

    ended_on: Optional[CardsJobEndedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    entity_def_id: Optional[str] = None
    """- job - Job"""

    is_current: Optional[bool] = None
    """This indicates whether the Job is current or not"""

    job_type: Optional[str] = None
    """Select a job type that best represent your role at the organization

    - advisor - Advisor
    - board_member - Board Member
    - board_observer - Board Observer
    - employee - Non-Executive Employee
    - executive - Executive
    """

    name: Optional[str] = None

    organization_identifier: Optional[CardsJobOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    person_identifier: Optional[CardsJobPersonIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    short_description: Optional[str] = None
    """Text of Job Description"""

    started_on: Optional[CardsJobStartedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    title: Optional[str] = None
    """Title of a Person's Job"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsKeyEmployeeChangeIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsKeyEmployeeChangeOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsKeyEmployeeChange(BaseModel):
    identifier: CardsKeyEmployeeChangeIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None
    """Time of Creation"""

    description: Optional[str] = None
    """Description of the event"""

    entity_def_id: Optional[str] = None
    """Entity Def Type

    - key_employee_change - Leadership Hire
    """

    key_event_date: Optional[date] = None
    """Date when the news article was posted"""

    organization_identifier: Optional[CardsKeyEmployeeChangeOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Time of Update"""

    uuid: Optional[str] = None
    """UUID"""


class CardsLayoffIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsLayoffOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsLayoff(BaseModel):
    identifier: CardsLayoffIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None
    """Laoyff entity creation date"""

    entity_def_id: Optional[str] = None
    """Layoff Signal

    - layoff - layoff
    """

    key_event_date: Optional[date] = None
    """Date when the news article was posted"""

    organization_identifier: Optional[CardsLayoffOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Entity Updating date"""

    uuid: Optional[str] = None
    """Entity UUID"""


class CardsParentOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsParentOrganizationDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsParentOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParentOrganizationExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsParentOrganizationFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsParentOrganizationFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParentOrganizationFundsTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParentOrganizationInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationLastEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParentOrganizationLastFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParentOrganizationLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationLocationGroupIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsParentOrganizationLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsParentOrganizationOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganizationValuation(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParentOrganizationWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsParentOrganization(BaseModel):
    identifier: CardsParentOrganizationIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_identifier: Optional[CardsParentOrganizationAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None
    """Alternate or previous names for the organization"""

    categories: Optional[List[CardsParentOrganizationCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsParentOrganizationCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsParentOrganizationClosedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    company_type: Optional[str] = None
    """Whether an Organization is for profit or non-profit

    - for_profit - For Profit
    - non_profit - Non-profit
    """

    contact_email: Optional[str] = None
    """General contact email for the organization"""

    created_at: Optional[datetime] = None

    delisted_on: Optional[CardsParentOrganizationDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    demo_days: Optional[bool] = None
    """Whether an accelerator hosts any demo days"""

    description: Optional[str] = None
    """Organization Description, Industries, Industry Groups"""

    diversity_spotlights: Optional[List[CardsParentOrganizationDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    entity_def_id: Optional[str] = None
    """- organization - Organization"""

    equity_funding_total: Optional[CardsParentOrganizationEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsParentOrganizationExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsParentOrganizationFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    founded_on: Optional[CardsParentOrganizationFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsParentOrganizationFounderIdentifier]] = None
    """Founders of the organization"""

    funding_stage: Optional[str] = None
    """This field describes an organization's most recent funding status (e.g.

    Early Stage Venture, Late Stage Venture, M&A)

    - early_stage_venture - Early Stage Venture
    - ipo - IPO
    - late_stage_venture - Late Stage Venture
    - m_and_a - M&A
    - private_equity - Private Equity
    - seed - Seed
    """

    funding_total: Optional[CardsParentOrganizationFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funds_total: Optional[CardsParentOrganizationFundsTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    growth_insight_confidence: Optional[str] = None
    """Confidence level associated with this company's growth status

    - c100_unknown - Unknown
    - c200_low - Low
    - c300_medium - Medium
    - c400_high - High
    """

    growth_insight_direction: Optional[str] = None
    """
    - c100_uncertain - Uncertain
    - c200_declining - Not Growing
    - c300_stable - Stable
    - c400_growing - Growing
    """

    hub_tags: Optional[List[str]] = None
    """
    Tags are labels assigned to organizations, which identify their belonging to a
    group with that shared label
    """

    image_id: Optional[str] = None
    """The profile image of the organization on Crunchbase"""

    image_url: Optional[str] = None
    """The url of the profile image"""

    investor_identifiers: Optional[List[CardsParentOrganizationInvestorIdentifier]] = None
    """
    The top 5 investors with investments in this company, ordered by Crunchbase Rank
    """

    investor_stage: Optional[List[str]] = None
    """This describes the stage of investments made by this organization (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    investor_type: Optional[List[str]] = None
    """This describes the type of investor this organization is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    ipo_status: Optional[str] = None
    """The current public status of the Organization

    - delisted - Delisted
    - private - Private
    - public - Public
    """

    last_equity_funding_total: Optional[CardsParentOrganizationLastEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_equity_funding_type: Optional[str] = None
    """The most recent Funding Round excluding debt

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_funding_at: Optional[date] = None
    """Date of most recent Funding Round"""

    last_funding_total: Optional[CardsParentOrganizationLastFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_funding_type: Optional[str] = None
    """Last funding round type (e.g. Seed, Series A, Private Equity)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_key_employee_change_date: Optional[date] = None
    """See companies that have hired executives (VP and above) in a certain date range"""

    last_layoff_date: Optional[date] = None
    """Date of last layoff event"""

    layout_id: Optional[str] = None
    """This is the auto-generated layout for the profile

    - investor - Investor Layout
    - school - School Layout
    """

    legal_name: Optional[str] = None
    """The legal name of the organization"""

    linkedin: Optional[CardsParentOrganizationLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    listed_stock_symbol: Optional[str] = None
    """Stock ticker symbol (e.g. AAPL, FB, TWTR)"""

    location_group_identifiers: Optional[List[CardsParentOrganizationLocationGroupIdentifier]] = None
    """Where the organization is headquartered (e.g.

    San Francisco Bay Area, Silicon Valley)
    """

    location_identifiers: Optional[List[CardsParentOrganizationLocationIdentifier]] = None
    """Where the organization is headquartered"""

    name: Optional[str] = None

    num_acquisitions: Optional[float] = None
    """Total number of Acquisitions"""

    num_alumni: Optional[float] = None
    """Total number of alumni"""

    num_articles: Optional[float] = None
    """Number of news articles that reference the Organization"""

    num_current_advisor_positions: Optional[float] = None
    """
    Total number of board member and advisor profiles an organization has on
    Crunchbase
    """

    num_current_positions: Optional[float] = None
    """Total number of employee profiles an organization has on Crunchbase"""

    num_diversity_spotlight_investments: Optional[float] = None
    """Total number of diversity investments made by an investor"""

    num_employees_enum: Optional[str] = None
    """Total number of employees

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_enrollments: Optional[str] = None
    """Total number of Enrollments

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_event_appearances: Optional[float] = None
    """Total number of events an Organization appeared in"""

    num_exits: Optional[float] = None
    """Total number of Exits"""

    num_exits_ipo: Optional[float] = None
    """Total number of Exits (IPO)"""

    num_founder_alumni: Optional[float] = None
    """Total number of Alumni that are Founders"""

    num_founders: Optional[float] = None
    """Total number of Founders"""

    num_funding_rounds: Optional[float] = None
    """Total number of Funding Rounds"""

    num_funds: Optional[float] = None
    """Total number of Funds raised"""

    num_investments: Optional[float] = None
    """Total number of Investments made"""

    num_investors: Optional[float] = None
    """Total number of investment firms and individual investors"""

    num_lead_investments: Optional[float] = None
    """Total number of Lead Investments made"""

    num_lead_investors: Optional[float] = None
    """Total number of lead investment firms and individual investors"""

    num_past_positions: Optional[float] = None
    """Total number of past employee profiles of an organization"""

    num_portfolio_organizations: Optional[float] = None
    """Total number of portfolio organizations"""

    num_sub_organizations: Optional[float] = None
    """Total number of sub-organizations that belongs to a parent Organization"""

    operating_status: Optional[str] = None
    """Operating Status of Organization e.g. Active, Closed

    - active - Active
    - closed - Closed
    """

    owner_identifier: Optional[CardsParentOrganizationOwnerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    phone_number: Optional[str] = None
    """Organization's general phone number"""

    program_application_deadline: Optional[date] = None
    """The deadline for applying to the Accelerator Program"""

    program_duration: Optional[float] = None
    """The duration of the Acceleration Program in number of weeks"""

    program_type: Optional[str] = None
    """The type of Accelerator Program (e.g. On-Site, Online)

    - on_site - On-Site
    - online - Online
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_delta_d30: Optional[float] = None
    """Movement in Rank over the last 30 days using a score from -10 to 10"""

    rank_delta_d7: Optional[float] = None
    """Movement in Rank over the last 7 days using a score from -10 to 10"""

    rank_delta_d90: Optional[float] = None
    """Movement in Rank over the last 90 days using a score from -10 to 10"""

    rank_org: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Organizations"""

    revenue_range: Optional[str] = None
    """Estimated revenue range for organization

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    school_method: Optional[str] = None
    """The type of School Method (e.g. On Campus, Online)

    - on_compus - On Campus
    - online - Online
    - online_and_on_campus - Online and On Campus
    """

    school_program: Optional[str] = None
    """The type of School Program (e.g. Bootcamp, Four Year University)

    - bootcamp - Bootcamp
    - community_college - Community College
    - four_year_university - Four Year University
    - graduate_university - Graduate University
    - high_school - High School
    - trade_school - Trade School
    - two_year_university - Two Year University
    """

    school_type: Optional[str] = None
    """The type of school

    - for_profit_private - Private
    - non_profit_private - Private (Non-Profit)
    - public - Public
    """

    short_description: Optional[str] = None
    """Text of Organization Description, Industries, and Industry Groups"""

    status: Optional[str] = None
    """Status of Organization e.g. Operating, Closed, Acquired, IPO

    - closed - Closed
    - ipo - IPO
    - operating - Operating
    - was_acquired - Was Acquired
    """

    stock_exchange_symbol: Optional[str] = None
    """Stock exchange where the Organization is listed e.g. NYSE, NASDAQ

    - adx - ADX - Abu Dhabi Securities Exchange
    - afx - AFX - Afghanistan Stock Exchange
    - altx - ALTX - ALTX East Africa Exchange
    - amex - AMEX - American Stock Exchange
    - ams - AMS - Euronext Amsterdam
    - amx - AMX - Armenia Securities Exchange
    - asce - ASCE - Abuja Securities and Commodities Exchange
    - asx - ASX - Australian Securities Exchange
    - ath - ATH - Athens Stock Exchange
    - bcba - BCBA - Buenos Aires Stock Exchange
    - bdp - BDP - Budapest Stock Exchange
    - belex - BELEX - Belgrade Stock Exchange
    - ber - BER - Berliner Börse
    - bfb - BFB - Baku Stock Exchange
    - bit - BIT - Italian Stock Exchange
    - bkk - BKK - Thailand Stock Exchange
    - blse - BLSE - Banja Luka Stock Exchange
    - bme - BME - Madrid Stock Exchange
    - bmv - BMV - Mexican Stock Exchange
    - bom - BOM - Bombay Stock Exchange
    - brvm - BRVM - Regional Securities Exchange SA
    - bse - BSE - Bulgarian Stock Exchange
    - bse_lb - BSE - Beirut Stock Exchange
    - bsse - BSSE - Bratislava Stock Exchange
    - bsx - BSX - Bermuda Stock Exchange
    - bvb - BVB - Bucharest Stock Exchange
    - bvc - BVC - Colombian Stock Exchange
    - bvfb - BVFB - Belarusian Currency and Stock Exchange
    - bvm - BVM - Montevideo Stock Exchange
    - bvmf - B3 - Brazil Stock Exchange and OTC Market
    - bvmt - BVMT - Tunis Stock Exchange
    - bx - BX - Berne Stock Exchange
    - cas - CAS - Casablanca Stock Exchange
    - cise - CISE - Channel Islands Stock Exchange
    - cnsx - CNSX - Canadian National Stock Exchange
    - col - COL - Colombo Stock Exchange
    - cph - CPH - Copenhagen Stock Exchange
    - cse - CSE - Canadian Securities Exchange
    - cse_cy - CSE - Cyprus Stock Exchange
    - csx - CSX - Cambodia Securities Exchange
    - cve - TSX-V - Toronto TSX Venture Exchange
    - dfm - DFM - Dubai Financial Market
    - dse - DSE - Dhaka Stock Exchange
    - dsx - DSX - Douala Stock Exchange
    - dus - DUS - Börse Düsseldorf
    - ebr - EBR - Euronext Brussels
    - egx - EGX - Egypt Stock Exchange
    - eli - ELI - Euronext Lisbon
    - epa - EPA - Euronext Paris
    - etr - ETR - Deutsche Börse XETRA
    - eurex - EUREX - Eurex Exchange
    - fra - FRA - Frankfurt Stock Exchange
    - fwb - FWB - Börse Frankfurt Stock Exchange
    - gha - GHA - Ghana Stock Exchange
    - gsx - GSX - Georgian Stock Exchange
    - gsx_gi - GSX - Gibraltar Stock Exchange
    - hel - HEL - Helsinki Stock Exchange
    - hkg - HKG - Hong Kong Stock Exchange
    - hnx - HNX - Hanoi Stock Exchange
    - hose - HOSE - Ho Chi Minh Stock Exchange
    - ice - ICE - Iceland Stock Exchange
    - idx - IDX - Indonesia Stock Exchange
    - iex - IEX - Investors Exchange
    - ifb - IFB - Iran Fara Bourse
    - ime - IME - Iran Mercantile Exchange
    - irenex - IRENEX - Iran Energy Exchange
    - ise - ISE - Irish Stock Exchange
    - ist - IST - Istanbul Stock Exchange
    - isx - ISX - Iraq Stock Exchange
    - jp - JP - Japan Exchange
    - jsc - JSC - Belarusian Currency and Stock Exchange
    - jse - JSE - Johannesburg Stock Exchange
    - jse_jam - JSE - Jamaica Stock Exchange
    - kase - KASE - Kazakhstan Stock Exchange
    - klse - KLSE - Malaysia Stock Exchange
    - kosdaq - KOSDAQ - Korean Securities Dealers Automated Quotations
    - krx - KRX - Korea Stock Exchange
    - kse - KSE - Kuwait Stock Exchange
    - lje - LJE - Ljubljana Stock Exchange
    - lse - LSE - London Stock Exchange
    - lsm - LSM - Libyan Stock Market
    - lsx - LSX - Lao Securities Exchange
    - luse - LuSE - Lusaka Securities Exchange
    - luxse - LuxSE - Luxembourg Stock Exchange
    - mal - MAL - Malta Stock Exchange
    - mcx - MCX - Multi Commodity Exchange of India
    - meff - MEFF - Mercado Spanish Financial Futures Market
    - mnse - MNSE - Montenegro Stock Exchange
    - moex - MOEX - Moscow Exchange
    - mse - MSE - Metropolitan Stock Exchange
    - mse_md - MSE - Moldova Stock Exchange
    - mse_mk - MSE - Macedonian Stock Exchange
    - msei - MSEI - Metropolitan Stock Exchange of India
    - msm - MSM - Muscat Securities Market
    - mun - MUN - Börse München
    - nasdaq - NASDAQ
    - nbo - NSE - Nairobi Securities Exchange
    - neeq - NEEQ - National Equities Exchange and Quotations
    - nepse - NEPSE - Nepal Stock Exchange
    - nex - NEX - NEX Exchange
    - ngm - NGM - Nordic Growth Market Exchange
    - nig - NIG - Nigerian Stock Exchange
    - notc - NOTC - Norwegian OTC
    - npex - NPEX - NPEX Stock Exchange
    - nse - NSE - National Stock Exchange of India
    - nsx - NSX - National Stock Exchange of Australia
    - nyse - NYSE - New York Stock Exchange
    - nysearca - NYSEARCA - NYSE Arca
    - nysemkt - NYSEAMERICAN - NYSE American
    - nze - NZE - New Zealand Stock Exchange
    - ose - OSE - Oslo Stock Exchange
    - otcbb - OTCBB - FINRA OTC Bulletin Board
    - otcpink - OTC Pink
    - otcqb - OTCQB
    - otcqx - OTCQX
    - pdex - PDEx - Philippine Dealing Exchange
    - pex - PEX - Palestine Exchange
    - pfts - PFTS - PFTS Ukraine Stock Exchange
    - pomsox - POMSoX - Port Moresby Stock Exchange
    - prg - PRA - Prague Stock Exchange
    - pse - PSE - Philippine Stock Exchange
    - psx - PSX - Pakistan Stock Exchange
    - qse - QSE - Qatar Stock Exchange
    - rfb - RFB - Riga Stock Exchange
    - rse - RSE - Rwanda Stock Exchange
    - rsebl - RSEBL - Royal Securities Exchange of Bhutan
    - sase - SASE - Sarajevo Stock Exchange
    - sbx - SBX - BX Swiss
    - sehk - SEHK - The Stock Exchange of Hong Kong
    - sem - SEM - Stock Exchange of Mauritius
    - sgbv - SGBV - Algiers Stock Exchange
    - sgx - SGX - Singapore Stock Exchange
    - six - SIX - SIX Swiss Exchange
    - spbex - SPBEX - Saint Petersburg Stock Exchange
    - spse - SPSE - South Pacific Stock Exchange
    - sse - SSE - Shanghai Stock Exchange
    - ssx - SSX - Sydney Stock Exchange
    - sto - STO - Stockholm Stock Exchange
    - stu - STU - Börse Stuttgart
    - swx - SWX - SIX Swiss Exchange
    - szse - SZSE - Shenzhen Stock Exchange
    - tadawul - Tadawul - Saudi Stock Exchange
    - tal - TSE - Tallinn Stock Exchange
    - tfex - TFEX - Thailand Futures Exchange
    - tise - TISE - The International Stock Exchange
    - tlv - TLV - Tel Aviv Stock Exchange
    - tpe - TWSE - Taiwan Stock Exchange
    - tse_al - TSE - Tirana Stock Exchange
    - tse_ir - TSE - Tehran Stock Exchange
    - tsec - TWO - Taiwan OTC Exchange
    - tsx - TSX - Toronto Stock Exchange
    - ttse - TTSE - Trinidad and Tobago Stock Exchange
    - tyo - TYO - Tokyo Stock Exchange
    - use - USE - Uganda Securities Exchange
    - ux - UX - Ukrainian Exchange
    - vie - VIE - Vienna Stock Exchange
    - vmf - VMF - Faroese Securities Market
    - vse - VSE - Vancouver Stock Exchange
    - wse - WSE - Warsaw Stock Exchange
    - ysx - YSX - Yangon Stock Exchange
    - zamace - ZAMACE - Zambian Commodity Exchange
    - zse - ZSE - Zimbabwe Stock Exchange
    - zse_hr - ZSE - Zagreb Stock Exchange
    """

    stock_symbol: Optional[CardsParentOrganizationStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsParentOrganizationTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    valuation: Optional[CardsParentOrganizationValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    valuation_date: Optional[date] = None
    """Date of latest post money valuation"""

    website: Optional[CardsParentOrganizationWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class CardsParentOwnershipIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOwnershipOwneeIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOwnershipOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParentOwnership(BaseModel):
    identifier: CardsParentOwnershipIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- ownership - Ownership"""

    name: Optional[str] = None

    ownee_identifier: Optional[CardsParentOwnershipOwneeIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    owner_identifier: Optional[CardsParentOwnershipOwnerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    ownership_type: Optional[str] = None
    """
    This is the relationship defining how a sub-organization is related to a parent
    organization

    - affiliated_company - Affiliated Company
    - division - Division
    - investment_arm - Investment Arm
    - joint_venture - Joint Venture
    - subsidiary - Subsidiary
    """

    permalink: Optional[str] = None

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsParticipatedFundingRoundIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedFundingRoundClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsParticipatedFundingRoundFundedOrganizationCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedFundingRoundFundedOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedFundingRoundFundedOrganizationFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParticipatedFundingRoundFundedOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedFundingRoundFundedOrganizationLocation(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsParticipatedFundingRoundInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedFundingRoundLeadInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedFundingRoundMoneyRaised(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParticipatedFundingRoundPostMoneyValuation(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParticipatedFundingRoundPreMoneyValuation(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParticipatedFundingRoundTargetMoneyRaised(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParticipatedFundingRound(BaseModel):
    identifier: CardsParticipatedFundingRoundIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    announced_on: Optional[date] = None
    """Date that the Funding Round was publicly announced"""

    closed_on: Optional[CardsParticipatedFundingRoundClosedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- funding_round - Funding Round"""

    funded_organization_categories: Optional[List[CardsParticipatedFundingRoundFundedOrganizationCategory]] = None
    """Industries of the organization that got funded"""

    funded_organization_description: Optional[str] = None
    """Description of the organization that got funded"""

    funded_organization_diversity_spotlights: Optional[
        List[CardsParticipatedFundingRoundFundedOrganizationDiversitySpotlight]
    ] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    funded_organization_funding_stage: Optional[str] = None
    """Organization's most recent funding status

    - early_stage_venture - Early Stage Venture
    - ipo - IPO
    - late_stage_venture - Late Stage Venture
    - m_and_a - M&A
    - private_equity - Private Equity
    - seed - Seed
    """

    funded_organization_funding_total: Optional[CardsParticipatedFundingRoundFundedOrganizationFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funded_organization_identifier: Optional[CardsParticipatedFundingRoundFundedOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    funded_organization_location: Optional[List[CardsParticipatedFundingRoundFundedOrganizationLocation]] = None
    """Location of the organization that got funded"""

    funded_organization_revenue_range: Optional[str] = None
    """Revenue range of the organization that got funded

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    image_id: Optional[str] = None

    investment_stage: Optional[str] = None
    """The funding stage of a funding round

    - early_stage_venture - Early Stage Venture
    - late_stage_venture - Late Stage Venture
    - private_equity - Private Equity
    - seed - Seed
    """

    investment_type: Optional[str] = None
    """Type of Funding Round (e.g. Seed, Series A, Private Equity, Debt Financing)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Funding Round
    """

    investor_identifiers: Optional[List[CardsParticipatedFundingRoundInvestorIdentifier]] = None
    """Names of all investors who invested in the funding round"""

    is_equity: Optional[bool] = None
    """This indicates whether the Funding Round is financed only through equity."""

    lead_investor_identifiers: Optional[List[CardsParticipatedFundingRoundLeadInvestorIdentifier]] = None
    """Name of the investor who led the investment in the funding round"""

    money_raised: Optional[CardsParticipatedFundingRoundMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    name: Optional[str] = None

    num_investors: Optional[float] = None
    """Total number of Investors in a Funding Round"""

    num_partners: Optional[float] = None
    """Total number of Partner Investors in a Funding Round"""

    permalink: Optional[str] = None

    post_money_valuation: Optional[CardsParticipatedFundingRoundPostMoneyValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    pre_money_valuation: Optional[CardsParticipatedFundingRoundPreMoneyValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_funding_round: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Funding Rounds"""

    short_description: Optional[str] = None
    """Short description of the Funding Round"""

    target_money_raised: Optional[CardsParticipatedFundingRoundTargetMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsParticipatedFundIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedFundInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedFundMoneyRaised(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParticipatedFundOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedFundStartedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsParticipatedFund(BaseModel):
    identifier: CardsParticipatedFundIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    announced_on: Optional[date] = None
    """Date when a fund raised is announced"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- fund - Fund"""

    image_id: Optional[str] = None

    investor_identifiers: Optional[List[CardsParticipatedFundInvestorIdentifier]] = None

    money_raised: Optional[CardsParticipatedFundMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    name: Optional[str] = None
    """Name of the Fund"""

    num_investors: Optional[float] = None
    """Total number of investment firms and individual investors"""

    owner_identifier: Optional[CardsParticipatedFundOwnerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    short_description: Optional[str] = None
    """A short description of the Fund"""

    started_on: Optional[CardsParticipatedFundStartedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsParticipatedInvestmentIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedInvestmentFundingRoundIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedInvestmentFundingRoundMoneyRaised(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParticipatedInvestmentInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedInvestmentMoneyInvested(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsParticipatedInvestmentOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedInvestmentOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedInvestmentPartnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsParticipatedInvestment(BaseModel):
    identifier: CardsParticipatedInvestmentIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    announced_on: Optional[date] = None
    """Date when the Investment is announced"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- investment - Investment"""

    funding_round_identifier: Optional[CardsParticipatedInvestmentFundingRoundIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    funding_round_investment_type: Optional[str] = None
    """Type of Funding Round where the Investment is made (e.g.

    Seed, Series A, Private Equity, Debt Financing)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Funding Round
    """

    funding_round_money_raised: Optional[CardsParticipatedInvestmentFundingRoundMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    investor_identifier: Optional[CardsParticipatedInvestmentInvestorIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    investor_stage: Optional[List[str]] = None
    """This describes the stage of investor this organization or person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    investor_type: Optional[List[str]] = None
    """This describes the type of investor this organization or person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    is_lead_investor: Optional[bool] = None
    """This field indicates whether an investor led/organized the investment"""

    money_invested: Optional[CardsParticipatedInvestmentMoneyInvested] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    name: Optional[str] = None

    organization_diversity_spotlights: Optional[List[CardsParticipatedInvestmentOrganizationDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    organization_identifier: Optional[CardsParticipatedInvestmentOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partner_identifiers: Optional[List[CardsParticipatedInvestmentPartnerIdentifier]] = None
    """Name of the individual who led a funding round for his/her firm"""

    permalink: Optional[str] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsPressReferenceIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPressReferenceActivityEntity(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPressReferenceURL(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsPressReference(BaseModel):
    identifier: CardsPressReferenceIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    activity_entities: Optional[List[CardsPressReferenceActivityEntity]] = None
    """Entities mentioned in the press reference"""

    author: Optional[str] = None
    """The author of the press reference"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- press_reference - Press Reference"""

    facet_ids: Optional[List[str]] = None

    posted_on: Optional[date] = None
    """Date when the press reference is posted"""

    publisher: Optional[str] = None
    """The publisher of the press reference"""

    thumbnail_url: Optional[str] = None

    title: Optional[str] = None
    """The title of the press reference"""

    updated_at: Optional[datetime] = None

    url: Optional[CardsPressReferenceURL] = None
    """An object representing both the url and some labeling text for that url"""

    uuid: Optional[str] = None


class CardsProductIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsProductOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsProduct(BaseModel):
    identifier: CardsProductIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Product description"""

    entity_def_id: Optional[str] = None
    """Product

    - product - Product
    """

    local_rank: Optional[float] = None
    """Rank relative to this organization's other products"""

    organization: Optional[CardsProductOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsRaisedFundingRoundIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedFundingRoundClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsRaisedFundingRoundFundedOrganizationCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedFundingRoundFundedOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedFundingRoundFundedOrganizationFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsRaisedFundingRoundFundedOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedFundingRoundFundedOrganizationLocation(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class CardsRaisedFundingRoundInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedFundingRoundLeadInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedFundingRoundMoneyRaised(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsRaisedFundingRoundPostMoneyValuation(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsRaisedFundingRoundPreMoneyValuation(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsRaisedFundingRoundTargetMoneyRaised(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsRaisedFundingRound(BaseModel):
    identifier: CardsRaisedFundingRoundIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    announced_on: Optional[date] = None
    """Date that the Funding Round was publicly announced"""

    closed_on: Optional[CardsRaisedFundingRoundClosedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- funding_round - Funding Round"""

    funded_organization_categories: Optional[List[CardsRaisedFundingRoundFundedOrganizationCategory]] = None
    """Industries of the organization that got funded"""

    funded_organization_description: Optional[str] = None
    """Description of the organization that got funded"""

    funded_organization_diversity_spotlights: Optional[
        List[CardsRaisedFundingRoundFundedOrganizationDiversitySpotlight]
    ] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    funded_organization_funding_stage: Optional[str] = None
    """Organization's most recent funding status

    - early_stage_venture - Early Stage Venture
    - ipo - IPO
    - late_stage_venture - Late Stage Venture
    - m_and_a - M&A
    - private_equity - Private Equity
    - seed - Seed
    """

    funded_organization_funding_total: Optional[CardsRaisedFundingRoundFundedOrganizationFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funded_organization_identifier: Optional[CardsRaisedFundingRoundFundedOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    funded_organization_location: Optional[List[CardsRaisedFundingRoundFundedOrganizationLocation]] = None
    """Location of the organization that got funded"""

    funded_organization_revenue_range: Optional[str] = None
    """Revenue range of the organization that got funded

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    image_id: Optional[str] = None

    investment_stage: Optional[str] = None
    """The funding stage of a funding round

    - early_stage_venture - Early Stage Venture
    - late_stage_venture - Late Stage Venture
    - private_equity - Private Equity
    - seed - Seed
    """

    investment_type: Optional[str] = None
    """Type of Funding Round (e.g. Seed, Series A, Private Equity, Debt Financing)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Funding Round
    """

    investor_identifiers: Optional[List[CardsRaisedFundingRoundInvestorIdentifier]] = None
    """Names of all investors who invested in the funding round"""

    is_equity: Optional[bool] = None
    """This indicates whether the Funding Round is financed only through equity."""

    lead_investor_identifiers: Optional[List[CardsRaisedFundingRoundLeadInvestorIdentifier]] = None
    """Name of the investor who led the investment in the funding round"""

    money_raised: Optional[CardsRaisedFundingRoundMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    name: Optional[str] = None

    num_investors: Optional[float] = None
    """Total number of Investors in a Funding Round"""

    num_partners: Optional[float] = None
    """Total number of Partner Investors in a Funding Round"""

    permalink: Optional[str] = None

    post_money_valuation: Optional[CardsRaisedFundingRoundPostMoneyValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    pre_money_valuation: Optional[CardsRaisedFundingRoundPreMoneyValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_funding_round: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Funding Rounds"""

    short_description: Optional[str] = None
    """Short description of the Funding Round"""

    target_money_raised: Optional[CardsRaisedFundingRoundTargetMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsRaisedFundIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedFundInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedFundMoneyRaised(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsRaisedFundOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedFundStartedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsRaisedFund(BaseModel):
    identifier: CardsRaisedFundIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    announced_on: Optional[date] = None
    """Date when a fund raised is announced"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- fund - Fund"""

    image_id: Optional[str] = None

    investor_identifiers: Optional[List[CardsRaisedFundInvestorIdentifier]] = None

    money_raised: Optional[CardsRaisedFundMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    name: Optional[str] = None
    """Name of the Fund"""

    num_investors: Optional[float] = None
    """Total number of investment firms and individual investors"""

    owner_identifier: Optional[CardsRaisedFundOwnerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    short_description: Optional[str] = None
    """A short description of the Fund"""

    started_on: Optional[CardsRaisedFundStartedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsRaisedInvestmentIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedInvestmentFundingRoundIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedInvestmentFundingRoundMoneyRaised(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsRaisedInvestmentInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedInvestmentMoneyInvested(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class CardsRaisedInvestmentOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedInvestmentOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedInvestmentPartnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsRaisedInvestment(BaseModel):
    identifier: CardsRaisedInvestmentIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    announced_on: Optional[date] = None
    """Date when the Investment is announced"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- investment - Investment"""

    funding_round_identifier: Optional[CardsRaisedInvestmentFundingRoundIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    funding_round_investment_type: Optional[str] = None
    """Type of Funding Round where the Investment is made (e.g.

    Seed, Series A, Private Equity, Debt Financing)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Funding Round
    """

    funding_round_money_raised: Optional[CardsRaisedInvestmentFundingRoundMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    investor_identifier: Optional[CardsRaisedInvestmentInvestorIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    investor_stage: Optional[List[str]] = None
    """This describes the stage of investor this organization or person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    investor_type: Optional[List[str]] = None
    """This describes the type of investor this organization or person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    is_lead_investor: Optional[bool] = None
    """This field indicates whether an investor led/organized the investment"""

    money_invested: Optional[CardsRaisedInvestmentMoneyInvested] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    name: Optional[str] = None

    organization_diversity_spotlights: Optional[List[CardsRaisedInvestmentOrganizationDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    organization_identifier: Optional[CardsRaisedInvestmentOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partner_identifiers: Optional[List[CardsRaisedInvestmentPartnerIdentifier]] = None
    """Name of the individual who led a funding round for his/her firm"""

    permalink: Optional[str] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class Cards(BaseModel):
    acquiree_acquisitions: Optional[List[CardsAcquireeAcquisition]] = None

    acquirer_acquisitions: Optional[List[CardsAcquirerAcquisition]] = None

    acquisition_predictions: Optional[List[CardsAcquisitionPrediction]] = None

    child_organizations: Optional[List[CardsChildOrganization]] = None

    child_ownerships: Optional[List[CardsChildOwnership]] = None

    closure_predictions: Optional[List[CardsClosurePrediction]] = None

    event_appearances: Optional[List[CardsEventAppearance]] = None

    fields: Optional[CardsFields] = None

    founders: Optional[List[CardsFounder]] = None

    funding_predictions: Optional[List[CardsFundingPrediction]] = None

    growth_insights: Optional[List[CardsGrowthInsight]] = None

    headquarters_address: Optional[List[CardsHeadquartersAddress]] = None

    investor_insights: Optional[List[CardsInvestorInsight]] = None

    investors: Optional[List[CardsInvestor]] = None

    ipo_predictions: Optional[List[CardsIpoPrediction]] = None

    ipos: Optional[List[CardsIpo]] = None

    jobs: Optional[List[CardsJob]] = None

    key_employee_changes: Optional[List[CardsKeyEmployeeChange]] = None

    layoffs: Optional[List[CardsLayoff]] = None

    parent_organization: Optional[List[CardsParentOrganization]] = None

    parent_ownership: Optional[List[CardsParentOwnership]] = None

    participated_funding_rounds: Optional[List[CardsParticipatedFundingRound]] = None

    participated_funds: Optional[List[CardsParticipatedFund]] = None

    participated_investments: Optional[List[CardsParticipatedInvestment]] = None

    press_references: Optional[List[CardsPressReference]] = None

    products: Optional[List[CardsProduct]] = None

    raised_funding_rounds: Optional[List[CardsRaisedFundingRound]] = None

    raised_funds: Optional[List[CardsRaisedFund]] = None

    raised_investments: Optional[List[CardsRaisedInvestment]] = None


class PropertiesIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class PropertiesDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class PropertiesDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class PropertiesExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class PropertiesFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class PropertiesFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class PropertiesFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class PropertiesFundsTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class PropertiesInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesLastEquityFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class PropertiesLastFundingTotal(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class PropertiesLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class PropertiesLocationGroupIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class PropertiesLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class PropertiesOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class PropertiesValuation(BaseModel):
    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "xts",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
    ]

    value: float

    value_usd: Optional[float] = None


class PropertiesWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class Properties(BaseModel):
    identifier: PropertiesIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_identifier: Optional[PropertiesAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None
    """Alternate or previous names for the organization"""

    categories: Optional[List[PropertiesCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[PropertiesCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[PropertiesClosedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    company_type: Optional[str] = None
    """Whether an Organization is for profit or non-profit

    - for_profit - For Profit
    - non_profit - Non-profit
    """

    contact_email: Optional[str] = None
    """General contact email for the organization"""

    created_at: Optional[datetime] = None

    delisted_on: Optional[PropertiesDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    demo_days: Optional[bool] = None
    """Whether an accelerator hosts any demo days"""

    description: Optional[str] = None
    """Organization Description, Industries, Industry Groups"""

    diversity_spotlights: Optional[List[PropertiesDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    entity_def_id: Optional[str] = None
    """- organization - Organization"""

    equity_funding_total: Optional[PropertiesEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[PropertiesExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[PropertiesFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    founded_on: Optional[PropertiesFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[PropertiesFounderIdentifier]] = None
    """Founders of the organization"""

    funding_stage: Optional[str] = None
    """This field describes an organization's most recent funding status (e.g.

    Early Stage Venture, Late Stage Venture, M&A)

    - early_stage_venture - Early Stage Venture
    - ipo - IPO
    - late_stage_venture - Late Stage Venture
    - m_and_a - M&A
    - private_equity - Private Equity
    - seed - Seed
    """

    funding_total: Optional[PropertiesFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funds_total: Optional[PropertiesFundsTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    growth_insight_confidence: Optional[str] = None
    """Confidence level associated with this company's growth status

    - c100_unknown - Unknown
    - c200_low - Low
    - c300_medium - Medium
    - c400_high - High
    """

    growth_insight_direction: Optional[str] = None
    """
    - c100_uncertain - Uncertain
    - c200_declining - Not Growing
    - c300_stable - Stable
    - c400_growing - Growing
    """

    hub_tags: Optional[List[str]] = None
    """
    Tags are labels assigned to organizations, which identify their belonging to a
    group with that shared label
    """

    image_id: Optional[str] = None
    """The profile image of the organization on Crunchbase"""

    image_url: Optional[str] = None
    """The url of the profile image"""

    investor_identifiers: Optional[List[PropertiesInvestorIdentifier]] = None
    """
    The top 5 investors with investments in this company, ordered by Crunchbase Rank
    """

    investor_stage: Optional[List[str]] = None
    """This describes the stage of investments made by this organization (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    investor_type: Optional[List[str]] = None
    """This describes the type of investor this organization is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    ipo_status: Optional[str] = None
    """The current public status of the Organization

    - delisted - Delisted
    - private - Private
    - public - Public
    """

    last_equity_funding_total: Optional[PropertiesLastEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_equity_funding_type: Optional[str] = None
    """The most recent Funding Round excluding debt

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_funding_at: Optional[date] = None
    """Date of most recent Funding Round"""

    last_funding_total: Optional[PropertiesLastFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    last_funding_type: Optional[str] = None
    """Last funding round type (e.g. Seed, Series A, Private Equity)

    - angel - Angel
    - convertible_note - Convertible Note
    - corporate_round - Corporate Round
    - debt_financing - Debt Financing
    - equity_crowdfunding - Equity Crowdfunding
    - grant - Grant
    - initial_coin_offering - Initial Coin Offering
    - non_equity_assistance - Non-equity Assistance
    - post_ipo_debt - Post-IPO Debt
    - post_ipo_equity - Post-IPO Equity
    - post_ipo_secondary - Post-IPO Secondary
    - pre_seed - Pre-Seed
    - private_equity - Private Equity
    - product_crowdfunding - Product Crowdfunding
    - secondary_market - Secondary Market
    - seed - Seed
    - series_a - Series A
    - series_b - Series B
    - series_c - Series C
    - series_d - Series D
    - series_e - Series E
    - series_f - Series F
    - series_g - Series G
    - series_h - Series H
    - series_i - Series I
    - series_j - Series J
    - series_unknown - Venture - Series Unknown
    - undisclosed - Undisclosed
    """

    last_key_employee_change_date: Optional[date] = None
    """See companies that have hired executives (VP and above) in a certain date range"""

    last_layoff_date: Optional[date] = None
    """Date of last layoff event"""

    layout_id: Optional[str] = None
    """This is the auto-generated layout for the profile

    - investor - Investor Layout
    - school - School Layout
    """

    legal_name: Optional[str] = None
    """The legal name of the organization"""

    linkedin: Optional[PropertiesLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    listed_stock_symbol: Optional[str] = None
    """Stock ticker symbol (e.g. AAPL, FB, TWTR)"""

    location_group_identifiers: Optional[List[PropertiesLocationGroupIdentifier]] = None
    """Where the organization is headquartered (e.g.

    San Francisco Bay Area, Silicon Valley)
    """

    location_identifiers: Optional[List[PropertiesLocationIdentifier]] = None
    """Where the organization is headquartered"""

    name: Optional[str] = None

    num_acquisitions: Optional[float] = None
    """Total number of Acquisitions"""

    num_alumni: Optional[float] = None
    """Total number of alumni"""

    num_articles: Optional[float] = None
    """Number of news articles that reference the Organization"""

    num_current_advisor_positions: Optional[float] = None
    """
    Total number of board member and advisor profiles an organization has on
    Crunchbase
    """

    num_current_positions: Optional[float] = None
    """Total number of employee profiles an organization has on Crunchbase"""

    num_diversity_spotlight_investments: Optional[float] = None
    """Total number of diversity investments made by an investor"""

    num_employees_enum: Optional[str] = None
    """Total number of employees

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_enrollments: Optional[str] = None
    """Total number of Enrollments

    - c_00001_00010 - 1-10
    - c_00011_00050 - 11-50
    - c_00051_00100 - 51-100
    - c_00101_00250 - 101-250
    - c_00251_00500 - 251-500
    - c_00501_01000 - 501-1000
    - c_01001_05000 - 1001-5000
    - c_05001_10000 - 5001-10000
    - c_10001_max - 10001+
    """

    num_event_appearances: Optional[float] = None
    """Total number of events an Organization appeared in"""

    num_exits: Optional[float] = None
    """Total number of Exits"""

    num_exits_ipo: Optional[float] = None
    """Total number of Exits (IPO)"""

    num_founder_alumni: Optional[float] = None
    """Total number of Alumni that are Founders"""

    num_founders: Optional[float] = None
    """Total number of Founders"""

    num_funding_rounds: Optional[float] = None
    """Total number of Funding Rounds"""

    num_funds: Optional[float] = None
    """Total number of Funds raised"""

    num_investments: Optional[float] = None
    """Total number of Investments made"""

    num_investors: Optional[float] = None
    """Total number of investment firms and individual investors"""

    num_lead_investments: Optional[float] = None
    """Total number of Lead Investments made"""

    num_lead_investors: Optional[float] = None
    """Total number of lead investment firms and individual investors"""

    num_past_positions: Optional[float] = None
    """Total number of past employee profiles of an organization"""

    num_portfolio_organizations: Optional[float] = None
    """Total number of portfolio organizations"""

    num_sub_organizations: Optional[float] = None
    """Total number of sub-organizations that belongs to a parent Organization"""

    operating_status: Optional[str] = None
    """Operating Status of Organization e.g. Active, Closed

    - active - Active
    - closed - Closed
    """

    owner_identifier: Optional[PropertiesOwnerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    phone_number: Optional[str] = None
    """Organization's general phone number"""

    program_application_deadline: Optional[date] = None
    """The deadline for applying to the Accelerator Program"""

    program_duration: Optional[float] = None
    """The duration of the Acceleration Program in number of weeks"""

    program_type: Optional[str] = None
    """The type of Accelerator Program (e.g. On-Site, Online)

    - on_site - On-Site
    - online - Online
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_delta_d30: Optional[float] = None
    """Movement in Rank over the last 30 days using a score from -10 to 10"""

    rank_delta_d7: Optional[float] = None
    """Movement in Rank over the last 7 days using a score from -10 to 10"""

    rank_delta_d90: Optional[float] = None
    """Movement in Rank over the last 90 days using a score from -10 to 10"""

    rank_org: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Organizations"""

    revenue_range: Optional[str] = None
    """Estimated revenue range for organization

    - r_00000000 - Less than $1M
    - r_00001000 - $1M to $10M
    - r_00010000 - $10M to $50M
    - r_00050000 - $50M to $100M
    - r_00100000 - $100M to $500M
    - r_00500000 - $500M to $1B
    - r_01000000 - $1B to $10B
    - r_10000000 - $10B+
    """

    school_method: Optional[str] = None
    """The type of School Method (e.g. On Campus, Online)

    - on_compus - On Campus
    - online - Online
    - online_and_on_campus - Online and On Campus
    """

    school_program: Optional[str] = None
    """The type of School Program (e.g. Bootcamp, Four Year University)

    - bootcamp - Bootcamp
    - community_college - Community College
    - four_year_university - Four Year University
    - graduate_university - Graduate University
    - high_school - High School
    - trade_school - Trade School
    - two_year_university - Two Year University
    """

    school_type: Optional[str] = None
    """The type of school

    - for_profit_private - Private
    - non_profit_private - Private (Non-Profit)
    - public - Public
    """

    short_description: Optional[str] = None
    """Text of Organization Description, Industries, and Industry Groups"""

    status: Optional[str] = None
    """Status of Organization e.g. Operating, Closed, Acquired, IPO

    - closed - Closed
    - ipo - IPO
    - operating - Operating
    - was_acquired - Was Acquired
    """

    stock_exchange_symbol: Optional[str] = None
    """Stock exchange where the Organization is listed e.g. NYSE, NASDAQ

    - adx - ADX - Abu Dhabi Securities Exchange
    - afx - AFX - Afghanistan Stock Exchange
    - altx - ALTX - ALTX East Africa Exchange
    - amex - AMEX - American Stock Exchange
    - ams - AMS - Euronext Amsterdam
    - amx - AMX - Armenia Securities Exchange
    - asce - ASCE - Abuja Securities and Commodities Exchange
    - asx - ASX - Australian Securities Exchange
    - ath - ATH - Athens Stock Exchange
    - bcba - BCBA - Buenos Aires Stock Exchange
    - bdp - BDP - Budapest Stock Exchange
    - belex - BELEX - Belgrade Stock Exchange
    - ber - BER - Berliner Börse
    - bfb - BFB - Baku Stock Exchange
    - bit - BIT - Italian Stock Exchange
    - bkk - BKK - Thailand Stock Exchange
    - blse - BLSE - Banja Luka Stock Exchange
    - bme - BME - Madrid Stock Exchange
    - bmv - BMV - Mexican Stock Exchange
    - bom - BOM - Bombay Stock Exchange
    - brvm - BRVM - Regional Securities Exchange SA
    - bse - BSE - Bulgarian Stock Exchange
    - bse_lb - BSE - Beirut Stock Exchange
    - bsse - BSSE - Bratislava Stock Exchange
    - bsx - BSX - Bermuda Stock Exchange
    - bvb - BVB - Bucharest Stock Exchange
    - bvc - BVC - Colombian Stock Exchange
    - bvfb - BVFB - Belarusian Currency and Stock Exchange
    - bvm - BVM - Montevideo Stock Exchange
    - bvmf - B3 - Brazil Stock Exchange and OTC Market
    - bvmt - BVMT - Tunis Stock Exchange
    - bx - BX - Berne Stock Exchange
    - cas - CAS - Casablanca Stock Exchange
    - cise - CISE - Channel Islands Stock Exchange
    - cnsx - CNSX - Canadian National Stock Exchange
    - col - COL - Colombo Stock Exchange
    - cph - CPH - Copenhagen Stock Exchange
    - cse - CSE - Canadian Securities Exchange
    - cse_cy - CSE - Cyprus Stock Exchange
    - csx - CSX - Cambodia Securities Exchange
    - cve - TSX-V - Toronto TSX Venture Exchange
    - dfm - DFM - Dubai Financial Market
    - dse - DSE - Dhaka Stock Exchange
    - dsx - DSX - Douala Stock Exchange
    - dus - DUS - Börse Düsseldorf
    - ebr - EBR - Euronext Brussels
    - egx - EGX - Egypt Stock Exchange
    - eli - ELI - Euronext Lisbon
    - epa - EPA - Euronext Paris
    - etr - ETR - Deutsche Börse XETRA
    - eurex - EUREX - Eurex Exchange
    - fra - FRA - Frankfurt Stock Exchange
    - fwb - FWB - Börse Frankfurt Stock Exchange
    - gha - GHA - Ghana Stock Exchange
    - gsx - GSX - Georgian Stock Exchange
    - gsx_gi - GSX - Gibraltar Stock Exchange
    - hel - HEL - Helsinki Stock Exchange
    - hkg - HKG - Hong Kong Stock Exchange
    - hnx - HNX - Hanoi Stock Exchange
    - hose - HOSE - Ho Chi Minh Stock Exchange
    - ice - ICE - Iceland Stock Exchange
    - idx - IDX - Indonesia Stock Exchange
    - iex - IEX - Investors Exchange
    - ifb - IFB - Iran Fara Bourse
    - ime - IME - Iran Mercantile Exchange
    - irenex - IRENEX - Iran Energy Exchange
    - ise - ISE - Irish Stock Exchange
    - ist - IST - Istanbul Stock Exchange
    - isx - ISX - Iraq Stock Exchange
    - jp - JP - Japan Exchange
    - jsc - JSC - Belarusian Currency and Stock Exchange
    - jse - JSE - Johannesburg Stock Exchange
    - jse_jam - JSE - Jamaica Stock Exchange
    - kase - KASE - Kazakhstan Stock Exchange
    - klse - KLSE - Malaysia Stock Exchange
    - kosdaq - KOSDAQ - Korean Securities Dealers Automated Quotations
    - krx - KRX - Korea Stock Exchange
    - kse - KSE - Kuwait Stock Exchange
    - lje - LJE - Ljubljana Stock Exchange
    - lse - LSE - London Stock Exchange
    - lsm - LSM - Libyan Stock Market
    - lsx - LSX - Lao Securities Exchange
    - luse - LuSE - Lusaka Securities Exchange
    - luxse - LuxSE - Luxembourg Stock Exchange
    - mal - MAL - Malta Stock Exchange
    - mcx - MCX - Multi Commodity Exchange of India
    - meff - MEFF - Mercado Spanish Financial Futures Market
    - mnse - MNSE - Montenegro Stock Exchange
    - moex - MOEX - Moscow Exchange
    - mse - MSE - Metropolitan Stock Exchange
    - mse_md - MSE - Moldova Stock Exchange
    - mse_mk - MSE - Macedonian Stock Exchange
    - msei - MSEI - Metropolitan Stock Exchange of India
    - msm - MSM - Muscat Securities Market
    - mun - MUN - Börse München
    - nasdaq - NASDAQ
    - nbo - NSE - Nairobi Securities Exchange
    - neeq - NEEQ - National Equities Exchange and Quotations
    - nepse - NEPSE - Nepal Stock Exchange
    - nex - NEX - NEX Exchange
    - ngm - NGM - Nordic Growth Market Exchange
    - nig - NIG - Nigerian Stock Exchange
    - notc - NOTC - Norwegian OTC
    - npex - NPEX - NPEX Stock Exchange
    - nse - NSE - National Stock Exchange of India
    - nsx - NSX - National Stock Exchange of Australia
    - nyse - NYSE - New York Stock Exchange
    - nysearca - NYSEARCA - NYSE Arca
    - nysemkt - NYSEAMERICAN - NYSE American
    - nze - NZE - New Zealand Stock Exchange
    - ose - OSE - Oslo Stock Exchange
    - otcbb - OTCBB - FINRA OTC Bulletin Board
    - otcpink - OTC Pink
    - otcqb - OTCQB
    - otcqx - OTCQX
    - pdex - PDEx - Philippine Dealing Exchange
    - pex - PEX - Palestine Exchange
    - pfts - PFTS - PFTS Ukraine Stock Exchange
    - pomsox - POMSoX - Port Moresby Stock Exchange
    - prg - PRA - Prague Stock Exchange
    - pse - PSE - Philippine Stock Exchange
    - psx - PSX - Pakistan Stock Exchange
    - qse - QSE - Qatar Stock Exchange
    - rfb - RFB - Riga Stock Exchange
    - rse - RSE - Rwanda Stock Exchange
    - rsebl - RSEBL - Royal Securities Exchange of Bhutan
    - sase - SASE - Sarajevo Stock Exchange
    - sbx - SBX - BX Swiss
    - sehk - SEHK - The Stock Exchange of Hong Kong
    - sem - SEM - Stock Exchange of Mauritius
    - sgbv - SGBV - Algiers Stock Exchange
    - sgx - SGX - Singapore Stock Exchange
    - six - SIX - SIX Swiss Exchange
    - spbex - SPBEX - Saint Petersburg Stock Exchange
    - spse - SPSE - South Pacific Stock Exchange
    - sse - SSE - Shanghai Stock Exchange
    - ssx - SSX - Sydney Stock Exchange
    - sto - STO - Stockholm Stock Exchange
    - stu - STU - Börse Stuttgart
    - swx - SWX - SIX Swiss Exchange
    - szse - SZSE - Shenzhen Stock Exchange
    - tadawul - Tadawul - Saudi Stock Exchange
    - tal - TSE - Tallinn Stock Exchange
    - tfex - TFEX - Thailand Futures Exchange
    - tise - TISE - The International Stock Exchange
    - tlv - TLV - Tel Aviv Stock Exchange
    - tpe - TWSE - Taiwan Stock Exchange
    - tse_al - TSE - Tirana Stock Exchange
    - tse_ir - TSE - Tehran Stock Exchange
    - tsec - TWO - Taiwan OTC Exchange
    - tsx - TSX - Toronto Stock Exchange
    - ttse - TTSE - Trinidad and Tobago Stock Exchange
    - tyo - TYO - Tokyo Stock Exchange
    - use - USE - Uganda Securities Exchange
    - ux - UX - Ukrainian Exchange
    - vie - VIE - Vienna Stock Exchange
    - vmf - VMF - Faroese Securities Market
    - vse - VSE - Vancouver Stock Exchange
    - wse - WSE - Warsaw Stock Exchange
    - ysx - YSX - Yangon Stock Exchange
    - zamace - ZAMACE - Zambian Commodity Exchange
    - zse - ZSE - Zimbabwe Stock Exchange
    - zse_hr - ZSE - Zagreb Stock Exchange
    """

    stock_symbol: Optional[PropertiesStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[PropertiesTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    valuation: Optional[PropertiesValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    valuation_date: Optional[date] = None
    """Date of latest post money valuation"""

    website: Optional[PropertiesWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class OrganizationRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
