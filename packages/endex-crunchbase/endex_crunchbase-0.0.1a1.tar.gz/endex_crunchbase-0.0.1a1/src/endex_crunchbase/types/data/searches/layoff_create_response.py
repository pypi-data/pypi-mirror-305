# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = ["LayoffCreateResponse", "Entity", "EntityIdentifier", "EntityOrganizationIdentifier"]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityOrganizationIdentifier(BaseModel):
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
    """Laoyff entity creation date"""

    entity_def_id: Optional[str] = None
    """Layoff Signal

    - layoff - layoff
    """

    key_event_date: Optional[date] = None
    """Date when the news article was posted"""

    organization_identifier: Optional[EntityOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Entity Updating date"""

    uuid: Optional[str] = None
    """Entity UUID"""


class LayoffCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Layoff entities"""

    entities: Optional[List[Entity]] = None
