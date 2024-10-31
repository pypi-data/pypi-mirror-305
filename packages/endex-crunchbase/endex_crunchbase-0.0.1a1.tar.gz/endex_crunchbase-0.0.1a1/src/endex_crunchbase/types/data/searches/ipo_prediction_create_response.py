# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = [
    "IpoPredictionCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityExampleFundingRound",
    "EntityExampleIpo",
    "EntityGrowthInsight",
    "EntityKeyLeadershipHire",
    "EntityOrganization",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityExampleFundingRound(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityExampleIpo(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityGrowthInsight(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityKeyLeadershipHire(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityOrganization(BaseModel):
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

    created_at: Optional[datetime] = None
    """Time of Creation"""

    entity_def_id: Optional[str] = None
    """Entity Def Type

    - ipo_prediction - IPO Prediction
    """

    example_funding_round: Optional[EntityExampleFundingRound] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    example_ipo: Optional[EntityExampleIpo] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this IPO Prediction was generated"""

    growth_insight: Optional[EntityGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_leadership_hire: Optional[EntityKeyLeadershipHire] = None
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

    organization: Optional[EntityOrganization] = None
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


class IpoPredictionCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of IpoPrediction entities"""

    entities: Optional[List[Entity]] = None
