---
layout: 2column
---

# Claim Payments Reference

The claims endpoint makes it easy to submit claims transactions to trading partners.
If you've enrolled for claim payment processing (Electronic Remittance Advice), valid claims requests will
receive a claim payment result after adjudication is complete.  For more information about enrolling for electronic remittance advice delivery via PokitDok, please contact us.

This document describes the PokitDok claim payment (835) result format.
It's meant to accompany the summary of claims functionality in
the [PokitDok Platform API Documentation](/documentation/v4).
All possible subobjects and acceptable field values are presented.

The claim payment result consists of a top-level JSON object, described
in the "Claim Payment Result Object" section below. This object can contain a number
of sub-objects as needed to describe the result, such as financial information and
patient information. Each sub-object is described in its own table, which
is linked from the "Type" parameter. Note that some sub-objects can themselves
be comprised of other objects.


# Claim Payment Result Object
<a name="claim_payment"></a>

| Parameters                      | Type                                                                                      | Description                                                                                                              | Required? |
|:--------------------------------|:------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------|
| adjudication_system_version     | {string}                                                                                  | The version number of the adjudication system that generated the claim payments.                                         | No        |
| authorization_number            | {string}                                                                                  | The authorization number associated with the claim.                                                                       | No        |
| claim_payments                  | List of <a href="#claim_payment_object">Claim Payment objects</a>                         | A list of payments that were processed as part of this claim.                                                            | Yes       |
| coverage_amount                 | <a href="#monetary_object">Monetary Amount object</a>                                     | Monetary amount to report the total covered charges for the claim.                                                       | No        |
| coverage_expiration_date        | {string}                                                                                  | The coverage expiration date.                                                                                             | No        |
| crossover_carrier               | <a href="#crossover_carrier_object">Crossover Carrier object</a>                          | The crossover carrier may be populated when the claim is transferred to another payer for processing after being finalized by the current payer.    | No        |
| discount_amount                 | <a href="#monetary_object">Monetary Amount object</a>                                     | Monetary amount representing discounts applied to the claim based on contractual obligations, etc.                       | No        |
| financial_information           | <a href="#financial_information_object">Financial Information object</a>                  | Financial institution information related to the claim payment.                                                           | Yes       |
| insured                         | <a href="#insured_object">Insured object</a>                                              | The insured information related to the claim.  This will be set when the patient is not also the insured.                | No        |
| interest_amount                 | <a href="#monetary_object">Monetary Amount object</a>                                     | Monetary amount representing interest applied to the claim.                       | No        |
| medical_record_number           | {string}                                                                                  | The medical record number associated with the claim.                                                                      | No        |
| meta          | <a href="#meta_object">Meta object</a>                                                                      | Additional information related to the transaction.                                                                      | No        |
| patient                         | <a href="#patient_object">Patient object</a>                                              | The patient information related to the claim.                                                                            | Yes       |
| payee                           | <a href="#payee_object">Payee object</a>                                                  | The payee information related to the claim.                                                                              | Yes       |
| payer                           | <a href="#payer_object">Payer object</a>                                                  | The payer information related to the claim.                                                                              | Yes       |
| patient_responsibility_amount   | <a href="#monetary_object">Monetary Amount object</a>                                     | Monetary amount left to be paid by the patient/insured.                                                                   | No        |
| prior_authorization_number      | {string}                                                                                  | The prior authorization number associated with the claim.                                                                | No        |
| production_date                 | {string}                                                                                  | The date the claim was processed.                                                                                         | No        |
| received_date                   | {string}                                                                                  | The date the claim was received.                                                                                         | No        |
| statement_period_start_date     | {string}                                                                                  | The claim statement period start date.                                                                                    | No        |
| statement_period_end_date       | {string}                                                                                  | The claim statement period end date.                                                                                      | No        |
| payment_adjustments           | <a href="#payment_adjustment_object">Payment Adjustment Object</a>             | A list of payment adjustments related to the claim payment.                                                              | No       |
| transaction_type                | {string}                                                                                  | The transaction type.  See <a href="#transaction_type_codes">Transaction Type Codes</a> for possible values.             | Yes       |


<a name="claim_payment_object"></a>
## Claim Payments object
| Parameters                 | Type                                                             | Description                       | Required? |
|:---------------------------|:-----------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|:----------|
| adjudication                | <a href="#outpatient_object">Outpatient object</a> or <a href="#inpatient_object">Inpatient object</a>        | Object outlining either outpatient or inpatient adjudication information                                                                               | No        |
| adjustments                | List of <a href="#adjustment_object">Adjustment objects</a>      | A list of adjustments that apply to the claim payment.                                                                                | No        |
| assigned_number            | {int}                                                            | Number assigned to the claim payment.                                                                                                  | No        |
| control_number             | {string}                                                         | Control number assigned by the payer to the claim payment.                                                                                          | Yes       |
| filing_indicator           | {string}                                                         | Filing indicator for this claim payment.  Possible values are listed in <a href="#filing_indicator_codes">Filing Indicator Codes</a>  | No        |
| patient_control_number     | {string}                                                         | Patient control number reference for the claim payment.  This value will always be PokitDok's encoded Activity ID when the claim is submitted via PokitDok's Claims API and can be used to ping the Activities API to retrieve original claim submission information.                                                                                | Yes       |
| payment_amount             | <a href="#monetary_object">Payment amount object</a>             | Claim payment amount.                                                                                                                  | Yes       |
| services                   | List of <a href="#service_object">Service objects</a>            | A list of services covered by this claim payment.                                                                                     | No        |
| status                     | {string}                                                         | Status of this claim payment.  Possible values are listed in <a href="#claim_payment_status_codes">Status Codes</a>.                   | Yes       |
| total_charge_amount        | <a href="#monetary_object">Total charge amount object</a>        | Total charge amount for services included in this claim payment.                                                                       | Yes       |


(<a href="#claim_payment">Back to Claim Payment Result</a>)


<a name="adjustment_object"></a>
## Adjustment object
| Parameters   | Type                                                  | Description                                                                                                                 | Required? |
|:-------------|:------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|:----------|
| amount       | <a href="#monetary_object">Monetary Amount object</a> | The amount of the adjustment.                                                                                               |           |
| group        | {string}                                              | The group classification of the adjustment. Possible values are listed in <a href="#adjustment_group_codes">Group Codes</a> |           |
| reason       | {string}                                              | The reason for the adjustment.                                                                                              |           |
| reason_code  | {string}                                              | The numerical reason code value for the adjustment reason.                                                                  |           |
| quantity     | {string}                                              | The number of items impacted by the adjustment.                                                                             |           |


(<a href="#claim_payment_object">Back to Claim Payment Object</a>)


<a name="service_object"></a>
## Services object
| Parameters                       | Type                                                            | Description                                                           | Required? |
|:---------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------------|:----------|
| adjudicated_procedure_code       | {string}                                                        | The procedure code that was adjudicated for the service.              | Yes       |
| adjudicated_procedure_code_qualifier       | {string}                                                        | The qualifier for the procedure code that was adjudicated for the service.  Possible values included in <a href="#procedure_code_qualifiers">Procedure Code Qualifiers</a>.              | Yes       |
| adjudicated_procedure_modifier_codes       | {string}                                                        | The modifiers for the procedure code that was adjudicated for the service.          | No        |
| charge_amount                    | <a href="#monetary_object">Monetary Amount object</a>           | The amount charged for the service on the claim.                      | Yes       |
| allowed_amount                   | <a href="#monetary_object">Monetary Amount object</a>           | The allowed amount is the amount the payer deems payable prior to considering patient responsibility for the service on the claim.     | No       |
| late_filing_amount               | <a href="#monetary_object">Monetary Amount object</a>           | The deduction amount for the late filing reduction for the service on the claim.                      | No       |
| provider_payment_amount          | <a href="#monetary_object">Monetary Amount object</a>           | The amount the provider was paid for the service.                     | Yes       |
| submitted_procedure_code         | {string}                                                        | The procedure code that was submitted in the claim for the service.   | No        |
| service_units_paid               | {int}                                                           | The number of service units that were paid.                           | No        |
| service_units_submitted          | {int}                                                           | The number of service units that were submitted on the claim.         | No        |
| control_number                   | {string}                                                        | The control number assigned to the service line.  This is the line item control number submitted on the original claim in claim.service_lines[].provider_control_number and is required to be returned if submitted.                    | No        |
| location_number                  | {string}                                                        | The location number assigned to the service line.  This is the payer’s identification value for the provider location associated with a claim. This should be populated by the payer when the location affected the payment of the claim.                    | No        |
| service_date                     | {string}                                                         | The service date assigned to this service line.                    | No        |
| adjustments                      | {list}                                                        | Adjustments applicable to the service line.  Uses the <a href="#adjustment_object">Adjustment object</a>                              | No       |
| remarks                          | {list}                                                        | A list of health care remark codes applicable to the claim payment.  Uses the <a href="#remarks_object">Remarks object</a>                              | No       |

