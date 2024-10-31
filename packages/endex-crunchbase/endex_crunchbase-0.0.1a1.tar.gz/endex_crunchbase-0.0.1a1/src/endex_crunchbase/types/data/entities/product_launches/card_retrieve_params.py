# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardRetrieveParams"]


class CardRetrieveParams(TypedDict, total=False):
    entity_id: Required[str]

    after_id: str
    """Lookup uuid of the last item in the previous page (not required for first page).

    Used to iterate a card's results starting at the beginning of the ordered set
    and moving forward. Suitable for implementing "next page" functionality. May not
    be provided simultaneously with before_id.
    """

    before_id: str
    """Lookup uuid of the first item in the previous page (not required for first
    page).

    Used to iterate a card's results starting at the end of the ordered set and
    moving backward. Suitable for implementing "previous page" functionality. May
    not be provided simultaneously with after_id.
    """

    card_field_ids: str
    """
    Card fields to include on the specified card - array of field_id strings in JSON
    encoded as string
    """

    limit: int
    """Number of rows to return. Default is 100, min is 1, max is 100."""

    order: str
    """Field name with order direction (asc/desc)"""
