# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "AddressCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityHeadquarteredOrganizationIdentifier",
    "EntityLocationIdentifier",
    "EntityOrganization",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityHeadquarteredOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


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

    country_code: Optional[str] = None
    """Country Code"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- address - Address"""

    headquartered_organization_identifier: Optional[EntityHeadquarteredOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    location_identifiers: Optional[List[EntityLocationIdentifier]] = None
    """What city the address is located in (e.g. San Francisco, London, Kiev)."""

    name: Optional[str] = None
    """Descriptive name of the Address (e.g. Headquarters, London Office)"""

    opening_date: Optional[date] = None
    """Date this location opened"""

    opening_description: Optional[str] = None
    """Summary of context regarding opening of this address"""

    organization: Optional[EntityOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    postal_code: Optional[str] = None
    """The postal code of the address"""

    region_code: Optional[str] = None
    """Region Code"""

    street_1: Optional[str] = None
    """The street address of the location"""

    street_2: Optional[str] = None
    """The street address of the location"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class AddressCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Address entities"""

    entities: Optional[List[Entity]] = None
