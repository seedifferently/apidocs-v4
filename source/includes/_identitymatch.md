## Identity Match
> Example: list all of the MatchConfigs owned by a production app.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match_config/
```

```python
client.get("/identity/match_config/")
```

```csharp
client.request("/identity/match_config/", "GET")
```

```ruby
client.request("/identity/match_config/", "GET")
```

```java
client.get("/identity/match_config/")
```

```swift
let path = "/identity/match_config/"
try client.request(path: path, method: "GET")
```

> Example response showing all MatchConfigs owned by a production app.

```json
{
    "data": [
        {
            "input_topic": "test_name_and_birth_year_source_ids",
            "algorithm_id": "test_name_and_birth_year"
        },
        {
            "input_topic": "test_name_and_strong_id_source_ids",
            "algorithm_id": "test_name_and_strong_id"
        },
        {
            "input_topic": "test_name_and_zipcode_source_ids",
            "algorithm_id": "test_name_and_zipcode"
        }
    ],
    "meta": {
        "..." : "..."
    }
}

```

> Example: Retrieves a single MatchConfig by uuid or algorithm_id

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match_config/test_name_and_strong_id
```

```python
client.get("/identity/match_config/test_name_and_strong_id")
```

```csharp
client.request("/identity/match_config/test_name_and_strong_id", "GET")
```

```ruby
client.request("/identity/match_config/test_name_and_strong_id", "GET")
```

```java
client.get("/identity/match_config/test_name_and_strong_id")
```

```swift
let path = "/identity/match_config/test_name_and_strong_id"
try client.request(path: path, method: "GET")
```

> Example response showing a single MatchConfigs owned by a production app.

```json
{
    "data": {
        "_type": "IdentityMatchConfig",
        "insert_dt": "Fri Feb 10 02:11:01 2017",
        "update_dt": "Fri Feb 10 02:11:01 2017",
        "deleted": false,
        "_uuid": "2b1822c8-ef36-11e6-89b8-08002778b074",
        "input_topic": "test_name_and_strong_id_source_ids",
        "algorithm_id": "test_name_and_strong_id",
        "_id": "589d21350640fd45d593ae64",
        "owner_id": "9P10N4H2F7ZbaAU6RYct"
    },
    "meta": {
        "..." : "..."
    }
}
```


> Example: Removes a single MatchConfig by uuid or algorithm_id

```shell
curl -i -XDELETE -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match_config/test_name_and_strong_id
```

```python
client.delete("/identity/match_config/test_name_and_strong_id")
```

```csharp
client.request("/identity/match_config/test_name_and_strong_id", "DELETE")
```

```ruby
client.request("/identity/match_config/test_name_and_strong_id", "DELETE")
```

```java
client.delete("/identity/match_config/test_name_and_strong_id")
```

```swift
let path = "/identity/match_config/test_name_and_strong_id"
try client.request(path: path, method: "DELETE")
```

> Example response showing a single MatchConfigs owned by a production app.

```json
{
    "data": {
        "status": "OK",
        "count": 1
    },
    "meta": {
        "..." : "..."
    }
}
```


> Example: Modifies a single MatchConfig by uuid or algorithm_id and then returns the result.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match_config/test_name_and_strong_id
```

```python
client.put("/identity/match_config/test_name_and_strong_id", data={"input_topic": "new_topic"})
```

```csharp
Dictionary<string, string> data = new Dictionary<string, string> {
                {"input_topic", "new_topic"}
        };
