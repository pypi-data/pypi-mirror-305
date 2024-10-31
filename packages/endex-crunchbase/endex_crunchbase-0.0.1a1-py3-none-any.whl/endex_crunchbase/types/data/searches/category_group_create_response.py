# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CategoryGroupCreateResponse", "Entity", "EntityIdentifier", "EntityCategory"]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityCategory(BaseModel):
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

    categories: Optional[List[EntityCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- category_group - Industry Group"""

    name: Optional[str] = None
    """Descriptive name of the Industry Group"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CategoryGroupCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of CategoryGroup entities"""

    entities: Optional[List[Entity]] = None
