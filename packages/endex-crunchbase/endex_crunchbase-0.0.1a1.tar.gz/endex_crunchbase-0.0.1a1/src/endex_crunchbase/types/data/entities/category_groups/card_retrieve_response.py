# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = [
    "CardRetrieveResponse",
    "Cards",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsCategory",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesCategory",
]


class CardsFieldsIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsCategory(BaseModel):
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

    categories: Optional[List[CardsFieldsCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- category_group - Industry Group"""

    name: Optional[str] = None
    """Descriptive name of the Industry Group"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class Cards(BaseModel):
    fields: Optional[CardsFields] = None


class PropertiesIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class PropertiesCategory(BaseModel):
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

    categories: Optional[List[PropertiesCategory]] = None
    """Descriptive keyword for an Organization (e.g.

    SaaS, Android, Cloud Computing, Medical Device)
    """

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- category_group - Industry Group"""

    name: Optional[str] = None
    """Descriptive name of the Industry Group"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CardRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
