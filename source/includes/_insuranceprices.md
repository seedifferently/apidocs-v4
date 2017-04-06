## Insurance Prices

> example fetching insurance price information

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/prices/insurance?cpt_code=90658&zip_code=94401
```

```python
client.insurance_prices(zip_code='94401', cpt_code='90658')
```

```csharp
client.pricesInsurance(
			new Dictionary<string, string> {
				{ "zip_code", "94401" },
				{ "cpt_code", "90658" }
			});
```

```ruby
client.insurance_prices({zip_code: '94401', cpt_code: '90658'})
```

```java
HashMap<String, String>() query = new HashMap<String, String>();
query.put("zip_code", "94401");
query.put("cpt_code", "90658");

client.insurancePrices(query);
```

```swift
try client.insurancePrices(cptCode: "90658", zipCode: "94401")
```

>Example Response:

```json
{
  "amounts": [
    {
      "high_price": 40.34,
      "standard_deviation": 6.362073336381782,
      "average_price": 20.896499999999996,
      "payer_type": "insurance",
      "payment_type": "allowed",
      "low_price": 14.8,
      "median_price": 20.33
    },
    {
      "high_price": 54.62,
      "standard_deviation": 10.572772826345037,
      "average_price": 32.0905,
      "payer_type": "insurance",
      "payment_type": "submitted",
      "low_price": 22.42,
      "median_price": 31.2
    }
  ],
  "cpt_code": "90658",
  "geo_zip_area": "944"
}
```

*Available modes of operation: real-time*

The Insurance Prices endpoint allows access to our collection of insurance
pricing data. The data comes from private payer data as well as data from
Medicare.

While the endpoint requires a five-digit zip code, only the first three digits
are significant. This is because the index is only granular to the first three
digits of the zip code, commonly called a "geozip" or a "ZIP Code Prefix". These
three digits refer to the geographical regions surrounding major cities or
metropolitan areas. There are approximately 900 "geozips" in the United States.

Available Insurance Prices Endpoints:

| Endpoint          | HTTP Method | Description                                                                                 |
|:------------------|:------------|:--------------------------------------------------------------------------------------------|
| /prices/insurance | GET         | Return a list of prices for a given procedure (by CPT Code) in a given region (by ZIP Code) |

The /prices/insurance endpoint accepts the following parameters:

| Parameter  | Type     | Description                                | Presence |
|:-----------|:---------|:-------------------------------------------|:---------|
| cpt_code   | {string} | The CPT code of the procedure in question  | Required |
| zip_code   | {string} | Zip code in which to search for procedures | Required |

The /prices/insurance response contains the following fields:

| Field                 	  | Type      | Description                                                     | Presence |
|:----------------------------|:----------|:----------------------------------------------------------------|:---------|
| cpt_code      	    	  | {string}  | The CPT code of the procedure                                   | Required |
| geo_zip_area  			  | {string}  | The three character zip code tabulation area code               | Required |
| amounts.high_price    	  | {decimal} | The maximum price for the procedure                             | Required |
| amounts.standard_deviation  | {decimal} | Standard deviation of the insurance price amounts.              | Required |
| amounts.average_price 	  | {decimal} | The weighted average price based on the number of procedures    | Required |
| amounts.low_price     	  | {decimal} | The lowest price for the procedure                              | Required |
| amounts.median_price  	  | {decimal} | The median price for the procedure                              | Required |
| amounts.payer_type    	  | {string}  | The insurance payer type: insurance or medicare                 | Required |
| amounts.payment_type  	  | {string}  | Possible values are "allowed", "submitted", "paid", or "standardized". The allowed amount when payer_type:insurance is the dollar amount typically considered payment-in-full by a payer and an associated network of healthcare providers. For Medicare (when payer_type:medicare) the allowed amount is the average of the Medicare allowed amount for the service; this figure is the sum of the amount Medicare pays, the deductible and coinsurance amounts, and any amounts that a third party is responsible for paying. The submitted amount is the dollar amount the provider submitted to the payer in the insurance claim. The paid amount is the dollar amount that was reimbursed to the provider.  The standardized amount removes geographic differences in payment rates for individual services. | Required |
