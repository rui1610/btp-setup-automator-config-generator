# business-entity-recognition (SERVICE)

Business Entity Recognition

## Additional details
- [Documentation](https://help.sap.com/ber)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/business-entity-recognition)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  free  |  free  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |
|  standard  |  standard  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **business-entity-recognition** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "business-entity-recognition",
      "plan: "free"
  ]
}
```

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "business-entity-recognition",
      "plan: "standard"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency