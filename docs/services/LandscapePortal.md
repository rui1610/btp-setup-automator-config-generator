# LandscapePortal (APPLICATION)

Landscape Portal

## Additional details
- [Documentation](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5eb70fb003954619b09224167a0afaa4.html)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Standard  | eu10 - Europe (Frankfurt)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **LandscapePortal** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "LandscapePortal",
      "plan: "standard"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency