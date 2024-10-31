# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = [
    "CardRetrieveResponse",
    "Cards",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsExampleFundingRound",
    "CardsFieldsExampleIpo",
    "CardsFieldsGrowthInsight",
    "CardsFieldsKeyLeadershipHire",
    "CardsFieldsOrganization",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesExampleFundingRound",
    "PropertiesExampleIpo",
    "PropertiesGrowthInsight",
    "PropertiesKeyLeadershipHire",
    "PropertiesOrganization",
]


class CardsFieldsIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsExampleFundingRound(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsExampleIpo(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsGrowthInsight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsKeyLeadershipHire(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFields(BaseModel):
    identifier: CardsFieldsIdentifier
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

    example_funding_round: Optional[CardsFieldsExampleFundingRound] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    example_ipo: Optional[CardsFieldsExampleIpo] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this IPO Prediction was generated"""

    growth_insight: Optional[CardsFieldsGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_leadership_hire: Optional[CardsFieldsKeyLeadershipHire] = None
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

    organization: Optional[CardsFieldsOrganization] = None
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


class Cards(BaseModel):
    fields: Optional[CardsFields] = None


class PropertiesIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesExampleFundingRound(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesExampleIpo(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesGrowthInsight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesKeyLeadershipHire(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class Properties(BaseModel):
    identifier: PropertiesIdentifier
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

    example_funding_round: Optional[PropertiesExampleFundingRound] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    example_ipo: Optional[PropertiesExampleIpo] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this IPO Prediction was generated"""

    growth_insight: Optional[PropertiesGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_leadership_hire: Optional[PropertiesKeyLeadershipHire] = None
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

    organization: Optional[PropertiesOrganization] = None
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


class CardRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