(<a href="#claim_payment_object">Back to Claim Payment Object</a>)


<a name="financial_information_object"></a>
## Financial Information object
| Parameters                   | Type                                                                     | Description                                                                                                              | Required?|
|:-----------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| check_eft_trace_number       | {string}                                                                 | The check or electronic funds transfer trace number.                                                                     | Yes      |
| transaction_type             | {string}                                                                 | The transaction type.  See <a href="#transaction_type_codes">Transaction Type Codes</a> for possible values.             | Yes      |
| effective_date               | {string}                                                                 | The effective date of the payment.                                                                                       | No       |
| payer_id                     | {string}                                                                 | The payer id associated with this financial information.                                                                  | No       |
| originating_company_id       | {string}                                                                 | The originating company id associated with this financial information.                                                    | No       |
| originating_institution      | <a href="#financial_institution_object">Financial Institution object</a> | The originating institution associated with this financial information.                                                   | No       |
| receiving_institution        | <a href="#financial_institution_object">Financial Institution object</a> | The receiving institution associated with this financial information.                                                     | No       |
| payment_amount               | <a href="#monetary_object">Monetary Amount object</a>                    | The amount paid.                                                                                                         | Yes      |
| payment_method               | {string}                                                                 | The method used to pay the claim.  See <a href="#payment_method_codes">Payment Method Codes</a> for possible values.     | Yes      |
| transaction_handling         | {string}                                                                 | The payment transaction type.  See <a href="#transaction_type_codes">Transaction Type Codes</a> for possible values.     | Yes      |

(<a href="#claim_payment">Back to Claim Payment Result</a>)


<a name="financial_institution_object"></a>
## Financial Institution object
| Parameters         | Type            | Description                                                                                                         | Required?|
|:-------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------|:---------|
| account_number     | {string}        | The bank account number used for claim payment.                                                                     | Yes      |
| account_type       | {string}        | The type of bank account.  See <a href="#account_type_codes">Account Type Codes</a> for possible values.            | Yes      |
| routing_number     | {string}        | The bank routing number used for claim payment.                                                                     | Yes      |


(<a href="#financial_information_object">Back to Financial Information object</a>)


<a name="insured_object"></a>
## Insured object
| Parameters    | Type     | Description                            | Required? |
|:--------------|:---------|:---------------------------------------|:----------|
| first_name    | {string} | The insured's first name.              | Yes       |
| middle_name   | {string} | The insured's middle name.             |           |
| last_name     | {string} | The insured's last name.               | Yes       |
| id            | {string} | The member ID assigned to the insured. |           |
| hic_number    | {string} | The health insurance claim number      |           |

(<a href="#claim_payment">Back to Claim Payment Result</a>)


<a name="patient_object"></a>
## Patient object
| Parameters    | Type     | Description                            | Required? |
|:--------------|:---------|:---------------------------------------|:----------|
| first_name    | {string} | The patient's first name.              | Yes       |
| middle_name   | {string} | The patient's middle name.             |           |
| last_name     | {string} | The patient's last name.               | Yes       |
| id            | {string} | The member ID assigned to the patient. |           |
| hic_number    | {string} | The health insurance claim number      |           |

(<a href="#claim_payment">Back to Claim Payment Result</a>)


