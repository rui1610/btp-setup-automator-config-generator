# document-translation (SERVICE)

Document Translation

## Additional details

- [Documentation](https://help.sap.com/viewer/9f73362817cd48339dd8a6acba160f7f/Cloud/en-US/c07bd4ee447b477b9ccb31b3abf5dae3.html)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  Default  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  free  |  Free  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **Document Translation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **document-translation** by configuring your `usecase.json` file.

### Using the service plan **default** (Default)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "document-translation",
      "plan": "default"
    }
  ]
}
```

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "document-translation",
      "plan": "free"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency