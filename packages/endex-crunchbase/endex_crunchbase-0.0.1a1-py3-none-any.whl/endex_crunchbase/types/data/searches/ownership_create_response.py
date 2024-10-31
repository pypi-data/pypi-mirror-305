# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["OwnershipCreateResponse", "Entity", "EntityIdentifier", "EntityOwneeIdentifier", "EntityOwnerIdentifier"]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityOwneeIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityOwnerIdentifier(BaseModel):
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
    """- ownership - Ownership"""

    name: Optional[str] = None

    ownee_identifier: Optional[EntityOwneeIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    owner_identifier: Optional[EntityOwnerIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    ownership_type: Optional[str] = None
    """
    This is the relationship defining how a sub-organization is related to a parent
    organization

    - affiliated_company - Affiliated Company
    - division - Division
    - investment_arm - Investment Arm
    - joint_venture - Joint Venture
    - subsidiary - Subsidiary
    """

    permalink: Optional[str] = None

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class OwnershipCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Ownership entities"""

    entities: Optional[List[Entity]] = None