<a name="payee_object"></a>
## Payee object
| Parameters | Type                                                  | Description                                | Required? |
|:-----------|:------------------------------------------------------|:-------------------------------------------|:----------|
| name       | {string}                                              | The name of the payee.                     | Yes       |
| npi        | {string}                                              | The payee's NPI.                           | No        |
| tax_id     | {string}                                              | The tax ID of the payee.                   | No        |
| address    | <a href="#address_object">Address object</a>          | The address of the payee.                   | No        |
| contacts   | List of <a href="#contact_object">Contact objects</a> | A list of contacts for the payee.          | No        |

(<a href="#claim_payment">Back to Claim Payment Result</a>)


<a name="payer_object"></a>
## Payer object
| Parameters | Type                                                                | Description                       | Required? |
|:-----------|:--------------------------------------------------------------------|:----------------------------------|:----------|
| name       | {string}                                                            | The name of the payer.            | Yes       |
| address    | <a href="#address_object">Address object</a>                        | The address of the payer.         | No        |
| contacts   | List of <a href="#contact_object">Contact objects</a>               | A list of contacts for the payer. | No        |
| id         | {string}                                                            | The id of the payer.              | No        |

(<a href="#claim_payment">Back to Claim Payment Result</a>)


<a name="crossover_carrier_object"></a>
## Crossover Carrier object
| Parameters | Type                                                                | Description                       | Required? |
|:-----------|:--------------------------------------------------------------------|:----------------------------------|:----------|
| name       | {string}                                                            | The name of the payer.            | Yes       |
| bcbs_plan_code   | {string}                                                      | The Blue Cross Blue Shield Association Plan Code of the payer.              | No        |
| tax_id     | {string}                                                            | The tax id of the payer.              | No        |
| naic_id    | {string}                                                            | The National Association of Insurance Commissioners identification of the payer.              | No        |
| payor_id   | {string}                                                            | The id of the payer.              | No        |
| pharmacy_processor_number   | {string}                                           | The Pharmacy Processor Number of the payer.              | No        |
| plan_id   | {string}                                                             | The Centers for Medicare and Medicaid Services PlanID of the payer.              | No        |

(<a href="#claim_payment">Back to Claim Payment Result</a>)


<a name="address_object"></a>
## Address object
| Parameter       | Type             | Description                                                             | Required? |
|:----------------|:-----------------|:------------------------------------------------------------------------|:----------|
| address_lines   | List of {string} | Street address information. (e.g. [“123 N MAIN ST”, "UNIT 20"])         | Yes       |
| city            | {string}         | city information. (e.g. “SAN MATEO”)                                    | Yes       |
| state           | {string}         | state information. (e.g. “CA”)                                          |           |
| zipcode         | {string}         | zip/postal code. (e.g. “94401”)                                         |           |
| country         | {string}         | country information. (e.g. “USA”)                                       |           |

(<a href="#payer_object">Back to Payer object</a>)


<a name="contact_object"></a>
## Contact object
| Parameter       | Type                                           | Description                          | Required? |
|:----------------|:-----------------------------------------------|:-------------------------------------|:----------|
| name            | {string}                                       | The name of the contact.              |           |
| contact_methods | List of <a href="#contact_method_object">Contact Method objects</a> |  Contact methods.                     |           |

(<a href="#payer_object">Back to Payer object</a>)


<a name="contact_method_object"></a>
## Contact Method object
| Parameter       | Type       | Description                                                                                                                | Required? |
|:----------------|:-----------|:---------------------------------------------------------------------------------------------------------------------------|:----------|
| type            | {string}   | The type of contact method.  See <a href="#contact_method_type_codes">Contact Method Type Codes</a> for possible values.   |           |
| value           | {string}   |  A value representing a Phone number, email address, etc.                                                                  |           |

(<a href="#payer_object">Back to Payer object</a>)


<a name="monetary_object"></a>
## Monetary Amount object
| Parameters | Type     | Description                       | Required? |
|:-----------|:---------|:----------------------------------|:----------|
| currency   | {string} | The type of currency. (e. g. USD) |           |
| amount     | {string} | The amount of currency.           |           |

(<a href="#claim_payment">Back to Claim Payment Result</a>)

<a name="meta_object"></a>
## Meta object
| Parameters | Type     | Description                       | Required? |
|:-----------|:---------|:----------------------------------|:----------|
| transaction_created_date   | {string} | The date the file was generated by the trading partner |           |

(<a href="#claim_payment">Back to Claim Payment Result</a>)

<a name="remarks_object"></a>
## Remarks object
| Parameters | Type     | Description                       | Required? |
|:-----------|:---------|:----------------------------------|:----------|
| description   | {string} | The claim payment remark provided by the trading partner to clarify the adjudication message for a given service line  |Yes       |
| code   | {string} | The numerical value associated with the remark | Yes       |

(<a href="#service_object">Back to Service Object</a>)

<a name="outpatient_object"></a>
## Outpatient object
| Parameters | Type     | Description                       | Required? |
|:-----------|:---------|:----------------------------------|:----------|
| remarks   | {list} | A list of health care remark codes applicable to the claim payment.  Uses the <a href="#remarks_object">Remarks object</a>  | No       |
| reimbursement_rate   | {float} | The percentage for reimbursement rate applied to the claim payment | No       |
| claim_hcpcs_payable   | <a href="#monetary_object">Monetary Amount object</a>   | The claim Health Care Financing Administration Common Procedural Coding System (HCPCS) payable amount | No       |
| claim_esrd_payment   | <a href="#monetary_object">Monetary Amount object</a>   | The End Stage Renal Disease (ESRD) payment amount | No       |
| nonpayable_professional_component   | <a href="#monetary_object">Monetary Amount object</a>  | The professional component amount billed but not payable | No       |

(<a href="#claim_payment_object">Back to Claim Payment Object</a>)

<a name="inpatient_object"></a>
## Inpatient object
| Parameters | Type     | Description                       | Required? |
|:-----------|:---------|:----------------------------------|:----------|
| remarks   | {list} | A list of health care remark codes applicable to the claim payment.  Uses the <a href="#remarks_object">Remarks object</a>  | No       |
| covered_days_or_visits   | {int} | The covered days or visits | No       |
| lifetime_psychiatric_days   | {int}   | The lifetime psychiatric days | No       |
| old_capital   | <a href="#monetary_object">Monetary Amount object</a>  | The old capital amount | No       |
| cost_report_days   | {int}   | The count of cost report days | No       |
| nonpayable_professional_component   | <a href="#monetary_object">Monetary Amount object</a>   | The professional component amount billed but not payable | No       |
| prospective_payment_system   | <a href="#pps_object">Prospective Payment System object</a>   | Information related to the prospective payment system (PPS) | No       |
| claim   | <a href="#claim_object">Claim object</a>   | Items related to the inpatient claim adjudication | No       |

(<a href="#claim_payment_object">Back to Claim Payment Object</a>)

<a name="pps_object"></a>
## Prospective Payment System object
| Parameters | Type     | Description                       | Required? |
|:-----------|:---------|:----------------------------------|:----------|
| capital   | <a href="#capital_object">Capital object</a> | Items related to capital  | No       |
| operating_outlier   | <a href="#monetary_object">Monetary Amount object</a>  | The Prospective Payment System (PPS) Operating Outlier amount | No       |
| operating_hospital_specific_drg   | <a href="#monetary_object">Monetary Amount object</a>   | The hospital specific Diagnosis Related Group (DRG) amount | No       |
| operating_federal_specific_drg   | <a href="#monetary_object">Monetary Amount object</a>  | The federal specific Diagnosis Related Group (DRG) amount | No       |

(<a href="#inpatient_object">Back to Inpatient Object</a>)

<a name="claim_object"></a>
## Claim object
| Parameters | Type     | Description                       | Required? |
|:-----------|:---------|:----------------------------------|:----------|
| diagnosis_related_group   | <a href="#monetary_object">Monetary Amount object</a>  | The Diagnosis Related Group (DRG) amount  | No       |
| disproportionate_share   | <a href="#monetary_object">Monetary Amount object</a>  | The disproportionate share amount | No       |
| medicare_secondary_payer_pass_through   | <a href="#monetary_object">Monetary Amount object</a>   | The Medicare Secondary Payer (MSP) pass-through amount | No       |
| prospective_payment_system_capital   | <a href="#monetary_object">Monetary Amount object</a>  | The total Prospective Payment System (PPS) capital amount | No       |
| prospective_payment_system_capital_outlier   | <a href="#monetary_object">Monetary Amount object</a>   | The Prospective Payment System (PPS) Capital Outlier amount | No       |
| indirect_teaching   | <a href="#monetary_object">Monetary Amount object</a>  | The indirect teaching amount | No       |

(<a href="#inpatient_object">Back to Inpatient Object</a>)

<a name="capital_object"></a>
## Capital object
| Parameters | Type     | Description                       | Required? |
|:-----------|:---------|:----------------------------------|:----------|
| federal_specific_portion_drg   | <a href="#monetary_object">Monetary Amount object</a> | The Prospective Payment System (PPS) capital, federal specific portion, Diagnosis Related Group (DRG) amount  | No       |
| hospital_specific_portion_drg   | <a href="#monetary_object">Monetary Amount object</a>  | The Prospective Payment System (PPS) capital, hospital specific portion, Diagnosis Related Group (DRG) amount | No       |
| disproportionate_share_hospital_specific_drg   | <a href="#monetary_object">Monetary Amount object</a>   | The Prospective Payment System (PPS) capital, disproportionate share, hospital Diagnosis Related Group (DRG) amount | No       |
| indirect_medical_education   | <a href="#monetary_object">Monetary Amount object</a>  | The Prospective Payment System (PPS) capital indirect medical education claim amount | No       |
| exception   | <a href="#monetary_object">Monetary Amount object</a>  | The capital exception amount | No       |

(<a href="#pps_object">Back to Prospective Payment System object</a>)

# Codes
Many of the values above are limited to a set of codes or constants.
These values are transformed from the corresponding EDI X12 code values that were received from a trading partner.

<a name="payment_adjustment_object"></a>
## Payment Adjustment Object
| Parameters                   | Type                                                                     | Description                                                                                                              | Required?|
|:-----------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| reason_code       | <a href="#payment_adjustment_reason_codes">Payment Adjustment Reason Codes</a> | The adjustment reason code, is the code indicating reason for debit or credit memo or adjustment to invoice, debit or credit memo, or payment.                                                                     | Yes      |
| reason             | {string}                                                                 | The transaction type.  See  <a href="#payment_adjustment_reason_codes">Payment Adjustment Reason Codes</a>              | Yes      |
| identifier               | {string}                                                                 | To assist the receiver in identifying,tracking or reconcilling the adjustment.                                               | Yes       |
| adjustment                     | <a href="#monetary_object">Monetary Amount object</a>  | The adjustment amount | No       |



(<a href="#claim_payment">Back to Claim Payment Result</a>)

<a name="payment_adjustment_reason_codes"></a>
## Payment Adjustment Reason Codes
| Reason                                          | Code (X12 Spec) |
|:------------------------------------------------------|:----------------|
| late_charge                                           | 50              |
| interest_penalty_charge                               | 51              |
| authorized_return                                     | 72              | 
| early_payment_allowance                               | 90              |
| origination_fee                                       | AH              |
| applied_to_borrowers_account                          | AM              |
| acceleration_of_benefits                              | AP              |
| rebate                                                | B2              |
| recovery_allowance                                    | B3              |
| bad_debt_adjustment                                   | BD              |
| bonus                                                 | BN              |
| temporary_allowance                                   | C5              |
| capitation_interest                                   | CR              |
| adjustment                                            | CS              |
| capitation_payment                                    | CT              |
| capital_passthru                                      | CV              |
| certified_registered_nurse_anesthetist_passthru       | CW              |
| direct_medical_education_passthru                     | DM              |
| withholding                                           | E3              |
| forwarding_balance                                    | FB              |
| fund_allocation                                       | FC              |
|  graduate_medical_education_passthru                  | GO              |
| hemophilia_clotting_factor_supplement                 | HM              |
| incentive_premium_payment                             | IP              |
| internal_revenue_service_withholding                  | IR              |
| interim_settlement                                    | IS              |
| nonreimbursable                                       | J1              |
| penalty                                               | L3              |
| interest_owed                                         | L6              |
| levy                                                  | LE              |
| lump_sum                                              | LS              |
| organ_acquisition_passthru                            | OA              |
| offset_for_affiliated_providers                       | OB              |
| periodic_interim_payment                              | PI              |
| payment_final                                         | PL              |
| retro_activity_adjustment                             | RA              |
| return_on_equity                                      | RE              |
| student_loan_repayment                                | SL              |
| third_party_liability                                 | TL              |
| overpayment_recovery                                  | WO              |
|  unspecified_recovery                                 | WU              |



(<a href="#payment_adjustment_reason_object">Back to Payment Adjustment Reason object</a>)

<a name="transaction_type_codes"></a>
## Transaction Type Codes
|                                          |
|:-----------------------------------------|
| payment_accompanies_remittance_advice    |
| make_payment_only                        |
| notification_only                        |
| remittance_information_only              |
| prenotification_of_future_transfers      |
| split_payment_and_remittance             |
| option_to_split_payment_and_remittance   |

(<a href="#claim_payment">Back to Claim Payment</a>)


<a name="filing_indicator_codes"></a>
## Filing Indicator Codes
|                                                  |                                     |
|:-------------------------------------------------|:------------------------------------|
| preferred_provider_organization                  |  point_of_service                   |
| exclusive_provider_organization                  |  indemnity_insurance                |
| health_maintenance_organization_medicare_risk    |  dental_maintenance_organization    |
| automobile_medical                               |  champus                            |
| disability                                       |  health_maintenance_organization    |
| liability_medical                                |  medicare_part_a                    |
| medicare_part_b                                  |  medicaid                           |
| other_federal_program                            |  title_v                            |
| veterans_affairs_plan                            |  workers_compensation_health_claim  |
| mutually_defined                                 |                                     |


(<a href="#claim_payment_object">Back to Claim Payment Object</a>)


<a name="adjustment_group_codes"></a>
## Adjustment Group Codes
|                                |
|:-------------------------------|
| contractual_obligations        |
| other_adjustments              |
| payor_initiated_reductions     |
| patient_responsibility         |


(<a href="#adjustment_object">Back to Adjustment Object</a>)

<a href="#procedure_code_qualifiers"></a>
## Procedure Code Qualifiers
|                                |
|:-------------------------------|
| dental                         |
| jurisdiction_specific          |
| health_care                    |
| nursing_facility               |
| home_infusion                  |
| drug                           |
| health_related_item            |
| hospital                       |
| upc                            |
| alternative                    |

(<a href="#service_object">Back to Service Object</a>)

<a name="payment_method_codes"></a>
## Payment Method Codes
|                                |
|:-------------------------------|
| automated_clearing_house       |
| financial_institution_option   |
| check                          |
| funds_wire_transfer            |
| non_payment_data               |

(<a href="#financial_information_object">Back to Financial Information Object</a>)

<a name="account_type_codes"></a>
## Account Type Codes
|                      |
|:---------------------|
| demand_deposit       |
| savings              |

(<a href="#financial_institution_object">Back to Financial Institution object</a>)


<a name="claim_payment_status_codes"></a>
## Claim Payment Status Codes
|                                                  |
|:-------------------------------------------------|
| processed_as_primary                             |
| processed_as_secondary                           |
| processed_as_tertiary                            |
| denied                                           |
| processed_as_primary_and_forwarded               |
| processed_as_secondary_and_forwarded             |
| processed_as_tertiary_and_forwarded              |
| reversal_of_previous_payment                     |
| not_our_claim_forwarded_to_additional_payers     |
| predetermination_pricing_only_no_payment         |

(<a href="#claim_payment_object">Back to Claim Payment object</a>)


<a name="contact_method_type_codes"></a>
## Contact Method Type Codes
|                                                  |
|:-------------------------------------------------|
| email                                            |
| fax                                              |
| phone                                            |
| phone_extension                                  |

(<a href="#contact_method_object">Back to Contact Method object</a>)
