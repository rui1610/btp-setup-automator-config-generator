# tnt-onboard-dataenrichment-dcp (APPLICATION)

Data Enrichment

## Additional details

- [Documentation](https://help.sap.com/viewer/product/Cloud_Platform_Data_Enrichment/latest/en-US)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  saas-application  |  Data Enrichment  | ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **Data Enrichment** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **tnt-onboard-dataenrichment-dcp** by configuring your `usecase.json` file.

### Using the service plan **saas-application** (Data Enrichment)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "tnt-onboard-dataenrichment-dcp",
      "plan": "saas-application"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency