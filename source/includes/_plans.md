## Plans
> example fetching information for plans in Texas:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/plans/?state=TX
```

```python
client.plans(state='TX')
```

```csharp
client.plans(
	new Dictionary<string, string> {
		{ "state", "TX" }
	}
);
```

```ruby
client.plans({state: 'TX'})
```

```java
HashMap<String, String> query = new HashMap<String, String>();
query.put("state", "TX");

client.plans(query);
```

```swift
let data = [
    "state": "TX"
] as [String:Any]
try client.plans(params: data)
```

> example fetching information for PPO plans in South Carolina:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/plans/?state=SC&plan_type=PPO
```

```python
client.plans(state='SC', plan_type='PPO')
```

```csharp
client.plans(
			new Dictionary<string, string> {
				{ "state", "TX" },
				{ "plan_type", "PPO" }
			}
		);
```

```ruby
client.plans({state: 'SC', plan_type: 'PPO'})
```

```java
HashMap<String, String> query = new HashMap<String, String>();
query.put("state", "TX");
query.put("plan_type", "PPO");

client.plans(query);
```

```swift
let data = [
    "state": "TX",
    "plan_type": "PPO"
] as [String:Any]
try client.plans(params: data)
```

> The plans endpoint will return an array of plan objects dependent on your query. The following is an incomplete example of response json for one plan object. If you would like a more complete example of the plans endpoint entire response json it is recommended you use the test application.

```json
{
  "benefits_summary_url": "http://www.bcbstx.com/coverage/individual/on-exchange/",
  "county": "Anderson",
  "customer_service_phone": "1-888-697-0683",
  "deductible": {
    "family": 9750.0,
    "individual": 3250.0
  },
  "max_out_of_pocket": {
    "family": 9750.0,
    "individual": 3250.0
  },
  "metallic_level": "gold",
  "plan_id": "33602TX0420001",
  "plan_name": "Blue Choice Gold PPO? 001",
  "plan_type": "PPO",
  "premiums": [
    {
      "adults": 1,
      "age": 21,
      "children": 0,
      "cost": 307.03
    }
  ],
  "public_exchange": true,
  "state": "TX",
  "trading_partner_id": "blue_cross_and_blue_shield_texas"
}
``` 

*Available modes of operation: real-time*

The Plans endpoint provides access to information about insurance plans.
The plans returned are those currently available through the federal exchange.
Additional plans may be added later.

### Endpoint Description

<!--- beginning of table -->

| Endpoint | HTTP Method | Description                       |
|:---------|:------------|:----------------------------------|
| /plans/  | GET         | Search insurance plan information |

<!--- end of table -->

### Response

The `/plans/` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter          | Description                                           										 | Presence |
|:-------------------|:----------------------------------------------------------------------------------------------|:---------|
| trading_partner_id | The trading partner id of the payer offering the plan 										 | Optional |
| issuer_name        | The plan issuer name (trading partner full name)        										 | Optional |
| county             | The county in which the plan is available             										 | Optional |
| state              | The state in which the plan is available              										 | Optional |
| plan_id            | The identifier for the plan                           										 | Optional |
| plan_type          | The type of plan (e.g. EPO, PPO, HMO, POS)            										 | Optional |
| plan_name          | The name of the plan                                  										 | Optional |
| metallic_level     | The metal level of the plan. A list of possible values can be found [below](#metallic_level). | Optional |

<!--- end of table -->

### Parameters

The `/plans/` response contains the following fields:

<!--- beginning of table -->

| Field                        | Type     | Description                                                                           | Presence |
|:-----------------------------|:---------|:--------------------------------------------------------------------------------------|:---------|
| benefits_summary_url         | {string} | URL to benefit summary information for the plan                                       | Required |
| customer_service_phone       | {string} | The customer service phone number for the plan                                        | Required |
| deductible                   | {object} | The deductible amounts for individual and family coverage (when available)            | Optional |
| deductible.individual        | {float}  | The deductible amount for individual coverage (when available)                        | Optional |
| deductible.family            | {float}  | The deductible amount for family coverage (when available)                            | Optional |
| max_out_of_pocket            | {object} | The maximum out of pocket amounts for individual and family coverage (when available) | Optional |
| max_out_of_pocket.individual | {float}  | The maximum out of pocket amount for individual coverage (when available)             | Optional |
| max_out_of_pocket.family     | {float}  | The maximum out of pocket amount for family coverage (when available)                 | Optional |
| metallic_level               | {string} | The metal level for marketplace plans (e.g.: bronze, silver, gold, and platinum)      | Required |
| plan_id                      | {string} | The ID assigned to the plan by the issuer                                             | Required |
| plan_name                    | {string} | Full name of the insurance plan                                                       | Required |
| public_exchange              | {boolean}| Whether or not the plan is offered on a public exchange                               | Required |
| plan_type                    | {string} | The type of the plan (e.g.: PPO, HMO, EPO, etc.)                                      | Required |
| premiums                     | {array}  | A list of monthly premium information for the plan (when available)                   | Required |
| premiums.age                 | {int}    | The age of the insurance subscriber                                                   | Required |
| premiums.adults              | {int}    | Number of adults covered on the plan                                                  | Required |
| premiums.children            | {int}    | Number of children covered on the plan                                                | Required |
| premiums.cost                | {float}  | The monthly premium cost for the plan                                                 | Required |
| state                        | {string} | The state where the plan is offered (e.g.: CA, SC, etc.)                              | Required |
| county                       | {string} | The county in which the plan is available   	  	                                  | Required |
| trading_partner_id           | {string} | The trading partner id for the issuer of the plan                                     | Required |
| emergency_room               | {object} | Emergency room cost-sharing object [below](#cost-sharing-object)                      | Optional |
| generic_drugs                | {object} | Generic drugs cost-sharing object  [below](#cost-sharing-object)                      | Optional |
| inpatient_facility           | {object} | Inpatient facility cost-sharing object [below](#cost-sharing-object)                  | Optional |
| inpatient_physician          | {object} | Inpatient physician cost-sharing object [below](#cost-sharing-object)                 | Optional |
| non_preferred_brand_drugs    | {object} | Non-preferred brand drugs cost-sharing object [below](#cost-sharing-object)           | Optional |
| preferred_brand_drugs        | {object} | Preferred brand drugs cost-sharing object [below](#cost-sharing-object)               | Optional |
| primary_care_physician       | {object} | Primary care physician cost-sharing object [below](#cost-sharing-object)              | Optional |
| specialist                   | {object} | Specialist cost-sharing object [below](#cost-sharing-object)                          | Optional |
| specialty_drugs              | {object} | Specialty drugs cost-sharing object [below](#cost-sharing-object)                     | Optional |

<!--- end of table -->


### Additional Object Tables

<a name="cost-sharing-object"></a>
(The silver plan variants below differ from the standard plan by the percentage of health care expenses covered by the plan for a typical group of enrollees (i.e., actuarial value))

<!--- beginning of table -->

| Field           | Description                                |
|:----------------|:-------------------------------------------|
| standard        | Standard copay and/or co-insurance amounts |
| percent_73      | 73 percent silver plan variant             |
| percent_87      | 87 percent silver plan variant             |
| percent_94      | 94 percent silver plan variant             |

<!--- end of table -->

<a name="metallic_level"></a>
Possible values that can be used in the `metallic_level` parameter:

<!--- beginning of table -->

| metallic_level     |                 |
|:-------------------|:----------------|
| bronze   	         | silver          |
| gold               | platinum        |
| catastrophic       |                 |

<!--- end of table -->