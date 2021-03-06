<img src="data:image/svg+xml;base64, PHN2ZyBpZD0ibW9iaWxlc2VydmljZXMiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDU2IDU2Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6IzA1M2I3MDt9LmNscy0ye2ZpbGw6IzBhNmVkMTt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPm1vYmlsZXNlcnZpY2VzPC90aXRsZT48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik0zNyw0YTUuNzgsNS43OCwwLDAsMSw0LjIxOSwxLjc4MUE1Ljc4LDUuNzgsMCwwLDEsNDMsMTBWNDZhNS43MjksNS43MjksMCwwLDEtMS43ODEsNC4yNjZBNS44Niw1Ljg2LDAsMCwxLDM3LDUySDE5YTUuODUxLDUuODUxLDAsMCwxLTQuMjE5LTEuNzM0QTUuNzE4LDUuNzE4LDAsMCwxLDEzLDQ2VjEwYTUuNzY4LDUuNzY4LDAsMCwxLDEuNzgxLTQuMjE5QTUuNzcsNS43NywwLDAsMSwxOSw0Wm0zLDZIMTZWNDNINDBaTTI4LDQ5YTIuMjYsMi4yNiwwLDAsMCwxLjU5NC0uNjA5LDIuMTM0LDIuMTM0LDAsMCwwLC42NTYtMS42NDEsMi4yNSwyLjI1LDAsMSwwLTQuNSwwLDIuMTIzLDIuMTIzLDAsMCwwLC42NTYsMS42NDFBMi4yNSwyLjI1LDAsMCwwLDI4LDQ5WiIvPjxyZWN0IGNsYXNzPSJjbHMtMiIgeD0iMjAuNSIgeT0iMjEuMDYzIiB3aWR0aD0iMyIgaGVpZ2h0PSI2LjkzOCIvPjxyZWN0IGNsYXNzPSJjbHMtMiIgeD0iMTkiIHk9IjMxIiB3aWR0aD0iMTgiIGhlaWdodD0iMS41Ii8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSIxOSIgeT0iMzguNSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjEuNSIvPjxyZWN0IGNsYXNzPSJjbHMtMiIgeD0iMTkiIHk9IjM0Ljc1IiB3aWR0aD0iMTgiIGhlaWdodD0iMS41Ii8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSIzMi41IiB5PSIxMy45MzgiIHdpZHRoPSIzIiBoZWlnaHQ9IjE0LjA2MyIvPjxyZWN0IGNsYXNzPSJjbHMtMiIgeD0iMjYuNSIgeT0iMTcuNDA2IiB3aWR0aD0iMyIgaGVpZ2h0PSIxMC41OTQiLz48L3N2Zz4=" alt="Icon for mobile-services-preview" width="80px"/>
# **mobile-services-preview** (Mobile Services, preview)

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/SAP_MOBILE_SERVICES/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/mobile-services)
- [Mobile Services Consolidated Documentation (Cloud Foundry)](https://developers.sap.com/mobile)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **Mobile Services, preview** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **mobile-services-preview** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "mobile-services-preview",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Experience