# ibx-connection-app (APPLICATION)

SAP Ariba Shopping

## Additional details
- [Documentation](https://help.sap.com/docs/ARIBA_SHOP_MOB)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ibx-connection-app** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "ibx-connection-app",
      "plan: "standard"
  ]
}
```


## Related categories
- Extension Suite - Digital Experience