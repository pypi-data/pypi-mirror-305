# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "EventRetrieveResponse",
    "Cards",
    "CardsAddress",
    "CardsAddressIdentifier",
    "CardsAddressHeadquarteredOrganizationIdentifier",
    "CardsAddressLocationIdentifier",
    "CardsAddressOrganization",
    "CardsAppearance",
    "CardsAppearanceIdentifier",
    "CardsAppearanceEventIdentifier",
    "CardsAppearanceEventLocationIdentifier",
    "CardsAppearanceParticipantIdentifier",
    "CardsContestant",
    "CardsContestantIdentifier",
    "CardsContestantCategory",
    "CardsContestantCategoryGroup",
    "CardsContestantClosedOn",
    "CardsContestantDelistedOn",
    "CardsContestantDiversitySpotlight",
    "CardsContestantEquityFundingTotal",
    "CardsContestantExitedOn",
    "CardsContestantFacebook",
    "CardsContestantFoundedOn",
    "CardsContestantFounderIdentifier",
    "CardsContestantFundingTotal",
    "CardsContestantInvestorIdentifier",
    "CardsContestantLastEquityFundingTotal",
    "CardsContestantLastFundingTotal",
    "CardsContestantLinkedin",
    "CardsContestantLocationGroupIdentifier",
    "CardsContestantLocationIdentifier",
    "CardsContestantPrimaryOrganization",
    "CardsContestantStockSymbol",
    "CardsContestantTwitter",
    "CardsContestantWebsite",
    "CardsExhibitor",
    "CardsExhibitorIdentifier",
    "CardsExhibitorCategory",
    "CardsExhibitorCategoryGroup",
    "CardsExhibitorClosedOn",
    "CardsExhibitorDelistedOn",
    "CardsExhibitorDiversitySpotlight",
    "CardsExhibitorEquityFundingTotal",
    "CardsExhibitorExitedOn",
    "CardsExhibitorFacebook",
    "CardsExhibitorFoundedOn",
    "CardsExhibitorFounderIdentifier",
    "CardsExhibitorFundingTotal",
    "CardsExhibitorInvestorIdentifier",
    "CardsExhibitorLastEquityFundingTotal",
    "CardsExhibitorLastFundingTotal",
    "CardsExhibitorLinkedin",
    "CardsExhibitorLocationGroupIdentifier",
    "CardsExhibitorLocationIdentifier",
    "CardsExhibitorPrimaryOrganization",
    "CardsExhibitorStockSymbol",
    "CardsExhibitorTwitter",
    "CardsExhibitorWebsite",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsCategory",
    "CardsFieldsCategoryGroup",
    "CardsFieldsEventURL",
    "CardsFieldsLocationGroupIdentifier",
    "CardsFieldsLocationIdentifier",
    "CardsFieldsOrganizerIdentifier",
    "CardsFieldsRegistrationURL",
    "CardsOrganizer",
    "CardsOrganizerIdentifier",
    "CardsOrganizerCategory",
    "CardsOrganizerCategoryGroup",
    "CardsOrganizerClosedOn",
    "CardsOrganizerDelistedOn",
    "CardsOrganizerDiversitySpotlight",
    "CardsOrganizerEquityFundingTotal",
    "CardsOrganizerExitedOn",
    "CardsOrganizerFacebook",
    "CardsOrganizerFoundedOn",
    "CardsOrganizerFounderIdentifier",
    "CardsOrganizerFundingTotal",
    "CardsOrganizerInvestorIdentifier",
    "CardsOrganizerLastEquityFundingTotal",
    "CardsOrganizerLastFundingTotal",
    "CardsOrganizerLinkedin",
    "CardsOrganizerLocationGroupIdentifier",
    "CardsOrganizerLocationIdentifier",
    "CardsOrganizerPrimaryOrganization",
    "CardsOrganizerStockSymbol",
    "CardsOrganizerTwitter",
    "CardsOrganizerWebsite",
    "CardsPressReference",
    "CardsPressReferenceIdentifier",
    "CardsPressReferenceActivityEntity",
    "CardsPressReferenceURL",
    "CardsSpeaker",
    "CardsSpeakerIdentifier",
    "CardsSpeakerCategory",
    "CardsSpeakerCategoryGroup",
    "CardsSpeakerClosedOn",
    "CardsSpeakerDelistedOn",
    "CardsSpeakerDiversitySpotlight",
    "CardsSpeakerEquityFundingTotal",
    "CardsSpeakerExitedOn",
    "CardsSpeakerFacebook",
    "CardsSpeakerFoundedOn",
    "CardsSpeakerFounderIdentifier",
    "CardsSpeakerFundingTotal",
    "CardsSpeakerInvestorIdentifier",
    "CardsSpeakerLastEquityFundingTotal",
    "CardsSpeakerLastFundingTotal",
    "CardsSpeakerLinkedin",
    "CardsSpeakerLocationGroupIdentifier",
    "CardsSpeakerLocationIdentifier",
    "CardsSpeakerPrimaryOrganization",
    "CardsSpeakerStockSymbol",
    "CardsSpeakerTwitter",
    "CardsSpeakerWebsite",
    "CardsSponsor",
    "CardsSponsorIdentifier",
    "CardsSponsorCategory",
    "CardsSponsorCategoryGroup",
    "CardsSponsorClosedOn",
    "CardsSponsorDelistedOn",
    "CardsSponsorDiversitySpotlight",
    "CardsSponsorEquityFundingTotal",
    "CardsSponsorExitedOn",
    "CardsSponsorFacebook",
    "CardsSponsorFoundedOn",
    "CardsSponsorFounderIdentifier",
    "CardsSponsorFundingTotal",
    "CardsSponsorInvestorIdentifier",
    "CardsSponsorLastEquityFundingTotal",
    "CardsSponsorLastFundingTotal",
    "CardsSponsorLinkedin",
    "CardsSponsorLocationGroupIdentifier",
    "CardsSponsorLocationIdentifier",
    "CardsSponsorPrimaryOrganization",
    "CardsSponsorStockSymbol",
    "CardsSponsorTwitter",
    "CardsSponsorWebsite",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesCategory",
    "PropertiesCategoryGroup",
    "PropertiesEventURL",
    "PropertiesLocationGroupIdentifier",
    "PropertiesLocationIdentifier",
    "PropertiesOrganizerIdentifier",
    "PropertiesRegistrationURL",
]


class CardsAddressIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAddressHeadquarteredOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAddressLocationIdentifier(BaseModel):
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


class CardsAddressOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAddress(BaseModel):
    identifier: CardsAddressIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    country_code: Optional[str] = None
    """Country Code"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- address - Address"""

    headquartered_organization_identifier: Optional[CardsAddressHeadquarteredOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    location_identifiers: Optional[List[CardsAddressLocationIdentifier]] = None
    """What city the address is located in (e.g. San Francisco, London, Kiev)."""

    name: Optional[str] = None
    """Descriptive name of the Address (e.g. Headquarters, London Office)"""

    opening_date: Optional[date] = None
    """Date this location opened"""

    opening_description: Optional[str] = None
    """Summary of context regarding opening of this address"""

    organization: Optional[CardsAddressOrganization] = None
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


class CardsAppearanceIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAppearanceEventIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAppearanceEventLocationIdentifier(BaseModel):
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


class CardsAppearanceParticipantIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsAppearance(BaseModel):
    identifier: CardsAppearanceIdentifier
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

    event_identifier: Optional[CardsAppearanceEventIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    event_location_identifiers: Optional[List[CardsAppearanceEventLocationIdentifier]] = None
    """Location of the Event (e.g. Japan, San Francisco, Europe, Asia)"""

    event_starts_on: Optional[date] = None
    """Start date of the Event"""

    name: Optional[str] = None

    participant_identifier: Optional[CardsAppearanceParticipantIdentifier] = None
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


class CardsContestantIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsContestantCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsContestantCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsContestantClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsContestantDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsContestantDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsContestantEquityFundingTotal(BaseModel):
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


class CardsContestantExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsContestantFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsContestantFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsContestantFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsContestantFundingTotal(BaseModel):
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


class CardsContestantInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsContestantLastEquityFundingTotal(BaseModel):
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


class CardsContestantLastFundingTotal(BaseModel):
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


class CardsContestantLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsContestantLocationGroupIdentifier(BaseModel):
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


class CardsContestantLocationIdentifier(BaseModel):
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


class CardsContestantPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsContestantStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsContestantTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsContestantWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsContestant(BaseModel):
    identifier: CardsContestantIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None

    born_on: Optional[date] = None

    categories: Optional[List[CardsContestantCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsContestantCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsContestantClosedOn] = None
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

    delisted_on: Optional[CardsContestantDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    description: Optional[str] = None
    """Organization or Person Description, Industries, Industry Groups"""

    died_on: Optional[date] = None

    diversity_spotlights: Optional[List[CardsContestantDiversitySpotlight]] = None
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

    equity_funding_total: Optional[CardsContestantEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsContestantExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsContestantFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    first_name: Optional[str] = None
    """First name of a Person"""

    founded_on: Optional[CardsContestantFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsContestantFounderIdentifier]] = None
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

    funding_total: Optional[CardsContestantFundingTotal] = None
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

    investor_identifiers: Optional[List[CardsContestantInvestorIdentifier]] = None
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

    last_equity_funding_total: Optional[CardsContestantLastEquityFundingTotal] = None
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

    last_funding_total: Optional[CardsContestantLastFundingTotal] = None
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

    linkedin: Optional[CardsContestantLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[CardsContestantLocationGroupIdentifier]] = None
    """Where the principal is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[CardsContestantLocationIdentifier]] = None
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

    primary_organization: Optional[CardsContestantPrimaryOrganization] = None
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

    stock_symbol: Optional[CardsContestantStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsContestantTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[CardsContestantWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class CardsExhibitorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsExhibitorDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsExhibitorDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorEquityFundingTotal(BaseModel):
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


class CardsExhibitorExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsExhibitorFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsExhibitorFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorFundingTotal(BaseModel):
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


class CardsExhibitorInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorLastEquityFundingTotal(BaseModel):
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


class CardsExhibitorLastFundingTotal(BaseModel):
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


class CardsExhibitorLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorLocationGroupIdentifier(BaseModel):
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


class CardsExhibitorLocationIdentifier(BaseModel):
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


class CardsExhibitorPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitorWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsExhibitor(BaseModel):
    identifier: CardsExhibitorIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None

    born_on: Optional[date] = None

    categories: Optional[List[CardsExhibitorCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsExhibitorCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsExhibitorClosedOn] = None
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

    delisted_on: Optional[CardsExhibitorDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    description: Optional[str] = None
    """Organization or Person Description, Industries, Industry Groups"""

    died_on: Optional[date] = None

    diversity_spotlights: Optional[List[CardsExhibitorDiversitySpotlight]] = None
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

    equity_funding_total: Optional[CardsExhibitorEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsExhibitorExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsExhibitorFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    first_name: Optional[str] = None
    """First name of a Person"""

    founded_on: Optional[CardsExhibitorFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsExhibitorFounderIdentifier]] = None
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

    funding_total: Optional[CardsExhibitorFundingTotal] = None
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

    investor_identifiers: Optional[List[CardsExhibitorInvestorIdentifier]] = None
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

    last_equity_funding_total: Optional[CardsExhibitorLastEquityFundingTotal] = None
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

    last_funding_total: Optional[CardsExhibitorLastFundingTotal] = None
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

    linkedin: Optional[CardsExhibitorLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[CardsExhibitorLocationGroupIdentifier]] = None
    """Where the principal is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[CardsExhibitorLocationIdentifier]] = None
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

    primary_organization: Optional[CardsExhibitorPrimaryOrganization] = None
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

    stock_symbol: Optional[CardsExhibitorStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsExhibitorTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[CardsExhibitorWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class CardsFieldsIdentifier(BaseModel):
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


class CardsFieldsEventURL(BaseModel):
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


class CardsFieldsOrganizerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsRegistrationURL(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFields(BaseModel):
    identifier: CardsFieldsIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    categories: Optional[List[CardsFieldsCategory]] = None
    """Descriptive keyword for a Company (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsFieldsCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Text from Event's description"""

    ends_on: Optional[date] = None
    """End date of the Event"""

    entity_def_id: Optional[str] = None
    """- event - Event"""

    event_type: Optional[List[str]] = None
    """Type of Event (e.g. hackathon, meetup, conference)"""

    event_url: Optional[CardsFieldsEventURL] = None
    """An object representing both the url and some labeling text for that url"""

    image_id: Optional[str] = None
    """The profile image of the event on Crunchbase"""

    image_url: Optional[str] = None
    """The url of the profile image"""

    location_group_identifiers: Optional[List[CardsFieldsLocationGroupIdentifier]] = None
    """Regions of the Event (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[CardsFieldsLocationIdentifier]] = None
    """Location of the Event (e.g. Japan, San Francisco, Europe, Asia)"""

    name: Optional[str] = None
    """Event Name"""

    num_contestants: Optional[float] = None
    """Total number of Contestants at the Event"""

    num_exhibitors: Optional[float] = None
    """Total number of Exhibitors at the Event"""

    num_organizers: Optional[float] = None
    """Total number of Organizers at the Event"""

    num_speakers: Optional[float] = None
    """Total number of Speakers at the Event"""

    num_sponsors: Optional[float] = None
    """Total number of Sponsors for the Event"""

    organizer_identifiers: Optional[List[CardsFieldsOrganizerIdentifier]] = None
    """The organizer of the Event"""

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_event: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Events"""

    registration_url: Optional[CardsFieldsRegistrationURL] = None
    """An object representing both the url and some labeling text for that url"""

    short_description: Optional[str] = None
    """A short description of the Event"""

    starts_on: Optional[date] = None
    """Start date of the Event"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    venue_name: Optional[str] = None
    """Name of the Event venue"""


class CardsOrganizerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsOrganizerDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsOrganizerDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerEquityFundingTotal(BaseModel):
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


class CardsOrganizerExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsOrganizerFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsOrganizerFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerFundingTotal(BaseModel):
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


class CardsOrganizerInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerLastEquityFundingTotal(BaseModel):
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


class CardsOrganizerLastFundingTotal(BaseModel):
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


class CardsOrganizerLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerLocationGroupIdentifier(BaseModel):
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


class CardsOrganizerLocationIdentifier(BaseModel):
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


class CardsOrganizerPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizerWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsOrganizer(BaseModel):
    identifier: CardsOrganizerIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None

    born_on: Optional[date] = None

    categories: Optional[List[CardsOrganizerCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsOrganizerCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsOrganizerClosedOn] = None
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

    delisted_on: Optional[CardsOrganizerDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    description: Optional[str] = None
    """Organization or Person Description, Industries, Industry Groups"""

    died_on: Optional[date] = None

    diversity_spotlights: Optional[List[CardsOrganizerDiversitySpotlight]] = None
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

    equity_funding_total: Optional[CardsOrganizerEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsOrganizerExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsOrganizerFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    first_name: Optional[str] = None
    """First name of a Person"""

    founded_on: Optional[CardsOrganizerFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsOrganizerFounderIdentifier]] = None
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

    funding_total: Optional[CardsOrganizerFundingTotal] = None
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

    investor_identifiers: Optional[List[CardsOrganizerInvestorIdentifier]] = None
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

    last_equity_funding_total: Optional[CardsOrganizerLastEquityFundingTotal] = None
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

    last_funding_total: Optional[CardsOrganizerLastFundingTotal] = None
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

    linkedin: Optional[CardsOrganizerLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[CardsOrganizerLocationGroupIdentifier]] = None
    """Where the principal is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[CardsOrganizerLocationIdentifier]] = None
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

    primary_organization: Optional[CardsOrganizerPrimaryOrganization] = None
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

    stock_symbol: Optional[CardsOrganizerStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsOrganizerTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[CardsOrganizerWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


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


class CardsSpeakerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsSpeakerDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsSpeakerDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerEquityFundingTotal(BaseModel):
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


class CardsSpeakerExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsSpeakerFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsSpeakerFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerFundingTotal(BaseModel):
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


class CardsSpeakerInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerLastEquityFundingTotal(BaseModel):
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


class CardsSpeakerLastFundingTotal(BaseModel):
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


class CardsSpeakerLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerLocationGroupIdentifier(BaseModel):
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


class CardsSpeakerLocationIdentifier(BaseModel):
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


class CardsSpeakerPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsSpeakerWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsSpeaker(BaseModel):
    identifier: CardsSpeakerIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None

    born_on: Optional[date] = None

    categories: Optional[List[CardsSpeakerCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsSpeakerCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsSpeakerClosedOn] = None
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

    delisted_on: Optional[CardsSpeakerDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    description: Optional[str] = None
    """Organization or Person Description, Industries, Industry Groups"""

    died_on: Optional[date] = None

    diversity_spotlights: Optional[List[CardsSpeakerDiversitySpotlight]] = None
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

    equity_funding_total: Optional[CardsSpeakerEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsSpeakerExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsSpeakerFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    first_name: Optional[str] = None
    """First name of a Person"""

    founded_on: Optional[CardsSpeakerFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsSpeakerFounderIdentifier]] = None
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

    funding_total: Optional[CardsSpeakerFundingTotal] = None
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

    investor_identifiers: Optional[List[CardsSpeakerInvestorIdentifier]] = None
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

    last_equity_funding_total: Optional[CardsSpeakerLastEquityFundingTotal] = None
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

    last_funding_total: Optional[CardsSpeakerLastFundingTotal] = None
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

    linkedin: Optional[CardsSpeakerLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[CardsSpeakerLocationGroupIdentifier]] = None
    """Where the principal is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[CardsSpeakerLocationIdentifier]] = None
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

    primary_organization: Optional[CardsSpeakerPrimaryOrganization] = None
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

    stock_symbol: Optional[CardsSpeakerStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsSpeakerTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[CardsSpeakerWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class CardsSponsorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsSponsorDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsSponsorDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorEquityFundingTotal(BaseModel):
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


class CardsSponsorExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsSponsorFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsSponsorFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorFundingTotal(BaseModel):
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


class CardsSponsorInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorLastEquityFundingTotal(BaseModel):
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


class CardsSponsorLastFundingTotal(BaseModel):
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


class CardsSponsorLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorLocationGroupIdentifier(BaseModel):
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


class CardsSponsorLocationIdentifier(BaseModel):
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


class CardsSponsorPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsSponsorWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsSponsor(BaseModel):
    identifier: CardsSponsorIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None

    born_on: Optional[date] = None

    categories: Optional[List[CardsSponsorCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsSponsorCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsSponsorClosedOn] = None
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

    delisted_on: Optional[CardsSponsorDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    description: Optional[str] = None
    """Organization or Person Description, Industries, Industry Groups"""

    died_on: Optional[date] = None

    diversity_spotlights: Optional[List[CardsSponsorDiversitySpotlight]] = None
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

    equity_funding_total: Optional[CardsSponsorEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsSponsorExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsSponsorFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    first_name: Optional[str] = None
    """First name of a Person"""

    founded_on: Optional[CardsSponsorFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsSponsorFounderIdentifier]] = None
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

    funding_total: Optional[CardsSponsorFundingTotal] = None
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

    investor_identifiers: Optional[List[CardsSponsorInvestorIdentifier]] = None
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

    last_equity_funding_total: Optional[CardsSponsorLastEquityFundingTotal] = None
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

    last_funding_total: Optional[CardsSponsorLastFundingTotal] = None
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

    linkedin: Optional[CardsSponsorLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[CardsSponsorLocationGroupIdentifier]] = None
    """Where the principal is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[CardsSponsorLocationIdentifier]] = None
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

    primary_organization: Optional[CardsSponsorPrimaryOrganization] = None
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

    stock_symbol: Optional[CardsSponsorStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsSponsorTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[CardsSponsorWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class Cards(BaseModel):
    address: Optional[List[CardsAddress]] = None

    appearances: Optional[List[CardsAppearance]] = None

    contestants: Optional[List[CardsContestant]] = None

    exhibitors: Optional[List[CardsExhibitor]] = None

    fields: Optional[CardsFields] = None

    organizers: Optional[List[CardsOrganizer]] = None

    press_references: Optional[List[CardsPressReference]] = None

    speakers: Optional[List[CardsSpeaker]] = None

    sponsors: Optional[List[CardsSponsor]] = None


class PropertiesIdentifier(BaseModel):
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


class PropertiesEventURL(BaseModel):
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


class PropertiesOrganizerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesRegistrationURL(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class Properties(BaseModel):
    identifier: PropertiesIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    categories: Optional[List[PropertiesCategory]] = None
    """Descriptive keyword for a Company (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[PropertiesCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Text from Event's description"""

    ends_on: Optional[date] = None
    """End date of the Event"""

    entity_def_id: Optional[str] = None
    """- event - Event"""

    event_type: Optional[List[str]] = None
    """Type of Event (e.g. hackathon, meetup, conference)"""

    event_url: Optional[PropertiesEventURL] = None
    """An object representing both the url and some labeling text for that url"""

    image_id: Optional[str] = None
    """The profile image of the event on Crunchbase"""

    image_url: Optional[str] = None
    """The url of the profile image"""

    location_group_identifiers: Optional[List[PropertiesLocationGroupIdentifier]] = None
    """Regions of the Event (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[PropertiesLocationIdentifier]] = None
    """Location of the Event (e.g. Japan, San Francisco, Europe, Asia)"""

    name: Optional[str] = None
    """Event Name"""

    num_contestants: Optional[float] = None
    """Total number of Contestants at the Event"""

    num_exhibitors: Optional[float] = None
    """Total number of Exhibitors at the Event"""

    num_organizers: Optional[float] = None
    """Total number of Organizers at the Event"""

    num_speakers: Optional[float] = None
    """Total number of Speakers at the Event"""

    num_sponsors: Optional[float] = None
    """Total number of Sponsors for the Event"""

    organizer_identifiers: Optional[List[PropertiesOrganizerIdentifier]] = None
    """The organizer of the Event"""

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_event: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Events"""

    registration_url: Optional[PropertiesRegistrationURL] = None
    """An object representing both the url and some labeling text for that url"""

    short_description: Optional[str] = None
    """A short description of the Event"""

    starts_on: Optional[date] = None
    """Start date of the Event"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    venue_name: Optional[str] = None
    """Name of the Event venue"""


class EventRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
