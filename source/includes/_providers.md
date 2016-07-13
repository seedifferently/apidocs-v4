## Providers
> Example fetching provider information by NPI:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/providers/1467560003"
```

```python
client.providers(npi='1467560003')
```

```csharp
client.providers("1467560003");
```

```ruby
client.providers({npi: '1467560003'})
```

```java
HashMap<String, String> query = new HashMap<String, String>();
query.put("npi", "1467560003");

client.providers(query)
```

>Example Response:

```json
{
  "provider": {
    "birth_date": "1972",
    "degree": "MD",
    "description": "Dr. Jerome Aya-Ay was raised in the small rural town of Grantsville, West Virginia. He graduated from the University of Notre Dame with a bachelor's degree in Biology.  After studying for a Masters in Biomedical Sciences at Marshall University, he continued on to graduate from Marshall University School of Medicine in Huntington, WV with a medical degree. Dr. Aya-Ay completed his residency in Family Medicine at Spartanburg Regional Medical Center where he was awarded the Family Medicine...",
    "education": {
      "graduation_year": 2004,
      "medical_school": "Marshall University School Of Medicine"
    },
    "fax": "8645625230",
    "first_name": "Jerome",
    "gender": "Male",
    "last_name": "Aya-Ay",
    "licenses": [
      {
        "number": "27210",
        "state": "SC"
      }
    ],
    "licensures": [
      {
        "expiration_date": "2017-06-25",
        "number": "27210",
        "state": "SC",
        "status": "active",
        "verified": "Y"
      }
    ],
    "locations": [
      {
        "address_lines": [
          "1703 John B White SR Blvd Ste A"
        ],
        "city": "Spartanburg",
        "geo_location": [
          -81.98184,
          34.92287
        ],
        "phone": "8646417229",
        "role": [
          "practice"
        ],
        "state": "SC",
        "zipcode": "29301"
      },
      {
        "address_lines": [
          "1120 N Pleasantburg Dr Ste 301"
        ],
        "city": "Greenville",
        "geo_location": [
          -82.36932,
          34.80968
        ],
        "phone": "8642524808",
        "role": [
          "practice"
        ],
        "state": "SC",
        "zipcode": "29607"
      }
    ],
    "middle_name": "Benitez",
    "npi": "1467560003",
    "phone": "8645625100",
    "prefix": "DR",
    "residencies": [
      {
        "institution_name": "Spartanburg Regional Healthcare System",
        "type": "Residency"
      },
      {
        "institution_name": "Marshall University School Of Medicine",
        "to_year": 2004,
        "type": "Medical School"
      }
    ],
    "small_image_url": "https://d2sc6ykmuixlzf.cloudfront.net/pda0233f41447f472dab57393b0cbf5bb7-29ef4cc83c4372854a573b302b259b2c-thumbnail.jpeg",
    "specialty": [
      "General & Family Medicine",
      "Family Practice",
      "Preventive Medicine",
      "General Practitioner"
    ],
    "specialty_primary": [
      "Family Practice"
    ],
    "specialty_secondary": [
      "Physician"
    ],
    "uuid": "fc44d0e0-ea7f-492e-90f0-0f9148453019",
    "verified": true
  }
}
```

> Example searching providers by zipcode and specialty:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/providers/?zipcode=29307&specialty=rheumatology&radius=3mi"
```

```python
client.providers(zipcode='29307', specialty='rheumatology', radius='3mi')
```

```csharp
 client.providers(
			new Dictionary<string, string> {
				{ "zipcode", "29307" },
				{ "specialty", "rheumatology" },
				{ "radius", "3mi" }
		});
```

```ruby
client.providers({zipcode: '29307', specialty: 'rheumatology', radius: '3mi'})
```

```java
HashMap<String, String> query = new HashMap<String, String>();
query.put("zipcode", "29307");
query.put("specialty", "rheumatology");
query.put("radius", "3mi");

client.providers(query)
```

>Example response:

