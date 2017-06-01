## Payments
> Example fetching payments for the current application:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/payments/
```

> Example response:

```json
[
    {
        "effective_date": "2010-09-23", 
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


The Payments endpoint provides access to payment information that's been associated with the application.
Applications that receive payments on the PokitDok platform are able to search and retrieve payment information.  
Applications receiving claim payments are able to fetch the Raw X12 835 data for those payments 
should they have a need for it.

Available Payments Endpoints:


Endpoint | HTTP Method | Description
-------- | ----------- | -----------
/payments/ | GET | List payments associated with the application that match the provided search criteria 
/payments/{id} | GET | Return detailed information about the specified payment.  API applications will receive a `payment_id` on their claims activities when they're associated with a payment.  The payment id may also be discovered by a /payments/ search or via a payments callback.
/payments/{id}/data | GET | Return the full data associated with the payment.  By default, it returns a list of claim payment objects as described in the [claim payments reference](claim_payments.html).  The `Accept` header may be used with a value of `application/edi-x12` to access the Raw X12 835 data when the payment type is `claim_payment` 


The /payments/ endpoint accepts the following search parameters:

| Parameter              | Type     | Description                                                                                                                                                                            |
|:-----------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trading_partner_id     | {string} | The trading partner associated with the payment.  This will match the `trading_partner_id` of linked claims activities when payments are returned for claims submitted on the platform |
| payment_type           | {string} | The type of payment that's been received.  This is currently limited to the `claim_payment` type.                                                                                      |
| check_eft_trace_number | {string} | The Check or EFT trace number that is associated with the payment.                                                                                                                     |
| amount                 | {string} | The amount of the payment (e.g. 14123.75 )                                                                                                                                             |
| effective_date         | {string} | The effective date for the payment                                                                                                                                                     |

