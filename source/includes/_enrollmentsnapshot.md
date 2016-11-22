## Enrollment Snapshot

> Example submitting an enrollment snapshot for the MOCKPAYER trading partner:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -XPOST -F file=@current_membership_enrollment.834 -F trading_partner_id=MOCKPAYER  https://platform.pokitdok.com/api/v4/enrollment/snapshot
```

```python
client.enrollment_snapshot('MOCKPAYER', '/path/to/current_membership_enrollment.834')
```

```csharp
client.enrollmentSnapshot("MOCKPAYER", "/path/to/current_membership_enrollment.834");
```

```ruby
client.enrollment_snapshot('MOCKPAYER', '/path/to/current_membership_enrollment.834')
```

```java
client.enrollmentSnapshot("MOCKPAYER", "/path/to/current_membership_enrollment.834");
```

```swift
try client.enrollmentSnapshot(tradingPartnerId: "MOCKPAYER", x12FilePath: "/path/to/current_membership_enrollment.834")
```

> Example response:

```json
{
  "units_of_work": 1,
  "_type": "PlatformActivityModel",
  "name": "enrollment_snapshot_PostTest",
  "parameters": {
    "trading_partner_id": "MOCKPAYER"
  },
  "remaining_transitions": [
    "wait",
    "receive",
    "notify",
    "complete"
  ],
  "_uuid": "580042ca-d23a-478f-b414-21dbccfc1ada",
  "state": {
    "name": "scheduled",
    "title": "Scheduled for execution"
  },
  "trading_partner_id": "MOCKPAYER",
  "id": "57571d8d0640fd3171a95552",
  "transition_path": [
    "schedule",
    "wait",
    "receive",
    "notify",
    "complete"
  ],
  "history": [
    {
      "record_dt": "2016-06-25T19:16:29.458590",
      "name": "init",
      "title": "Initializing"
    }
  ]
}
``` 

> Example fetching a list of enrollment snapshots owned by the current application:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/enrollment/snapshot
```

```python
client.enrollment_snapshots()
```

```csharp
client.enrollmentSnapshot();
```

```ruby
client.enrollment_snapshots
```

```java
client.enrollmentSnapshots();
```

```swift
try client.enrollmentSnapshots()
```

> Example response:

```json
[
  {
    "snapshot_date": "2016-05-25T20:21:47.099000",
    "trading_partner_id": "MOCKPAYER",
    "snapshot_id": "5744b7db0640fd757c0c0d6e"
  },
  {
    "snapshot_date": "2016-05-25T20:21:46.168000",
    "trading_partner_id": "MOCKPAYER",
    "snapshot_id": "5744b7da0640fd757c0c0d67"
  }
]
```

> Example fetching information for a specific enrollment snapshot owned by the current application:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/enrollment/snapshot/5317f51527a27620f2ec7533
```

```python
client.enrollment_snapshots(snapshot_id='5317f51527a27620f2ec7533')
```

```csharp
client.enrollmentSnapshot("5317f51527a27620f2ec7533");
```

```ruby
client.enrollment_snapshots({snapshot_id: '5317f51527a27620f2ec7533'})
```

```java
client.enrollmentSnapshot("5317f51527a27620f2ec7533");
```

```swift
try client.enrollmentSnapshots(snapshotId: "5317f51527a27620f2ec7533")
```

> Example response:

```json
{
    "snapshot_date": "2016-06-25T19:42:45.395000",
    "trading_partner_id": "MOCKPAYER",
    "snapshot_id": "5317f51527a27620f2ec7533"
}
```

> Example fetching enrollment data associated with a specific enrollment snapshot owned by the current application:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/enrollment/snapshot/5317f51527a27620f2ec7533/data
```

```python
client.enrollment_snapshot_data('5317f51527a27620f2ec7533')
```

```csharp
client.enrollmentSnapshotData("5317f51527a27620f2ec7533");
```

```ruby
client.enrollment_snapshot_data(snapshot_id: '5317f51527a27620f2ec7533')
```

```java
client.enrollmentSnapshotData("5317f51527a27620f2ec7533");
```

```swift
try client.enrollmentSnapshotData(snapshotId: "5317f51527a27620f2ec7533")
```

> Example response: 

