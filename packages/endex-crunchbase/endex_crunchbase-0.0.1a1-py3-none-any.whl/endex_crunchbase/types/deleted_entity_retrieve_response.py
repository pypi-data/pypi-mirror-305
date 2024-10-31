# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DeletedEntityRetrieveResponse", "Entity", "EntityIdentifier"]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class Entity(BaseModel):
    deleted_at: Optional[datetime] = None
    """Timestamp when entity was deleted"""

    identifier: Optional[EntityIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """


class DeletedEntityRetrieveResponse(BaseModel):
    entities: Optional[List[Entity]] = None
