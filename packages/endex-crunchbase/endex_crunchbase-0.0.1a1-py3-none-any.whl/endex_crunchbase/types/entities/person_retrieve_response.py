# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "PersonRetrieveResponse",
    "Cards",
    "CardsDegree",
    "CardsDegreeIdentifier",
    "CardsDegreeCompletedOn",
    "CardsDegreePersonIdentifier",
    "CardsDegreeSchoolIdentifier",
    "CardsDegreeStartedOn",
    "CardsEventAppearance",
    "CardsEventAppearanceIdentifier",
    "CardsEventAppearanceEventIdentifier",
    "CardsEventAppearanceEventLocationIdentifier",
    "CardsEventAppearanceParticipantIdentifier",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsFacebook",
    "CardsFieldsLinkedin",
    "CardsFieldsLocationGroupIdentifier",
    "CardsFieldsLocationIdentifier",
    "CardsFieldsPrimaryOrganization",
    "CardsFieldsTwitter",
    "CardsFieldsWebsite",
    "CardsFoundedOrganization",
    "CardsFoundedOrganizationIdentifier",
    "CardsFoundedOrganizationAcquirerIdentifier",
    "CardsFoundedOrganizationCategory",
    "CardsFoundedOrganizationCategoryGroup",
    "CardsFoundedOrganizationClosedOn",
    "CardsFoundedOrganizationDelistedOn",
    "CardsFoundedOrganizationDiversitySpotlight",
    "CardsFoundedOrganizationEquityFundingTotal",
    "CardsFoundedOrganizationExitedOn",
    "CardsFoundedOrganizationFacebook",
    "CardsFoundedOrganizationFoundedOn",
    "CardsFoundedOrganizationFounderIdentifier",
    "CardsFoundedOrganizationFundingTotal",
    "CardsFoundedOrganizationFundsTotal",
    "CardsFoundedOrganizationInvestorIdentifier",
    "CardsFoundedOrganizationLastEquityFundingTotal",
    "CardsFoundedOrganizationLastFundingTotal",
    "CardsFoundedOrganizationLinkedin",
    "CardsFoundedOrganizationLocationGroupIdentifier",
    "CardsFoundedOrganizationLocationIdentifier",
    "CardsFoundedOrganizationOwnerIdentifier",
    "CardsFoundedOrganizationStockSymbol",
    "CardsFoundedOrganizationTwitter",
    "CardsFoundedOrganizationValuation",
    "CardsFoundedOrganizationWebsite",
    "CardsJob",
    "CardsJobIdentifier",
    "CardsJobEndedOn",
    "CardsJobOrganizationIdentifier",
    "CardsJobPersonIdentifier",
    "CardsJobStartedOn",
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
    "CardsPartnerFundingRound",
    "CardsPartnerFundingRoundIdentifier",
    "CardsPartnerFundingRoundClosedOn",
    "CardsPartnerFundingRoundFundedOrganizationCategory",
    "CardsPartnerFundingRoundFundedOrganizationDiversitySpotlight",
    "CardsPartnerFundingRoundFundedOrganizationFundingTotal",
    "CardsPartnerFundingRoundFundedOrganizationIdentifier",
    "CardsPartnerFundingRoundFundedOrganizationLocation",
    "CardsPartnerFundingRoundInvestorIdentifier",
    "CardsPartnerFundingRoundLeadInvestorIdentifier",
    "CardsPartnerFundingRoundMoneyRaised",
    "CardsPartnerFundingRoundPostMoneyValuation",
    "CardsPartnerFundingRoundPreMoneyValuation",
    "CardsPartnerFundingRoundTargetMoneyRaised",
    "CardsPartnerInvestment",
    "CardsPartnerInvestmentIdentifier",
    "CardsPartnerInvestmentFundingRoundIdentifier",
    "CardsPartnerInvestmentFundingRoundMoneyRaised",
    "CardsPartnerInvestmentInvestorIdentifier",
    "CardsPartnerInvestmentMoneyInvested",
    "CardsPartnerInvestmentOrganizationDiversitySpotlight",
    "CardsPartnerInvestmentOrganizationIdentifier",
    "CardsPartnerInvestmentPartnerIdentifier",
    "CardsPressReference",
    "CardsPressReferenceIdentifier",
    "CardsPressReferenceActivityEntity",
    "CardsPressReferenceURL",
    "CardsPrimaryJob",
    "CardsPrimaryJobIdentifier",
    "CardsPrimaryJobEndedOn",
    "CardsPrimaryJobOrganizationIdentifier",
    "CardsPrimaryJobPersonIdentifier",
    "CardsPrimaryJobStartedOn",
    "CardsPrimaryOrganization",
    "CardsPrimaryOrganizationIdentifier",
    "CardsPrimaryOrganizationAcquirerIdentifier",
    "CardsPrimaryOrganizationCategory",
    "CardsPrimaryOrganizationCategoryGroup",
    "CardsPrimaryOrganizationClosedOn",
    "CardsPrimaryOrganizationDelistedOn",
    "CardsPrimaryOrganizationDiversitySpotlight",
    "CardsPrimaryOrganizationEquityFundingTotal",
    "CardsPrimaryOrganizationExitedOn",
    "CardsPrimaryOrganizationFacebook",
    "CardsPrimaryOrganizationFoundedOn",
    "CardsPrimaryOrganizationFounderIdentifier",
    "CardsPrimaryOrganizationFundingTotal",
    "CardsPrimaryOrganizationFundsTotal",
    "CardsPrimaryOrganizationInvestorIdentifier",
    "CardsPrimaryOrganizationLastEquityFundingTotal",
    "CardsPrimaryOrganizationLastFundingTotal",
    "CardsPrimaryOrganizationLinkedin",
    "CardsPrimaryOrganizationLocationGroupIdentifier",
    "CardsPrimaryOrganizationLocationIdentifier",
    "CardsPrimaryOrganizationOwnerIdentifier",
    "CardsPrimaryOrganizationStockSymbol",
    "CardsPrimaryOrganizationTwitter",
    "CardsPrimaryOrganizationValuation",
    "CardsPrimaryOrganizationWebsite",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesFacebook",
    "PropertiesLinkedin",
    "PropertiesLocationGroupIdentifier",
    "PropertiesLocationIdentifier",
    "PropertiesPrimaryOrganization",
    "PropertiesTwitter",
    "PropertiesWebsite",
]


class CardsDegreeIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsDegreeCompletedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsDegreePersonIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsDegreeSchoolIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsDegreeStartedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsDegree(BaseModel):
    identifier: CardsDegreeIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    completed_on: Optional[CardsDegreeCompletedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- degree - Degree"""

    name: Optional[str] = None

    person_identifier: Optional[CardsDegreePersonIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    school_identifier: Optional[CardsDegreeSchoolIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    started_on: Optional[CardsDegreeStartedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    subject: Optional[str] = None
    """The subject or major that the person focused his/her degree on"""

    type_name: Optional[str] = None
    """The type of degree that the person received"""

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


class CardsFieldsFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


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


class CardsFieldsPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFields(BaseModel):
    identifier: CardsFieldsIdentifier
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

    facebook: Optional[CardsFieldsFacebook] = None
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

    linkedin: Optional[CardsFieldsLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[CardsFieldsLocationGroupIdentifier]] = None
    """Where the person is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[CardsFieldsLocationIdentifier]] = None
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

    primary_organization: Optional[CardsFieldsPrimaryOrganization] = None
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

    twitter: Optional[CardsFieldsTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[CardsFieldsWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to a Person's website"""


class CardsFoundedOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsFoundedOrganizationDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsFoundedOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationEquityFundingTotal(BaseModel):
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


class CardsFoundedOrganizationExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsFoundedOrganizationFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsFoundedOrganizationFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationFundingTotal(BaseModel):
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


class CardsFoundedOrganizationFundsTotal(BaseModel):
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


class CardsFoundedOrganizationInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationLastEquityFundingTotal(BaseModel):
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


class CardsFoundedOrganizationLastFundingTotal(BaseModel):
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


class CardsFoundedOrganizationLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationLocationGroupIdentifier(BaseModel):
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


class CardsFoundedOrganizationLocationIdentifier(BaseModel):
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


class CardsFoundedOrganizationOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganizationValuation(BaseModel):
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


class CardsFoundedOrganizationWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsFoundedOrganization(BaseModel):
    identifier: CardsFoundedOrganizationIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_identifier: Optional[CardsFoundedOrganizationAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None
    """Alternate or previous names for the organization"""

    categories: Optional[List[CardsFoundedOrganizationCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsFoundedOrganizationCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsFoundedOrganizationClosedOn] = None
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

    delisted_on: Optional[CardsFoundedOrganizationDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    demo_days: Optional[bool] = None
    """Whether an accelerator hosts any demo days"""

    description: Optional[str] = None
    """Organization Description, Industries, Industry Groups"""

    diversity_spotlights: Optional[List[CardsFoundedOrganizationDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    entity_def_id: Optional[str] = None
    """- organization - Organization"""

    equity_funding_total: Optional[CardsFoundedOrganizationEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsFoundedOrganizationExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsFoundedOrganizationFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    founded_on: Optional[CardsFoundedOrganizationFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsFoundedOrganizationFounderIdentifier]] = None
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

    funding_total: Optional[CardsFoundedOrganizationFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funds_total: Optional[CardsFoundedOrganizationFundsTotal] = None
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

    investor_identifiers: Optional[List[CardsFoundedOrganizationInvestorIdentifier]] = None
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

    last_equity_funding_total: Optional[CardsFoundedOrganizationLastEquityFundingTotal] = None
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

    last_funding_total: Optional[CardsFoundedOrganizationLastFundingTotal] = None
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

    linkedin: Optional[CardsFoundedOrganizationLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    listed_stock_symbol: Optional[str] = None
    """Stock ticker symbol (e.g. AAPL, FB, TWTR)"""

    location_group_identifiers: Optional[List[CardsFoundedOrganizationLocationGroupIdentifier]] = None
    """Where the organization is headquartered (e.g.

    San Francisco Bay Area, Silicon Valley)
    """

    location_identifiers: Optional[List[CardsFoundedOrganizationLocationIdentifier]] = None
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

    owner_identifier: Optional[CardsFoundedOrganizationOwnerIdentifier] = None
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

    stock_symbol: Optional[CardsFoundedOrganizationStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsFoundedOrganizationTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    valuation: Optional[CardsFoundedOrganizationValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    valuation_date: Optional[date] = None
    """Date of latest post money valuation"""

    website: Optional[CardsFoundedOrganizationWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


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


class CardsPartnerFundingRoundIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerFundingRoundClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsPartnerFundingRoundFundedOrganizationCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerFundingRoundFundedOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerFundingRoundFundedOrganizationFundingTotal(BaseModel):
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


class CardsPartnerFundingRoundFundedOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerFundingRoundFundedOrganizationLocation(BaseModel):
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


class CardsPartnerFundingRoundInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerFundingRoundLeadInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerFundingRoundMoneyRaised(BaseModel):
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


class CardsPartnerFundingRoundPostMoneyValuation(BaseModel):
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


class CardsPartnerFundingRoundPreMoneyValuation(BaseModel):
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


class CardsPartnerFundingRoundTargetMoneyRaised(BaseModel):
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


class CardsPartnerFundingRound(BaseModel):
    identifier: CardsPartnerFundingRoundIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    announced_on: Optional[date] = None
    """Date that the Funding Round was publicly announced"""

    closed_on: Optional[CardsPartnerFundingRoundClosedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- funding_round - Funding Round"""

    funded_organization_categories: Optional[List[CardsPartnerFundingRoundFundedOrganizationCategory]] = None
    """Industries of the organization that got funded"""

    funded_organization_description: Optional[str] = None
    """Description of the organization that got funded"""

    funded_organization_diversity_spotlights: Optional[
        List[CardsPartnerFundingRoundFundedOrganizationDiversitySpotlight]
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

    funded_organization_funding_total: Optional[CardsPartnerFundingRoundFundedOrganizationFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funded_organization_identifier: Optional[CardsPartnerFundingRoundFundedOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    funded_organization_location: Optional[List[CardsPartnerFundingRoundFundedOrganizationLocation]] = None
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

    investor_identifiers: Optional[List[CardsPartnerFundingRoundInvestorIdentifier]] = None
    """Names of all investors who invested in the funding round"""

    is_equity: Optional[bool] = None
    """This indicates whether the Funding Round is financed only through equity."""

    lead_investor_identifiers: Optional[List[CardsPartnerFundingRoundLeadInvestorIdentifier]] = None
    """Name of the investor who led the investment in the funding round"""

    money_raised: Optional[CardsPartnerFundingRoundMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    name: Optional[str] = None

    num_investors: Optional[float] = None
    """Total number of Investors in a Funding Round"""

    num_partners: Optional[float] = None
    """Total number of Partner Investors in a Funding Round"""

    permalink: Optional[str] = None

    post_money_valuation: Optional[CardsPartnerFundingRoundPostMoneyValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    pre_money_valuation: Optional[CardsPartnerFundingRoundPreMoneyValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_funding_round: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Funding Rounds"""

    short_description: Optional[str] = None
    """Short description of the Funding Round"""

    target_money_raised: Optional[CardsPartnerFundingRoundTargetMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsPartnerInvestmentIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerInvestmentFundingRoundIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerInvestmentFundingRoundMoneyRaised(BaseModel):
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


class CardsPartnerInvestmentInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerInvestmentMoneyInvested(BaseModel):
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


class CardsPartnerInvestmentOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerInvestmentOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerInvestmentPartnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPartnerInvestment(BaseModel):
    identifier: CardsPartnerInvestmentIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    announced_on: Optional[date] = None
    """Date when the Investment is announced"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- investment - Investment"""

    funding_round_identifier: Optional[CardsPartnerInvestmentFundingRoundIdentifier] = None
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

    funding_round_money_raised: Optional[CardsPartnerInvestmentFundingRoundMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    investor_identifier: Optional[CardsPartnerInvestmentInvestorIdentifier] = None
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

    money_invested: Optional[CardsPartnerInvestmentMoneyInvested] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    name: Optional[str] = None

    organization_diversity_spotlights: Optional[List[CardsPartnerInvestmentOrganizationDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    organization_identifier: Optional[CardsPartnerInvestmentOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partner_identifiers: Optional[List[CardsPartnerInvestmentPartnerIdentifier]] = None
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


class CardsPrimaryJobIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryJobEndedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsPrimaryJobOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryJobPersonIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryJobStartedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsPrimaryJob(BaseModel):
    identifier: CardsPrimaryJobIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    employee_featured_order: Optional[float] = None
    """These are the featured employees of an organization"""

    ended_on: Optional[CardsPrimaryJobEndedOn] = None
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

    organization_identifier: Optional[CardsPrimaryJobOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    person_identifier: Optional[CardsPrimaryJobPersonIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    short_description: Optional[str] = None
    """Text of Job Description"""

    started_on: Optional[CardsPrimaryJobStartedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    title: Optional[str] = None
    """Title of a Person's Job"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardsPrimaryOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsPrimaryOrganizationDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsPrimaryOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationEquityFundingTotal(BaseModel):
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


class CardsPrimaryOrganizationExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsPrimaryOrganizationFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class CardsPrimaryOrganizationFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationFundingTotal(BaseModel):
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


class CardsPrimaryOrganizationFundsTotal(BaseModel):
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


class CardsPrimaryOrganizationInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationLastEquityFundingTotal(BaseModel):
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


class CardsPrimaryOrganizationLastFundingTotal(BaseModel):
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


class CardsPrimaryOrganizationLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationLocationGroupIdentifier(BaseModel):
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


class CardsPrimaryOrganizationLocationIdentifier(BaseModel):
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


class CardsPrimaryOrganizationOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganizationValuation(BaseModel):
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


class CardsPrimaryOrganizationWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class CardsPrimaryOrganization(BaseModel):
    identifier: CardsPrimaryOrganizationIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_identifier: Optional[CardsPrimaryOrganizationAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None
    """Alternate or previous names for the organization"""

    categories: Optional[List[CardsPrimaryOrganizationCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[CardsPrimaryOrganizationCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[CardsPrimaryOrganizationClosedOn] = None
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

    delisted_on: Optional[CardsPrimaryOrganizationDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    demo_days: Optional[bool] = None
    """Whether an accelerator hosts any demo days"""

    description: Optional[str] = None
    """Organization Description, Industries, Industry Groups"""

    diversity_spotlights: Optional[List[CardsPrimaryOrganizationDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    entity_def_id: Optional[str] = None
    """- organization - Organization"""

    equity_funding_total: Optional[CardsPrimaryOrganizationEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[CardsPrimaryOrganizationExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[CardsPrimaryOrganizationFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    founded_on: Optional[CardsPrimaryOrganizationFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[CardsPrimaryOrganizationFounderIdentifier]] = None
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

    funding_total: Optional[CardsPrimaryOrganizationFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funds_total: Optional[CardsPrimaryOrganizationFundsTotal] = None
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

    investor_identifiers: Optional[List[CardsPrimaryOrganizationInvestorIdentifier]] = None
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

    last_equity_funding_total: Optional[CardsPrimaryOrganizationLastEquityFundingTotal] = None
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

    last_funding_total: Optional[CardsPrimaryOrganizationLastFundingTotal] = None
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

    linkedin: Optional[CardsPrimaryOrganizationLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    listed_stock_symbol: Optional[str] = None
    """Stock ticker symbol (e.g. AAPL, FB, TWTR)"""

    location_group_identifiers: Optional[List[CardsPrimaryOrganizationLocationGroupIdentifier]] = None
    """Where the organization is headquartered (e.g.

    San Francisco Bay Area, Silicon Valley)
    """

    location_identifiers: Optional[List[CardsPrimaryOrganizationLocationIdentifier]] = None
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

    owner_identifier: Optional[CardsPrimaryOrganizationOwnerIdentifier] = None
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

    stock_symbol: Optional[CardsPrimaryOrganizationStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[CardsPrimaryOrganizationTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    valuation: Optional[CardsPrimaryOrganizationValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    valuation_date: Optional[date] = None
    """Date of latest post money valuation"""

    website: Optional[CardsPrimaryOrganizationWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class Cards(BaseModel):
    degrees: Optional[List[CardsDegree]] = None

    event_appearances: Optional[List[CardsEventAppearance]] = None

    fields: Optional[CardsFields] = None

    founded_organizations: Optional[List[CardsFoundedOrganization]] = None

    jobs: Optional[List[CardsJob]] = None

    participated_funding_rounds: Optional[List[CardsParticipatedFundingRound]] = None

    participated_funds: Optional[List[CardsParticipatedFund]] = None

    participated_investments: Optional[List[CardsParticipatedInvestment]] = None

    partner_funding_rounds: Optional[List[CardsPartnerFundingRound]] = None

    partner_investments: Optional[List[CardsPartnerInvestment]] = None

    press_references: Optional[List[CardsPressReference]] = None

    primary_job: Optional[List[CardsPrimaryJob]] = None

    primary_organization: Optional[List[CardsPrimaryOrganization]] = None


class PropertiesIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


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


class PropertiesPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class PropertiesWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class Properties(BaseModel):
    identifier: PropertiesIdentifier
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

    facebook: Optional[PropertiesFacebook] = None
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

    linkedin: Optional[PropertiesLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[PropertiesLocationGroupIdentifier]] = None
    """Where the person is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[PropertiesLocationIdentifier]] = None
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

    primary_organization: Optional[PropertiesPrimaryOrganization] = None
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

    twitter: Optional[PropertiesTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[PropertiesWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to a Person's website"""


class PersonRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
