## Payers
> Example fetching the list of all payers supported by the platform:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/payers/
```

```python
client.payers()
```

```csharp
client.payers();
```

```ruby
client.payers
```

```java
client.payers();
```

```swift
try client.payers()
```

*Available modes of operation: real-time*

<aside class="warning">
The Payers endpoint will be deprecated in v5. Use <a href="#trading-partners">Trading Partners</a> instead.
</aside>

The Payers endpoint provides access to PokitDok's collection of payer information.

| Endpoint | HTTP Method | Description          |
|:---------|:------------|:---------------------|
| /payers/ | GET         | Get a list of payers |

The /payers/ response contains the following fields

| Field                  | Type      | Description                                                             |
|:-----------------------|:----------|:------------------------------------------------------------------------|
| payer_key              | {string}  | A short name or code representing this payer                            |
| payer_name             | {string}  | Full name for the payer                                                 |
| production_status      | {boolean} | Specifies if the Platform supports data transmissions with the payer.   |
| supported_transactions | {array}   | A list of X12 Transaction set codes, 270, 276, etc, the payer supports. |
| trading_partner_id     | {string}  | An id to be used in requests/EDI files to identify this payer           |
