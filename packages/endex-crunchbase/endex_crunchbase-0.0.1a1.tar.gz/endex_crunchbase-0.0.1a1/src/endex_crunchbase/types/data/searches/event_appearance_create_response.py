# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "EventAppearanceCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityEventIdentifier",
    "EntityEventLocationIdentifier",
    "EntityParticipantIdentifier",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityEventIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityEventLocationIdentifier(BaseModel):
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


class EntityParticipantIdentifier(BaseModel):
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

    appearance_type: Optional[str] = None
    """Describe how an Organization or a Person is participating in an Event (e.g.

    Speaker, Sponsor, etc.)

    - contestant - Contestant
    - exhibitor - Exhibitor
    - organizer - Organizer
    - speaker - Speaker
    - sponsor - Sponsor
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- event_appearance - Event Appearance"""

    event_identifier: Optional[EntityEventIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    event_location_identifiers: Optional[List[EntityEventLocationIdentifier]] = None
    """Location of the Event (e.g. Japan, San Francisco, Europe, Asia)"""

    event_starts_on: Optional[date] = None
    """Start date of the Event"""

    name: Optional[str] = None

    participant_identifier: Optional[EntityParticipantIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    short_description: Optional[str] = None
    """
    A short description of how a person or an organization is participant in an
    Event
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class EventAppearanceCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of EventAppearance entities"""

    entities: Optional[List[Entity]] = None