client.request("/identity/match_config/test_name_and_strong_id", "PUT", data)
```

```ruby
client.request("/identity/match_config/test_name_and_strong_id", "PUT", params={"input_topic": "new_topic"})
```

```java
HashMap<String, String>() params = new HashMap<String, String>();
params.put("input_topic", "new_topic");
client.put("/identity/match_config/test_name_and_strong_id", params)
```

```swift
let path = "/identity/match_config/test_name_and_strong_id"
let params = [
                "input_topic": "new_topic"
] as [String:String]
try client.request(path: path, method: "PUT", params: params)
```

> Example response showing a single MatchConfigs owned by a production app.

```json
{
    "data": {
        "_type": "IdentityMatchConfig",
        "insert_dt": "Fri Feb 10 02:12:01 2017",
        "update_dt": "Fri Feb 10 02:24:36 2017",
        "deleted": false,
        "_uuid": "4f3af8ba-ef36-11e6-b589-08002778b074",
        "input_topic": "new_topic",
        "algorithm_id": "test_name_and_zipcode",
        "_id": "589d21710640fd45d593ae6a",
        "owner_id": "9P10N4H2F7ZbaAU6RYct"
    },
    "meta": {
        "..." : "..."
    }
}
```

>Example: Uses the MatchConfig with `<algorithm_id>` to query the match index for a canonical_id that matches the submitted. If no canonical\_id is matched then an empty dictionary is returned instead.


```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" '{
    "phone": "1365465555",
    "first_name": "Siena",
    "last_name": "Hermana",
    "middle_name": "Madalynn",
    "suffix": "",
    "gender": "F",
    "prefix": "",
    "ssn": "432900000",
    "address": {
        'street1': "765 Osa Tunnel",
        'street2': "Apt. 108",
        "state_or_province": "ND",
        "postal_code": "36672",
        "city": "Aileenshire"
    },
    "birth_date": {
        'day': 13,
        'month': 5,
        'year': 1988
    }
}' https://platform.pokitdok.com/api/v4/identity/match_config/<algorithm_id>/find
```

```python
params = {
    "phone": "1365465555",
    "first_name": "Siena",
    "last_name": "Hermana",
    "middle_name": "Madalynn",
    "suffix": "",
    "gender": "F",
    "prefix": "",
    "ssn": "432900000",
    "address": {
        'street1': "765 Osa Tunnel",
        'street2': "Apt. 108",
        "state_or_province": "ND",
        "postal_code": "36672",
        "city": "Aileenshire"
    },
    "birth_date": {
        'day': 13,
        'month': 5,
        'year': 1988
    }
}
client.post("/identity/match_config/<algorithm_id>/find", data=params)
```

```csharp
Dictionary<string, object> data = new Dictionary<string, string> {
    { "phone", "1365465555"} ,
    { "first_name", "Siena"} ,
    { "last_name", "Hermana"} ,
    { "middle_name", "Madalynn"} ,
    { "suffix", ""} ,
    { "gender", "F"} ,
    { "prefix", ""} ,
    { "ssn", "432900000"} ,
    { "address",  new Dictionary<string, object> {
        { "street1', "765 Osa Tunnel"} ,
        { "street2', "Apt. 108"} ,
        { "state_or_province", "ND"} ,
        { "postal_code", "36672"} ,
        { "city", "Aileenshire"}
    },
    { "birth_date", new Dictionary<string, object> {
        { "day", 13} ,
        { "month", 5} ,
        { "year", 1988}
    }
}
client.request("/identity/match_config/<algorithm_id>/find", "POST", data)
```

```ruby
params = {
    phone: "1365465555",
    first_name: "Siena",
    last_name: "Hermana",
    middle_name: "Madalynn",
    suffix: "",
    gender: "F",
    prefix: "",
    ssn: "432900000",
    address: {
        street1: "765 Osa Tunnel",
        street2: "Apt. 108",
        state_or_province: "ND",
        postal_code: "36672",
        city: "Aileenshire"
    },
    birth_date: {
        day: 13,
        month: 5,
        year: 1988
    }
}
client.request("/identity/match_config/<algorithm_id>/find", "POST", params=data)
```

```java
HashMap<String, Object>() params = new HashMap<String, Object>();
params.put("phone", "1365465555");
params.put("first_name", "Siena");
params.put("last_name", "Hermana");
params.put("middle_name", "Madalynn");
params.put("suffix", "");
params.put("gender", "F");
params.put("prefix", "");
params.put("ssn", "432900000");
HashMap<String, Object>() address = new HashMap<String, Object>();
address.put("street1", "765 Osa Tunnel");
address.put("street2", "Apt. 108");
address.put("state_or_province", "ND");
address.put("postal_code", "36672");
address.put("city", "Aileenshire");
params.put("address", address);
HashMap<String, Object>() birth_date = new HashMap<String, Object>();
birth_date.put("day", 13);
birth_date.put("month", 5);
birth_date.put("year", 1988);
params.put("birth_date", birth_date);
client.post("/identity/match_config/<algorithm_id>/find", params)
```

```swift
let path = "/identity/match_config/<algorithm_id>/find"
let params = [
    phone: "1365465555",
    first_name: "Siena",
    last_name: "Hermana",
    middle_name: "Madalynn",
    suffix: "",
    gender: "F",
    prefix: "",
    ssn: "432900000",
    address: [
        street1: "765 Osa Tunnel",
        street2: "Apt. 108",
        state_or_province: "ND",
        postal_code: "36672",
        city: "Aileenshire"
    ],
    birth_date: [
        day: 13,
        month: 5,
        year: 1988
    ]
] as [String:Object]
try client.request(path: path, method: "POST", params: params)
```


> Example response when a matching record is found:

```json
{
    "data": {
        "record_id": "d92a6984-ee41-11e6-8973-82d1feccb5b2",
        "sources": [
            "d8fa22d8-ee41-11e6-9b4e-02cfa09edce7"
        ],
        "last_updated": "2017-02-08T21:02:06Z",
        "data": {
            "first_name": "Siena",
            "last_name": "Hermann",
            "middle_name": "Madalynn",
            "phone": "1365465555",
            "prefix": "Ms",
            "ssn": "432900000",
            "address": {
                "city": "Aileenshire",
                "street2": "Apt. 108",
                "postal_code": "36672",
                "state_or_province": "ND",
                "street1": "765 Osa Tunnel "
            },
            "birth_date": {
                "month": 5,
                "day": 13,
                "year": 1988
            },
            "email": "Siena.Hermann@hotmail.com"
        }
    },
    "meta": {
        "..." : "..."
    }
}
```

> Example response when there is no matching response:

```json
{
    "data": {},
    "meta": {
        "..." : "..."
    }
}
```

> Example to submit a new IdentityMatchRequest to the MatchConfig specified by `<algorithm_id>`. If the IdentityMatchRequest fails validation the endpoint will respond with a 422 status code and the response body will contain relevant error messages. Otherwise the response will contain the `source_id` assigned to the IdentityMatchRequest document by the match system. This uuid can then later be used to look up the canonical_id that the IdentityMatchRequest was matched to.


```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -d '{
    "phone": "1365465555",
    "first_name": "Siena",
    "last_name": "Hermana",
    "middle_name": "Madalynn",
    "suffix": "",
    "gender": "F",
    "prefix": "",
    "ssn": "432900000",
    "address": {
        'street1': "765 Osa Tunnel",
        'street2': "Apt. 108",
        "state_or_province": "ND",
        "postal_code": "36672",
        "city": "Aileenshire"
    },
    "birth_date": {
        'day': 13,
        'month': 5,
        'year': 1988
    }
}' https://platform.pokitdok.com/api/v4/identity/match_config/<algorithm_id>
```

```python
params = {
    "phone": "1365465555",
    "first_name": "Siena",
    "last_name": "Hermana",
    "middle_name": "Madalynn",
    "suffix": "",
    "gender": "F",
    "prefix": "",
    "ssn": "432900000",
    "address": {
        'street1': "765 Osa Tunnel",
        'street2': "Apt. 108",
        "state_or_province": "ND",
        "postal_code": "36672",
        "city": "Aileenshire"
    },
    "birth_date": {
        'day': 13,
        'month': 5,
        'year': 1988
    }
}
client.post("/identity/match_config/<algorithm_id>", data=params)
```

```csharp
Dictionary<string, object> data = new Dictionary<string, string> {
    { "phone", "1365465555"} ,
    { "first_name", "Siena"} ,
    { "last_name", "Hermana"} ,
    { "middle_name", "Madalynn"} ,
    { "suffix", ""} ,
    { "gender", "F"} ,
    { "prefix", ""} ,
    { "ssn", "432900000"} ,
    { "address",  new Dictionary<string, object> {
        { "street1', "765 Osa Tunnel"} ,
        { "street2', "Apt. 108"} ,
        { "state_or_province", "ND"} ,
        { "postal_code", "36672"} ,
        { "city", "Aileenshire"}
    },
    { "birth_date", new Dictionary<string, object> {
        { "day", 13} ,
        { "month", 5} ,
        { "year", 1988}
    }
}
client.request("/identity/match_config/<algorithm_id>", "POST", data)
```

```ruby
params = {
    phone: "1365465555",
    first_name: "Siena",
    last_name: "Hermana",
    middle_name: "Madalynn",
    suffix: "",
    gender: "F",
    prefix: "",
    ssn: "432900000",
    address: {
        street1: "765 Osa Tunnel",
        street2: "Apt. 108",
        state_or_province: "ND",
        postal_code: "36672",
        city: "Aileenshire"
    },
    birth_date: {
        day: 13,
        month: 5,
        year: 1988
    }
}
client.request("/identity/match_config/<algorithm_id>", "POST", params=data)
```

```java
HashMap<String, Object>() params = new HashMap<String, Object>();
params.put("phone", "1365465555");
params.put("first_name", "Siena");
params.put("last_name", "Hermana");
params.put("middle_name", "Madalynn");
params.put("suffix", "");
params.put("gender", "F");
params.put("prefix", "");
params.put("ssn", "432900000");
HashMap<String, Object>() address = new HashMap<String, Object>();
address.put("street1", "765 Osa Tunnel");
address.put("street2", "Apt. 108");
address.put("state_or_province", "ND");
address.put("postal_code", "36672");
address.put("city", "Aileenshire");
params.put("address", address);
HashMap<String, Object>() birth_date = new HashMap<String, Object>();
birth_date.put("day", 13);
birth_date.put("month", 5);
birth_date.put("year", 1988);
params.put("birth_date", birth_date);
client.post("/identity/match_config/<algorithm_id>", params)
```

```swift
let path = "/identity/match_config/<algorithm_id>"
let params = [
    phone: "1365465555",
    first_name: "Siena",
    last_name: "Hermana",
    middle_name: "Madalynn",
    suffix: "",
    gender: "F",
    prefix: "",
    ssn: "432900000",
    address: [
        street1: "765 Osa Tunnel",
        street2: "Apt. 108",
        state_or_province: "ND",
        postal_code: "36672",
        city: "Aileenshire"
    ],
    birth_date: [
        day: 13,
        month: 5,
        year: 1988
    ]
] as [String:Object]
try client.request(path: path, method: "POST", params: params)
```

> Example Response when IdentityMatchRequest passes validation

```json
{
    "data": {
        "_source_id": "908908ce-ef69-11e6-8304-92b49a60ff89"
    },
    "meta": {
        "..." : "..."
    }
}
```

> Example Response when IdentityMatchRequest fails validation (Same request as before with birthday.month removed.)

```json
{
    "data": {
        "errors": {
            "validation": {
                "birth_date": {
                    "month": "Missing field."
                }
            }
        }
    },
    "meta": {
        "..." : "..."
    }
}
```

> Example request for a specific canonical_id document from the MatchConfig specified by `<algorithm_id>`, using a direct uuid lookup. It is much more efficient than a `/<algorithm_id>/find [POST]` query, but returns the same response format.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match_config/
```

```python
pd.get("/identity/match/test_name_and_strong_id/canonical_id")
```

```csharp
client.request("/identity/match/test_name_and_strong_id/canonical_id", "GET")
```

```ruby
client.request("/identity/match/test_name_and_strong_id/canonical_id", "GET")
```

```java
client.get("/identity/match/test_name_and_strong_id/canonical_id")
```

```swift
let path = "/identity/match/test_name_and_strong_id/canonical_id"
try client.request(path: path, method: "GET")
```

> Example response of a document representing the identity found at canonical_id

```json
{
    "data": {
        "record_id": "d92a6984-ee41-11e6-8973-82d1feccb5b2",
        "sources": [
            "d8fa22d8-ee41-11e6-9b4e-02cfa09edce7"
        ],
        "last_updated": "2017-02-08T21:02:06Z",
        "data": {
            "first_name": "Siena",
            "last_name": "Hermann",
            "middle_name": "Madalynn",
            "phone": "1365465555",
            "prefix": "Ms",
            "ssn": "432900000",
            "address": {
                "city": "Aileenshire",
                "street2": "Apt. 108",
                "postal_code": "36672",
                "state_or_province": "ND",
                "street1": "765 Osa Tunnel "
            },
            "birth_date": {
                "month": 5,
                "day": 13,
                "year": 1988
            },
            "email": "Siena.Hermann@hotmail.com"
        }
    },
    "meta": {
        "..." : "..."
    }
}
```

> Example request of the source_id documents associated with a specified canonical_id document within the given MatchConfig, using a direct uuid lookups. The response will contain full documents, not just the source\_ids' uuids. If an array of uuids is desired then look no further than the `canonical_id.sources` attribute.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match/test_name_and_strong_id/canonical_id/sources"
```

```python
pd.get("/identity/match/test_name_and_strong_id/canonical_id/sources")
```

```csharp
client.request("/identity/match/test_name_and_strong_id/canonical_id/sources", "GET")
```

```ruby
client.request("/identity/match/test_name_and_strong_id/canonical_id/sources", "GET")
```

```java
client.get("/identity/match/test_name_and_strong_id/canonical_id/sources")
```

```swift
let path = "/identity/match/test_name_and_strong_id/canonical_id/sources"
try client.request(path: path, method: "GET")
```

> Example response of a document representing the identity found at canonical_id

```json
{
    "data": [
        {
            "_source_id": "d8fa22d8-ee41-11e6-9b4e-02cfa09edce7",
            "data": {
                "first_name": "Siena",
                "last_name": "Hermann",
                "middle_name": "Madalynn",
                "phone": "1365465555",
                "prefix": "Ms",
                "ssn": "432900000",
                "address": {
                    "city": "Aileenshire",
                    "street2": "Apt. 108",
                    "postal_code": "36672",
                    "state_or_province": "ND",
                    "street1": "765 Osa Tunnel "
                },
                "birth_date": {
                    "month": 5,
                    "day": 13,
                    "year": 1988
                },
                "email": "Siena.Hermann@hotmail.com"
            }
        },
        {
            "_source_id": "0283885e-ef6b-11e6-8304-92b49a60ff89",
            "data": {"..." : "..."}
        }, "..." : "..."
    ],
    "meta": {
        "..." : "..."
    }
}
```

The identity match is an identity validation service that serves to collect source identity documents (`source_ids`) into canonical identities (`canonical_ids`). Ideally, a `canonical_id` is a unique digital representation of an individual.

### MatchConfig Endpoints

Users interact with the identity match system through an interface called a `match configuration`, which consists of a matching algorithm (designed and deployed by PokitDok) and an input topic, which defines a collection of identity documents that incoming requests will be written to. It's possible, and expected, for different `MatchConfigs` to share an input topic, as this allows the same raw data to be processed according to a variety of matching schemes in parallel.


| Endpoint      | HTTP Method | Description                                                  |
|:--------------|:------------|:-------------------------------------------------------------|
| /identity/match_config/ | GET        | List all of the MatchConfigs |
| /identity/match_config/ | POST        | Update or create a single MatchConfig |
| /identity/match_config/`<uuid_or_algorithm_id>` | GET        | Retrieve a single MatchConfig by uuid or algorithm_id |
| /identity/match_config/`<uuid_or_algorithm_id>` | DELETE        | Removes a single MatchConfig by uuid or algorithm_id |
| /identity/match_config/`<uuid_or_algorithm_id>` | PUT        | Modify a single MatchConfig by uuid or algorithm_id |


The following endpoints provide basic CRUD operations for an platform app's `MatchConfigs`. Each `MatchConfig` has two fields:

| Parameter    | Type   | Description                                                                    | Unique | Required |
|:-------------|:-------|:-------------------------------------------------------------------------------|:-------|:---------|
| algorithm_id | string | The name of the PokitDok match algorithm to be applied.                        | Yes    | Yes      |
| input_topic  | string | The collection of identity data that the match algorithm should be applied to. | No     | Yes      |


### Match Endpoints

The matching endpoints are how MatchConfig operations are exposed to the end user. Each matching endpoint starts with `/identity/match/<algorithm_id>`, designating which of MatchConfig will process the requests. Many of the match operations pass all of their parameters as part of the url; those that don't all accept a standardized document called an `IdentityMatchRequest`.

| Endpoint      | HTTP Method | Description                                                  |
|:--------------|:------------|:-------------------------------------------------------------|
| /identity/match/`<algorithm_id>`/find | POST        | Request for a specific canonical_id document from the MatchConfig specified by `<algorithm_id>` |
| /identity/match/`<algorithm_id>` | POST        | Submits a new IdentityMatchRequest to the MatchConfig specified by `<algorithm_id>`. |
| /identity/match/`<algorithm_id>`/<canonical_id> | GET        | Request for a specific canonical_id document from the MatchConfig specified by `<algorithm_id>` |
| /identity/match/`<algorithm_id>`/source/<source_id>| GET        | Removes a single MatchConfig by uuid or algorithm_id |
| /identity/match/`<algorithm_id>`/source/<source_id>/canonical | GET        | Modify a single MatchConfig by uuid or algorithm_id |

When submiting a `POST` to `/identity/match/<algorithm_id>`, if the IdentityMatchRequest fails validation the endpoint will respond with a 422 status code and the response body will contain relevant error messages. Otherwise the response will contain the `source_id` assigned to the IdentityMatchRequest document by the match system. This uuid can then later be used to look up the canonical_id that the IdentityMatchRequest was matched to. It is also useful to note that `/<algorithm_id>/<canonical_id>` via a `GET` is much more efficient than a `/<algorithm_id>/find` via a `POST` query, but returns the same response format.

The `source_id` endpoints are the `source_id` equivalents of the above `canonical_id` endpoints. The former retrieves a source id by `uuid`, and the latter retrieves the `canonical_id`s which the `source_id` has been associated with by the specified `MatchConfig`. It's worth mentioning that the `/<algorithm_id>/source/<source_id>/canonical [GET]` endpoint will return a list of documents, (usually just a single document), not just a list of `uuid`s.

The `IdentityMatchRequest` object is defined as follows:

| Field 	| Type 	| Description 	| Example Inputs 	|
|:---------------------------	|:--------	|:-----------------------------------------------------	|:---------------------------------	|
| first_name 	| string 	| Patient's given name 	| 'Alice', 'Bob', 'Carter'... 	|
| middle_name 	| string 	| Patient's middle name 	| 'Drew', 'Eric', 'Felicia'... 	|
| last_name 	| string 	| Patient's surname 	| 'Gavin', 'Highsmith', 'Jilk'... 	|
| prefix 	| string 	| Patient's legal prefix 	| 'Dr', 'Mr', 'Ms'... 	|
| suffix 	| string 	| Patient's legal suffix 	| 'Jr', 'III', 'PhD.'... 	|
| ssn 	| string 	| Social Security Number 	| '123448765', '123-44-8765'... 	|
| gender 	| string 	| Patient's Gender 	| 'M', 'F', 'O' 	|
| email 	| string 	| Patient's email address 	| 'ImNotReal@fake.bs' 	|
| phone 	| string 	| Patient's primary phone number 	| '843-123-5555', '8431235555'... 	|
| birth_date.year 	| int 	| Patient's birth year 	| 1959, 1989, 2001... 	|
| birth_date.month 	| int 	| Patient's birth month (numeric) 	| 01, 10, 11... 	|
| birth_date.day 	| int 	| Patient's birth day (numeric) 	| 01, 11, 28... 	|
| address.street1 	| string 	| First line of patient's street address 	| '123 Fake Circle' 	|
| address.street2 	| string 	| Second line of patient's street address 	| 'Apt. 45' 	|
| address.city 	| string 	| The city/town the patient lives in 	| 'Charleston', 'Worsetown'... 	|
| address.state_or_province 	| string 	| The patient's home state's two character state code 	| 'SC', 'CA', 'NY'... 	|
| address.postal_code 	| string 	| The patient's zipcode 	| '31414', '29414-1234'... 	|
| address.country_code 	| string 	| Two character country code (defaults to 'US') 	| 'US' 	|
| id | string | External identifier | '123asdf123'

**Note: while no fields are required, birth_date must be included in its entirety or not at all. **
