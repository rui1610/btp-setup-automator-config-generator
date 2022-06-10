# sapappgyver (APPLICATION)

SAP AppGyver

## Additional details

- [Documentation](https://help.sap.com/viewer/6a5fc562f6e2402aa84b0416614a05fc/Dev/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/sap-appgyver)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **SAP AppGyver** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sapappgyver** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sapappgyver",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency