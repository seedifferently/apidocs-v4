## Payments
> Example fetching payments for the current application:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/payments/
```

```python
client.get('/payments/')
```

```ruby
client.request('/payments/')
```

```csharp
client.request("/payments", "GET");
```


> Example response:

```json
[
    {
        "effective_date": "2017-06-02", 
        "id": "5930819201a3af0082bc3dfb", 
        "linked_activity_count": 0, 
        "payment_type": "claim_payment", 
        "received_date": "2017-06-01T21:05:22.335789", 
        "total": {
            "amount": "15096.46", 
            "currency": "USD"
        }, 
        "trading_partner_id": "MOCKPAYER", 
        "transaction_count": 1
    }
]
```


> Example fetching information for a specific payment:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/payments/5930819201a3af0082bc3dfb
```


```python
client.get('/payments/5930819201a3af0082bc3dfb')
```

```ruby
client.request('/payments/5930819201a3af0082bc3dfb')
```

```csharp
client.request("/payments/5930819201a3af0082bc3dfb", "GET");
```


> Example response:

```json
{
    "financial_information": {
        "check_eft_trace_number": "70408535", 
        "effective_date": "2010-09-23", 
        "originating_company_id": "15714001", 
        "payment_amount": {
            "amount": "15096.46", 
            "currency": "USD"
        }, 
        "payment_method": "check", 
        "transaction_handling": "remittance_information_only", 
        "transaction_type": "credit"
    }, 
    "id": "5930819201a3af0082bc3dfb", 
    "linked_activity_count": 0, 
    "payee": {
        "address": {
            "address_lines": [
                "100 Calhoun St",
                "Suite 210"
            ], 
            "city": "CHARLESTON", 
            "state": "SC", 
            "zipcode": "29401"
        }, 
        "name": "POKITDOK INC", 
        "npi": "1912301953", 
        "tax_id": "123456789"
    }, 
    "payer": {
        "address": {
            "address_lines": [
                "100 Calhoun St",
                "Suite 210"
            ], 
            "city": "CHARLESTON", 
            "state": "SC", 
            "zipcode": "29401"
        }, 
        "contacts": [
            {
                "contact_methods": [
                    {
                        "type": "phone", 
                        "value": "8775645029"
                    }
                ], 
                "function": "business"
            }
        ], 
        "name": "POKITDOK MOCKPAYER"
    }, 
    "payment_type": "claim_payment", 
    "trading_partner_id": "MOCKPAYER", 
    "transaction_count": 1
}
```


> Example fetching Raw X12 835 data for a specific payment:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Accept: application/edi-x12" https://platform.pokitdok.com/api/v4/payments/5930819201a3af0082bc3dfb/data
```

```python
import requests

response = requests.get('https://platform.pokitdok.com/api/v4/payments/5930819201a3af0082bc3dfb/data', 
                        headers={'Authorization': 'Bearer {}'.format(access_token), 'Accept': 'application/edi-x12'})
