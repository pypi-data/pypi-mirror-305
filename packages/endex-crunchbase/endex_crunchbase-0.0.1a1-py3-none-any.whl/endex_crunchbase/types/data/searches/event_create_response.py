# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "EventCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityCategory",
    "EntityCategoryGroup",
    "EntityEventURL",
    "EntityLocationGroupIdentifier",
    "EntityLocationIdentifier",
    "EntityOrganizerIdentifier",
    "EntityRegistrationURL",
]


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


class EntityCategoryGroup(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityEventURL(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class EntityLocationGroupIdentifier(BaseModel):
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


class EntityOrganizerIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityRegistrationURL(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class Entity(BaseModel):
    identifier: EntityIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    categories: Optional[List[EntityCategory]] = None
    """Descriptive keyword for a Company (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    category_groups: Optional[List[EntityCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Text from Event's description"""

    ends_on: Optional[date] = None
    """End date of the Event"""

    entity_def_id: Optional[str] = None
    """- event - Event"""

    event_type: Optional[List[str]] = None
    """Type of Event (e.g. hackathon, meetup, conference)"""

    event_url: Optional[EntityEventURL] = None
    """An object representing both the url and some labeling text for that url"""

    image_id: Optional[str] = None
    """The profile image of the event on Crunchbase"""

    image_url: Optional[str] = None
    """The url of the profile image"""

    location_group_identifiers: Optional[List[EntityLocationGroupIdentifier]] = None
    """Regions of the Event (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[EntityLocationIdentifier]] = None
    """Location of the Event (e.g. Japan, San Francisco, Europe, Asia)"""

    name: Optional[str] = None
    """Event Name"""

    num_contestants: Optional[float] = None
    """Total number of Contestants at the Event"""

    num_exhibitors: Optional[float] = None
    """Total number of Exhibitors at the Event"""

    num_organizers: Optional[float] = None
    """Total number of Organizers at the Event"""

    num_speakers: Optional[float] = None
    """Total number of Speakers at the Event"""

    num_sponsors: Optional[float] = None
    """Total number of Sponsors for the Event"""

    organizer_identifiers: Optional[List[EntityOrganizerIdentifier]] = None
    """The organizer of the Event"""

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_event: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active Events"""

    registration_url: Optional[EntityRegistrationURL] = None
    """An object representing both the url and some labeling text for that url"""

    short_description: Optional[str] = None
    """A short description of the Event"""

    starts_on: Optional[date] = None
    """Start date of the Event"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    venue_name: Optional[str] = None
    """Name of the Event venue"""


class EventCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Event entities"""

    entities: Optional[List[Entity]] = None
