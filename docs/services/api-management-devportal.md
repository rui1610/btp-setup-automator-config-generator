# api-management-devportal (APPLICATION)

API Management, API Business Hub Enterprise

## Additional details
- [Documentation](https://help.sap.com/viewer/product/SAP_CLOUD_PLATFORM_API_MANAGEMENT)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  API Management-Developer Portal  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **api-management-devportal** by configuring your `usecase.json` file.

### Using the service plan **standard** (API Management-Developer Portal)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "api-management-devportal",
      "plan: "standard"
  ]
}
```


## Related categories
- Integration Suite