```

```ruby
See cURL example.
```

```csharp
See cURL example.
```


> Example response:

```text
ISA*00*          *00*          *ZZ*123456789      *ZZ*1234           *100101*1000*^*00501*006000600*0*T*:~
GS*HP*123456789*ETIN*20170101*1050*6000600*X*005010X221A1~
ST*835*1740~
BPR*I*219.65*C*ACH*CCP*01*111*DA*33*1234567890**01*111*DA*22*20170101~
.
.
.
SE*42*1740~
GE*1*6000600~
IEA*1*006000600~
```


The Payments endpoint provides access to payment information associated with your application.
Applications receiving claim payments (ERA’s) through PokitDok Platform may review details for claims submitted
through PokitDok Platform as well as payment information received for claims originating outside of
PokitDok Platform.  Applications receiving claim payments may also fetch raw ERA (X12 835) data if
more detail is needed.

### Endpoint Description

Available Payments Endpoints:


Endpoint | HTTP Method | Description
-------- | ----------- | -----------
/payments/ | GET | List payments associated with the application that match the provided search criteria 
/payments/{id} | GET | Return detailed information about the specified payment.  API applications will receive a `payment_id` on their claims activities when they're associated with a payment.  The payment id may also be discovered by a /payments/ search or via a payments callback.
/payments/{id}/data | GET | Return the full data associated with the payment.  By default, it returns a list of claim payment objects as described in the [claim payments reference](claim_payments.html).  The `Accept` header may be used with a value of `application/edi-x12` to access the Raw X12 835 data when the payment type is `claim_payment` 


### Parameters

The `GET /payments/` endpoint accepts the following search parameters:

| Parameter              | Type     | Description                                                                                                                                                                            |
|:-----------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trading_partner_id     | {string} | The trading partner associated with the payment.  This will match the `trading_partner_id` of linked claims activities when payments are returned for claims submitted on the platform |
| payment_type           | {string} | The type of payment that's been received.  This is currently limited to the `claim_payment` type.                                                                                      |
| check_eft_trace_number | {string} | The Check or EFT trace number that is associated with the payment.                                                                                                                     |
| amount                 | {string} | The amount of the payment (e.g. 14123.75 )                                                                                                                                             |
| effective_date         | {string} | The effective date for the payment (e.g. 2017-06-02)                                                                                                                                   |


### Response

The `GET /payments/` response contains the following fields for objects returned in the listing:


| Field                  | Type     | Description                                                                                                                                                                                                |
|:-----------------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| effective_date         | {string} | The effective date for the payment (e.g. 2017-06-02).  Payments may be received prior to their effective date.                                                                                             |
| id                     | {string} | The unique id for the payment.  This id may be used with the other Payments endpoints to retrieve additional information related to the payment                                                            |
| linked_activity_count  | {int}    | The number of activities that were identified within the payment data.  This value may be `0` when payment information is returned to the platform but transactions were submitted outside of the platform |
| payment_type           | {string} | The type of payment that's been received.  This is currently limited to the `claim_payment` type.                                                                                                          |
| received_date          | {string} | The date and time that the payment was received by the platform.                                                                                                                                           |
| total.amount           | {string} | The total amount for the payment.  The payment currency is in `total.currency` and will typically be `USD`                                                                                                 |
| trading_partner_id     | {string} | The trading partner associated with the payment.  This will match the `trading_partner_id` of linked claims activities when payments are returned for claims submitted on the platform                     |
| transaction_count      | {int}    | The total number of transactions found within the payment data.                                                                                                                                            |


The `GET /payments/<id>` response contains the following fields:

| Field                  | Type     | Description                                                                                                                                                                                                |
|:-----------------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| financial_information  | {object} | See the [claim payments reference](claim_payments.html#financial_information_object) for more information on the `financial_information` object                                                            |
| id                     | {string} | The unique id for the payment.  This id may be used with the other Payments endpoints to retrieve additional information related to the payment                                                            |
| linked_activity_count  | {int}    | The number of activities that were identified within the payment data.  This value may be `0` when payment information is returned to the platform but transactions were submitted outside of the platform |
| payee                  | {object} | See the [claim payments reference](claim_payments.html#payee_object) for more information on the `payee` object                                                                                            |
| payer                  | {object} | See the [claim payments reference](claim_payments.html#payer_object) for more information on the `payer` object                                                                                            |
| payment_type           | {string} | The type of payment that's been received.  This is currently limited to the `claim_payment` type.                                                                                                          |
| trading_partner_id     | {string} | The trading partner associated with the payment.  This will match the `trading_partner_id` of linked claims activities when payments are returned for claims submitted on the platform                     |
| transaction_count      | {int}    | The total number of transactions found within the payment data.                                                                                                                                            |


The `GET /payments/<id>/data` response will vary depending upon the type of payment and the `Accept` header value that is included with the request.
By default, payments of type `claim_payment` will return a list of claim payment objects as described in the [claim payments reference](claim_payments.html).
When the `Accept` header is set to `application/edi-x12`, these payments will return the raw X12 835 data associated with the payment.
