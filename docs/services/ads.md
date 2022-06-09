# ads (SERVICE)

Forms Service by Adobe

## Additional details

- [Documentation](https://help.sap.com/viewer/dcbea777ceb3411cb10500a1a392273e/Cloud/en-US/8a668ee41fea4cf39c6bd6d21bff6a6e.html)
- [Discovery Center](https://discovery-center.cloud.sap/protected/index.html#/serviceCatalog/forms-service-by-adobe)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Standard  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **Forms Service by Adobe** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ads** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ads",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Experience