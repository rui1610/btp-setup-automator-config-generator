# cias (APPLICATION)

Cloud Integration Automation Service

## Additional details

- [Documentation](https://help.sap.com/viewer/product/Cloud%2520Integration%2520Automation%2520Service/Latest/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/cloud-integration-automation)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap10 - Australia (Sydney)<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> us10 - US East (VA)  |

## Sample configuration of **Cloud Integration Automation Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **cias** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "cias",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Integration Suite