# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = [
    "JobCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityEndedOn",
    "EntityOrganizationIdentifier",
    "EntityPersonIdentifier",
    "EntityStartedOn",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityEndedOn(BaseModel):
    precision: str

    value: Optional[date] = None


class EntityOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityPersonIdentifier(BaseModel):
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

    created_at: Optional[datetime] = None

    employee_featured_order: Optional[float] = None
    """These are the featured employees of an organization"""

    ended_on: Optional[EntityEndedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    entity_def_id: Optional[str] = None
    """- job - Job"""

    is_current: Optional[bool] = None
    """This indicates whether the Job is current or not"""

    job_type: Optional[str] = None
    """Select a job type that best represent your role at the organization

    - advisor - Advisor
    - board_member - Board Member
    - board_observer - Board Observer
    - employee - Non-Executive Employee
    - executive - Executive
    """

    name: Optional[str] = None

    organization_identifier: Optional[EntityOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    permalink: Optional[str] = None

    person_identifier: Optional[EntityPersonIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    short_description: Optional[str] = None
    """Text of Job Description"""

    started_on: Optional[EntityStartedOn] = None
    """A field that will contain date information up to a certain level of precision.

    E.g. month, day, etc.
    """

    title: Optional[str] = None
    """Title of a Person's Job"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class JobCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Job entities"""

    entities: Optional[List[Entity]] = None
