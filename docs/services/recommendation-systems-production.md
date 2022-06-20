# recommendation-systems-production (SERVICE)

Personalized Recommendation

## Additional details

- [Documentation](https://help.sap.com/pr)
- [Support](https://help.sap.com/docs/Personalized_Recommendation/2c2078b9efa84566ac19d44df9625c65/c9cb13e6510248bdbb60ab0ea799d046.html)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> us10 - US East (VA)  |
|  free  |  free  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> us10 - US East (VA)  |

## Sample configuration of **Personalized Recommendation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **recommendation-systems-production** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "recommendation-systems-production",
      "plan": "standard"
    }
  ]
}
```

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "recommendation-systems-production",
      "plan": "free"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency