# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FundingRoundRetrieveParams"]


class FundingRoundRetrieveParams(TypedDict, total=False):
    card_ids: str
    """
    Cards to include on the resulting entity - array of card_id strings in JSON
    encoded as string Card Ids for FundingRound: [fields, investments, investors,
    lead_investors, organization, partners, press_references]
    """

    field_ids: str
    """
    Fields to include on the resulting entity - either an array of field_id strings
    in JSON or a comma-separated list encoded as string
    """