```json
[
  {
    "reference_number": "a4db5c6981cb418eab3401fa36dbf1b6",
    "trading_partner_id": "MOCKPAYER",
    "payer": {
      "name": "WELLPOINT COMPANY",
      "tax_id": "953760001"
    },
    "subscriber": {
      "maintenance_type": "Addition",
      "first_name": "JOHN",
      "last_name": "DOE",
      "benefits": [
        {
          "maintenance_type": "Addition",
          "begin_date": "2015-09-25",
          "late_enrollment": false,
          "benefit_type": "Preferred Provider Organization",
          "description": "1K4C"
        },
        {
          "maintenance_type": "Addition",
          "begin_date": "2015-09-25",
          "late_enrollment": false,
          "benefit_type": "Dental",
          "description": "1QCS"
        }
      ],
      "relationship": "Self",
      "benefit_status": "Active",
      "gender": "Male",
      "employment_status": "Full-time",
      "group_or_policy_number": "A64692",
      "maintenance_reason": "Active",
      "handicapped": false,
      "hire_date": "2015-08-25",
      "eligibility_begin_date": "2015-09-25",
      "ssn": "777999542",
      "address": {
        "city": "CANOGA PARK",
        "line": "123 MAIN ST",
        "postal_code": "91303",
        "state": "CA"
      },
      "birth_date": "1985-11-25",
      "substance_abuse": false,
      "tobacco_use": false
    },
    "correlation_id": "acafbe38-e4fa-4af0-808b-147056dd391b",
    "purpose": "Original",
    "action": "Change",
    "dependents": [],
    "sponsor": {
      "name": "ACME INC",
      "tax_id": "123456789"
    }
  }
]
```

*Available modes of operation: batch/async only*

The enrollment snapshot endpoint allows client applications to establish the current state of benefits enrollment for a
group that will be managed via the [enrollment](#benefits-enrollment) endpoint.
Many enrollment trading partners require full X12 834 files to be delivered each time changes are made to membership
information for a group.  The enrollment snapshot functionality allows you to easily establish the current state of a
group using your application such that you can focus on making [enrollment](#benefits-enrollment) requests when new members are added
or when existing members need to make changes.  All of the trading partner specifics around the handling of full files
will be handled in the background for your application.  Typically, the enrollment snapshot functionality will be used
when your application first begins handling enrollment transactions for a group.  As enrollment transactions are acknowledged
by a trading partner, new enrollment snapshots are automatically created to reflect the current state of benefits enrollment
for the group.

Enrollment snapshot may also be used periodically to synchronize with another membership system or as part of an audit.
Many applications may find that they only need to use enrollment snapshot once for each group using their application
and then they can move forward making only [enrollment](#benefits-enrollment) API requests to manage additions, changes
and terminations. Applications may also find the enrollment snapshot index and data access suitable for providing
point-in-time reporting for groups using their system.


| Endpoint                       | HTTP Method | Description                                                                                          |
|:-------------------------------|:------------|:-----------------------------------------------------------------------------------------------------|
| /enrollment/snapshot           | POST        | Submit a X12 834 file as the current snapshot of a group's benefits enrollment data                  |
| /enrollment/snapshot           | GET         | List enrollment snapshots owned by the current application                                           |
| /enrollment/snapshot/{id}      | GET         | Get information about a specific enrollment snapshot owned by the current application                |
| /enrollment/snapshot/{id}/data | GET         | List enrollment data associated with a specific enrollment snapshot owned by the current application |

The enrollment snapshot endpoint requires these parameters when creating a new enrollment snapshot:

| Parameter         | Description                                                              |
|:-------------------|:-------------------------------------------------------------------------|
| file               | X12 834 file containing the full benefits enrollment for a group         |
| trading_partner_id | the id of the trading partner to be associated with this enrollment data |

The /enrollment/snapshot POST returns an enrollment snapshot activity object. For reference take a look at the activites response object [above](#activities_response).

The /enrollment/snapshot GET response includes the following fields:

| Field                  | Type      | Description                                                              												                           |
|:-----------------------|:----------|:----------------------------------------------------------------------------------------------------------------------------|
| snapshot_date          | {datetime}| The date of the snapshot. In ISO8601 format (YYYY-MM-DDThh:mm:ss.ssssss).                                 				 							 |
| trading_partner_id     | {string}	 | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.			       |
| snapshot_id            | {string}  | The id of the snapshot.                                 				 													                                   |

The /enrollment/snapshot/{id}/data returns a list of enrollment request objects. For reference take a look at the enrollment request object [above](#enrollment_table).

