# mdo-one-mds-master (APPLICATION)

Master Data Integration (Orchestration)

## Additional details
- [Documentation](https://help.sap.com/viewer/product/DRAFT/SAP_CLOUD_PLATFORM_MASTER_DATA_INTEGRATION/CLOUD/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/master-data-integration)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **mdo-one-mds-master** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "mdo-one-mds-master",
      "plan: "standard"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency