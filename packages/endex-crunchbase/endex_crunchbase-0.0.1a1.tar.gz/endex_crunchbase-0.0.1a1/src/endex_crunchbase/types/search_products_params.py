# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchProductsParams", "Query", "Order"]


class SearchProductsParams(TypedDict, total=False):
    field_ids: Required[List[str]]

    query: Required[Iterable[Query]]
    """Order in which the search results should be returned"""

    after_id: str
    """Used to paginate search results to the next page.

    after_id should be the uuid of the last item in the current page. May not be
    provided simultaneously with before_id.
    """

    before_id: str
    """Used to paginate search results to the previous page.

    before_id should be the uuid of the first item in the current page. May not be
    provided simultaneously with after_id.
    """

    limit: int
    """Number of rows to return. Default is 100, min is 1, max is 2000."""

    order: Iterable[Order]
    """Order in which the search results should be returned"""


class Query(TypedDict, total=False):
    field_id: Required[str]
    """the type of the query"""

    operator_id: Required[
        Literal[
            "blank",
            "eq",
            "not_eq",
            "gt",
            "gte",
            "lt",
            "lte",
            "starts",
            "contains",
            "between",
            "includes",
            "not_includes",
            "includes_all",
            "not_includes_all",
            "domain_eq",
            "domain_blank",
        ]
    ]

    type: Required[Literal["predicate"]]

    values: List[Union[str, float, bool]]
    """values array with data type matching field_id type"""


class Order(TypedDict, total=False):
    field_id: Required[str]
    """Name of the field to sort on"""

    sort: Required[Literal["asc", "desc"]]

    nulls: Literal["first", "last"]
