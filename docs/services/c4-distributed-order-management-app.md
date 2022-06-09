# c4-distributed-order-management-app (APPLICATION)

SAP Order Management Foundation

## Additional details

- [Documentation](https://help.sap.com/viewer/product/C4_OrdMgmt/latest/en-US)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  Central Order  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **SAP Order Management Foundation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **c4-distributed-order-management-app** by configuring your `usecase.json` file.

### Using the service plan **default** (Central Order)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "c4-distributed-order-management-app",
      "plan": "default"      
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Process Automation