# print-app (APPLICATION)

Print Service

## Additional details
- [Documentation](https://help.sap.com/viewer/product/SCP_PRINT_SERVICE/SHIP/en-US)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> us10 - US East (VA)<br> us20 - US West (WA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **print-app** by configuring your `usecase.json` file.

### Using the service plan **standard** (standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "print-app",
      "plan: "standard"
  ]
}
```


## Related categories
- Extension Suite - Digital Experience