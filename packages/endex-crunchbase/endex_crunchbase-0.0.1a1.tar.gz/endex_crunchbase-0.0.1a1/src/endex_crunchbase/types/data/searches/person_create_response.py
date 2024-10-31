# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "PersonCreateResponse",
    "Entity",
    "EntityIdentifier",
    "EntityFacebook",
    "EntityLinkedin",
    "EntityLocationGroupIdentifier",
    "EntityLocationIdentifier",
    "EntityPrimaryOrganization",
    "EntityTwitter",
    "EntityWebsite",
]


class EntityIdentifier(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityFacebook(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class EntityLinkedin(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class EntityLocationGroupIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class EntityLocationIdentifier(BaseModel):
    entity_def_id: str
    """What type of entity this be"""

    uuid: str
    """Globally unique id of this entity"""

    image_id: Optional[str] = None
    """Optionally provided location to obtain an image representing this entity"""

    location_type: Optional[Literal["city", "region", "country", "continent", "group"]] = None

    permalink: Optional[str] = None
    """Optionally provided within Entity Def unique nice id of this entity"""

    value: Optional[str] = None
    """Textual representation of this entity (i.e. its "name")"""


class EntityPrimaryOrganization(BaseModel):
    entity_def_id: str

    uuid: str
    """a wild uuid!"""

    image_id: Optional[str] = None

    permalink: Optional[str] = None

    value: Optional[str] = None


class EntityTwitter(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class EntityWebsite(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None


class Entity(BaseModel):
    identifier: EntityIdentifier
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    aliases: Optional[List[str]] = None
    """Alternate or previous names for the individual"""

    born_on: Optional[date] = None
    """The birthdate of the person"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Text from a Person's biography"""

    died_on: Optional[date] = None
    """The date when a person died"""

    entity_def_id: Optional[str] = None
    """- person - Person"""

    facebook: Optional[EntityFacebook] = None
    """An object representing both the url and some labeling text for that url"""

    facet_ids: Optional[List[str]] = None

    first_name: Optional[str] = None
    """First name of a Person"""

    gender: Optional[str] = None
    """A Person's gender

    - agender - Agender
    - androgyne - Androgyne
    - androgynous - Androgynous
    - bigender - Bigender
    - female - Female
    - ftm - Female to Male (FTM)
    - gender_fluid - Gender Fluid
    - gender_nonconforming - Gender Nonconforming
    - gender_questioning - Gender Questioning
    - gender_variant - Gender Variant
    - genderqueer - Genderqueer
    - male - Male
    - mtf - Male to Female (MTF)
    - neutrois - Neutrois
    - non_binary - Non-Binary
    - not_provided - Prefer not to identify
    - other - Other
    - pangender - Pangender
    - transfeminine - Transfeminine
    - transgender_female - Transgender Female
    - transgender_male - Transgender Male
    - transgender_man - Transgender Man
    - transgender_person - Transgender Person
    - transgender_woman - Transgender Woman
    - transmasculine - Transmasculine
    - transsexual_female - Transsexual Female
    - transsexual_male - Transsexual Male
    - transsexual_man - Transsexual Man
    - transsexual_person - Transsexual Person
    - transsexual_woman - Transsexual Woman
    - two_spirit - Two-Spirit
    """

    image_id: Optional[str] = None
    """The profile image of the person on Crunchbase"""

    image_url: Optional[str] = None
    """The url of the profile image"""

    investor_stage: Optional[List[str]] = None
    """This describes the stage of investor this person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    investor_type: Optional[List[str]] = None
    """This describes the type of investor the person is (e.g.

    Angel, Fund of Funds, Venture Capital)
    """

    last_name: Optional[str] = None
    """Last name of a Person"""

    layout_id: Optional[str] = None
    """This is the auto-generated layout for the profile

    - investor - Investor Layout
    """

    linkedin: Optional[EntityLinkedin] = None
    """An object representing both the url and some labeling text for that url"""

    location_group_identifiers: Optional[List[EntityLocationGroupIdentifier]] = None
    """Where the person is located (e.g. San Francisco Bay Area, Silicon Valley)"""

    location_identifiers: Optional[List[EntityLocationIdentifier]] = None
    """Where the person is located (e.g. Europe, Menlo Park, China)"""

    middle_name: Optional[str] = None
    """Middle name of a Person"""

    name: Optional[str] = None
    """Full name of a Person"""

    num_articles: Optional[float] = None
    """Number of news articles that reference the Person"""

    num_current_advisor_jobs: Optional[float] = None
    """Total number of current Advisors and Board roles the person has"""

    num_current_jobs: Optional[float] = None
    """Total number of current Jobs the person has"""

    num_diversity_spotlight_investments: Optional[float] = None
    """Total number of diversity investments made by an investor"""

    num_event_appearances: Optional[float] = None
    """Total number of events the individual appeared in"""

    num_exits: Optional[float] = None
    """Total number of Exits"""

    num_exits_ipo: Optional[float] = None
    """Total number of Exits (IPO)"""

    num_founded_organizations: Optional[float] = None
    """Number of Organizations that the person founded"""

    num_investments: Optional[float] = None
    """Number of Investments the Individual has participated in"""

    num_jobs: Optional[float] = None

    num_lead_investments: Optional[float] = None
    """Number of Investments led by the Individual"""

    num_partner_investments: Optional[float] = None
    """Number of Investments the Individual has partnered in"""

    num_past_advisor_jobs: Optional[float] = None
    """Total number of past Board and Advisor roles the person has"""

    num_past_jobs: Optional[float] = None
    """Total number of past Jobs the person has"""

    num_portfolio_organizations: Optional[float] = None
    """Number of portfolio companies associated to the Person"""

    permalink: Optional[str] = None

    permalink_aliases: Optional[List[str]] = None
    """These are the alternative aliases to the primary permalink of the Organization"""

    primary_job_title: Optional[str] = None
    """The person's primary job title"""

    primary_organization: Optional[EntityPrimaryOrganization] = None
    """
    Every entity in the system has a unique identifier that contains all necessary
    properties to represent it.
    """

    rank: Optional[float] = None
    """Algorithmic rank assigned to the top profiles on Crunchbase"""

    rank_delta_d30: Optional[float] = None
    """Movement in Rank over the last 30 days using a score from -10 to 10"""

    rank_delta_d7: Optional[float] = None
    """Movement in Rank over the last 7 days using a score from -10 to 10"""

    rank_delta_d90: Optional[float] = None
    """Movement in Rank over the last 90 days using a score from -10 to 10"""

    rank_person: Optional[float] = None
    """Algorithmic rank assigned to the top 100,000 most active People"""

    short_description: Optional[str] = None
    """Text of Person Description, Industries, and Industry Groups"""

    twitter: Optional[EntityTwitter] = None
    """An object representing both the url and some labeling text for that url"""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    website: Optional[EntityWebsite] = None
    """An object representing both the url and some labeling text for that url"""

    website_url: Optional[str] = None
    """Link to a Person's website"""


class PersonCreateResponse(BaseModel):
    count: Optional[int] = None
    """Total number of Person entities"""

    entities: Optional[List[Entity]] = None
