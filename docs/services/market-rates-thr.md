# market-rates-thr (SERVICE)

Market Rates, Refinitiv

## Additional details

- [Documentation](https://help.sap.com/viewer/p/SAP_CP_BUS_REUSE_SERVICE_MRM_TR)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **Market Rates, Refinitiv** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **market-rates-thr** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "market-rates-thr",
      "plan": "default"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency