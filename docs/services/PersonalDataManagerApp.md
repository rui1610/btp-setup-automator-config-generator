# PersonalDataManagerApp (APPLICATION)

Personal Data Manager

## Additional details
- [Documentation](https://help.sap.com/viewer/product/PERSONAL_DATA_MANAGER/SHIP/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/personal-data-manager)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap21 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **PersonalDataManagerApp** by configuring your `usecase.json` file.

### Using the service plan **standard** (standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "PersonalDataManagerApp",
      "plan: "standard"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency