# data-privacy-integration-application (APPLICATION)

Data Privacy Integration

## Additional details

- [Documentation](https://help.sap.com/viewer/product/DATA_PRIVACY_INTEGRATION/SHIP/en-US)
- [Support](https://help.sap.com/viewer/313a456d8f6c47289945699fbf5ab0c6/DEV/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/data-privacy-integration)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap21 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)  |

## Sample configuration of **Data Privacy Integration** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **data-privacy-integration-application** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "data-privacy-integration-application",
      "plan": "default"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency