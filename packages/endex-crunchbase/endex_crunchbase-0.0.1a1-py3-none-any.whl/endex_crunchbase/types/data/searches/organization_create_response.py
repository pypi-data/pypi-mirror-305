# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "OrganizationCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityAcquirerIdentifier",
    "EntityCategory",
    "EntityCategoryGroup",
    "EntityClosedOn",
    "EntityDelistedOn",
    "EntityDiversitySpotlight",
    "EntityEquityFundingTotal",
    "EntityExitedOn",
    "EntityFacebook",
    "EntityFoundedOn",
    "EntityFounderIdentifier",
    "EntityFundingTotal",
    "EntityFundsTotal",
    "EntityInvestorIdentifier",
    "EntityLastEquityFundingTotal",
    "EntityLastFundingTotal",
    "EntityLinkedin",
    "EntityLocationGroupIdentifier",
    "EntityLocationIdentifier",
    "EntityOwnerIdentifier",
    "EntityStockSymbol",
    "EntityTwitter",
    "EntityValuation",
    "EntityWebsite",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityAcquirerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityCategory(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityClosedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class EntityDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class EntityDiversitySpotlight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityEquityFundingTotal(BaseModel):
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


class EntityExitedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class EntityFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class EntityFoundedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class EntityFounderIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityFundingTotal(BaseModel):
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


class EntityFundsTotal(BaseModel):
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


class EntityLastEquityFundingTotal(BaseModel):
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


class EntityLastFundingTotal(BaseModel):
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


class EntityLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class EntityLocationGroupIdentifier(BaseModel):
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


class EntityLocationIdentifier(BaseModel):
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


class EntityOwnerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityStockSymbol(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class EntityValuation(BaseModel):
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


class EntityWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class Entity(BaseModel):
    identifier: EntityIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    acquirer_identifier: Optional[EntityAcquirerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None
    """Alternate or previous names for the organization"""

    categories: Optional[List[EntityCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[EntityCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    closed_on: Optional[EntityClosedOn] = None
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

    delisted_on: Optional[EntityDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    demo_days: Optional[bool] = None
    """Whether an accelerator hosts any demo days"""

    description: Optional[str] = None
    """Organization Description, Industries, Industry Groups"""

    diversity_spotlights: Optional[List[EntityDiversitySpotlight]] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    entity_def_id: Optional[str] = None
    """- organization - Organization"""

    equity_funding_total: Optional[EntityEquityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    exited_on: Optional[EntityExitedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    facebook: Optional[EntityFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    founded_on: Optional[EntityFoundedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    founder_identifiers: Optional[List[EntityFounderIdentifier]] = None
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

    funding_total: Optional[EntityFundingTotal] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    funds_total: Optional[EntityFundsTotal] = None
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

    investor_identifiers: Optional[List[EntityInvestorIdentifier]] = None
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

    last_equity_funding_total: Optional[EntityLastEquityFundingTotal] = None
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

    last_funding_total: Optional[EntityLastFundingTotal] = None
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

    linkedin: Optional[EntityLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    listed_stock_symbol: Optional[str] = None
    """Stock ticker symbol (e.g. AAPL, FB, TWTR)"""

    location_group_identifiers: Optional[List[EntityLocationGroupIdentifier]] = None
    """Where the organization is headquartered (e.g.

    San Francisco Bay Area, Silicon Valley)
    """

    location_identifiers: Optional[List[EntityLocationIdentifier]] = None
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

    owner_identifier: Optional[EntityOwnerIdentifier] = None
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

    stock_symbol: Optional[EntityStockSymbol] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    twitter: Optional[EntityTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    valuation: Optional[EntityValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    valuation_date: Optional[date] = None
    """Date of latest post money valuation"""

    website: Optional[EntityWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to homepage"""

    went_public_on: Optional[date] = None
    """The date when the Organization went public"""


class OrganizationCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Organization entities"""

    entities: Optional[List[Entity]] = None
