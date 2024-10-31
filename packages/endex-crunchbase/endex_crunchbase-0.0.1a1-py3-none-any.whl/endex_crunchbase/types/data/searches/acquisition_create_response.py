# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "AcquisitionCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityAcquireeCategory",
    "EntityAcquireeFundingTotal",
    "EntityAcquireeIdentifier",
    "EntityAcquireeLocation",
    "EntityAcquirerCategory",
    "EntityAcquirerFundingTotal",
    "EntityAcquirerIdentifier",
    "EntityAcquirerLocation",
    "EntityAnnouncedOn",
    "EntityCompletedOn",
    "EntityPrice",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityAcquireeCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityAcquireeFundingTotal(BaseModel):
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


class EntityAcquireeIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityAcquireeLocation(BaseModel):
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


class EntityAcquirerCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityAcquirerFundingTotal(BaseModel):
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


class EntityAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityAcquirerLocation(BaseModel):
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


class EntityAnnouncedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class EntityCompletedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class EntityPrice(BaseModel):
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


class Entity(BaseModel):
    identifier: EntityIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquiree_categories: Optional[List[EntityAcquireeCategory]] = None
    """Keyword, sector, or industry"""

    acquiree_funding_total: Optional[EntityAcquireeFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    acquiree_identifier: Optional[EntityAcquireeIdentifier] = None
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

    acquiree_locations: Optional[List[EntityAcquireeLocation]] = None
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

    acquirer_categories: Optional[List[EntityAcquirerCategory]] = None
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

    acquirer_funding_total: Optional[EntityAcquirerFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    acquirer_identifier: Optional[EntityAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_locations: Optional[List[EntityAcquirerLocation]] = None
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

    announced_on: Optional[EntityAnnouncedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    completed_on: Optional[EntityCompletedOn] = None
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

    price: Optional[EntityPrice] = None
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


class AcquisitionCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Acquisition entities"""

    entities: Optional[List[Entity]] = None
