## ICD Convert


*Available modes of operation: real-time*

The ICD Convert endpoint allows a client application to request ICD-9 to ICD-10 mapping information for the
specified ICD-9 code.

#### Available ICD Convert Endpoint
| Endpoint     | HTTP Method | Description                                  |
|:-------------|:------------|:---------------------------------------------|
| /icd/convert | GET         | retrieve ICD-9 to ICD-10 mapping information |


#### Accepted Parameters
The `/icd/convert` endpoint accepts the following parameters:

| Parameter | Description |
|:----------|:------------|
| code      | ICD-9 code  |

#### Example Request

> Example ICD convert request to map an ICD-9 code to possible ICD-10 codes


```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/icd/convert/250.12
```

```python
client.icd_convert('250.12')
```

```csharp
client.icdConvert("250.12");
```

```ruby
client.icd_convert({code: '250.12'})
```

```java
client.icdConvert("250.12");
```

```swift
try client.icdConvert(code: "250.12")
```

#### ICD Convert Fields

The `/icd/convert` response contains the following fields:

| Field                                                     | Description                                                                                                       |
|:----------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| source_code                                               | information about a source diagnosis code                                                                                |
| source_code.description                                   | a string representing a description of the source ICD-9 code                                                      |
| source_code.system                                        | a string representing the code system (icd9)                                                                      |
| source_code.value                                         | a string containing the ICD-9 code value                                                                          |
| approximate                                               | a boolean of whether or not the mapping from ICD-9 to ICD-10 was direct or more of an approximation.              |
| combination                                               | a boolean of whether or not multiple ICD-9 values were combined and mapped to fewer ICD-10 values.                |
| destination_scenarios                                     | a list of ICD-10 mapping scenarios that apply for the matched ICD-9 code                                          |
| destination_scenarios.choice_lists                        | a list of codes that represent a destination scenario for diagnosis mapping                                       |
| destination_scenarios.choice_lists.description            | a string representing a description of the source ICD-9 code                                                      |
| destination_scenarios.choice_lists.system                 | a string representing the code system (icd9)                                                                      |
| destination_scenarios.choice_lists.value                  | a string containing the ICD-9 code value                                                                          |


#### Example Response

> Example ICD convert response

```json
{
    "approximate": true,
    "combination": false,
    "destination_scenarios": [
        {
            "choice_lists": [
                [
                    {
                        "description": "Type 2 diabetes mellitus with hyperglycemia",
                        "system": "icd10",
                        "value": "E1165"
                    }
                ],
                [
                    {
                        "description": "Type 2 diabetes mellitus with other specified complication",
                        "system": "icd10",
                        "value": "E1169"
                    },
                    {
                        "description": "Other specified diabetes mellitus with ketoacidosis without coma",
                        "system": "icd10",
                        "value": "E1310"
                    }
                ]
            ]
        }
    ],
    "source_code": {
        "description": "Diabetes with ketoacidosis, type II or unspecified type, uncontrolled",
        "system": "icd9",
        "value": "25012"
    }
}
```
