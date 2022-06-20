# responsibility-management-application-beta (APPLICATION)

Responsibility Management Service

## Additional details

- [Documentation](https://help.sap.com/viewer/product/DRAFT/RESPONSIBILITY_MANAGEMENT/1.0/en-US)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  beta  |  Beta  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **Responsibility Management Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **responsibility-management-application-beta** by configuring your `usecase.json` file.

### Using the service plan **beta** (Beta)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "responsibility-management-application-beta",
      "plan": "beta"
    }
  ]
}
```

## Related categories

- Integration Suite