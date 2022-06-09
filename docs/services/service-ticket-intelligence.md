# service-ticket-intelligence (SERVICE)

Service Ticket Intelligence

## Additional details
- [Documentation](https://help.sap.com/stint)
- [Support](https://help.sap.com/viewer/934ccff77ddb4fa2bf268a0085984db0/LATEST/en-US/76a77fbf8d3645978d98711450f0b8bc.html)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/service-ticket-intelligence)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  blocks_of_100  |  blocks_of_100  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> us10 - US East (VA)<br> us30 - US Central (IA)  |
|  free  |  Free  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> us10 - US East (VA)<br> us30 - US Central (IA)  |
|  standard  |  standard  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> us10 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **service-ticket-intelligence** by configuring your `usecase.json` file.

### Using the service plan **blocks_of_100** (blocks_of_100)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "service-ticket-intelligence",
      "plan: "blocks_of_100"
  ]
}
````

### Using the service plan **free** (Free)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "service-ticket-intelligence",
      "plan: "free"
  ]
}
````

### Using the service plan **standard** (standard)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "service-ticket-intelligence",
      "plan: "standard"
  ]
}
````


## Related categories
- Extension Suite - Development Efficiency