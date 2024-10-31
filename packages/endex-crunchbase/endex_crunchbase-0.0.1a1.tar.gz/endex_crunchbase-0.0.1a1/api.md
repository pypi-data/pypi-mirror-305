# Entities

## Organizations

Types:

```python
from endex_crunchbase.types.entities import OrganizationRetrieveResponse
```

Methods:

- <code title="get /data/entities/organizations/{entity_id}">client.entities.organizations.<a href="./src/endex_crunchbase/resources/entities/organizations/organizations.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/organization_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/organization_retrieve_response.py">OrganizationRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.organizations import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/organizations/{entity_id}/cards/{card_id}">client.entities.organizations.cards.<a href="./src/endex_crunchbase/resources/entities/organizations/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/organizations/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/organizations/card_retrieve_response.py">CardRetrieveResponse</a></code>

## People

Types:

```python
from endex_crunchbase.types.entities import PersonRetrieveResponse
```

Methods:

- <code title="get /data/entities/people/{entity_id}">client.entities.people.<a href="./src/endex_crunchbase/resources/entities/people/people.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/person_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/person_retrieve_response.py">PersonRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.people import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/people/{entity_id}/cards/{card_id}">client.entities.people.cards.<a href="./src/endex_crunchbase/resources/entities/people/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/people/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/people/card_retrieve_response.py">CardRetrieveResponse</a></code>

## FundingRounds

Types:

```python
from endex_crunchbase.types.entities import FundingRoundRetrieveResponse
```

Methods:

- <code title="get /data/entities/funding_rounds/{entity_id}">client.entities.funding_rounds.<a href="./src/endex_crunchbase/resources/entities/funding_rounds/funding_rounds.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/funding_round_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/funding_round_retrieve_response.py">FundingRoundRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.funding_rounds import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/funding_rounds/{entity_id}/cards/{card_id}">client.entities.funding_rounds.cards.<a href="./src/endex_crunchbase/resources/entities/funding_rounds/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/funding_rounds/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/funding_rounds/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Acquisitions

Types:

```python
from endex_crunchbase.types.entities import AcquisitionRetrieveResponse
```

Methods:

- <code title="get /data/entities/acquisitions/{entity_id}">client.entities.acquisitions.<a href="./src/endex_crunchbase/resources/entities/acquisitions/acquisitions.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/acquisition_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/acquisition_retrieve_response.py">AcquisitionRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.acquisitions import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/acquisitions/{entity_id}/cards/{card_id}">client.entities.acquisitions.cards.<a href="./src/endex_crunchbase/resources/entities/acquisitions/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/acquisitions/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/acquisitions/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Investments

Types:

```python
from endex_crunchbase.types.entities import InvestmentRetrieveResponse
```

Methods:

- <code title="get /data/entities/investments/{entity_id}">client.entities.investments.<a href="./src/endex_crunchbase/resources/entities/investments/investments.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/investment_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/investment_retrieve_response.py">InvestmentRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.investments import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/investments/{entity_id}/cards/{card_id}">client.entities.investments.cards.<a href="./src/endex_crunchbase/resources/entities/investments/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/investments/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/investments/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Events

Types:

```python
from endex_crunchbase.types.entities import EventRetrieveResponse
```

Methods:

- <code title="get /data/entities/events/{entity_id}">client.entities.events.<a href="./src/endex_crunchbase/resources/entities/events/events.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/event_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/event_retrieve_response.py">EventRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.events import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/events/{entity_id}/cards/{card_id}">client.entities.events.cards.<a href="./src/endex_crunchbase/resources/entities/events/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/events/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/events/card_retrieve_response.py">CardRetrieveResponse</a></code>

## PressReferences

Types:

```python
from endex_crunchbase.types.entities import PressReferenceRetrieveResponse
```

Methods:

- <code title="get /data/entities/press_references/{entity_id}">client.entities.press_references.<a href="./src/endex_crunchbase/resources/entities/press_references/press_references.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/press_reference_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/press_reference_retrieve_response.py">PressReferenceRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.press_references import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/press_references/{entity_id}/cards/{card_id}">client.entities.press_references.cards.<a href="./src/endex_crunchbase/resources/entities/press_references/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/press_references/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/press_references/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Funds

Types:

