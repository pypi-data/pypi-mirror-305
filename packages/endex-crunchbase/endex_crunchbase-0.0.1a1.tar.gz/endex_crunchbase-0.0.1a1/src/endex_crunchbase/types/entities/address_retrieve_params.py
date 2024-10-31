# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AddressRetrieveParams"]


class AddressRetrieveParams(TypedDict, total=False):
    card_ids: str
    """
    Cards to include on the resulting entity - array of card_id strings in JSON
    encoded as string Card Ids for Address: [event, fields, organization]
    """

    field_ids: str
    """
    Fields to include on the resulting entity - either an array of field_id strings
    in JSON or a comma-separated list encoded as string
    """
