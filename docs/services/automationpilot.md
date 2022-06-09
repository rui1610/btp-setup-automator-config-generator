# automationpilot (APPLICATION)

Automation Pilot

## Additional details
- [Documentation](https://help.sap.com/viewer/product/AUTOMATION_PILOT)
- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/automation-pilot)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  free  |  free  | ap10 - Australia (Sydney)<br> eu10 - Europe (Frankfurt)<br> jp20 - Japan (Tokyo)<br> us30 - US Central (IA)  |
|  standard  |  Standard  | ap10 - Australia (Sydney)<br> eu10 - Europe (Frankfurt)<br> jp20 - Japan (Tokyo)<br> us30 - US Central (IA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **automationpilot** by configuring your `usecase.json` file.

### Using the service plan **free** (free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "automationpilot",
      "plan: "free"
  ]
}
```

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "automationpilot",
      "plan: "standard"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency