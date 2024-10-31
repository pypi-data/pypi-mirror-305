# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "IpoCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityAmountRaised",
    "EntityDelistedOn",
    "EntityOrganizationIdentifier",
    "EntitySharePrice",
    "EntityValuation",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityAmountRaised(BaseModel):
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


class EntityDelistedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class EntityOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntitySharePrice(BaseModel):
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


class Entity(BaseModel):
    identifier: EntityIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    amount_raised: Optional[EntityAmountRaised] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    created_at: Optional[datetime] = None

    delisted_on: Optional[EntityDelistedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    entity_def_id: Optional[str] = None
    """- ipo - Ipo"""

    image_id: Optional[str] = None

    organization_identifier: Optional[EntityOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_ipo: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active IPOs"""

    share_price: Optional[EntitySharePrice] = None
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

    valuation: Optional[EntityValuation] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    went_public_on: Optional[date] = None
    """Date the Organization went public"""


class IpoCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Ipo entities"""

    entities: Optional[List[Entity]] = None
