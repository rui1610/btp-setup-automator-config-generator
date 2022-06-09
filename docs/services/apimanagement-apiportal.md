# apimanagement-apiportal (SERVICE)

API Management, API portal

## Additional details
- [Documentation](https://help.sap.com/viewer/product/SAP_CLOUD_PLATFORM_API_MANAGEMENT)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  apiportal-apiaccess  |  apiportal-apiaccess  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  on-premise-connectivity  |  on-premise-connectivity  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  apim-as-route-service  |  apim-as-route-service  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **apimanagement-apiportal** by configuring your `usecase.json` file.

### Using the service plan **apiportal-apiaccess** (apiportal-apiaccess)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "apimanagement-apiportal",
      "plan: "apiportal-apiaccess"
  ]
}
```

### Using the service plan **on-premise-connectivity** (on-premise-connectivity)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "apimanagement-apiportal",
      "plan: "on-premise-connectivity"
  ]
}
```

### Using the service plan **apim-as-route-service** (apim-as-route-service)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "apimanagement-apiportal",
      "plan: "apim-as-route-service"
  ]
}
```


## Related categories
- Integration Suite