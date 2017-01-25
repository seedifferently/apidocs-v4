## Identity Management

**Available modes of operation: real-time.**
**Identity Match jobs are performed asynchronously.**

PokitDok's Identity Management (IdM) API queries an EMPI (Enterprise Master Patient Index) and/or MPI (Master Patient Index), both typically components of an EMR or EHR system, to find a patient identifier and details in the target EMR/EHR system. This helps providers identify the patient through past visits or other records within other EMR/EHR systems.

Within the Identity Management product, there are three availalbe interfaces: Identity, Identity History and Identity Match. The Identity API provides the foundational POST/PUT/GET capability for respectively inserting, updating and retrieving identities in the system. The Identity system updates and returns a single best record while simultaneously tracking the historical updates made to the entity. The Identity History API provides access to the historical versions of an identity. Lastly, the Identity Match API supports the execution of a tune-able and configurable match job which detects duplicates across a historical data load.

Learn more about our [Identity Management workflows](https://platform.pokitdok.com/workflows#anchor-idm).

### Identity

#### Available Identity Endpoints:
| Endpoint         | HTTP Method | Description                                                            |
|:-----------------|:------------|:-----------------------------------------------------------------------|
| /identity/       | POST        | Creates an identity resource. Returns the created resource with a uuid |
| /identity/{uuid} | GET         | Returns an identity's single best record with a given uuid             |
| /identity/{uuid} | PUT         | Updates an existing identity resource. Returns the updated resource    |


#### Accepted Parameters

The `/identity/` endpoint accepts the following parameters:

| Parameter             | Type     | Description                                                                                                        |
|:----------------------|:---------|:-------------------------------------------------------------------------------------------------------------------|
| address.address_lines | {array}  | Address lines                                                                                                      |
| address.city          | {string} | Name of city in which to search for identity records (e.g. "San Mateo" or "Charleston")                            |
| address.state         | {string} | Name of U.S. state in which to search for identity records (e.g. "CA" or "SC")                                     |
| address.zipcode       | {string} | Geographic center point in which to search for identity records.                                                   |
| birth_date            | {string} | Birth date in ISO-8601 format. Ex: 1990-01-25                                                                      |
| email                 | {string} | Valid email address including "@" separator and appropriate domain prefix                                          |
| first_name            | {string} | First name                                                                                                         |
| gender                | {string} | Valid values include: male, female, or unknown                                                                     |
| identifiers           | {array}  | List of external identifiers. Each identifier entry is qualified using a system_uuid, provider_uuid, and location. |
| last_name             | {string} | Last name                                                                                                          |
| member_id             | {string} | The primary insurance membership id associated with the identity resource                                          |
| middle_name           | {string} | Middle name                                                                                                        |
| phone                 | {string} | Primary phone number                                                                                               |
| prefix                | {string} | Prefix/Title                                                                                                       |
| secondary_phone       | {string} | Secondary phone number                                                                                             |
| ssn                   | {string} | Social security number                                                                                             |
| suffix                | {string} | Suffix                                                                                                             |
| uuid                  | {uuid}   | Identity resource unique identifier                                                                                |

Each identifier, or identifiers list entry, represents an external system utilized by a provider at a specific location. Parameters within an identifier entry include:

| Parameter     | Type     | Description                                        |
|:--------------|:---------|:---------------------------------------------------|
| location      | {array}  | Optional: GeoJSON array of \[longitude, latitude\] |
| provider_uuid | {uuid}   | The unique identifier for the provider             |
| system_uuid   | {uuid}   | The unique identifier for the system               |
| value         | {string} | The identifier value                               |

The `location` and `provider_uuid` values correspond to provider resources accessed through the /providers endpoint. system_uuid values correspond to registered systems under the /schedule/schedulers endpoint.

#### Accepted Parameters

Supported query string parameters to the `/identity/` endpoint are listed below. Parameters highlighted in ​*bold*​ utilize
a fuzzy matching strategy which finds comparable (or similar) records within a maximum edit distance of two characters.
All other parameters employ an exact matching strategy.

- *first_name*
- *middle_name*
- *last_name*
- gender
- birth_date
- email
- member_id
- *address*
- *city*
- state
- zipcode
- phone
- secondary_phone

External id search is executed using the `id` parameter: `/identity?id={identifier value}`

The `id` parameter, if present, overrides other search parameters.

#### Identity Examples
> Example creating an identity resource

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"
 -XPOST -d '{
    "prefix": "Mr.",
       "first_name": "Oscar",
       "middle_name": "Harold",
       "last_name": "Whitmire",
       "suffix": "IV",
       "birth_date": "2000-05-25",
       "gender": "male",
       "email": "oscar@pokitdok.com",
       "phone": "555-555-5555",
       "secondary_phone": "333-333-4444",
       "address": {
           "address_lines": ["1400 Anyhoo Avenue"],
           "city": "Springfield",
           "state": "IL",
           "zipcode": "90210"
       },
       "identifiers": [
           {
               "location": [-121.93831, 37.53901],
               "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
               "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
               "value": "W90100-IG-88"

           }
       ]    
    }' https://platform.pokitdok.com/api/v4/identity/
```

```python
client.create_identity({
    "prefix": "Mr.",
    "first_name": "Oscar",
    "middle_name": "Harold",
    "last_name": "Whitmire",
    "suffix": "IV",
    "birth_date": "2000-05-25",
    "gender": "male",
    "email": "oscar@pokitdok.com",
    "phone": "555-555-5555",
    "secondary_phone": "333-333-4444",
    "address": {
        "address_lines": ["1400 Anyhoo Avenue"],
        "city": "Springfield",
        "state": "IL",
        "zipcode": "90210"
    },
    "identifiers": [
        {
            "location": [-121.93831, 37.53901],
            "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
            "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
            "value": "W90100-IG-88"

        }
    ]
})
```

```csharp
client.createIdentity(
    new Dictionary<string, object> {
        {"prefix", "Mr."},
        {"first_name", "Oscar"},
        {"middle_name", "Harold"},
        {"last_name", "Whitmire"},
        {"suffix", "IV"},
        {"birth_date", "2000-05-25"},
        {"gender", "male"},
        {"email", "oscar@pokitdok.com"},
        {"phone", "555-555-5555"},
        {"secondary_phone", "333-333-4444"},
        {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"1400 Anyhoo Avenue"}},
                {"city", "Springfield"},
                {"state", "IL"},
                {"zipcode", "90210"}
            }},
        {"identifiers", new Object[] {new Dictionary<string, object> {
                    {"location", new Object[] {-121.93831, 37.53901}},
                    {"provider_uuid", "1917f12b-fb6a-4016-93bc-adeb83204c83"},
                    {"system_uuid", "967d207f-b024-41cc-8cac-89575a1f6fef"},
                    {"value", "W90100-IG-88"}
                }}}
    }
);
```

```ruby
client.create_identity({
    prefix: "Mr.",
    first_name: "Oscar",
    middle_name: "Harold",
    last_name: "Whitmire",
    suffix: "IV",
    birth_date: "2000-05-25",
    gender: "male",
    email: "oscar@pokitdok.com",
    phone: "555-555-5555",
    secondary_phone: "333-333-4444",
    address: {
        address_lines: ["1400 Anyhoo Avenue"],
        city: "Springfield",
        state: "IL",
        zipcode: "90210"
    },
    identifiers: [
        {
            location: [-121.93831, 37.53901],
            provider_uuid: "1917f12b-fb6a-4016-93bc-adeb83204c83",
            system_uuid: "967d207f-b024-41cc-8cac-89575a1f6fef",
            value: "W90100-IG-88"

        }
    ]
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"prefix\": \"Mr.\",");
buf.append("       \"first_name\": \"Oscar\",");
buf.append("       \"middle_name\": \"Harold\",");
buf.append("       \"last_name\": \"Whitmire\",");
buf.append("       \"suffix\": \"IV\",");
buf.append("       \"birth_date\": \"2000-05-25\",");
buf.append("       \"gender\": \"male\",");
buf.append("       \"email\": \"oscar@pokitdok.com\",");
buf.append("       \"phone\": \"555-555-5555\",");
buf.append("       \"secondary_phone\": \"333-333-4444\",");
buf.append("       \"address\": {");
buf.append("           \"address_lines\": [\"1400 Anyhoo Avenue\"],");
buf.append("           \"city\": \"Springfield\",");
buf.append("           \"state\": \"IL\",");
buf.append("           \"zipcode\": \"90210\"");
buf.append("       },");
buf.append("       \"identifiers\": [");
buf.append("           {");
buf.append("               \"location\": [-121.93831, 37.53901],");
buf.append("               \"provider_uuid\": \"1917f12b-fb6a-4016-93bc-adeb83204c83\",");
buf.append("               \"system_uuid\": \"967d207f-b024-41cc-8cac-89575a1f6fef\",");
buf.append("               \"value\": \"W90100-IG-88\"");
buf.append("");
buf.append("           }");
buf.append("       ]    ");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.createIdentity(query);
```

```swift
let data = [
    "prefix": "Mr.",
    "first_name": "Oscar",
    "middle_name": "Harold",
    "last_name": "Whitmire",
    "suffix": "IV",
    "birth_date": "2000-05-25",
    "gender": "male",
    "email": "oscar@pokitdok.com",
    "phone": "555-555-5555",
    "secondary_phone": "333-333-4444",
    "address": [
        "address_lines": ["1400 Anyhoo Avenue"],
        "city": "Springfield",
        "state": "IL",
        "zipcode": "90210"
    ],
    "identifiers": [
        [
            "location": [-121.93831, 37.53901],
            "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
            "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
            "value": "W90100-IG-88"
        ]
    ]
] as [String:Any]
try client.createIdentity(params: data)
```

> Example updating an identity resource

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"
 -XPUT -d '{
    "prefix": "Mr.",
       "first_name": "Oscar",
       "middle_name": "Harold",
       "last_name": "Whitmire",
       "suffix": "IV",
       "birth_date": "2000-05-25",
       "gender": "male",
       "email": "oscar.whitmire@pokitdok.com",
       "phone": "555-555-5555",
       "secondary_phone": "333-333-4444",
       "address": {
           "address_lines": ["1400 Anyhoo Avenue"],
           "city": "Springfield",
           "state": "IL",
           "zipcode": "90210"
       },
       "identifiers": [
           {
               "location": [-121.93831, 37.53901],
               "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
               "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
               "value": "W90100-IG-88"

           }
       ]    
    }' "https://platform.pokitdok.com/api/v4/identity/881bc095-2068-43cb-9783-cce630364122"
```

```python
client.update_identity("881bc095-2068-43cb-9783-cce630364122", {
    "prefix": "Mr.",
    "first_name": "Oscar",
    "middle_name": "Harold",
    "last_name": "Whitmire",
    "suffix": "IV",
    "birth_date": "2000-05-25",
    "gender": "male",
    "email": "oscar.whitmire@pokitdok.com",
    "phone": "555-555-5555",
    "secondary_phone": "333-333-4444",
    "address": {
        "address_lines": ["1400 Anyhoo Avenue"],
        "city": "Springfield",
        "state": "IL",
        "zipcode": "90210"
    },
    "identifiers": [
        {
            "location": [-121.93831, 37.53901],
            "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
            "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
            "value": "W90100-IG-88"

        }
    ]
})
```

```csharp
client.updateIdentity("881bc095-2068-43cb-9783-cce630364122",
    new Dictionary<string, object> {
		{"prefix", "Mr."},
		{"first_name", "Oscar"},
		{"middle_name", "Harold"},
		{"last_name", "Whitmire"},
		{"suffix", "IV"},
		{"birth_date", "2000-05-25"},
		{"gender", "male"},
		{"email", "oscar.whitmire@pokitdok.com"},
		{"phone", "555-555-5555"},
		{"secondary_phone", "333-333-4444"},
		{"address", new Dictionary<string, object> {
				{"address_lines", new string[] {"1400 Anyhoo Avenue"}},
				{"city", "Springfield"},
				{"state", "IL"},
				{"zipcode", "90210"}
			}},
		{"identifiers", new Object[] {new Dictionary<string, object> {
					{"location", new Object[] {-121.93831, 37.53901}},
					{"provider_uuid", "1917f12b-fb6a-4016-93bc-adeb83204c83"},
					{"system_uuid", "967d207f-b024-41cc-8cac-89575a1f6fef"},
					{"value", "W90100-IG-88"}
				}}}
	}
);
```

```ruby
client.update_identity("881bc095-2068-43cb-9783-cce630364122", {
    prefix: "Mr.",
    first_name: "Oscar",
    middle_name: "Harold",
    last_name: "Whitmire",
    suffix: "IV",
    birth_date: "2000-05-25",
    gender: "male",
    email: "oscar.whitmire@pokitdok.com",
    phone: "555-555-5555",
    secondary_phone: "333-333-4444",
    address: {
        address_lines: ["1400 Anyhoo Avenue"],
        city: "Springfield",
        state: "IL",
        zipcode: "90210"
    },
    identifiers: [
        {
            location: [-121.93831, 37.53901],
            provider_uuid: "1917f12b-fb6a-4016-93bc-adeb83204c83",
            system_uuid: "967d207f-b024-41cc-8cac-89575a1f6fef",
            value: "W90100-IG-88"

        }
    ]
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"prefix\": \"Mr.\",");
buf.append("       \"first_name\": \"Oscar\",");
buf.append("       \"middle_name\": \"Harold\",");
buf.append("       \"last_name\": \"Whitmire\",");
buf.append("       \"suffix\": \"IV\",");
buf.append("       \"birth_date\": \"2000-05-25\",");
buf.append("       \"gender\": \"male\",");
buf.append("       \"email\": \"oscar.whitmire@pokitdok.com\",");
buf.append("       \"phone\": \"555-555-5555\",");
buf.append("       \"secondary_phone\": \"333-333-4444\",");
buf.append("       \"address\": {");
buf.append("           \"address_lines\": [\"1400 Anyhoo Avenue\"],");
buf.append("           \"city\": \"Springfield\",");
buf.append("           \"state\": \"IL\",");
buf.append("           \"zipcode\": \"90210\"");
buf.append("       },");
buf.append("       \"identifiers\": [");
buf.append("           {");
buf.append("               \"location\": [-121.93831, 37.53901],");
buf.append("               \"provider_uuid\": \"1917f12b-fb6a-4016-93bc-adeb83204c83\",");
buf.append("               \"system_uuid\": \"967d207f-b024-41cc-8cac-89575a1f6fef\",");
buf.append("               \"value\": \"W90100-IG-88\"");
buf.append("           }");
buf.append("       ]    ");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.updateIdentity(query);
```

```swift
let data = [
    "prefix": "Mr.",
    "first_name": "Oscar",
    "middle_name": "Harold",
    "last_name": "Whitmire",
    "suffix": "IV",
    "birth_date": "2000-05-25",
    "gender": "male",
    "email": "oscar@pokitdok.com",
    "phone": "555-555-5555",
    "secondary_phone": "333-333-4444",
    "address": [
        "address_lines": ["1400 Anyhoo Avenue"],
        "city": "Springfield",
        "state": "IL",
        "zipcode": "90210"
    ],
    "identifiers": [
        [
            "location": [-121.93831, 37.53901],
            "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
            "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
            "value": "W90100-IG-88"
        ]
    ]
] as [String:Any]
try client.updateIdentity(identityUuid: "881bc095-2068-43cb-9783-cce630364122", params: data)
```

> Query for a single identity resource

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/identity/881bc095-2068-43cb-9783-cce630364122"
```

```python
client.identity("881bc095-2068-43cb-9783-cce630364122")
```

```csharp
client.identity("4d04d8dc-3d0b-4ea1-8add-4dbc9619e1ae");
```

```ruby
client.identity(identity_uuid: "881bc095-2068-43cb-9783-cce630364122")
```

```java
client.identity("881bc095-2068-43cb-9783-cce630364122");
```

```swift
try client.identity(identityUuid: "881bc095-2068-43cb-9783-cce630364122")
```

> Query for one or more identity resources using parameters:

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/identity?first_name=Oscar&last_name=Whitmire&gender=male"
```

```python
client.identity(first_name='Oscar', last_name='Whitmire', gender='male')
```

```ruby
client.identity({first_name: 'Oscar', last_name: 'Whitmire', gender: 'male'})
```

```csharp
client.identity(
    new Dictionary<string, string> {
        { "first_name", "Oscar" },
        { "last_name", "Whitmire" },
        { "gender", "male" },
});
```

```swift
let data = [
    "first_name": "Oscar",
    "last_name": "Whitmire",
    "gender": "male"
] as [String:Any]
try client.identity(params: data)
```

> Query for identity record history:

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/identity/881bc095-2068-43cb-9783-cce630364122/history"
```

```python
client.identity_history("881bc095-2068-43cb-9783-cce630364122")
```

```ruby
client.identity_history("881bc095-2068-43cb-9783-cce630364122")
```

```csharp
client.identityHistory("881bc095-2068-43cb-9783-cce630364122");
```

```java
client.identityHistory("881bc095-2068-43cb-9783-cce630364122");
```

```swift
try client.identityHistory(identityUuid: "881bc095-2068-43cb-9783-cce630364122")
```


### Identity History

We store a historical chain of the updates to a given consumer while also maintaining a single best record for the duration of the data record. The Identity History endpoint gives you access to historical snapshots of the identity.

#### Available Identity History Endpoints:

| Endpoint                              | HTTP Method | Description                                                                                     |
|:--------------------------------------|:------------|:------------------------------------------------------------------------------------------------|
| /identity/{uuid}/history              | GET         | Returns an identity record's change history including the insert date and historical version id |
| /identity/{uuid}/history/{version id} | GET         | Returns a historical identity record                                                            |

### Identity Match

#### Available Identity Match Endpoints:
The Identity Match API supports supports the execution of a tune-able and configurable match job which detects duplicates across a historical data load. This endpoint operates asynchronously. There are three components of the API which can be adjusted to find the best set of matches across your historical data: the match algorithm, the search fields and the match weight. The different match algorithms can be set for exact or approximate string matching. The use of different source and search fields allows for the detection of transposition within an entity's values. Lastly, setting different match weights allows you to control the importance of any individual field level match.

| Endpoint        | HTTP Method | Description                                                     |
|:----------------|:------------|:----------------------------------------------------------------|
| /identity/match | POST        | Creates an identity duplication job. Returns the activity uuid. |


#### Accepted Parameters
Supported query parameters include:

-	city
-	state
-	zipcode
-	birth_date
-	email
-	first_name
-	gender
-	last_name
-	member_id
-	middle_name
-	prefix
-	secondary_phone
-	uuid

