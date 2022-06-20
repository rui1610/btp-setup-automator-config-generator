# ml-foundation (SERVICE)

SAP Leonardo ML Foundation

## Additional details

- [Documentation](https://help.sap.com/viewer/p/SAP_LEONARDO_MACHINE_LEARNING_FOUNDATION)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/machine-learning-foundation)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **SAP Leonardo ML Foundation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ml-foundation** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ml-foundation",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency