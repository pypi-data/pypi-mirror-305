# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PrincipalRetrieveParams"]


class PrincipalRetrieveParams(TypedDict, total=False):
    card_ids: str
    """Principal entity doesn't have any cards"""

    field_ids: str
    """
    Fields to include on the resulting entity - either an array of field_id strings
    in JSON or a comma-separated list encoded as string
    """