```python
from endex_crunchbase.types.entities import FundRetrieveResponse
```

Methods:

- <code title="get /data/entities/funds/{entity_id}">client.entities.funds.<a href="./src/endex_crunchbase/resources/entities/funds/funds.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/fund_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/fund_retrieve_response.py">FundRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.funds import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/funds/{entity_id}/cards/{card_id}">client.entities.funds.cards.<a href="./src/endex_crunchbase/resources/entities/funds/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/funds/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/funds/card_retrieve_response.py">CardRetrieveResponse</a></code>

## EventAppearances

Types:

```python
from endex_crunchbase.types.entities import EventAppearanceRetrieveResponse
```

Methods:

- <code title="get /data/entities/event_appearances/{entity_id}">client.entities.event_appearances.<a href="./src/endex_crunchbase/resources/entities/event_appearances/event_appearances.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/event_appearance_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/event_appearance_retrieve_response.py">EventAppearanceRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.event_appearances import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/event_appearances/{entity_id}/cards/{card_id}">client.entities.event_appearances.cards.<a href="./src/endex_crunchbase/resources/entities/event_appearances/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/event_appearances/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/event_appearances/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Ipos

Types:

```python
from endex_crunchbase.types.entities import IpoRetrieveResponse
```

Methods:

- <code title="get /data/entities/ipos/{entity_id}">client.entities.ipos.<a href="./src/endex_crunchbase/resources/entities/ipos/ipos.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/ipo_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/ipo_retrieve_response.py">IpoRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.ipos import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/ipos/{entity_id}/cards/{card_id}">client.entities.ipos.cards.<a href="./src/endex_crunchbase/resources/entities/ipos/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/ipos/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/ipos/card_retrieve_response.py">CardRetrieveResponse</a></code>

## KeyEmployeeChanges

Types:

```python
from endex_crunchbase.types.entities import KeyEmployeeChangeRetrieveResponse
```

Methods:

- <code title="get /data/entities/key_employee_changes/{entity_id}">client.entities.key_employee_changes.<a href="./src/endex_crunchbase/resources/entities/key_employee_changes/key_employee_changes.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/key_employee_change_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/key_employee_change_retrieve_response.py">KeyEmployeeChangeRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.key_employee_changes import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/key_employee_changes/{entity_id}/cards/{card_id}">client.entities.key_employee_changes.cards.<a href="./src/endex_crunchbase/resources/entities/key_employee_changes/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/key_employee_changes/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/key_employee_changes/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Layoffs

Types:

```python
from endex_crunchbase.types.entities import LayoffRetrieveResponse
```

Methods:

- <code title="get /data/entities/layoffs/{entity_id}">client.entities.layoffs.<a href="./src/endex_crunchbase/resources/entities/layoffs/layoffs.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/layoff_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/layoff_retrieve_response.py">LayoffRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.layoffs import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/layoffs/{entity_id}/cards/{card_id}">client.entities.layoffs.cards.<a href="./src/endex_crunchbase/resources/entities/layoffs/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/layoffs/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/layoffs/card_retrieve_response.py">CardRetrieveResponse</a></code>

## AcquisitionPredictions

Types:

```python
from endex_crunchbase.types.entities import AcquisitionPredictionRetrieveResponse
```

Methods:

- <code title="get /data/entities/acquisition_predictions/{entity_id}">client.entities.acquisition_predictions.<a href="./src/endex_crunchbase/resources/entities/acquisition_predictions/acquisition_predictions.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/acquisition_prediction_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/acquisition_prediction_retrieve_response.py">AcquisitionPredictionRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.acquisition_predictions import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/acquisition_predictions/{entity_id}/cards/{card_id}">client.entities.acquisition_predictions.cards.<a href="./src/endex_crunchbase/resources/entities/acquisition_predictions/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/acquisition_predictions/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/acquisition_predictions/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Addresses

Types:

```python
from endex_crunchbase.types.entities import AddressRetrieveResponse
```

Methods:

- <code title="get /data/entities/addresses/{entity_id}">client.entities.addresses.<a href="./src/endex_crunchbase/resources/entities/addresses/addresses.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/address_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/address_retrieve_response.py">AddressRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.addresses import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/addresses/{entity_id}/cards/{card_id}">client.entities.addresses.cards.<a href="./src/endex_crunchbase/resources/entities/addresses/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/addresses/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/addresses/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Awards

Types:

```python
from endex_crunchbase.types.entities import AwardRetrieveResponse
```

Methods:

- <code title="get /data/entities/awards/{entity_id}">client.entities.awards.<a href="./src/endex_crunchbase/resources/entities/awards/awards.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/award_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/award_retrieve_response.py">AwardRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.awards import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/awards/{entity_id}/cards/{card_id}">client.entities.awards.cards.<a href="./src/endex_crunchbase/resources/entities/awards/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/awards/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/awards/card_retrieve_response.py">CardRetrieveResponse</a></code>

## InvestorInsights

Types:

```python
from endex_crunchbase.types.entities import InvestorInsightRetrieveResponse
```

Methods:

- <code title="get /data/entities/investor_insights/{entity_id}">client.entities.investor_insights.<a href="./src/endex_crunchbase/resources/entities/investor_insights/investor_insights.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/investor_insight_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/investor_insight_retrieve_response.py">InvestorInsightRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.investor_insights import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/investor_insights/{entity_id}/cards/{card_id}">client.entities.investor_insights.cards.<a href="./src/endex_crunchbase/resources/entities/investor_insights/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/investor_insights/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/investor_insights/card_retrieve_response.py">CardRetrieveResponse</a></code>

## IpoPredictions

Types:

```python
from endex_crunchbase.types.entities import IpoPredictionRetrieveResponse
```

Methods:

- <code title="get /data/entities/ipo_predictions/{entity_id}">client.entities.ipo_predictions.<a href="./src/endex_crunchbase/resources/entities/ipo_predictions/ipo_predictions.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/ipo_prediction_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/ipo_prediction_retrieve_response.py">IpoPredictionRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.ipo_predictions import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/ipo_predictions/{entity_id}/cards/{card_id}">client.entities.ipo_predictions.cards.<a href="./src/endex_crunchbase/resources/entities/ipo_predictions/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/ipo_predictions/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/ipo_predictions/card_retrieve_response.py">CardRetrieveResponse</a></code>

## LegalProceedings

Types:

```python
from endex_crunchbase.types.entities import LegalProceedingRetrieveResponse
```

Methods:

- <code title="get /data/entities/legal_proceedings/{entity_id}">client.entities.legal_proceedings.<a href="./src/endex_crunchbase/resources/entities/legal_proceedings/legal_proceedings.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/legal_proceeding_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/legal_proceeding_retrieve_response.py">LegalProceedingRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.legal_proceedings import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/legal_proceedings/{entity_id}/cards/{card_id}">client.entities.legal_proceedings.cards.<a href="./src/endex_crunchbase/resources/entities/legal_proceedings/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/legal_proceedings/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/legal_proceedings/card_retrieve_response.py">CardRetrieveResponse</a></code>

## PartnershipAnnouncements

Types:

```python
from endex_crunchbase.types.entities import PartnershipAnnouncementRetrieveResponse
```

Methods:

- <code title="get /data/entities/partnership_announcements/{entity_id}">client.entities.partnership_announcements.<a href="./src/endex_crunchbase/resources/entities/partnership_announcements/partnership_announcements.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/partnership_announcement_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/partnership_announcement_retrieve_response.py">PartnershipAnnouncementRetrieveResponse</a></code>

### Cards

Types:

