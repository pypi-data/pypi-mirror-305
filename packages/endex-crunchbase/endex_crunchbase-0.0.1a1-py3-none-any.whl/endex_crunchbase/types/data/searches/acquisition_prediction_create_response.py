# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = [
    "AcquisitionPredictionCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityExampleAcquisition",
    "EntityGrowthInsight",
    "EntityKeyLeadershipHire",
    "EntityOrganization",
    "EntityPartnershipAnnouncement",
    "EntityRunwaySpeculation",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityExampleAcquisition(BaseModel):
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

    - acquisition_prediction - Acquisition Prediction
    """

    example_acquisition: Optional[EntityExampleAcquisition] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this Acquisition Prediction was generated"""

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
    """The predicted probability that this Organization will be acquired"""

    runway_speculation: Optional[EntityRunwaySpeculation] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Time of Update"""

    uuid: Optional[str] = None
    """UUID"""


class AcquisitionPredictionCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of AcquisitionPrediction entities"""

    entities: Optional[List[Entity]] = None
