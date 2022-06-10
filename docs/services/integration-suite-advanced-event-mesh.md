# integration-suite-advanced-event-mesh (APPLICATION)

SAP Integration Suite, advanced event mesh

## Additional details


## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  Default  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **SAP Integration Suite, advanced event mesh** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **integration-suite-advanced-event-mesh** by configuring your `usecase.json` file.

### Using the service plan **default** (Default)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "integration-suite-advanced-event-mesh",
      "plan": "default"      
    }
  ]
}
```

## Related categories