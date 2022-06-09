# adsrestapi (SERVICE)

Forms Service by Adobe API

## Additional details
- [Documentation](https://help.sap.com/viewer/dcbea777ceb3411cb10500a1a392273e/Cloud/en-US/661c02ef20d54bfeb309d42608baeaca.html)
- [Discovery Center](https://discovery-center.cloud.sap/protected/index.html#/serviceCatalog/forms-service-by-adobe)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Standard  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **adsrestapi** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "adsrestapi",
      "plan: "standard"
  ]
}
````


## Related categories
- Extension Suite - Digital Experience