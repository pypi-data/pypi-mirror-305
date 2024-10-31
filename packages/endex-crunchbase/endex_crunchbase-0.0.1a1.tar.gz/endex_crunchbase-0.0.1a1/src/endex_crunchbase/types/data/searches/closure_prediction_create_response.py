# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = [
    "ClosurePredictionCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityAddress",
    "EntityAward",
    "EntityGrowthInsight",
    "EntityKeyEmployeeChange",
    "EntityLayoff",
    "EntityLegalProceeding",
    "EntityOrganization",
    "EntityPartnershipAnnouncement",
    "EntityProductLaunch",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityAddress(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityAward(BaseModel):
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


class EntityKeyEmployeeChange(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityLayoff(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityLegalProceeding(BaseModel):
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


class Entity(BaseModel):
    identifier: EntityIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    address: Optional[EntityAddress] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    award: Optional[EntityAward] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- closure_prediction - Closure Prediction"""

    generated_on: Optional[date] = None

    growth_insight: Optional[EntityGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_employee_change: Optional[EntityKeyEmployeeChange] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    layoff: Optional[EntityLayoff] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    legal_proceeding: Optional[EntityLegalProceeding] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    media_sentiment: Optional[str] = None
    """
    - c100_evidence_absent - No Increased Negative Media Coverage
    - c200_evidence_present - Increased Negative Media Coverage
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

    probability_tier: Optional[str] = None
    """
    - p100_positive_high - Very Likely
    - p200_positive_low - Likely
    - p300_neutral - Unsure
    - p400_negative_low - Unlikely
    - p500_negative_high - Very Unlikely
    """

    product_launch: Optional[EntityProductLaunch] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class ClosurePredictionCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of ClosurePrediction entities"""

    entities: Optional[List[Entity]] = None