```json
[
  {
    "distance": 2.0202967583329134,
    "provider": {
      "fax": "8645821269",
      "locations": [
        {
          "address_lines": [
            "1770 Skylyn Dr"
          ],
          "city": "Spartanburg",
          "county": "Spartanburg",
          "fax": "8645821269",
          "geo_location": [
            -81.892414,
            34.980127
          ],
          "phone": "8645827892",
          "state": "SC",
          "zipcode": "29307"
        }
      ],
      "npi": "1588809198",
      "organization_name": "Mary Black Physicians Group LLC",
      "other_organization_name": "Piedmont Rheumatology",
      "phone": "8645827892",
      "specialty": [
        "Internal Medicine",
        "Rheumatology"
      ],
      "specialty_primary": [
        "Rheumatology"
      ],
      "specialty_secondary": [
        "Allopathic and Osteopathic Physicians (MD/DO)"
      ],
      "uuid": "03d41ad4-4744-425c-882f-4136bf5d5d86",
      "verified": false
    }
  },
  {
    "distance": 2.0202967583329134,
    "provider": {
      "birth_date": "1971",
      "degree": "MD",
      "education": {
        "graduation_year": 1997,
        "medical_school": "Sri Devaraj Urs Medical College"
      },
      "fax": "8645821582",
      "first_name": "Muthamma",
      "gender": "Female",
      "last_name": "Machimada",
      "licenses": [
        {
          "number": "28487",
          "state": "SC"
        }
      ],
      "licensures": [
        {
          "expiration_date": "2017-06-25",
          "number": "28487",
          "state": "SC",
          "status": "active",
          "verified": "Y"
        }
      ],
      "locations": [
        {
          "address_lines": [
            "1770 Skylyn Dr"
          ],
          "city": "Spartanburg",
          "county": "Spartanburg",
          "fax": "8645821582",
          "geo_location": [
            -81.892414,
            34.980127
          ],
          "phone": "8645827892",
          "state": "SC",
          "zipcode": "29307"
        },
        {
          "address_lines": [
            "1650 Skylyn Dr",
            "Suite 220"
          ],
          "city": "Spartanburg",
          "county": "Spartanburg",
          "geo_location": [
            -81.894438,
            34.977198
          ],
          "state": "SC",
          "suite": "220",
          "zipcode": "29307"
        }
      ],
      "middle_name": "J",
      "npi": "1699725986",
      "phone": "8645827892",
      "residencies": [
        {
          "institution_name": "University Mo Columbia School Medicine",
          "type": "Residency"
        },
        {
          "institution_name": "Sri Devaraj Urs Medical College",
          "to_year": 1997,
          "type": "Medical School"
        }
      ],
      "specialty": [
        "Internal Medicine",
        "Rheumatology"
      ],
      "specialty_primary": [
        "Rheumatology"
      ],
      "specialty_secondary": [
        "Physician"
      ],
      "uuid": "e3f3690d-b49b-458f-b83c-f159b7a18b6e",
      "verified": false
    }
  },
  {
    "distance": 2.037465294795502,
    "provider": {
      "degree": "MD",
      "fax": "8645821582",
      "first_name": "KEVIN",
      "gender": "Male",
      "last_name": "TRACY",
      "licenses": [
        {
          "number": "14815",
          "state": "SC"
        }
      ],
      "locations": [
        {
          "address_lines": [
            "PO Box 277827"
          ],
          "city": "Atlanta",
          "country": "US",
          "geo_location": [
            -84.47405,
            33.844371
          ],
          "phone": "8642538080",
          "role": [
            "mailing"
          ],
          "state": "GA",
          "zipcode": "30384"
        },
        {
          "address_lines": [
            "1770 Skylyn Dr"
          ],
          "city": "Spartanburg",
          "country": "US",
          "fax": "8645821582",
          "geo_location": [
            -81.89268,
            34.97982
          ],
          "phone": "8645827892",
          "role": [
            "practice"
          ],
          "state": "SC",
          "zipcode": "29307"
        }
      ],
      "middle_name": "PATRICK",
      "npi": "1215993159",
      "phone": "8645827892",
      "prefix": "DR",
      "specialty": [
        "Internal Medicine",
        "Rheumatology"
      ],
      "specialty_primary": [
        "Rheumatology"
      ],
      "specialty_secondary": [
        "Internal Medicine"
      ],
      "uuid": "bd67dda2-51c2-4325-999f-73052b372885",
      "verified": false
    }
  }
]
```

