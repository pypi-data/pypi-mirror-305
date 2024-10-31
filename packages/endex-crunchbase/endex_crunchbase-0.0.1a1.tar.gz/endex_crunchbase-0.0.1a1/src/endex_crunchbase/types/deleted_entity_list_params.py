# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DeletedEntityListParams"]


class DeletedEntityListParams(TypedDict, total=False):
    after_id: str
    """Used to paginate search results to the next page.

    after_id should be the uuid of the last item in the current page. May not be
    provided simultaneously with before_id.
    """

    before_id: str
    """Used to paginate search results to the previous page.

    before_id should be the uuid of the first item in the current page. May not be
    provided simultaneously with after_id
    """

    collection_ids: str
    """Filter by collection id(s).

    Comma separated list of collection ids. E.g. organizations, people,
    funding_rounds, acquisitions, investments, events, press_references, funds,
    event_appearances, ipos, ownerships, categories, locations, jobs
    """

    deleted_at_order: Literal["asc", "desc"]
    """Direction of sorting by deleted_at property"""

    limit: int
    """Number of results to retrieve; default = 10, max = 25"""
