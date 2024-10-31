# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OrganizationRetrieveParams"]


class OrganizationRetrieveParams(TypedDict, total=False):
    card_ids: str
    """
    Cards to include on the resulting entity - array of card_id strings in JSON
    encoded as string Card Ids for Organization: [acquiree_acquisitions,
    acquirer_acquisitions, acquisition_predictions, child_organizations,
    child_ownerships, closure_predictions, event_appearances, fields, founders,
    funding_predictions, growth_insights, headquarters_address, investor_insights,
    investors, ipo_predictions, ipos, jobs, key_employee_changes, layoffs,
    parent_organization, parent_ownership, participated_funding_rounds,
    participated_funds, participated_investments, press_references, products,
    raised_funding_rounds, raised_funds, raised_investments]
    """

    field_ids: str
    """
    Fields to include on the resulting entity - either an array of field_id strings
    in JSON or a comma-separated list encoded as string
    """
