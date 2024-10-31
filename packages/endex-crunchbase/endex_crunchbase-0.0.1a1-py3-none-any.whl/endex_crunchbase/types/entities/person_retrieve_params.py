# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PersonRetrieveParams"]


class PersonRetrieveParams(TypedDict, total=False):
    card_ids: str
    """
    Cards to include on the resulting entity - array of card_id strings in JSON
    encoded as string Card Ids for Person: [degrees, event_appearances, fields,
    founded_organizations, jobs, participated_funding_rounds, participated_funds,
    participated_investments, partner_funding_rounds, partner_investments,
    press_references, primary_job, primary_organization]
    """

    field_ids: str
    """
    Fields to include on the resulting entity - either an array of field_id strings
    in JSON or a comma-separated list encoded as string
    """
