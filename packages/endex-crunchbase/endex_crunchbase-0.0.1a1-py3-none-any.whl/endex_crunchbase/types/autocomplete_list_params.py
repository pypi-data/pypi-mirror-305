# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AutocompleteListParams"]


class AutocompleteListParams(TypedDict, total=False):
    query: Required[str]
    """Value to perform the autocomplete search with."""

    collection_ids: str
    """A comma separated list of collection ids to search against.

    Leaving this blank means it will search across all identifiers. Entity defs can
    be constrained to specific facets by providing them as facet collections.
    Relationship collections will resolve to their underlying entity def.
    \\CCollection ids are: acquisition_predictions, acquisitions, addresses, awards,
    categories, category_groups, closure_predictions, degrees, diversity_spotlights,
    event_appearances, events, funding_predictions, funding_rounds, funds,
    growth_insights, investments, investor_insights, ipo_predictions, ipos, jobs,
    key_employee_changes, layoffs, legal_proceedings, locations, organizations,
    ownerships, partnership_announcements, people, press_references, principals,
    product_launches, products
    """

    limit: int
    """Number of results to retrieve; default = 10, max = 25"""
