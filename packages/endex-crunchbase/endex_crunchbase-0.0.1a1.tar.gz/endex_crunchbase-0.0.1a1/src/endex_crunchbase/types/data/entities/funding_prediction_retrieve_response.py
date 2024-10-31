# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = [
    "FundingPredictionRetrieveResponse",
    "Cards",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsExampleFundingRound",
    "CardsFieldsGrowthInsight",
    "CardsFieldsKeyLeadershipHire",
    "CardsFieldsOrganization",
    "CardsFieldsPartnershipAnnouncement",
    "CardsFieldsProductLaunch",
    "CardsFieldsRunwaySpeculation",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesExampleFundingRound",
    "PropertiesGrowthInsight",
    "PropertiesKeyLeadershipHire",
    "PropertiesOrganization",
    "PropertiesPartnershipAnnouncement",
    "PropertiesProductLaunch",
    "PropertiesRunwaySpeculation",
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


class CardsFieldsPartnershipAnnouncement(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsProductLaunch(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsRunwaySpeculation(BaseModel):
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

    - funding_prediction - Funding Prediction
    """

    example_funding_round: Optional[CardsFieldsExampleFundingRound] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this Funding Prediction was generated"""

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

    organization: Optional[CardsFieldsOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partnership_announcement: Optional[CardsFieldsPartnershipAnnouncement] = None
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

    product_launch: Optional[CardsFieldsProductLaunch] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    runway_speculation: Optional[CardsFieldsRunwaySpeculation] = None
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


class PropertiesPartnershipAnnouncement(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesProductLaunch(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesRunwaySpeculation(BaseModel):
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

    - funding_prediction - Funding Prediction
    """

    example_funding_round: Optional[PropertiesExampleFundingRound] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    generated_on: Optional[date] = None
    """Date on which this Funding Prediction was generated"""

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

    organization: Optional[PropertiesOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    partnership_announcement: Optional[PropertiesPartnershipAnnouncement] = None
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

    product_launch: Optional[PropertiesProductLaunch] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    runway_speculation: Optional[PropertiesRunwaySpeculation] = None
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


class FundingPredictionRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
