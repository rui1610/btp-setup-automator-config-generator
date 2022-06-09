# dateandtime (SERVICE)

Date and Time

## Additional details
- [Documentation](https://help.sap.com/docs/DATE_AND_TIME)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/date-and-time)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **dateandtime** by configuring your `usecase.json` file.

### Using the service plan **default** (default)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "dateandtime",
      "plan: "default"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency