# iot (SERVICE)

Internet of Things

## Additional details
- [Documentation](https://help.sap.com/viewer/product/SAP_CP_IOT_CF/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-iot)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **iot** by configuring your `usecase.json` file.

### Using the service plan **standard** (standard)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "iot",
      "plan: "standard"
  ]
}
````


## Related categories
- Integration Suite