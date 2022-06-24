<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iYXBwYXV0b3NjYWxpbmciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDU2IDU2Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6IzBhNmVkMTt9LmNscy0ye2ZpbGw6IzA1M2I3MDt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPmFwcGF1dG9zY2FsaW5nPC90aXRsZT48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik0xMy43LDQyLjNhMi4zMzMsMi4zMzMsMCwwLDAsMS44NDcuNzExbDkuOTQ3LS4yODRBMS4xODksMS4xODksMCwwLDAsMjYuOCw0MS40MnEuMDU3LTEuMzA4LTEuMzA3LTEuMzA3bC04LjEyOC40LDIzLjEzLTIzLjEzLS40LDguMTI4YTEuMzA4LDEuMzA4LDAsMSwwLDIuNjE1LDBMNDMsMTUuNTYyQTIuNDM1LDIuNDM1LDAsMCwwLDQwLjQzOCwxM2wtOS44OS4zNDFhMS4zMDgsMS4zMDgsMCwxLDAsMCwyLjYxNWw4LjEyOC0uNC0yMy4xMywyMy4xM0wxNiwzMC42MnEuMDU1LTEuMzA4LTEuMzA4LTEuMzA3YTEuMTg5LDEuMTg5LDAsMCwwLTEuMzA3LDEuMzA3bC0uNCw5LjgzNEEyLjMzMywyLjMzMywwLDAsMCwxMy43LDQyLjNaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNNDguMTU2LDcuODkxQTIuODQ4LDIuODQ4LDAsMCwwLDQ2LDdIMTlhMi44NDQsMi44NDQsMCwwLDAtMi4xNTYuODkxQTIuOTYyLDIuOTYyLDAsMCwwLDE2LDEwVjI4aDNWMTBINDZWMzdIMjh2M0g0NmEyLjg4OSwyLjg4OSwwLDAsMCwzLTNWMTBBMi45NjIsMi45NjIsMCwwLDAsNDguMTU2LDcuODkxWiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTI4LDQ2SDEwVjI4aDNWMjVIMTBhMi44NDQsMi44NDQsMCwwLDAtMi4xNTYuODkxQTIuOTYyLDIuOTYyLDAsMCwwLDcsMjhWNDZhMi44ODksMi44ODksMCwwLDAsMywzSDI4YTIuODg5LDIuODg5LDAsMCwwLDMtM1Y0M0gyOFoiLz48L3N2Zz4=" alt="Icon for autoscaler" width="80px" />
# Application Autoscaler (technical name: **autoscaler**

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/Application_Autoscaler/Cloud/en-US)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)
- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/application-autoscaler)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> ch20 - cf-ch20<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Application Autoscaler** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **autoscaler** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "autoscaler",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency