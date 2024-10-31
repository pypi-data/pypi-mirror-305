# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ....._models import BaseModel

__all__ = [
    "CardRetrieveResponse",
    "Cards",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsAddress",
    "CardsFieldsAward",
    "CardsFieldsGrowthInsight",
    "CardsFieldsKeyEmployeeChange",
    "CardsFieldsLayoff",
    "CardsFieldsLegalProceeding",
    "CardsFieldsOrganization",
    "CardsFieldsPartnershipAnnouncement",
    "CardsFieldsProductLaunch",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesAddress",
    "PropertiesAward",
    "PropertiesGrowthInsight",
    "PropertiesKeyEmployeeChange",
    "PropertiesLayoff",
    "PropertiesLegalProceeding",
    "PropertiesOrganization",
    "PropertiesPartnershipAnnouncement",
    "PropertiesProductLaunch",
]


class CardsFieldsIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsAddress(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsAward(BaseModel):
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


class CardsFieldsKeyEmployeeChange(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsLayoff(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsLegalProceeding(BaseModel):
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


class CardsFields(BaseModel):
    identifier: CardsFieldsIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    address: Optional[CardsFieldsAddress] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    award: Optional[CardsFieldsAward] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- closure_prediction - Closure Prediction"""

    generated_on: Optional[date] = None

    growth_insight: Optional[CardsFieldsGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_employee_change: Optional[CardsFieldsKeyEmployeeChange] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    layoff: Optional[CardsFieldsLayoff] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    legal_proceeding: Optional[CardsFieldsLegalProceeding] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    media_sentiment: Optional[str] = None
    """
    - c100_evidence_absent - No Increased Negative Media Coverage
    - c200_evidence_present - Increased Negative Media Coverage
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

    probability_tier: Optional[str] = None
    """
    - p100_positive_high - Very Likely
    - p200_positive_low - Likely
    - p300_neutral - Unsure
    - p400_negative_low - Unlikely
    - p500_negative_high - Very Unlikely
    """

    product_launch: Optional[CardsFieldsProductLaunch] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class Cards(BaseModel):
    fields: Optional[CardsFields] = None


class PropertiesIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesAddress(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesAward(BaseModel):
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


class PropertiesKeyEmployeeChange(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesLayoff(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesLegalProceeding(BaseModel):
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


class Properties(BaseModel):
    identifier: PropertiesIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    address: Optional[PropertiesAddress] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    award: Optional[PropertiesAward] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- closure_prediction - Closure Prediction"""

    generated_on: Optional[date] = None

    growth_insight: Optional[PropertiesGrowthInsight] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    key_employee_change: Optional[PropertiesKeyEmployeeChange] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    layoff: Optional[PropertiesLayoff] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    legal_proceeding: Optional[PropertiesLegalProceeding] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    media_sentiment: Optional[str] = None
    """
    - c100_evidence_absent - No Increased Negative Media Coverage
    - c200_evidence_present - Increased Negative Media Coverage
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

    probability_tier: Optional[str] = None
    """
    - p100_positive_high - Very Likely
    - p200_positive_low - Likely
    - p300_neutral - Unsure
    - p400_negative_low - Unlikely
    - p500_negative_high - Very Unlikely
    """

    product_launch: Optional[PropertiesProductLaunch] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
