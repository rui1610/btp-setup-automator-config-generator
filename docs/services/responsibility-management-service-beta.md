# responsibility-management-service-beta (SERVICE)

Responsibility Management Service

## Additional details
- [Documentation](https://help.sap.com/viewer/product/DRAFT/RESPONSIBILITY_MANAGEMENT/1.0/en-US)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  beta  |  beta  | eu10 - Europe (Frankfurt)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **responsibility-management-service-beta** by configuring your `usecase.json` file.

### Using the service plan **beta** (beta)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "responsibility-management-service-beta",
      "plan: "beta"
  ]
}
````


## Related categories
- Integration Suite