# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel

__all__ = ["SearchPartnershipAnnouncementsResponse", "Entity", "EntityIdentifier", "EntityOrganization"]


class EntityIdentifier(BaseModel):
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

    description: Optional[str] = None
    """Brief context summary"""

    entity_def_id: Optional[str] = None
    """Entity Def Type

    - partnership_announcement - Partnership Announcement
    """

    key_event_date: Optional[date] = None
    """Date when the news article was posted"""

    organization: Optional[EntityOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Time of Update"""

    uuid: Optional[str] = None
    """UUID"""


class SearchPartnershipAnnouncementsResponse(BaseModel):
    count: Optional[int] = None
    """Total number of PartnershipAnnouncement entities"""

    entities: Optional[List[Entity]] = None
