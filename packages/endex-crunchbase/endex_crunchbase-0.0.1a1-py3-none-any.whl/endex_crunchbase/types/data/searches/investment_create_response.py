# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "InvestmentCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityFundingRoundIdentifier",
    "EntityFundingRoundMoneyRaised",
    "EntityInvestorIdentifier",
    "EntityMoneyInvested",
    "EntityOrganizationDiversitySpotlight",
    "EntityOrganizationIdentifier",
    "EntityPartnerIdentifier",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityFundingRoundIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityFundingRoundMoneyRaised(BaseModel):
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


class EntityInvestorIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityMoneyInvested(BaseModel):
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


class EntityOrganizationDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityPartnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class Entity(BaseModel):
    identifier: EntityIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    announced_on: Optional[date] = None
    """Date when the Investment is announced"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- investment - Investment"""

    funding_round_identifier: Optional[EntityFundingRoundIdentifier] = None
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

    funding_round_money_raised: Optional[EntityFundingRoundMoneyRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    investor_identifier: Optional[EntityInvestorIdentifier] = None
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

    money_invested: Optional[EntityMoneyInvested] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    name: Optional[str] = None

    organization_diversity_spotlights: Optional[List[EntityOrganizationDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    organization_identifier: Optional[EntityOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partner_identifiers: Optional[List[EntityPartnerIdentifier]] = None
    """Name of the individual who led a funding round for his/her firm"""

    permalink: Optional[str] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class InvestmentCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Investment entities"""

    entities: Optional[List[Entity]] = None
