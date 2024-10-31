# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "LocationRetrieveResponse",
    "Cards",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsGroup",
    "CardsFieldsLocation",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesGroup",
    "PropertiesLocation",
]


class CardsFieldsIdentifier(BaseModel):
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


class CardsFieldsGroup(BaseModel):
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


class CardsFieldsLocation(BaseModel):
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


class CardsFields(BaseModel):
    identifier: CardsFieldsIdentifier
    """
    Every location entity in the system has a unique identifier that contains all
    necessary properties to represent it.
    """

    country_code: Optional[str] = None
    """Short alphabetic or numeric geographical codes that represent countries (e.g.

    TWN, USA, ZAF)
    """

    country_code_ext: Optional[str] = None

    created_at: Optional[datetime] = None
    """Created At"""

    entity_def_id: Optional[str] = None
    """- location - Location"""

    facet_ids: Optional[List[str]] = None
    """Type of location (e.g. City, Continent, Regional Area)"""

    groups: Optional[List[CardsFieldsGroup]] = None
    """Regional areas this location belongs to (e.g.

    San Francisco Bay Area, Silicon Valley)
    """

    locations: Optional[List[CardsFieldsLocation]] = None
    """Full location name (e.g. Denver, Colorado, United States, North America)"""

    name: Optional[str] = None

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    region_code: Optional[str] = None
    """Region code used to define location"""

    short_description: Optional[str] = None
    """Description"""

    updated_at: Optional[datetime] = None
    """Updated At"""

    uuid: Optional[str] = None


class Cards(BaseModel):
    fields: Optional[CardsFields] = None


class PropertiesIdentifier(BaseModel):
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


class PropertiesGroup(BaseModel):
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


class PropertiesLocation(BaseModel):
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


class Properties(BaseModel):
    identifier: PropertiesIdentifier
    """
    Every location entity in the system has a unique identifier that contains all
    necessary properties to represent it.
    """

    country_code: Optional[str] = None
    """Short alphabetic or numeric geographical codes that represent countries (e.g.

    TWN, USA, ZAF)
    """

    country_code_ext: Optional[str] = None

    created_at: Optional[datetime] = None
    """Created At"""

    entity_def_id: Optional[str] = None
    """- location - Location"""

    facet_ids: Optional[List[str]] = None
    """Type of location (e.g. City, Continent, Regional Area)"""

    groups: Optional[List[PropertiesGroup]] = None
    """Regional areas this location belongs to (e.g.

    San Francisco Bay Area, Silicon Valley)
    """

    locations: Optional[List[PropertiesLocation]] = None
    """Full location name (e.g. Denver, Colorado, United States, North America)"""

    name: Optional[str] = None

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    region_code: Optional[str] = None
    """Region code used to define location"""

    short_description: Optional[str] = None
    """Description"""

    updated_at: Optional[datetime] = None
    """Updated At"""

    uuid: Optional[str] = None


class LocationRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
