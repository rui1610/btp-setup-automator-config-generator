# spatialservices (SERVICE)

SAP HANA spatial services

## Additional details
- [Documentation](https://help.sap.com/viewer/product/SAP_HANA_SPATIAL_SERVICES/latest/)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-hana-spatial-services)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)  |
|  lite  |  lite  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **spatialservices** by configuring your `usecase.json` file.

### Using the service plan **standard** (standard)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "spatialservices",
      "plan: "standard"
  ]
}
````

### Using the service plan **lite** (lite)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "spatialservices",
      "plan: "lite"
  ]
}
````


## Related categories
- Extension Suite - Development Efficiency