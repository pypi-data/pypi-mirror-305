# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["DiversitySpotlightCreateResponse", "Entity", "EntityIdentifier"]


class EntityIdentifier(BaseModel):
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

    entity_def_id: Optional[str] = None
    """- diversity_spotlight - Diversity Spotlight"""

    facet_ids: Optional[List[str]] = None

    name: Optional[str] = None
    """
    Types of diversity represented in an organization, specifically of those who are
    founding members, currently the CEO, or have check-writing abilities in an
    investment firm. This feature is in beta and may change with future updates.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class DiversitySpotlightCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of DiversitySpotlight entities"""

    entities: Optional[List[Entity]] = None
