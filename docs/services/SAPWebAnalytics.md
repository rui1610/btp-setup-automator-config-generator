# SAPWebAnalytics (APPLICATION)

Web Analytics

## Additional details
- [Documentation](https://help.sap.com/viewer/product/SAP_WEB_ANALYTICS/1.0/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/web-analytics)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  SAP Web Analytics  | ap10 - Australia (Sydney)<br> ap21 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **SAPWebAnalytics** by configuring your `usecase.json` file.

### Using the service plan **standard** (SAP Web Analytics)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "SAPWebAnalytics",
      "plan: "standard"
  ]
}
````


## Related categories
- Extension Suite - Digital Experience