*Available modes of operation: real-time only*

The Providers endpoints provide access to PokitDok's provider directory.
The Providers endpoints can be used to search for Providers, view biographical,
education, credential, and license information. For a complete reference to all possible 
provider specialties, see our [provider specialties reference](provider_specialties.html).

Available Provider Endpoints:

| Endpoint        | HTTP Method | Description                                                              |
|:----------------|:------------|:-------------------------------------------------------------------------|
| /providers/     | GET         | Get a list of providers meeting certain search criteria                  |
| /providers/{id} | GET         | Retrieve the data for a specified provider; the ID is the provider's NPI |

The /providers/ endpoint accepts the following search parameters:

| Parameter         | Type     | Description                                                                                                                                         |
|:------------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| address_lines     | {string} | Any or all of number, street name, apartment, suite number                                                                                          |
| city              | {string} | Name of city in which to search for providers (e.g. "San Mateo" or "Charleston")                                                                    |
| first_name        | {string} | The provider's first name                                                                                                                           |
| middle_name       | {string} | The provider's middle name                                                                                                                          |
| last_name         | {string} | The provider's last name                                                                                                                            |
| gender            | {string} | The provider's gender                                                                                                                               |
| organization_name | {string} | The business practice name                                                                                                                          |
| name              | {string} | Queries against the provider's full name (first, middle, last) for individuals, organization and other organization names for organizations. For best results individual name properties and organization name should be omitted when passing this parameter.|
| radius            | {string} | Search distance from geographic centerpoint, with unit (e.g. "1mi")                                                                                 |
| specialty         | {string} | The provider's specialty name (e.g. "rheumatology").  Partial name-prefixes may be specified (e.g. "rheum")                                         |
| state             | {string} | Name of U.S. state in which to search for providers (e.g. "CA" or "SC")                                                                             |
| zipcode           | {string} | Geographic center point in which to search for providers (e.g. "94401")                                                                             |
| sort              | {string} | Accepted values include 'distance' (default) or 'rank'.  'distance' sort requires city & state or zipcode parameters otherwise sort will be 'rank'. |
| entity_types      | {string} | The entity type of the provider. Possibilities are individual, organization, and individual,organization.                                           |

The response from the /providers/ endpoints contain the following fields:

