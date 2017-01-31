## Referrals

*Available modes of operation: batch/async or real-time*

The Referrals endpoint allows an application to request approval for a referral
to another health care provider.

Primary Care Physicians can enable their patients to receive the consult and services
of a specialist or specialist entity. This request will be sent to the reviewing
entity (e.g. Utilization Management Organization) for approval.

#### Available Referrals Endpoint

| Endpoint    | HTTP Method | Description                                                                |
|:------------|:------------|:---------------------------------------------------------------------------|
| /referrals/ | POST        | Submit a specialty care referral request to a trading partner for approval |

#### Accepted Parameters

The `/referrals/` endpoint uses the same object for both its parameters and response. Most of the fields below can be passed in via the request object. Some of the fields will be assigned internally and can be seen in the response object.

| Parameter                                     | Description                                                                                                                                                                                                                           |
|:----------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| client_id                                     | The unique identifier associated with the client making the eligibility request.                                                                                                                                                      |
| event                                         | The patient event that is being submitted for approval.                                                                                                                                                                               |
| event.category                                | The category of the event being submitted for review. For referrals to specialists, a category value of "specialty_care_review" should always be used.                                                                                |
| event.delivery.units                          | The units of services being requested.                                                                                                                                                                                                |
| event.delivery.sample_selection_modulus       | Specify the sampling frequency in terms of a modulus of the Unit of Measure, e.g., every fifth bag, every 1.5 minutes.                                                                                                                |
| event.delivery.delivery_frequency_code        | Code which specifies frequency by which services can be performed.                                                                                                                                                                    |
| event.delivery.delivery_pattern_time_code     | Code which specifies the time delivery pattern of the services.                                                                                                                                                                       |
| event.delivery.quantity                       | The quantity of services being requested.                                                                                                                                                                                             |
| event.delivery.quantity_qualifier             | The qualifier used to indicate the quantity type. (e.g. visits, month, hours, units, days)                                                                                                                                            |
| event.delivery.quantity                       | The quantity of services being requested.                                                                                                                                                                                             |
| event.delivery.quantity_qualifier             | The qualifier used to indicate the quantity type. (e.g. visits, month, hours, units, days)                                                                                                                                            |
| event.diagnoses                               | An array of diagnosis information related to the event.                                                                                                                                                                               |
| event.diagnoses.code                          | The diagnosis code. (e.g. H72.90)                                                                                                                                                                                                     |
| event.diagnoses.date                          | The date of the diagnosis. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                            |
| event.place_of_service                        | The location where health care services are rendered.                                                                                                                                                                                 |
| event.provider                                | Information about the provider being requested for this event. The object used for provider can be seen [below](#referral_service_review_provider_object).                                                                            |
| event.admission_date                          | The date the patient was admitted. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                    |
| event.discharge_date                          | The date the patient was discharged. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                  |
| event.review                                  | Information about the outcome of a health care services review.                                                                                                                                                                       |
| event.review.certification_action             | Indicates the outcome of the review. For example, "certified_in_total" will be returned when the event is certified/authorized.  A full list of possible values can be found [below](#referral_certaction).                           |
| event.review.certification_number             | The review certification/reference number.                                                                                                                                                                                            |
| event.review.decision_reason                  | If the event is not authorized, the reason for that decision.  A full list of possible values can be found [below](#referral_decision).                                                                                               |
| event.review.event_start_date                 | Effective date of referral. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                           |
| event.review.event_end_date                   | End date for referral. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                |
| event.review.second_surgical_opinion_required | Boolean of whether or not a second surgical opinion is required.                                                                                                                                                                      |
| event.type                                    | The type of service being requested. For example, a value of consultation would be used when referring to a specialist for an initial consultation.                                                                                   |
| event.start_date                              | Optional: The start date of the given event. For a single date, provide only event.start_date. For a date range, provide event.start_date and event.end_date. In ISO8601 format (YYYY-MM-DD).                                         |
| event.end_date                                | Optional: The end date of the given event. Only provide the end_date if the start_date is also given. In ISO8601 format (YYYY-MM-DD).                                                                                                 |
| follow_up_action                              | When a referral request is rejected, a follow up action will be provided to inform your application how to proceed. See the possibilities [below](#referral_follow_up_action).                                                        |
| patient                                       | The patient for the referral. The object used for the patient can be seen [below](#referral_service_review_member_object).                                                                                                            |
| originating_company_id                        | The id of the company where the request originated.                                                                                                                                                                                   |
| payer                                         | The information source providing referral information; i.e., the insurance company.                                                                                                                                                   |
| payer.organization_name                       | The payer's organization name.                                                                                                                                                                                                        |
| payer.id                                      | The payer's unique identifier.                                                                                                                                                                                                        |
| provider                                      | The requesting provider. The object used for provider can be seen [below](#referral_service_review_provider_object).                                                                                                                  |
| subscriber                                    | The subscriber for the referral. The object used for the subscriber can be seen [below](#referral_service_review_member_object).                                                                                                      |
| trading_partner_id                            | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.                                                                                                                       |
| valid_request                                 | A boolean of whether or not the request was valid.                                                                                                                                                                                    |

#### Example Requests

> Here's an example referral request to an Otolaryngologist (ENT) by a primary
care physician. In this example, the patient is also the subscriber on the
insurance policy.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "event": {
        "category": "specialty_care_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "H72.90",
                "date": "2014-09-25"
            }
        ],
        "place_of_service": "office",
        "provider": {
            "first_name": "JOHN",
            "npi": "1154387751",
            "last_name": "FOSTER",
            "phone": "8645822900"
        },
        "type": "consultation"
    },
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "CHRISTINA",
        "last_name": "BERTOLAMI",
        "npi": "1619131232"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/referrals/
```

```python
client.referrals({
    "event": {
        "category": "specialty_care_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "H72.90",
                "date": "2014-09-25"
            }
        ],
        "place_of_service": "office",
        "provider": {
            "first_name": "JOHN",
            "npi": "1154387751",
            "last_name": "FOSTER",
            "phone": "8645822900"
        },
        "type": "consultation"
    },
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "CHRISTINA",
        "last_name": "BERTOLAMI",
        "npi": "1619131232"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
 client.referrals(
			new Dictionary<string, object> {
				{"event", new Dictionary<string, object> {
						{"category", "specialty_care_review"},
						{"certification_type", "initial"},
						{"delivery", new Dictionary<string, object> {
							{"quantity", 1},
							{"quantity_qualifier", "visits"}
							}},
						{"diagnoses", new Dictionary<string, string>[] {
							new Dictionary<string, string> {
								{"code", "H72.90"},
								{"date", "2014-09-25"}
							}}},
						{"place_of_service", "office"},
						{"provider", new Dictionary<string, string> {
							{"first_name", "JOHN"},
							{"npi", "1154387751"},
							{"last_name", "FOSTER"},
							{"phone", "8645822900"}
							}},
						{"type", "consultation"},
					}},
				{"patient", new Dictionary<string, string> {
						{"birth_date", "1970-01-25"},
						{"first_name", "JANE"},
						{"last_name", "DOE"},
						{"id", "1234567890"}
					}},
				{"provider", new Dictionary<string, string> {
						{"first_name", "CHRISTINA"},
						{"last_name", "BERTOLAMI"},
						{"npi", "1619131232"}
					}},
				{"trading_partner_id", "MOCKPAYER"}
			});
```

```ruby
client.referrals({
    event: {
        category: "specialty_care_review",
        certification_type: "initial",
        delivery: {
            quantity: 1,
            quantity_qualifier: "visits"
        },
        diagnoses: [
            {
                code: "H72.90",
                date: "2014-09-25"
            }
        ],
        place_of_service: "office",
        provider: {
            first_name: "JOHN",
            npi: "1154387751",
            last_name: "FOSTER",
            phone: "8645822900"
        },
        type: "consultation"
    },
    patient: {
        birth_date: "1970-01-25",
        first_name: "JANE",
        last_name: "DOE",
        id: "1234567890"
    },
    provider: {
        first_name: "CHRISTINA",
        last_name: "BERTOLAMI",
        npi: "1619131232"
    },
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"event\": {");
buf.append("        \"category\": \"specialty_care_review\",");
buf.append("        \"certification_type\": \"initial\",");
buf.append("        \"delivery\": {");
buf.append("            \"quantity\": 1,");
buf.append("            \"quantity_qualifier\": \"visits\"");
buf.append("        },");
buf.append("        \"diagnoses\": [");
buf.append("            {");
buf.append("                \"code\": \"H72.90\",");
buf.append("                \"date\": \"2014-09-25\"");
buf.append("            }");
buf.append("        ],");
buf.append("        \"place_of_service\": \"office\",");
buf.append("        \"provider\": {");
buf.append("            \"first_name\": \"JOHN\",");
buf.append("            \"npi\": \"1154387751\",");
buf.append("            \"last_name\": \"FOSTER\",");
buf.append("            \"phone\": \"8645822900\"");
buf.append("        },");
buf.append("        \"type\": \"consultation\"");
buf.append("    },");
buf.append("    \"patient\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"JANE\",");
buf.append("        \"last_name\": \"DOE\",");
buf.append("        \"id\": \"1234567890\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"CHRISTINA\",");
buf.append("        \"last_name\": \"BERTOLAMI\",");
buf.append("        \"npi\": \"1619131232\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.referrals(query);
```

```swift
let data = [
    "event": [
        "category": "specialty_care_review",
        "certification_type": "initial",
        "delivery": [
            "quantity": 1,
            "quantity_qualifier": "visits"
        ],
        "diagnoses": [
            [
                "code": "H72.90",
                "date": "2014-09-25"
            ]
        ],
        "place_of_service": "office",
        "provider": [
            "first_name": "JOHN",
            "npi": "1154387751",
            "last_name": "FOSTER",
            "phone": "8645822900"
        ],
        "type": "consultation"
    ],
    "patient": [
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    ],
    "provider": [
        "first_name": "CHRISTINA",
        "last_name": "BERTOLAMI",
        "npi": "1619131232"
    ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.referrals(params: data)
```

If the referral request is sent using a real-time interface, a referral response will be returned.

Interested in requesting authorization for a particular service for a patient? See PokitDok’s API Reference for the
Authorizations endpoint.

#### Referals Fields

<a name="referral_service_review_member_object"></a>
##### Member object:

| Field                             | Description                                                                           |
|:----------------------------------|:--------------------------------------------------------------------------------------|
| birth_date                        | The member’s birth date as specified on their policy. In ISO8601 format (YYYY-MM-DD). |
| gender                            | The member's gender (Male, Female, Unknown)                                           |
| last_name                         | The member’s last name as specified on their policy.                                  |
| first_name                        | The member’s first name as specified on their policy.                                 |
| middle_name                       | The member’s middle name as specified on their policy.                                |
| suffix                            | The suffix for the member                                                             |
| id                                | The member identifier.                                                                |
| last_menstrual_date               | The last menstrual date of the member. In ISO8601 format (YYYY-MM-DD).                |
| group_number                      | The group number of the patient.                                                      |
| ssn                               | The ssn of the member.                                                                |
| estimated_birth_date              | The estimated date of birth of the patient. In ISO8601 format (YYYY-MM-DD).           |
| illness_date                      | The date the member became ill. In ISO8601 format (YYYY-MM-DD).                       |
| accident_date                     | The date of the member's accident. In ISO8601 format (YYYY-MM-DD).                     |

<a name="referral_service_review_provider_object"></a>
##### Provider object:

| Field                             | Description                                                                                                                                                                            |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| first_name                        | The provider’s first name when the provider is an individual.                                                                                                                          |
| middle_name                       | The provider’s middle name when the provider is an individual.                                                                                                                         |
| last_name                         | The provider’s last name when the provider is an individual.                                                                                                                           |
| suffix                            | The suffix for the provider.                                                                                                                                                           |
| tax_id                            | The federal tax id for the provider billing for services. For individual providers, this may be the tax id of the medical practice or organization where a provider works.             |
| phone                             | The phone number for the provider.                                                                                                                                                     |
| taxonomy_code                     | The taxonomy code for the provider.                                                                                                                                                    |
| npi                               | The NPI for the provider.                                                                                                                                                              |
| organization_name                 | The provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                   |

<a name="referral_certaction"></a>
Full list of possible values that can be returned in the `event.review.certification_action` parameter
on the referral response:

| certification_action Values |                    |
|:----------------------------|:-------------------|
| cancelled                   | modified           |
| certified_in_total          | no_action_required |
| certified_partial           | not_certified      |
| contact_payer               | pended             |

<a name="referral_follow_up_action"></a>
Possible values that can be returned in the `follow_up_action` field on the referral response:

| follow_up_action Values               |                                   |
|:--------------------------------------|:----------------------------------|
| do_not_resubmit_sent_to_third_party   | do_not_resubmit_will_respond_again|
| correct_and_resubmit                  | resubmit_original                 |
| wait_10_days_and_resubmit             | wait_30_days_and_resubmit         |
| resubmission_allowed                  | resubmission_not_allowed          |


<a name="referral_decision"></a>
Full list of possible values that can be returned in the `event.review.decision_reason` parameter on the referrals response:

| decision_reason Values                                    |                                                      |
|:----------------------------------------------------------|:-----------------------------------------------------|
| additional_patient_information_required                   | patient_in_premium_payment_grace_period_second_month |
| administrative_cancellation                               | patient_in_premium_payment_grace_period_third_month  |
| ambulance_certification_transport_address_mismatch        | patient_restricted_to_specific_provider              |
| authorization_restrictions                                | pre_existing_condition                               |
| authorized_quantity_exceeded                              | price_authorization_expired                          |
| certification_not_required_service                        | price_authorization_no_longer_required               |
| certification_responsibility_external_review_organization | pricing                                              |
| computed_mileage_transport_information_mismatch           | primary_care_service                                 |
| contractual_geographic_restriction                        | product_delivery_pattern                             |
| contractual_guidelines_not_followed                       | product_not_on_the_price_authorization               |
| cosmetic                                                  | provider_not_primary_care_physician                  |
| disposition_pending_review                                | request_forwarded_to_external_review_organization    |
| duplicate_request                                         | requested_information_not_received                   |
| exceeds_plan_maximums                                     | requires_medical_review                              |
| experimental_service                                      | requires_pcp_authorization                           |
| inappropriate_facility_type                               | service_authorized_for_another_provider              |
| level_of_care_not_appropriate                             | service_inconsistent_with_diagnosis                  |
| mileage_cant_be_computed_based_on_data_submitted          | service_inconsistent_with_patient_age                |
| missing_provider_role                                     | service_inconsistent_with_patient_gender             |
| no_credit_allowed                                         | service_inconsistent_with_provider_type              |
| no_prior_approval                                         | services_not_considered_due_to_other_errors          |
| non_covered_service                                       | special_cost_incorrect                               |
| not_medically_necessary                                   | testing_not_included                                 |
| notification_received                                     | time_limits_not_met                                  |
| once_in_a_lifetime_restriction_applies                    | transport_request_denied                             |
| out_of_network                                            | unit_resale_higher_than_authorized                   |
| patient_in_premium_payment_grace_period_first_month       |                                                      |

<a name="certification_r_type"></a>
Full list of possible values that can be returned in the `event.certification_type` parameter on the referral response:

| certification_type |                 |
|:-------------------|:----------------|
| appeal_immediate   | initial         |
| appeal_standard    | reconsideration |
| cancel             | renewal         |
| extension          | revised         |


<a name="r_category"></a>
Full list of possible values that can be returned in the `event.category` parameter on the referral response:

| category               |                       |
|:-----------------------|:----------------------|
| admission_review       | individual            |
| health_services_review | specialty_care_review |

#### Example Response

> Example referrals response when the trading partner has authorized the request:

```json
{
    "client_id": "<client_id>",
    "event": {
        "category": "specialty_care_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "H72.90",
                "date": "2014-09-25"
            }
        ],
        "place_of_service": "office",
        "provider": {
            "first_name": "JOHN",
            "npi": "1154387751",
            "last_name": "FOSTER",
            "phone": "8645822900"
        },
        "review": {
            "certification_action": "certified_in_total",
            "certification_number": "AUTH0001"
        },
        "type": "consultation"
    },
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "CHRISTINA",
        "last_name": "BERTOLAMI",
        "npi": "1619131232"
    },
    "trading_partner_id": "MOCKPAYER"
}
```

