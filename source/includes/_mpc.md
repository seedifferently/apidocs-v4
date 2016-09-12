## Medical Procedure Code
> Example fetching medical procedure information by code:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/mpc/99213
```

```python
client.mpc(code='99213')
```

```csharp
client.medicalProcedureCode("99211");
```

```ruby
client.mpc({code: '99213'})
```

```java
HashMap<String, String>() query = new HashMap<String, String>();
query.put("code", "office");

client.mpc(query);
```

>Example Response:

```json
{
  "code": "99213",
  "name": "Established patient office or other outpatient visit, typically 15 minutes",
  "description": "Level 3 outpatient visit for evaluation and management of establlished patient with problem of low to moderate severity, including expanded history and medical decision making of low complexity - typical time with patient and/or family 15 minutes"
}
```

> Example searching medical procedure information by consumer friendly name:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/mpc/?name=office
```

```python
client.mpc(name='office')
```

```csharp
client.medicalProcedureCode(
    new Dictionary<string, string> {
        {"name", "Established patient office or other outpatient visit, typically 15 minutes"}
    });
```

```ruby
client.mpc({name: 'office'})
```

```java
HashMap<String, String>() query = new HashMap<String, String>();
query.put("name", "office");

client.mpc(query);
```

> Example Response:

```json
[
  {
    "code": "99244",
    "name": "Patient office consultation, typically 60 minutes",
    "description": "Level 4 outpatient consultation for established patient with problem of moderate to high severity, including comprehensive history and physical examination and medical decision making of moderate complexity - typical time with patient and/or family 60 minutes"
  },
  {
    "code": "99243",
    "name": "Patient office consultation, typically 40 minutes",
    "description": "Level 3 outpatient consultation for established patient with problem of moderate severity, including detailed history and physical examination and medical decision making of moderate complexity - typical time with patient and/or family 40 minutes"
  },
  {
    "code": "99242",
    "name": "Patient office consultation, typically 30 minutes",
    "description": "Level 2 outpatient consultation for established patient with problem of low severity, including expanded problem focused history and physical examination and straightforward medical decision making - typical time with patient and/or family 30 minutes"
  },
  {
    "code": "99241",
    "name": "Patient office consultation, typically 15 minutes",
    "description": "Level 1 outpatient consultation for established patient with self-limited and/or minor problem, including problem focused history and physical examination and straightforward medical decision making - typical time with patient and/or family 15 minutes"
  },
  {
    "code": "99245",
    "name": "Patient office consultation, typically 80 minutes",
    "description": "Level 5 outpatient consultation for established patient with problem of moderate to high severity, including comprehensive history and physical examination and medical decision making of high complexity - typical time with patient and/or family 80 minutes"
  },
  {
    "code": "99050",
    "name": "Services provided in the office when the office is normally closed",
    "description": "Services provided in the office at times other than regularly scheduled office hours, or days when the office is normally closed"
  },
  {
    "code": "99051",
    "name": "Services provided in an office during regularly scheduled office hours, evening, weekend, or holiday",
    "description": "Services provided in the office during regularly scheduled evening, weekend, or holiday office hours"
  }
]
```

*Available modes of operation: real-time only*

The Medical Procedure Code endpoints provide access to clinical and consumer
friendly information related to medical procedures. It's useful for identifying
the procedure code (or codes) that match search queries. It can also be used
for determining the official descriptions for a specific procedure code.

Available Medical Procedure Code Endpoints:

| Endpoint    | HTTP Method | Description                                                                 |
|:------------|:------------|:----------------------------------------------------------------------------|
| /mpc/       | GET         | Get a list of medical procedure information meeting certain search criteria |
| /mpc/{code} | GET         | Retrieve the data for a specific procedure code                             |

The /mpc/ endpoint accepts the following parameters:

| Parameter   | Type     | Description                                                                      | Presence |
|:------------|:---------|:---------------------------------------------------------------------------------|:---------|
| name        | {string} | Search medical procedure information by consumer friendly name                   | Optional |
| description | {string} | A partial or full description to be used to locate medical procedure information | Optional |

The /mpc/ response contains the following fields:

| Field       | Type     | Description                                        | Presence |
|:------------|:---------|:---------------------------------------------------|:---------|
| code        | {string} | The procedure code                                 | Required |
| name        | {string} | A consumer friendly name for the medical procedure | Required |
| description | {string} | The medical procedure's clinical description       | Optional |
