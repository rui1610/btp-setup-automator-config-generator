# invoice-object-recommendation (SERVICE)

Invoice Object Recommendation

## Additional details

- [Documentation](https://help.sap.com/viewer/product/Invoice_Object_Recommendation)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **Invoice Object Recommendation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **invoice-object-recommendation** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "invoice-object-recommendation",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency