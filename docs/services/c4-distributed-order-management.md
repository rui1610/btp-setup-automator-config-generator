# c4-distributed-order-management (SERVICE)

SAP Order Management Foundation

## Additional details

- [Documentation](https://help.sap.com/docs/SAP_Order_Management_Foundation?version=Cloud&locale=en-US)
- [Support](https://help.sap.com/docs/SAP_Order_Management_Foundation/d91676a7fa624c31b7b1c526d7787e2f/ca6630612cf741ed8927d60fabe13929.html?locale=en-US&version=Cloud)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)  |

## Sample configuration of **SAP Order Management Foundation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **c4-distributed-order-management** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "c4-distributed-order-management",
      "plan": "default"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Process Automation