| Field                                 | Type      | Description                                                                                                              |
|:--------------------------------------|:----------|:-------------------------------------------------------------------------------------------------------------------------|
| provider.birth_date                   | {string}  | Optional: The provider's birth year. In ISO8601 format (YYYY-MM-DD).                                                     |
| provider.board_certifications         | {array}   | Optional: The provider's board certifications                                                                            |
| provider.board_subcertifications      | {array}   | Optional/Deprecated: The provider's board sub-certifications                                                             |
| provider.degree                       | {string}  | Optional: The provider's degree ("MD" or "DO")                                                                           |
| provider.description                  | {string}  | Optional: (verified providers only) Provider full-text description                                                       |
| provider.education                    | {dict}    | Optional: The provider's medical school information                                                                      |
| provider.education.medical_school     | {string}  | Optional: Provider's medical school                                                                                      |
| provider.education.graduation_year    | {string}  | Optional: Provider's graduation year                                                                                     |
| provider.fax                          | {string}  | Optional: The provider's fax number                                                                                      |
| provider.first_name                   | {string}  | Optional: The provider's first name                                                                                      |
| provider.gender                       | {string}  | Optional: The provider's gender                                                                                          |
| provider.last_name                    | {string}  | Optional: The provider's last name                                                                                       |
| provider.licenses                     | {array}   | Optional: CMS-NPI license information                                                                                    |
| provider.licenses.number              | {string}  | Optional: License number                                                                                                 |
| provider.licenses.state               | {string}  | Optional: License state                                                                                                  |
| provider.licensures                   | {array}   | Optional: State licensure information                                                                                    |
| provider.licensures.as_of_date        | {string}  | Optional: Licensure as of date. In ISO8601 format (YYYY-MM-DD).                                                          |
| provider.licensures.expiration_date   | {string}  | Optional: Licensure expiration date. In ISO8601 format (YYYY-MM-DD).                                                     |
| provider.licensures.number            | {string}  | Optional: Licensure number                                                                                               |
| provider.licensures.status            | {string}  | Optional: Licensure status ('active', 'inactive')                                                                        |
| provider.licensures.state             | {string}  | Optional: Licensure state                                                                                                |
| provider.licensures.verified          | {string}  | Optional: Licensure verification status ('Y' or 'N')                                                                     |
| provider.locations                    | {array}   | Optional: List of locations associated with the provider                                                                 |
| provider.locations.address_lines      | {array}   | Address lines                                                                                                            |
| provider.locations.city               | {string}  | City                                                                                                                     |
| provider.locations.country            | {string}  | Optional: Country                                                                                                        |
| provider.locations.fax                | {string}  | Optional: Fax number                                                                                                     |
| provider.locations.geo_location       | {array}   | GeoJSON array of \[longitude, latitude\]                                                                                 |
| provider.locations.phone              | {string}  | Optional: Phone number                                                                                                   |
| provider.locations.state              | {string}  | State                                                                                                                    |
| provider.locations.zipcode            | {string}  | Zip code                                                                                                                 |
| provider.locations.county             | {string}  | County                                                                                                                   |
| provider.locations.role               | {list}    | Optional: Address role(s). One or both of: ('mailing' or 'practice').  When missing the address is the practice address. |
| provider.locations.suite              | {string}  | Optional: Address suite																								                                                   |
| provider.middle_name                  | {string}  | Optional: The provider's middle name or initial                                                                          |
| provider.npi                          | {string}  | The provider's NPI                                                                                                       |
| provider.organization_name            | {string}  | Optional: The business practice name                                                                                     |
| provider.other_organization_name      | {string}  | Optional: The business practice's other name                                                                             |
| provider.phone                        | {string}  | Optional: The provider's phone number                                                                                    |
| provider.prefix                       | {string}  | Optional: The provider's prefix (Mr., Mrs., Dr., etc)                                                                    |
| provider.residencies                  | {array}   | Optional: Provider residency and education information                                                                   |
| provider.residencies.institution_name | {string}  | Optional: Institution name                                                                                               |
| provider.residencies.type             | {string}  | Optional: Education type.  One of: ('Medical School', 'Residency','Internship', 'Fellowship', 'College Attended')        |
| provider.residencies.to_year          | {string}  | Optional: Graduation year                                                                                                |
| provider.residencies.from_year        | {string}  | Optional/Deprecated: Start year                                                                                          |
| provider.residencies.city             | {string}  | Optional/Deprecated: Residency city                                                                                      |
| provider.residencies.specialty        | {string}  | Optional/Deprecated: Residency specialty                                                                                 |
| provider.specialty                    | {array}   | Optional: List of specialties from the specialty taxonomy associated with the provider                                   |
| provider.specialty_primary            | {array}   | Optional: List of provider's primary specialties                                                                         |
| provider.specialty_secondary          | {array}   | Optional: List of provider's secondary specialties                                                                       |
| provider.suffix                       | {string}  | Optional: The provider's suffix (MD, Jr., etc)                                                                           |
| provider.uuid                         | {uuid}    | The provider's unique PokitDok Platform identifier                                                                       |
| provider.verified                     | {boolean} | Optional: Provider PokitDok verification status                                                                          |
| provider.facebook_url                 | {string}  | Optional: (verified providers only) Provider Facebook URL                                                                |
| provider.small_image_url              | {string}  | Optional: (verified providers only) Provider small image URL                                                             |
| provider.twitter_url                  | {string}  | Optional: (verified providers only) Provider Twitter URL                                                                 |
| provider.website_url                  | {string}  | Optional: (verified providers only) Provider website URL                                                                 |
| distance                              | {string}  | Optional: When sort is 'distance' (default) this is the distance from the city & state or zipcode centroid               |
| entity_type                           | {string}  | The entity type of the provider. Possibilities are individual and organization.                                          |
