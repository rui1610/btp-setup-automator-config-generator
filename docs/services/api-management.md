# api-management (SERVICE)

API Management

## Additional details

- [Documentation](https://help.sap.com/viewer/product/SAP_CLOUD_PLATFORM_API_MANAGEMENT/Cloud/en-US)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  preview  |  Expose your data and processes as APIs for omni-channel consumption and manage the lifecycle of those APIs  | eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **API Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **api-management** by configuring your `usecase.json` file.

### Using the service plan **preview** (Expose your data and processes as APIs for omni-channel consumption and manage the lifecycle of those APIs)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "api-management",
      "plan": "preview"      
    }
  ]
}
```

## Related categories

- Integration Suite