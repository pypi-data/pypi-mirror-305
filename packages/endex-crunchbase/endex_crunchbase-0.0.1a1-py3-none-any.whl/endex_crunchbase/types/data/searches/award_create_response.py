# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = ["AwardCreateResponse", "Entity", "EntityIdentifier", "EntityOrganization"]


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

    description: Optional[str] = None
    """Award description"""

    entity_def_id: Optional[str] = None
    """Award

    - award - Award
    """

    key_event_date: Optional[date] = None
    """Date award presented or announced"""

    name: Optional[str] = None
    """Award name"""

    organization: Optional[EntityOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Date entity was updated"""

    uuid: Optional[str] = None
    """Award entity UUID"""


class AwardCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Award entities"""

    entities: Optional[List[Entity]] = None
