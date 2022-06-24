<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iZHFhYXMiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDU2IDU2Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6IzA1M2I3MDt9LmNscy0ye2ZpbGw6IzBhNmVkMTt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPmRxYWFzPC90aXRsZT48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik0xOS4xLDI4YTM2LjgzNSwzNi44MzUsMCwwLDEsLjYyMS02SDM2LjQ4M2EyNS44LDI1LjgsMCwwLDEsLjQ0NiwyLjk5MWgzQTI1LjgsMjUuOCwwLDAsMCwzOS40ODMsMjJoOC42ODlBMjUuMjU1LDI1LjI1NSwwLDAsMSw0OSwyNWgzQTI0LjQsMjQuNCwwLDAsMCwyOCw0LDIzLjk1MSwyMy45NTEsMCwwLDAsNCwyOEM0LDQxLjAzNCwxNS4wNjksNTEuNjksMjgsNTJWNDcuMzQ1QTE4LjY4MywxOC42ODMsMCwwLDEsMjAuNDQ4LDM3SDI4VjM0SDE5LjcyNEEyOC43OTEsMjguNzkxLDAsMCwxLDE5LjEsMjhabTI3LjgyOC05SDM4Ljc1OWMtMS40NDktNC45NjYtMy44MjgtOS02LjkzMS0xMS41ODZBMjAuNSwyMC41LDAsMCwxLDQ2LjkzMSwxOVpNMjgsOC4zNDVjMy40MTQsMS44NjIsNi4xLDUuNjg5LDcuNjU1LDEwLjY1NUgyMC40NDhDMjEuOSwxNC4wMzQsMjQuNjksMTAuMjA3LDI4LDguMzQ1Wm0tMy44MjgtLjkzMUMyMS4wNjksMTAsMTguNjksMTQuMTM4LDE3LjM0NSwxOUg5LjA2OUEyMC42NzksMjAuNjc5LDAsMCwxLDI0LjE3Miw3LjQxNFpNNywyOGEyMi43NDMsMjIuNzQzLDAsMCwxLC45MzEtNmg4LjU4NkEzNy4wNTUsMzcuMDU1LDAsMCwwLDE2LDI4YTM4LjEwOCwzOC4xMDgsMCwwLDAsLjUxNyw2SDcuOTMxQTIyLjc0MywyMi43NDMsMCwwLDEsNywyOFpNMjQuMTcyLDQ4LjU4NkEyMS4xNzcsMjEuMTc3LDAsMCwxLDkuMDY5LDM3aDguMTcyQTI0LjM3LDI0LjM3LDAsMCwwLDI0LjE3Miw0OC41ODZaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMzcuODk0LDM2LjhsLS45LjlhLjYwOC42MDgsMCwwLDAsMCwuOGw1LjYsNi4yYS42NjguNjY4LDAsMCwwLDEtLjFsOC4zLTEyLjJhLjQ5NC40OTQsMCwwLDAtLjEtLjdsLTEtLjlhLjU1NS41NTUsMCwwLDAtLjkuMWwtNi42LDkuM2EuNTkuNTksMCwwLDEtLjkuMmwtMy42LTMuNkEuNTYxLjU2MSwwLDAsMCwzNy44OTQsMzYuOFoiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik00OSw0NnYzLjdIMzRWMzRoNlYzMUgzMi40QTEuNDMsMS40MywwLDAsMCwzMSwzMi40VjUwLjZBMS4zNjcsMS4zNjcsMCwwLDAsMzIuNCw1Mkg1MC42QTEuMzY3LDEuMzY3LDAsMCwwLDUyLDUwLjZWNDZaIi8+PC9zdmc+" alt="Icon for dq-services" width="80px" />
# Data Quality Services

Technical name: **dq-services**

Technical service category: **SERVICE**

## Additional details

- [$18n{applicationCoordinates.serviceDescription.title_documentation}](https://help.sap.com/viewer/d95546360fea44988eb614718ff7e959/Cloud/en-US)
- [License Terms](https://www.sap.com/about/trust-center/agreements/on-premise/product-use-and-support-terms.html?tag=agreements:product-use-support-terms/on-premise-software/software-use-rights/)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-data-quality-management)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)  |
|  free  |  free  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **Data Quality Services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **dq-services** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "dq-services",
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
      "name": "dq-services",
      "plan": "free"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency