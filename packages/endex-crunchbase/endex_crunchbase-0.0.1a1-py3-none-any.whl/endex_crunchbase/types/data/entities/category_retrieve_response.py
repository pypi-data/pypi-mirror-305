# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = [
    "CategoryRetrieveResponse",
    "Cards",
    "CardsFields",
    "CardsFieldsIdentifier",
    "CardsFieldsCategoryGroup",
    "Properties",
    "PropertiesIdentifier",
    "PropertiesCategoryGroup",
]


class CardsFieldsIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class CardsFieldsCategoryGroup(BaseModel):
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

    category_groups: Optional[List[CardsFieldsCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- category - Industry"""

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


class PropertiesCategoryGroup(BaseModel):
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

    category_groups: Optional[List[PropertiesCategoryGroup]] = None
    """Superset of Industries (e.g. Software, Mobile, Health Care)"""

    created_at: Optional[datetime] = None

    entity_def_id: Optional[str] = None
    """- category - Industry"""

    name: Optional[str] = None
    """Descriptive name of the Industry Group"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class CategoryRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
