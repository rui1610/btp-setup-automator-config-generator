<img src="data:;base64, None" alt="Icon for MDMBusinessPartnerApplication" width="80px" />
# SAP Business Partner Application (technical name: **MDMBusinessPartnerApplication**

Service category: **APPLICATION**

## Additional details


## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  saas-application  |  SAP Cloud Platform Master Data Management for business partners  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **SAP Business Partner Application** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **MDMBusinessPartnerApplication** by configuring your `usecase.json` file.

### Using the service plan **saas-application** (SAP Cloud Platform Master Data Management for business partners)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "MDMBusinessPartnerApplication",
      "plan": "saas-application"
    }
  ]
}
```

## Related categories
