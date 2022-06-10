# sap-calm (SERVICE)

SAP Cloud ALM, memory extension

## Additional details

- [Documentation](https://support.sap.com/en/alm/sap-cloud-alm.html)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-cloud-alm-memory-extension)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)  |

## Sample configuration of **SAP Cloud ALM, memory extension** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-calm** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-calm",
      "plan": "default"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Experience