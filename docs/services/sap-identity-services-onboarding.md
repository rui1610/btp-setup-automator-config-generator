# sap-identity-services-onboarding (APPLICATION)

Cloud Identity Services

## Additional details
- [Documentation](https://help.sap.com/viewer/p/IDENTITY_AUTHENTICATION)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  additional-tenant  |  additional-tenant  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  connectivity  |  connectivity  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-identity-services-onboarding** by configuring your `usecase.json` file.

### Using the service plan **default** (default)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "sap-identity-services-onboarding",
      "plan: "default"
  ]
}
```

### Using the service plan **additional-tenant** (additional-tenant)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "sap-identity-services-onboarding",
      "plan: "additional-tenant"
  ]
}
```

### Using the service plan **connectivity** (connectivity)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "sap-identity-services-onboarding",
      "plan: "connectivity"
  ]
}
```


## Related categories
- Integration Suite