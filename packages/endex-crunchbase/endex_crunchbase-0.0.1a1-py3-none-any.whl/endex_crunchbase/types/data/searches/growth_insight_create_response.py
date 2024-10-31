# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ...._models import BaseModel

__all__ = ["GrowthInsightCreateResponse", "Entity", "EntityIdentifier", "EntityOrganization"]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class Entity(BaseModel):
    identifier: EntityIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    created_at: Optional[datetime] = None

    customers: Optional[str] = None
    """Fluctuations in the number of customers or users

    - c100_worsening - Customer Decline
    - c200_improving - Customer Growth
    """

    description: Optional[str] = None
    """A concise text statement highlighting the company's growth trajectory"""

    engagement: Optional[str] = None
    """
    Changes in product engagement levels, including increases or decreases in
    website traffic, app downloads, and user activity

    - c100_worsening - Product Usage Decline
    - c200_improving - Product Usage Growth
    """

    entity_def_id: Optional[str] = None
    """Growth Insight

    - growth_insight - Growth Insight
    """

    finance: Optional[str] = None
    """
    Changes in key financial metrics including revenue, sales, earnings, profit
    margins, dividends, return on investment, stock performance, and commercial
    contracts

    - c100_worsening - Financial Decline
    - c200_improving - Financial Growth
    """

    funding_raised: Optional[str] = None
    """
    Activities related to financial investments, including receiving funding or
    making strategic investments into other organizations

    - c100_worsening - Has Not Recently Raised Funding
    - c200_improving - Recently Raised Funding
    """

    generated_on: Optional[date] = None
    """Date on which this insight was generated"""

    growth_confidence: Optional[str] = None
    """Assessment of the reliability and accuracy of the provided data

    - c100_unknown - Unknown
    - c200_low - Low
    - c300_medium - Medium
    - c400_high - High
    """

    growth_direction: Optional[str] = None
    """Direction of the company's growth trajectory

    - c100_uncertain - Uncertain
    - c200_declining - Not Growing
    - c300_stable - Stable
    - c400_growing - Growing
    """

    headcount: Optional[str] = None
    """
    Variations in employee numbers, including hiring sprees, layoffs, workforce
    expansions, and reductions

    - c100_worsening - Headcount Reduction
    - c200_improving - Headcount Growth
    """

    market_share: Optional[str] = None
    """
    Changes in the company’s market share, including growth through new market
    entries and decline due to market exits

    - c100_worsening - Market Share Decline
    - c200_improving - Market Share Expansion
    """

    mergers_acquisitions: Optional[str] = None
    """Business consolidations involving mergers, acquisitions, or divestitures

    - c100_worsening - No Merger or Acquisition
    - c200_improving - Merger or Acquisition
    """

    operations: Optional[str] = None
    """
    Modifications in operational footprints, including acquisitions or reductions of
    facilities, and regional expansions or contractions

    - c100_worsening - Operations Contraction
    - c200_improving - Operations Expansion
    """

    organization: Optional[EntityOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    outbound_investment: Optional[str] = None
    """Records the company's financial investments into external entities or projects

    - c100_worsening - No Strategic Investment
    - c200_improving - Strategic Investment
    """

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class GrowthInsightCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of GrowthInsight entities"""

    entities: Optional[List[Entity]] = None
