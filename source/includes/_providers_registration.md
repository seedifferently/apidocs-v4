
[comment]: # (NOT FOR DEPLOYMENT)

## Providers Registration
> Example fetching provider information by NPI:
```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/providers/registration/1467560003"
```

>Example Request/Response:
```json
{
    "entity_type": "individual",
    "ssn": "432900000",
    "prefix": "",
    "first_name": "Siena",
    "middle_name": "",
    "last_name": "Madalynn",
    "suffix": "",
    "gender": "F",
    "email": "s.madalynn@gmail.com",
    "birth_date": {
        "year": 1988,
        "month": 5,
        "day": 13
    },
    "phone_number": "1234567890",
    "npi": "01232456789",
    "addresses": [
        {
            "role": "primary_practice"
            "street1": "123 Fake St.",
            "street2": "Suite C.",
            "city": "Charleston",
            "state_or_province": "SC",
            "postal_code": "29414",
            "country_code": "US"
        },
    ],
    "specialties": [
        {
            "nucc_code": "207RS0010X",
            "name": "Sports Medicine"
        },
        {
          "nucc_code": "207XX0005X",
          "name": "Orthopaedic Surgery - Sports Medicine"
        }
    ]
}
```

*Available modes of operation: real-time only*

The Provider Registrations endpoints provide access to PokitDok's provider directory, while also allowing each app to overwrite the shared provider record; allowing each app to store extra data or to tailor the shared record to the app's purpose.

Available Provider Endpoints:

| Endpoint        | HTTP Method | Description                                                              |
|:----------------|:------------|:-------------------------------------------------------------------------|
| /provider/registration/{id} | GET         | Retrieve the data for a specified provider; the ID is the provider's NPI |
| /provider/registration/{id} | PUT         | Update the data for a specified provider; the ID is the provider's NPI |
| /provider/registration/{id} | DELETE      | Unregister the provider from the application. |
| /provider/registration/ | POST         | Registers a new provider with the application. If a pre-existing app_provider document is found the endpoint will instead update it. |

Requests and responses should contain the following fields:

| Parameter                 | Type     | Description                                                                       | Required |
|---------------------------|----------|-----------------------------------------------------------------------------------|----------|
| entity_type               | {string} | Type of provider                                                                  | Yes      |
| first_name                | {string} | Provider's legal first name.                                                      | No       |
| middle_name               | {string} | Provider's legal middle name.                                                     | No       |
| last_name                 | {string} | Provider's legal surname.                                                         | No       |
| ssn                       | {string} | Provider's social security number.                                                | No       |
| birth_date.year           | {string} | The year the provider was born. (ISO 4-digit form, e.g. 1987)                     | No       |
| birth_date.month          | {string} | The month the provider was born. (Unpadded numeric form, e.g. 1)                  | No       |
| birth_date.day            | {string} | The day of the month the provider was born (Unpadded numeric form, e.g. 1)        | No       |
| addreses                  | {list of addresses} | A list of provider locations. (see below for address schema)           | No       |
| phone_number              | {string} | The provider's phone number.                                                      | No       |
| email                     | {string} | The provider's email address.                                                     | No       |
| specialties               | {list of specialties} | A list of specialties with nucc codes.                               | No       |

Addresses are described with the following schema:
| Parameter                 | Type     | Description                                                                       | Required |
|---------------------------|----------|-----------------------------------------------------------------------------------|----------|
| address.role              | {string} | Description of the location's role (e.g. primary practice)                        | No       |
| address.street1           | {string} | The first line of the patient's street address.                                   | Yes      |
| address.street2           | {string} | The second line of the patient's street address.                                  | No       |
| address.city              | {string} | The city/town of the patient's street address.                                    | Yes      |
| address.state_or_province | {string} | The two-letter state abbreviation code of the patient's street address. (e.g. SC) | Yes      |
| address.postal_code       | {string} | The zip or postal code of the patient's address. (e.g. 29414)                     | Yes      |
| address.country_code      | {string} | The country code of the patient's address. (e.g. USA)                             | Yes      |

Specialties are described with the following schema:
| Parameter                 | Type     | Description                                                                       | Required |
|---------------------------|----------|-----------------------------------------------------------------------------------|----------|
| name                      | {string} | Human readable specialty title (e.g. Sports Medicine)                             | Yes      |
| nucc_code                 | {string} | NUCC code associated with the given specialty                                     | No       |