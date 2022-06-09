# intelligent-situation-automation-app (APPLICATION)

Intelligent Situation Automation

## Additional details
- [Documentation](https://help.sap.com/viewer/product/INTELLIGENT_SITUATION_AUT/1.0/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/intelligent-situation-automation)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)  |
|  beta  |  Beta  | eu10 - Europe (Frankfurt)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **intelligent-situation-automation-app** by configuring your `usecase.json` file.

### Using the service plan **standard** (standard)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "intelligent-situation-automation-app",
      "plan: "standard"
  ]
}
````

### Using the service plan **beta** (Beta)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "intelligent-situation-automation-app",
      "plan: "beta"
  ]
}
````


## Related categories
- Extension Suite - Digital Process Automation