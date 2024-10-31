# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = [
    "CardRetrieveResponse",
    "Cards",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsOrganizationIdentifier",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesOrganizationIdentifier",
]


class CardsFieldsIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFields(BaseModel):
    identifier: CardsFieldsIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None
    """Laoyff entity creation date"""

    entity_def_id: Optional[str] = None
    """Layoff Signal

    - layoff - layoff
    """

    key_event_date: Optional[date] = None
    """Date when the news article was posted"""

    organization_identifier: Optional[CardsFieldsOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Entity Updating date"""

    uuid: Optional[str] = None
    """Entity UUID"""


class Cards(BaseModel):
    fields: Optional[CardsFields] = None


class PropertiesIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesOrganizationIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class Properties(BaseModel):
    identifier: PropertiesIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None
    """Laoyff entity creation date"""

    entity_def_id: Optional[str] = None
    """Layoff Signal

    - layoff - layoff
    """

    key_event_date: Optional[date] = None
    """Date when the news article was posted"""

    organization_identifier: Optional[PropertiesOrganizationIdentifier] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None
    """Entity Updating date"""

    uuid: Optional[str] = None
    """Entity UUID"""


class CardRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
