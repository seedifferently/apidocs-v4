## In-Network Pharmacies

> Example fetching pharmacy information by NPI:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"  'https://platform.pokitdok.com/api/v4/pharmacy/network/1427382266?trading_partner_id=medicare_national&plan_number=S5820003'
```

```python
client.pharmacy_network(npi='1427382266', trading_partner_id='medicare_national', plan_number='S5820003')
```

```ruby
client.pharmacy_network(npi: '1427382266', trading_partner_id: 'medicare_national', plan_number: 'S5820003')
```

```csharp
client.pharmacyNetwork(
                    "1427382266",
                    new Dictionary<string, string> {
                      {"trading_partner_id", "medicare_national"},
                      {"plan_number", "S5820003"}
                  });
```

```java
Map<String, Object> params = new HashMap<String, Object>();
params.put("trading_partner_id", "medicare_national");
params.put("plan_number", "S5820003");
client.pharmacyNetwork("1427382266", params);
```

> Example searching for in-network pharmacies by plan and zip code:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"  'https://platform.pokitdok.com/api/v4/pharmacy/network?trading_partner_id=medicare_national&plan_number=S5820003&zipcode=07030&radius=1mi'
```

```python
client.pharmacy_network(trading_partner_id='medicare_national', plan_number='S5820003' , zipcode='07030', radius='1mi')
```

```ruby
client.pharmacy_network(trading_partner_id: 'medicare_national', plan_number: 'S5820003' , zipcode: '07030', radius: '1mi')
```

```csharp
client.pharmacyNetwork(
                    new Dictionary<string, string> {
                      {"trading_partner_id", "medicare_national"},
                      {"plan_number", "S5820003"},
                      {"zipcode", "07030"},
                      {"radius", "1mi"}
                  });
```

```java
Map<String, Object> params = new HashMap<String, Object>();
params.put("trading_partner_id", "medicare_national");
params.put("plan_number", "S5820003");
params.put("zipcode", "07030");
params.put("radius", "1mi");
client.pharmacyNetwork(params);
```

> Sample response for /pharmacy/network/{npi} endpoint :

```
{
    "data": [
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "307 1st St"
                ],
                "city": "Hoboken",
                "country": "US",
                "geo_location": [
                    -74.03467,
                    40.738
                ],
                "phone": "2014207777",
                "state": "NJ",
                "zipcode": "07030"
            },
            "mail": false,
            "pharmacy_name": "HOBOKEN DRUGS",
            "retail": true
        }
    ]
}

```

> Sample response for /pharmacy/network endpoint when using zipcode and radius as parameters:

```
{
    "data": [
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "165 Erie St"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.04339,
                    40.72829
                ],
                "phone": "2019631903",
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "NEWPORT PHARMACEUTICAL SERVICES INC",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "204 Washington St Apt 1B"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.03771,
                    40.71469
                ],
                "phone": "2013335189",
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "HOOK PHARMACY",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "325 7th St"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.04907,
                    40.72638
                ],
                "phone": "2016538378",
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "SLM PHARMACY INC",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "110 Newark Ave"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.04271,
                    40.71997
                ],
                "phone": "2014330108",
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "DUANE READE",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "400 Marin Blvd"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.03995,
                    40.72313
                ],
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "INSERRA SUPERMARKETS INC",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "355 Grand St"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.05094,
                    40.71591
                ],
                "phone": "2019152166",
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "LSC PHARMACY SERVICES, INC",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "501 Jersey Ave"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.04745,
                    40.71944
                ],
                "phone": "2014358112",
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "NORMANS PHARMACY INC",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "52 River Dr S"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.032139,
                    40.727533
                ],
                "phone": "2012161166",
                "state": "NJ",
                "zipcode": "07310"
            },
            "mail": false,
            "pharmacy_name": "DUANE READE",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "52 Essex St"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.03595,
                    40.71295
                ],
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "DOWNTOWN CHEMISTS CORP",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "129 Newark Ave"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.04401,
                    40.72019
                ],
                "phone": "2013332223",
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "FENNY PHARMACY LLC",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "172 Newark Ave"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.0453,
                    40.72129
                ],
                "phone": "2014323300",
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "TRANQUIL PHARM INC",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "75 Bright St"
                ],
                "city": "Jersey City",
                "country": "US",
                "geo_location": [
                    -74.04841,
                    40.71719
                ],
                "phone": "2013324488",
                "state": "NJ",
                "zipcode": "07302"
            },
            "mail": false,
            "pharmacy_name": "CARRY PHARMACY INC",
            "retail": true
        }
    ]
}
```

The In-Network Pharmacy Endpoint returns in-network pharmacies for a plan.

| Endpoint               | HTTP Method | Description                                                              |
|:-----------------------|:------------|:-------------------------------------------------------------------------|
| /pharmacy/network/     | GET         | Get a list of pharmacies meeting certain search criteria                 |
| /pharmacy/network/{id} | GET         | Retrieve the data for a specified pharmacy; the ID is the provider’s NPI |

To use the In-Network Pharmacy Endpoint with a Medicare member, you will need the plan number. This is the contract ID (ex. S1234) + Plan's Plan Benefit Package (PBP) Number PBP number (ex. 001) concatenated together in that order. There are several ways to get this number. The plan number may be on the member’s insurance card. If not, you can use an NCPDP E1 eligibility check or PokitDok’s Eligibility Endpoint. With the Eligibility Endpoint, Medicare members with Part D coverage will have pharmacy.is_eligible set to true and the pharmacy.plan_number will contain their Medicare Part D plan_number. Note: Your NPI must be registered with Medicare to check eligibility.

A list of pharmacies will be returned for a given location and radius. The in-network pharmacy endpoint defaults to retail pharmacies.

The response will include details about the pharmacy such as name, address, phone number, etc.

The /pharmacy/network endpoint accepts the following parameters:

| Parameter          | Type     | Description                                                                                                                                                    |
|:-------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trading_partner_id | {string} | Unique id for the intended trading partner, as specified by the [Trading Partners](https://platform.pokitdok.com/documentation/v4/#trading-partners) endpoint. |
| plan_number        | {string} | Member’s plan identification number. Note: If unknown can use X12 270/271 eligibility                                                                          |
| zipcode            | {string} | Zip code for location                                                                                                                                          |
| radius             | {string} | Radius of area (miles)                                                                                                                                         |
| pharmacy_name      | {string} | Name of pharmacy                                                                                                                                               |
| state              | {string} | Name of U.S. state in which to search for providers (e.g. “CA” or “SC”)                                                                                        |
| sort               | {string} | Accepted values include ‘distance’ (default) or 'rank’. 'distance’ sort requires city & state or zipcode parameters otherwise sort will be 'rank’.             |

The /pharmacy/network response contains the following fields:

| Field                            | Type      | Description                            |
|:---------------------------------|:----------|:---------------------------------------|
| pharmacy.pharmacy_name           | {string}  | Name of pharmacy                       |
| pharmacy.locations.address_lines | {array}   | Address lines                          |
| pharmacy.locations.city          | {string}  | City                                   |
| pharmacy.locations.country       | {string}  | Optional: Country                      |
| pharmacy.locations.geo_location  | {array}   | GeoJSON array of [longitude, latitude] |
| pharmacy.locations.phone         | {string}  | Optional: Phone number                 |
| pharmacy.locations.state         | {string}  | State                                  |
| pharmacy.locations.zipcode       | {string}  | Zip code                               |
| pharmacy.mail                    | {boolean} | Is location a mail order pharmacy?     |
| pharmacy.retail                  | {boolean} | Is location a mail order pharmacy?     |

