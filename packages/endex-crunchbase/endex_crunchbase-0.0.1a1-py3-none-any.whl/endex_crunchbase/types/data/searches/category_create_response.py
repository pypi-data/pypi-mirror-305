# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CategoryCreateResponse", "Entity", "EntityIdentifier", "EntityCategoryGroup"]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityCategoryGroup(BaseModel):
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

    category_groups: Optional[List[EntityCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- category - Industry"""

    name: Optional[str] = None
    """Descriptive name of the Industry Group"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CategoryCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Category entities"""

    entities: Optional[List[Entity]] = None
