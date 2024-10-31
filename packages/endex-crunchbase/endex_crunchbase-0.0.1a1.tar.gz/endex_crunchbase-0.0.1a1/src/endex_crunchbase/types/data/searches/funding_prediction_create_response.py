# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = [
    "FundingPredictionCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityExampleFundingRound",
    "EntityGrowthInsight",
    "EntityKeyLeadershipHire",
    "EntityOrganization",
    "EntityPartnershipAnnouncement",
    "EntityProductLaunch",
    "EntityRunwaySpeculation",
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


class EntityPartnershipAnnouncement(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityProductLaunch(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityRunwaySpeculation(BaseModel):
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

    - funding_prediction - Funding Prediction
    """

    example_funding_round: Optional[EntityExampleFundingRound] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this Funding Prediction was generated"""

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

    organization: Optional[EntityOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partnership_announcement: Optional[EntityPartnershipAnnouncement] = None
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

    product_launch: Optional[EntityProductLaunch] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    runway_speculation: Optional[EntityRunwaySpeculation] = None
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


class FundingPredictionCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of FundingPrediction entities"""

    entities: Optional[List[Entity]] = None
