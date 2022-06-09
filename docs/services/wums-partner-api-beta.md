# wums-partner-api-beta (SERVICE)

Workspace Utilization

## Additional details
- [Documentation](https://help.sap.com/viewer/p/SAP_CLOUD_FOR_REAL_ESTATE)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | eu10 - Europe (Frankfurt)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **wums-partner-api-beta** by configuring your `usecase.json` file.

### Using the service plan **default** (default)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "wums-partner-api-beta",
      "plan: "default"
  ]
}
````


## Related categories
- Integration Suite