```python
from endex_crunchbase.types.entities.partnership_announcements import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/partnership_announcements/{entity_id}/cards/{card_id}">client.entities.partnership_announcements.cards.<a href="./src/endex_crunchbase/resources/entities/partnership_announcements/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/entities/partnership_announcements/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/partnership_announcements/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Principals

Types:

```python
from endex_crunchbase.types.entities import PrincipalRetrieveResponse
```

Methods:

- <code title="get /data/entities/principals/{entity_id}">client.entities.principals.<a href="./src/endex_crunchbase/resources/entities/principals.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/principal_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/principal_retrieve_response.py">PrincipalRetrieveResponse</a></code>

## Products

Types:

```python
from endex_crunchbase.types.entities import ProductRetrieveResponse
```

Methods:

- <code title="get /data/entities/products/{entity_id}">client.entities.products.<a href="./src/endex_crunchbase/resources/entities/products.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/entities/product_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/entities/product_retrieve_response.py">ProductRetrieveResponse</a></code>

# Data

## Entities

### Ownerships

Types:

```python
from endex_crunchbase.types.data.entities import OwnershipRetrieveResponse
```

Methods:

- <code title="get /data/entities/ownerships/{entity_id}">client.data.entities.ownerships.<a href="./src/endex_crunchbase/resources/data/entities/ownerships/ownerships.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/ownership_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/ownership_retrieve_response.py">OwnershipRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.ownerships import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/ownerships/{entity_id}/cards/{card_id}">client.data.entities.ownerships.cards.<a href="./src/endex_crunchbase/resources/data/entities/ownerships/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/ownerships/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/ownerships/card_retrieve_response.py">CardRetrieveResponse</a></code>

### Categories

Types:

```python
from endex_crunchbase.types.data.entities import CategoryRetrieveResponse
```

Methods:

- <code title="get /data/entities/categories/{entity_id}">client.data.entities.categories.<a href="./src/endex_crunchbase/resources/data/entities/categories/categories.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/category_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/category_retrieve_response.py">CategoryRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.categories import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/categories/{entity_id}/cards/{card_id}">client.data.entities.categories.cards.<a href="./src/endex_crunchbase/resources/data/entities/categories/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/categories/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/categories/card_retrieve_response.py">CardRetrieveResponse</a></code>

### CategoryGroups

Types:

```python
from endex_crunchbase.types.data.entities import CategoryGroupRetrieveResponse
```

Methods:

- <code title="get /data/entities/category_groups/{entity_id}">client.data.entities.category_groups.<a href="./src/endex_crunchbase/resources/data/entities/category_groups/category_groups.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/category_group_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/category_group_retrieve_response.py">CategoryGroupRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.category_groups import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/category_groups/{entity_id}/cards/{card_id}">client.data.entities.category_groups.cards.<a href="./src/endex_crunchbase/resources/data/entities/category_groups/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/category_groups/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/category_groups/card_retrieve_response.py">CardRetrieveResponse</a></code>

### Locations

Types:

```python
from endex_crunchbase.types.data.entities import LocationRetrieveResponse
```

Methods:

- <code title="get /data/entities/locations/{entity_id}">client.data.entities.locations.<a href="./src/endex_crunchbase/resources/data/entities/locations/locations.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/location_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/location_retrieve_response.py">LocationRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.locations import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/locations/{entity_id}/cards/{card_id}">client.data.entities.locations.cards.<a href="./src/endex_crunchbase/resources/data/entities/locations/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/locations/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/locations/card_retrieve_response.py">CardRetrieveResponse</a></code>

### Jobs

Types:

```python
from endex_crunchbase.types.data.entities import JobRetrieveResponse
```

Methods:

- <code title="get /data/entities/jobs/{entity_id}">client.data.entities.jobs.<a href="./src/endex_crunchbase/resources/data/entities/jobs/jobs.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/job_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/job_retrieve_response.py">JobRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.jobs import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/jobs/{entity_id}/cards/{card_id}">client.data.entities.jobs.cards.<a href="./src/endex_crunchbase/resources/data/entities/jobs/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/jobs/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/jobs/card_retrieve_response.py">CardRetrieveResponse</a></code>

### ClosurePredictions

Types:

```python
from endex_crunchbase.types.data.entities import ClosurePredictionRetrieveResponse
```

Methods:

- <code title="get /data/entities/closure_predictions/{entity_id}">client.data.entities.closure_predictions.<a href="./src/endex_crunchbase/resources/data/entities/closure_predictions/closure_predictions.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/closure_prediction_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/closure_prediction_retrieve_response.py">ClosurePredictionRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.closure_predictions import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/closure_predictions/{entity_id}/cards/{card_id}">client.data.entities.closure_predictions.cards.<a href="./src/endex_crunchbase/resources/data/entities/closure_predictions/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/closure_predictions/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/closure_predictions/card_retrieve_response.py">CardRetrieveResponse</a></code>

### Degrees

Types:

```python
from endex_crunchbase.types.data.entities import DegreeRetrieveResponse
```

Methods:

- <code title="get /data/entities/degrees/{entity_id}">client.data.entities.degrees.<a href="./src/endex_crunchbase/resources/data/entities/degrees/degrees.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/degree_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/degree_retrieve_response.py">DegreeRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.degrees import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/degrees/{entity_id}/cards/{card_id}">client.data.entities.degrees.cards.<a href="./src/endex_crunchbase/resources/data/entities/degrees/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/degrees/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/degrees/card_retrieve_response.py">CardRetrieveResponse</a></code>

### DiversitySpotlights

Types:

```python
from endex_crunchbase.types.data.entities import DiversitySpotlightRetrieveResponse
```

Methods:

- <code title="get /data/entities/diversity_spotlights/{entity_id}">client.data.entities.diversity_spotlights.<a href="./src/endex_crunchbase/resources/data/entities/diversity_spotlights/diversity_spotlights.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/diversity_spotlight_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/diversity_spotlight_retrieve_response.py">DiversitySpotlightRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.diversity_spotlights import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/diversity_spotlights/{entity_id}/cards/{card_id}">client.data.entities.diversity_spotlights.cards.<a href="./src/endex_crunchbase/resources/data/entities/diversity_spotlights/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/diversity_spotlights/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/diversity_spotlights/card_retrieve_response.py">CardRetrieveResponse</a></code>

### FundingPredictions

Types:

```python
from endex_crunchbase.types.data.entities import FundingPredictionRetrieveResponse
```

Methods:

- <code title="get /data/entities/funding_predictions/{entity_id}">client.data.entities.funding_predictions.<a href="./src/endex_crunchbase/resources/data/entities/funding_predictions/funding_predictions.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/funding_prediction_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/funding_prediction_retrieve_response.py">FundingPredictionRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.funding_predictions import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/funding_predictions/{entity_id}/cards/{card_id}">client.data.entities.funding_predictions.cards.<a href="./src/endex_crunchbase/resources/data/entities/funding_predictions/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/funding_predictions/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/funding_predictions/card_retrieve_response.py">CardRetrieveResponse</a></code>

### GrowthInsights

Types:

```python
from endex_crunchbase.types.data.entities import GrowthInsightRetrieveResponse
```

Methods:

- <code title="get /data/entities/growth_insights/{entity_id}">client.data.entities.growth_insights.<a href="./src/endex_crunchbase/resources/data/entities/growth_insights/growth_insights.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/growth_insight_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/growth_insight_retrieve_response.py">GrowthInsightRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.growth_insights import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/growth_insights/{entity_id}/cards/{card_id}">client.data.entities.growth_insights.cards.<a href="./src/endex_crunchbase/resources/data/entities/growth_insights/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/growth_insights/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/growth_insights/card_retrieve_response.py">CardRetrieveResponse</a></code>

### Products

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.products import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/products/{entity_id}/cards/{card_id}">client.data.entities.products.cards.<a href="./src/endex_crunchbase/resources/data/entities/products/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/products/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/products/card_retrieve_response.py">CardRetrieveResponse</a></code>

### ProductLaunches

Types:

```python
from endex_crunchbase.types.data.entities import ProductLaunchRetrieveResponse
```

Methods:

- <code title="get /data/entities/product_launches/{entity_id}">client.data.entities.product_launches.<a href="./src/endex_crunchbase/resources/data/entities/product_launches/product_launches.py">retrieve</a>(entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/product_launch_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/product_launch_retrieve_response.py">ProductLaunchRetrieveResponse</a></code>

#### Cards

Types:

```python
from endex_crunchbase.types.data.entities.product_launches import CardRetrieveResponse
```

Methods:

- <code title="get /data/entities/product_launches/{entity_id}/cards/{card_id}">client.data.entities.product_launches.cards.<a href="./src/endex_crunchbase/resources/data/entities/product_launches/cards.py">retrieve</a>(card_id, \*, entity_id, \*\*<a href="src/endex_crunchbase/types/data/entities/product_launches/card_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/entities/product_launches/card_retrieve_response.py">CardRetrieveResponse</a></code>

## Searches

### Organizations

Types:

```python
from endex_crunchbase.types.data.searches import OrganizationCreateResponse
```

Methods:

- <code title="post /data/searches/organizations">client.data.searches.organizations.<a href="./src/endex_crunchbase/resources/data/searches/organizations.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/organization_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/organization_create_response.py">OrganizationCreateResponse</a></code>

### People

Types:

```python
from endex_crunchbase.types.data.searches import PersonCreateResponse
```

Methods:

- <code title="post /data/searches/people">client.data.searches.people.<a href="./src/endex_crunchbase/resources/data/searches/people.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/person_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/person_create_response.py">PersonCreateResponse</a></code>

### FundingRounds

Types:

```python
from endex_crunchbase.types.data.searches import FundingRoundCreateResponse
```

Methods:

- <code title="post /data/searches/funding_rounds">client.data.searches.funding_rounds.<a href="./src/endex_crunchbase/resources/data/searches/funding_rounds.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/funding_round_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/funding_round_create_response.py">FundingRoundCreateResponse</a></code>

### Acquisitions

Types:

```python
from endex_crunchbase.types.data.searches import AcquisitionCreateResponse
```

Methods:

- <code title="post /data/searches/acquisitions">client.data.searches.acquisitions.<a href="./src/endex_crunchbase/resources/data/searches/acquisitions.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/acquisition_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/acquisition_create_response.py">AcquisitionCreateResponse</a></code>

### Investments

Types:

```python
from endex_crunchbase.types.data.searches import InvestmentCreateResponse
```

Methods:

- <code title="post /data/searches/investments">client.data.searches.investments.<a href="./src/endex_crunchbase/resources/data/searches/investments.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/investment_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/investment_create_response.py">InvestmentCreateResponse</a></code>

### Events

Types:

```python
from endex_crunchbase.types.data.searches import EventCreateResponse
```

Methods:

- <code title="post /data/searches/events">client.data.searches.events.<a href="./src/endex_crunchbase/resources/data/searches/events.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/event_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/event_create_response.py">EventCreateResponse</a></code>

### PressReferences

Types:

```python
from endex_crunchbase.types.data.searches import PressReferenceCreateResponse
```

Methods:

- <code title="post /data/searches/press_references">client.data.searches.press_references.<a href="./src/endex_crunchbase/resources/data/searches/press_references.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/press_reference_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/press_reference_create_response.py">PressReferenceCreateResponse</a></code>

### Funds

Types:

```python
from endex_crunchbase.types.data.searches import FundCreateResponse
```

Methods:

- <code title="post /data/searches/funds">client.data.searches.funds.<a href="./src/endex_crunchbase/resources/data/searches/funds.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/fund_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/fund_create_response.py">FundCreateResponse</a></code>

### EventAppearances

Types:

```python
from endex_crunchbase.types.data.searches import EventAppearanceCreateResponse
```

Methods:

- <code title="post /data/searches/event_appearances">client.data.searches.event_appearances.<a href="./src/endex_crunchbase/resources/data/searches/event_appearances.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/event_appearance_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/event_appearance_create_response.py">EventAppearanceCreateResponse</a></code>

### Ipos

Types:

```python
from endex_crunchbase.types.data.searches import IpoCreateResponse
```

Methods:

- <code title="post /data/searches/ipos">client.data.searches.ipos.<a href="./src/endex_crunchbase/resources/data/searches/ipos.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/ipo_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/ipo_create_response.py">IpoCreateResponse</a></code>

### Ownerships

Types:

```python
from endex_crunchbase.types.data.searches import OwnershipCreateResponse
```

Methods:

- <code title="post /data/searches/ownerships">client.data.searches.ownerships.<a href="./src/endex_crunchbase/resources/data/searches/ownerships.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/ownership_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/ownership_create_response.py">OwnershipCreateResponse</a></code>

### Categories

Types:

```python
from endex_crunchbase.types.data.searches import CategoryCreateResponse
```

Methods:

- <code title="post /data/searches/categories">client.data.searches.categories.<a href="./src/endex_crunchbase/resources/data/searches/categories.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/category_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/category_create_response.py">CategoryCreateResponse</a></code>

### CategoryGroups

Types:

```python
from endex_crunchbase.types.data.searches import CategoryGroupCreateResponse
```

Methods:

- <code title="post /data/searches/category_groups">client.data.searches.category_groups.<a href="./src/endex_crunchbase/resources/data/searches/category_groups.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/category_group_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/category_group_create_response.py">CategoryGroupCreateResponse</a></code>

### Locations

Types:

```python
from endex_crunchbase.types.data.searches import LocationCreateResponse
```

Methods:

- <code title="post /data/searches/locations">client.data.searches.locations.<a href="./src/endex_crunchbase/resources/data/searches/locations.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/location_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/location_create_response.py">LocationCreateResponse</a></code>

### Jobs

Types:

```python
from endex_crunchbase.types.data.searches import JobCreateResponse
```

Methods:

- <code title="post /data/searches/jobs">client.data.searches.jobs.<a href="./src/endex_crunchbase/resources/data/searches/jobs.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/job_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/job_create_response.py">JobCreateResponse</a></code>

### KeyEmployeeChanges

Types:

```python
from endex_crunchbase.types.data.searches import KeyEmployeeChangeCreateResponse
```

Methods:

- <code title="post /data/searches/key_employee_changes">client.data.searches.key_employee_changes.<a href="./src/endex_crunchbase/resources/data/searches/key_employee_changes.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/key_employee_change_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/key_employee_change_create_response.py">KeyEmployeeChangeCreateResponse</a></code>

### Layoffs

Types:

```python
from endex_crunchbase.types.data.searches import LayoffCreateResponse
```

Methods:

- <code title="post /data/searches/layoffs">client.data.searches.layoffs.<a href="./src/endex_crunchbase/resources/data/searches/layoffs.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/layoff_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/layoff_create_response.py">LayoffCreateResponse</a></code>

### AcquisitionPredictions

Types:

```python
from endex_crunchbase.types.data.searches import AcquisitionPredictionCreateResponse
```

Methods:

- <code title="post /data/searches/acquisition_predictions">client.data.searches.acquisition_predictions.<a href="./src/endex_crunchbase/resources/data/searches/acquisition_predictions.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/acquisition_prediction_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/acquisition_prediction_create_response.py">AcquisitionPredictionCreateResponse</a></code>

### Addresses

Types:

```python
from endex_crunchbase.types.data.searches import AddressCreateResponse
```

Methods:

- <code title="post /data/searches/addresses">client.data.searches.addresses.<a href="./src/endex_crunchbase/resources/data/searches/addresses.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/address_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/address_create_response.py">AddressCreateResponse</a></code>

### Awards

Types:

```python
from endex_crunchbase.types.data.searches import AwardCreateResponse
```

Methods:

- <code title="post /data/searches/awards">client.data.searches.awards.<a href="./src/endex_crunchbase/resources/data/searches/awards.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/award_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/award_create_response.py">AwardCreateResponse</a></code>

### ClosurePredictions

Types:

```python
from endex_crunchbase.types.data.searches import ClosurePredictionCreateResponse
```

Methods:

- <code title="post /data/searches/closure_predictions">client.data.searches.closure_predictions.<a href="./src/endex_crunchbase/resources/data/searches/closure_predictions.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/closure_prediction_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/closure_prediction_create_response.py">ClosurePredictionCreateResponse</a></code>

### Degrees

Types:

```python
from endex_crunchbase.types.data.searches import DegreeCreateResponse
```

Methods:

- <code title="post /data/searches/degrees">client.data.searches.degrees.<a href="./src/endex_crunchbase/resources/data/searches/degrees.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/degree_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/degree_create_response.py">DegreeCreateResponse</a></code>

### DiversitySpotlights

Types:

```python
from endex_crunchbase.types.data.searches import DiversitySpotlightCreateResponse
```

Methods:

- <code title="post /data/searches/diversity_spotlights">client.data.searches.diversity_spotlights.<a href="./src/endex_crunchbase/resources/data/searches/diversity_spotlights.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/diversity_spotlight_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/diversity_spotlight_create_response.py">DiversitySpotlightCreateResponse</a></code>

### FundingPredictions

Types:

```python
from endex_crunchbase.types.data.searches import FundingPredictionCreateResponse
```

Methods:

- <code title="post /data/searches/funding_predictions">client.data.searches.funding_predictions.<a href="./src/endex_crunchbase/resources/data/searches/funding_predictions.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/funding_prediction_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/funding_prediction_create_response.py">FundingPredictionCreateResponse</a></code>

### GrowthInsights

Types:

```python
from endex_crunchbase.types.data.searches import GrowthInsightCreateResponse
```

Methods:

- <code title="post /data/searches/growth_insights">client.data.searches.growth_insights.<a href="./src/endex_crunchbase/resources/data/searches/growth_insights.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/growth_insight_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/growth_insight_create_response.py">GrowthInsightCreateResponse</a></code>

### InvestorInsights

Types:

```python
from endex_crunchbase.types.data.searches import InvestorInsightCreateResponse
```

Methods:

- <code title="post /data/searches/investor_insights">client.data.searches.investor_insights.<a href="./src/endex_crunchbase/resources/data/searches/investor_insights.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/investor_insight_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/investor_insight_create_response.py">InvestorInsightCreateResponse</a></code>

### IpoPredictions

Types:

```python
from endex_crunchbase.types.data.searches import IpoPredictionCreateResponse
```

Methods:

- <code title="post /data/searches/ipo_predictions">client.data.searches.ipo_predictions.<a href="./src/endex_crunchbase/resources/data/searches/ipo_predictions.py">create</a>(\*\*<a href="src/endex_crunchbase/types/data/searches/ipo_prediction_create_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/data/searches/ipo_prediction_create_response.py">IpoPredictionCreateResponse</a></code>

# Searches

Types:

```python
from endex_crunchbase.types import (
    SearchLegalProceedingsResponse,
    SearchPartnershipAnnouncementsResponse,
    SearchPrincipalsResponse,
    SearchProductLaunchesResponse,
    SearchProductsResponse,
)
```

Methods:

- <code title="post /data/searches/legal_proceedings">client.searches.<a href="./src/endex_crunchbase/resources/searches.py">legal_proceedings</a>(\*\*<a href="src/endex_crunchbase/types/search_legal_proceedings_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/search_legal_proceedings_response.py">SearchLegalProceedingsResponse</a></code>
- <code title="post /data/searches/partnership_announcements">client.searches.<a href="./src/endex_crunchbase/resources/searches.py">partnership_announcements</a>(\*\*<a href="src/endex_crunchbase/types/search_partnership_announcements_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/search_partnership_announcements_response.py">SearchPartnershipAnnouncementsResponse</a></code>
- <code title="post /data/searches/principals">client.searches.<a href="./src/endex_crunchbase/resources/searches.py">principals</a>(\*\*<a href="src/endex_crunchbase/types/search_principals_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/search_principals_response.py">SearchPrincipalsResponse</a></code>
- <code title="post /data/searches/product_launches">client.searches.<a href="./src/endex_crunchbase/resources/searches.py">product_launches</a>(\*\*<a href="src/endex_crunchbase/types/search_product_launches_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/search_product_launches_response.py">SearchProductLaunchesResponse</a></code>
- <code title="post /data/searches/products">client.searches.<a href="./src/endex_crunchbase/resources/searches.py">products</a>(\*\*<a href="src/endex_crunchbase/types/search_products_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/search_products_response.py">SearchProductsResponse</a></code>

# Autocompletes

Types:

```python
from endex_crunchbase.types import AutocompleteListResponse
```

Methods:

- <code title="get /data/autocompletes">client.autocompletes.<a href="./src/endex_crunchbase/resources/autocompletes.py">list</a>(\*\*<a href="src/endex_crunchbase/types/autocomplete_list_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/autocomplete_list_response.py">AutocompleteListResponse</a></code>

# DeletedEntities

Types:

```python
from endex_crunchbase.types import DeletedEntityRetrieveResponse, DeletedEntityListResponse
```

Methods:

- <code title="get /data/deleted_entities/{collection_id}">client.deleted_entities.<a href="./src/endex_crunchbase/resources/deleted_entities.py">retrieve</a>(collection_id, \*\*<a href="src/endex_crunchbase/types/deleted_entity_retrieve_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/deleted_entity_retrieve_response.py">DeletedEntityRetrieveResponse</a></code>
- <code title="get /data/deleted_entities">client.deleted_entities.<a href="./src/endex_crunchbase/resources/deleted_entities.py">list</a>(\*\*<a href="src/endex_crunchbase/types/deleted_entity_list_params.py">params</a>) -> <a href="./src/endex_crunchbase/types/deleted_entity_list_response.py">DeletedEntityListResponse</a></code>
