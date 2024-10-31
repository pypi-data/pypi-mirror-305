# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ..._models import BaseModel

__all__ = [
    "PartnershipAnnouncementRetrieveResponse",
    "Cards",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsOrganization",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesOrganization",
]


class CardsFieldsIdentifier(BaseModel):
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

    description: Optional[str] = None
    """Brief context summary"""

    entity_def_id: Optional[str] = None
    """Entity Def Type

    - partnership_announcement - Partnership Announcement
    """

    key_event_date: Optional[date] = None
    """Date when the news article was posted"""

    organization: Optional[CardsFieldsOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
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

    description: Optional[str] = None
    """Brief context summary"""

    entity_def_id: Optional[str] = None
    """Entity Def Type

    - partnership_announcement - Partnership Announcement
    """

    key_event_date: Optional[date] = None
    """Date when the news article was posted"""

    organization: Optional[PropertiesOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Time of Update"""

    uuid: Optional[str] = None
    """UUID"""


class PartnershipAnnouncementRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
