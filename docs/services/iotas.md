# iotas (APPLICATION)

SAP IoT

## Additional details
- [Documentation](https://help.sap.com/viewer/p/SAP_Leonardo_IoT)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Leonardo IoT  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  oneproduct  |  oneproduct  | eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> us10 - US East (VA)<br> us20 - US West (WA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **iotas** by configuring your `usecase.json` file.

### Using the service plan **standard** (Leonardo IoT)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "iotas",
      "plan: "standard"
  ]
}
```

### Using the service plan **oneproduct** (oneproduct)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "iotas",
      "plan: "oneproduct"
  ]
}
```


## Related categories
- Integration Suite