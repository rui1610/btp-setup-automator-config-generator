<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iZmVhdHVyZWZsYWdzIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NiA1NiI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiMwYTZlY2Y7fS5jbHMtMntmaWxsOiMwNjNiNzA7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5mZWF0dXJlZmxhZ3M8L3RpdGxlPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTM3LDI5LjVIMTlhOSw5LDAsMCwwLDAsMThIMzdhOSw5LDAsMCwwLDAtMThabTAsMTUuNzVIMTlhNi43NSw2Ljc1LDAsMCwxLDAtMTMuNUgzN2E2Ljc1LDYuNzUsMCwwLDEsMCwxMy41WiIvPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTE5LDI2LjVIMzdhOSw5LDAsMCwwLDAtMThIMTlhOSw5LDAsMCwwLDAsMThabTE4LTE1YTYsNiwwLDEsMS02LDZBNiw2LDAsMCwxLDM3LDExLjVaIi8+PGNpcmNsZSBjbGFzcz0iY2xzLTIiIGN4PSIzNyIgY3k9IjE3LjUiIHI9IjQuMTI1Ii8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMTksMzMuNjI1QTQuODc1LDQuODc1LDAsMSwwLDIzLjg3NSwzOC41LDQuODc1LDQuODc1LDAsMCwwLDE5LDMzLjYyNVptMCw3LjVBMi42MjUsMi42MjUsMCwxLDEsMjEuNjI1LDM4LjUsMi42MjksMi42MjksMCwwLDEsMTksNDEuMTI1WiIvPjwvc3ZnPg==" alt="Icon for feature-flags" width="80px" />
# Feature Flags (technical name: **feature-flags**

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/FEATURE_FLAGS/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/feature-flags-service)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> ch20 - cf-ch20<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  lite  |  lite  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> ch20 - cf-ch20<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Feature Flags** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **feature-flags** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "feature-flags",
      "plan": "standard"
    }
  ]
}
```

### Using the service plan **lite**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "feature-flags",
      "plan": "lite"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency