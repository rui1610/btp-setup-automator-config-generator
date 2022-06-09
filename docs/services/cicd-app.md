# cicd-app (APPLICATION)

Continuous Integration & Delivery

## Additional details
- [Documentation](https://help.sap.com/docs/CONTINUOUS_DELIVERY?version=Cloud)
- [Support](https://help.sap.com/docs/CONTINUOUS_DELIVERY/99c72101f7ee40d0b2deb4df72ba1ad3/6e10ad426e434180a0c62d4e7b6115bc.html)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/continuous-integration--delivery?region=all)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  Default  | eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **cicd-app** by configuring your `usecase.json` file.

### Using the service plan **default** (Default)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "cicd-app",
      "plan: "default"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency