# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = [
    "DegreeCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityCompletedOn",
    "EntityPersonIdentifier",
    "EntitySchoolIdentifier",
    "EntityStartedOn",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityCompletedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class EntityPersonIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntitySchoolIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityStartedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class Entity(BaseModel):
    identifier: EntityIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    completed_on: Optional[EntityCompletedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- degree - Degree"""

    name: Optional[str] = None

    person_identifier: Optional[EntityPersonIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    school_identifier: Optional[EntitySchoolIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    started_on: Optional[EntityStartedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    subject: Optional[str] = None
    """The subject or major that the person focused his/her degree on"""

    type_name: Optional[str] = None
    """The type of degree that the person received"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class DegreeCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Degree entities"""

    entities: Optional[List[Entity]] = None
