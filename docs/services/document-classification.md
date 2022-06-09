# document-classification (SERVICE)

Document Classification

## Additional details
- [Documentation](https://help.sap.com/dc)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/document-classification)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  blocks_of_100  |  blocks_of_100  | eu10 - Europe (Frankfurt)  |
|  default  |  default  | eu10 - Europe (Frankfurt)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **document-classification** by configuring your `usecase.json` file.

### Using the service plan **blocks_of_100**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "document-classification",
      "plan: "blocks_of_100"
  ]
}
```

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "document-classification",
      "plan: "default"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency