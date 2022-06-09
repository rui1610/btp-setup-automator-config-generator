# process-automation-service (SERVICE)

SAP Process Automation

## Additional details
- [Documentation](https://help.sap.com/viewer/p/PROCESS_AUTOMATION)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap10 - Australia (Sydney)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **process-automation-service** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "process-automation-service",
      "plan: "standard"
  ]
}
```


## Related categories
- Extension Suite - Digital Process Automation