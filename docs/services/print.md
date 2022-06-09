# print (SERVICE)

Print Service

## Additional details

- [Documentation](https://help.sap.com/viewer/product/SCP_PRINT_SERVICE/SHIP/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/print-service)
- [Support](https://launchpad.support.sap.com)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  sender  |  sender  | eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> us10 - US East (VA)<br> us20 - US West (WA)  |
|  receiver  |  receiver  | eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> us10 - US East (VA)<br> us20 - US West (WA)  |

## Sample configuration of **Print Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **print** by configuring your `usecase.json` file.

### Using the service plan **sender**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "print",
      "plan": "sender"
    }
  ]
}
```

### Using the service plan **receiver**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "print",
      "plan": "receiver"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Experience