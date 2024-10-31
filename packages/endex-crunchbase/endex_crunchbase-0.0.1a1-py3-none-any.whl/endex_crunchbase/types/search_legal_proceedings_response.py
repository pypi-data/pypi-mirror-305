# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel

__all__ = ["SearchLegalProceedingsResponse", "Entity", "EntityIdentifier", "EntityOrganization"]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


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

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Description of legal proceeding"""

    entity_def_id: Optional[str] = None
    """Proceedings relating to law, regulation, or compliance

    - legal_proceeding - Legal Proceeding
    """

    key_event_date: Optional[date] = None
    """Date of proceeding or when expected"""

    name: Optional[str] = None
    """Legal proceeding name"""

    organization: Optional[EntityOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    proceeding_type: Optional[str] = None
    """The type of proceeding

    - compliance - Compliance
    - lawsuit - Lawsuit
    - other - Other
    - regulatory - Regulatory
    """

    sentiment: Optional[str] = None
    """Sentiment associated with proceeding

    - c100_positive - Positive
    - c200_neutral - Neutral
    - c300_negative - Negative
    """

    updated_at: Optional[datetime] = None
    """Date entity was updated"""

    uuid: Optional[str] = None
    """UUID of legal proceeding entity"""


class SearchLegalProceedingsResponse(BaseModel):
    count: Optional[int] = None
    """Total number of LegalProceeding entities"""

    entities: Optional[List[Entity]] = None
