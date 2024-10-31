# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ..._models import BaseModel

__all__ = [
    "LegalProceedingRetrieveResponse",
    "Cards",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsOrganization",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesOrganization",
]


class CardsFieldsIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsOrganization(BaseModel):
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

    organization: Optional[CardsFieldsOrganization] = None
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


class Cards(BaseModel):
    fields: Optional[CardsFields] = None


class PropertiesIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesOrganization(BaseModel):
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

    organization: Optional[PropertiesOrganization] = None
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


class LegalProceedingRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
