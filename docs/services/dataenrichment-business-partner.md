<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iZGF0YS1lbnJpY2htZW50IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NiA1NiI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiMwNTNiNzA7fS5jbHMtMntmaWxsOiMwYTZlZDE7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5kYXRhLWVucmljaG1lbnQ8L3RpdGxlPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTQ1Ljg0LDE4LjQ2MmE4LjQ4OSw4LjQ4OSwwLDAsMC0xMi43ODMtNS43MTNBMTAuNzQ3LDEwLjc0NywwLDAsMCwyMi40MSw1LjVDMTAsNS41LDExLjA5LDE4LjQ4OCwxMS4wOSwxOC40ODhBMTAuMjQ5LDEwLjI0OSwwLDAsMCw0LDI4LjIxNSwxMC4zOCwxMC4zOCwwLDAsMCwxMywzOC41aDBWMzUuNDVhNy4zNDEsNy4zNDEsMCwwLDEtNi03LjIzNSw3LjI0OSw3LjI0OSwwLDAsMSw1LjAyNy02Ljg3N2wyLjI1MS0uNzQtLjItMi4zNjFjMC0uMDQ3LS4zMTgtNC43MjcsMi4yNTQtNy41MjVDMTcuNyw5LjIyMywxOS42OTEsOC41LDIyLjQxLDguNWE3Ljc1NSw3Ljc1NSwwLDAsMSw3Ljg1OSw1LjM1NmwxLjMwNiwzLjI5LDMuMDMxLTEuODI4YTUuNDUsNS40NSwwLDAsMSwyLjg0My0uODE4LDUuNTQ2LDUuNTQ2LDAsMCwxLDUuNDQzLDQuNTE3bC4yODgsMS41MjksMS40MTUuNjQ1QTcuNTE1LDcuNTE1LDAsMCwxLDQ5LDI4YTcuNiw3LjYsMCwwLDEtNiw3LjQzN1YzOC41aDBBMTAuNjI1LDEwLjYyNSwwLDAsMCw1MiwyOCwxMC40ODMsMTAuNDgzLDAsMCwwLDQ1Ljg0LDE4LjQ2MloiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik00MCwyMS45NTFhNC41LDQuNSwwLDAsMC0yLjQ0NCw4LjI3MUEzLjgxMywzLjgxMywwLDAsMSwzNCwzMi40NWE2LjU4MSw2LjU4MSwwLDAsMC00LjUsMS42MzhWMjcuNjc2YTQuNSw0LjUsMCwxLDAtMywwdjYuNDEyQTYuNTgxLDYuNTgxLDAsMCwwLDIyLDMyLjQ1YTMuODUxLDMuODUxLDAsMCwxLTMuNTc2LTIuMjE3LDQuNTEzLDQuNTEzLDAsMSwwLTMsLjY2QTYuODA3LDYuODA3LDAsMCwwLDIyLDM1LjQ1YzQuNDE1LDAsNC41LDUuNzYsNC41LDZ2LjMyM2E0LjUsNC41LDAsMSwwLDMsMFY0MS40NWMwLS4yNDYuMDUtNiw0LjUtNmE2LjgwNSw2LjgwNSwwLDAsMCw2LjU2OS00LjU1NkE0LjQ4OSw0LjQ4OSwwLDAsMCw0MCwyMS45NTFabS0yNCw2YTEuNSwxLjUsMCwxLDEsMS41LTEuNUExLjUsMS41LDAsMCwxLDE2LDI3Ljk1MVptMTItM2ExLjUsMS41LDAsMSwxLDEuNS0xLjVBMS41LDEuNSwwLDAsMSwyOCwyNC45NTFabTEyLDNhMS41LDEuNSwwLDEsMSwxLjUtMS41QTEuNSwxLjUsMCwwLDEsNDAsMjcuOTUxWiIvPjwvc3ZnPg==" alt="Icon for dataenrichment-business-partner" width="80px" />
# **dataenrichment-business-partner** (Data Enrichment)

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/Cloud_Platform_Data_Enrichment/latest/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/data-enrichment)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **Data Enrichment** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **dataenrichment-business-partner** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "dataenrichment-business-partner",
      "plan": "default"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency