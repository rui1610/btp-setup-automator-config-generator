<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgODAgODAiPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50IiB4MT0iMC4xOCIgeTE9IjQwIiB4Mj0iNzkuODIiIHkyPSI0MCIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzNiODNjMSIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzg2YmZjOCIvPjwvbGluZWFyR3JhZGllbnQ+PC9kZWZzPjx0aXRsZT5sb2dvMTI4eDEyODwvdGl0bGU+PHBvbHlsaW5lIHBvaW50cz0iNTIuNzkgNDAuOSA3Ni4zMiA0MC45IDc2LjMyIDcwLjY3IDQxLjM2IDcwLjY3IDQxLjM2IDkuMzMgMy42OCA5LjMzIDMuNjggMzkuMDIgMjcuNDcgMzkuMDIiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSI3IiBzdHJva2U9InVybCgjbGluZWFyLWdyYWRpZW50KSIvPjwvc3ZnPg==" alt="Icon for quorum" width="80px" />
# Quorum

Technical name: **quorum**

Technical service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/p/QUORUM)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  cyon  |  cyon  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  testnet  |  testnet  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  dev  |  dev  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **Quorum** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **quorum** by configuring your `usecase.json` file.

### Using the service plan **cyon**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "quorum",
      "plan": "cyon"
    }
  ]
}
```

### Using the service plan **testnet**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "quorum",
      "plan": "testnet"
    }
  ]
}
```

### Using the service plan **dev**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "quorum",
      "plan": "dev"
    }
  ]
}
```

## Related categories

- Integration Suite