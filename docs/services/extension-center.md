<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iZXh0ZW5zaW9uLWZhY3Rvcnktc2VydmVybGVzcy1ydW50aW1lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NiA1NiI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiMwNTNiNzA7fS5jbHMtMntmaWxsOiMwYTZlZDE7fTwvc3R5bGU+PC9kZWZzPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTUxLjU4OSwyNi40NzgsNDEuMTEzLDguNDkyYTMuMDI0LDMuMDI0LDAsMCwwLTIuNjE0LTEuNUgyOC4wMTJ2M0gzOC41bC4wMi4wMTFMNDksMjguMDEybC0xMC41LDE4TDI4LjAxMiw0NnYzLjAwN0gzOC41YTMuMDI0LDMuMDI0LDAsMCwwLDIuNjE0LTEuNUw1MS41ODksMjkuNTIyQTMuMDI0LDMuMDI0LDAsMCwwLDUxLjU4OSwyNi40NzhaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMjguMDEyLDQ2LDE3LjQ4MSw0Niw3LjAwNSwyNy45ODhsMTAuNS0xOEgyOC4wMTJ2LTNIMTcuNWEzLjAyNCwzLjAyNCwwLDAsMC0yLjYxNCwxLjVMNC40MTEsMjYuNDc4YTMuMDI0LDMuMDI0LDAsMCwwLDAsMy4wNDRMMTQuODg3LDQ3LjUwOGEzLjAyNCwzLjAyNCwwLDAsMCwyLjYxNCwxLjVIMjguMDEyWiIvPjwvc3ZnPg==" alt="Icon for extension-center" width="80px" />
# **extension-center** (Extension Center)

Service category: **APPLICATION**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/XF_SERVERLESS_RUNTIME/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/serverless-runtime)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Extension Center  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)  |

## Sample configuration of **Extension Center** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **extension-center** by configuring your `usecase.json` file.

### Using the service plan **standard** (Extension Center)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "extension-center",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency