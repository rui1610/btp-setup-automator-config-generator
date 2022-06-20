# dqmmicroui (APPLICATION)

Data Quality Services UI

## Additional details

- [Documentation](https://help.sap.com/viewer/d95546360fea44988eb614718ff7e959/Cloud/en-US/8bb7b22e6d4c40b5bfdaef86f59e2036.html)
- [License Terms](https://www.sap.com/about/trust-center/agreements/on-premise/product-use-and-support-terms.html?tag=agreements:product-use-support-terms/on-premise-software/software-use-rights/)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Standard  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **Data Quality Services UI** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **dqmmicroui** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "dqmmicroui",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency