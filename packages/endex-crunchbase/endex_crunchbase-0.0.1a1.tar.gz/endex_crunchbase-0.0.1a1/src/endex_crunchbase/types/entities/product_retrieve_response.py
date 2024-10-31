# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "ProductRetrieveResponse",
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
    """Product description"""

    entity_def_id: Optional[str] = None
    """Product

    - product - Product
    """

    local_rank: Optional[float] = None
    """Rank relative to this organization's other products"""

    organization: Optional[CardsFieldsOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

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
    """Product description"""

    entity_def_id: Optional[str] = None
    """Product

    - product - Product
    """

    local_rank: Optional[float] = None
    """Rank relative to this organization's other products"""

    organization: Optional[PropertiesOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class ProductRetrieveResponse(BaseModel):
    cards: Optional[Cards] = None

    properties: Optional[Properties] = None
