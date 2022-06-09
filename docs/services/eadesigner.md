# eadesigner (APPLICATION)

SAP EA Designer, cloud edition

## Additional details
- [Documentation](https://help.sap.com/viewer/product/EAD_CLOUD/Cloud/en-US)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  eadesigner  |  SAP Enterprise Architecture Designer, cloud edition  | eu10 - Europe (Frankfurt)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **eadesigner** by configuring your `usecase.json` file.

### Using the service plan **eadesigner** (SAP Enterprise Architecture Designer, cloud edition)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "eadesigner",
      "plan: "eadesigner"
  ]
}
```


## Related categories
- Extension Suite - Digital Experience