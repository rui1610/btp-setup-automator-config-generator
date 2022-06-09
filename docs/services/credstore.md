# credstore (SERVICE)

Credential Store

## Additional details
- [Documentation](https://help.sap.com/viewer/product/CREDENTIAL_STORE/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/credential-store)
- [Support](https://help.sap.com/viewer/601525c6e5604e4192451d5e7328fa3c/Cloud/en-US/c6ebd580c0a642e9a99dbb8ae5c6c562.html)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  free  |  free  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  standard  |  standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  proxy  |  proxy  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **credstore** by configuring your `usecase.json` file.

### Using the service plan **free** (free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "credstore",
      "plan: "free"
  ]
}
```

### Using the service plan **standard** (standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "credstore",
      "plan: "standard"
  ]
}
```

### Using the service plan **proxy** (proxy)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "credstore",
      "plan: "proxy"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency