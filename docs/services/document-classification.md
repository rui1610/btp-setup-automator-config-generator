<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iZG9jdW1lbnQtY2xhc3NpZmljYXRpb24iIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDU2IDU2Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6IzA1M2I3MDt9LmNscy0ye2ZpbGw6IzBhNmVkMTt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPmRvY3VtZW50LWNsYXNzaWZpY2F0aW9uPC90aXRsZT48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik01MS42MjUsMzIuNWEyLjg5NCwyLjg5NCwwLDAsMC0uOTM3LTEuMDMxQTIuODQ5LDIuODQ5LDAsMCwwLDQ5LDMxSDM5LjE1NmwtMi42MjUtM0gyNWEyLjc5MiwyLjc5MiwwLDAsMC0xLjczNC40NjksMy4wMSwzLjAxLDAsMCwwLS44OTEsMS4wMzFBMi45NTIsMi45NTIsMCwwLDAsMjIsMzFWNDlhMi43ODEsMi43ODEsMCwwLDAsLjQ2OSwxLjczNEEzLjEzOSwzLjEzOSwwLDAsMCwyNSw1Mkg0OWEyLjk3NSwyLjk3NSwwLDAsMCwxLjUtLjM3NSwzLjAxLDMuMDEsMCwwLDAsMS4wMzEtLjg5MUEyLjgsMi44LDAsMCwwLDUyLDQ5VjM0QTIuOTgyLDIuOTgyLDAsMCwwLDUxLjYyNSwzMi41Wk00OSw0OWwtMjQsLjAyM1Y0OWwtLjAyNS0xOGgxMC4yTDM2LjksMzIuOTc2LDM3LjgsMzRoMS4zNjFMNDksMzQuMDA5WiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTI1LDRIMTBMNCwxMFYzMWEyLjg4OSwyLjg4OSwwLDAsMCwzLDNIMTlWMzFIN1YxM0g5LjkwNmEzLjA4MiwzLjA4MiwwLDAsMCwyLjItLjg0NEEyLjg0NCwyLjg0NCwwLDAsMCwxMywxMFY3SDI1VjI1aDNWN2EyLjg0NCwyLjg0NCwwLDAsMC0uODkxLTIuMTU2QTIuOTYyLDIuOTYyLDAsMCwwLDI1LDRaIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSIxMCIgeT0iMTYiIHdpZHRoPSIxMiIgaGVpZ2h0PSIzIi8+PHBvbHlnb24gY2xhc3M9ImNscy0yIiBwb2ludHM9IjEwIDI1IDE5IDI1IDIyIDI1IDIyIDIyIDEwIDIyIDEwIDI1Ii8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNNDguNjQ4LDE5LjM1MmExLjEsMS4xLDAsMCwwLTEuNjE3LDBsLTIuNiwzLjAyMy4wNy0xLjEyNWE4Ljc2Nyw4Ljc2NywwLDAsMC0uNy0zLjQ4LDguOTY4LDguOTY4LDAsMCwwLTEuOTM0LTIuODgzLDkuMTU4LDkuMTU4LDAsMCwwLTIuODQ3LTEuOTM0LDguNzMsOC43MywwLDAsMC0zLjUxNi0uN0gzMVYxNC41aDQuNWE2LjcyMyw2LjcyMywwLDAsMSw2Ljc1LDYuNzVsLS4wNywxLjEyNS0yLjUzMi0zLjAyM2ExLjAzNywxLjAzNywwLDAsMC0xLjYxNywwLC45NjguOTY4LDAsMCwwLDAsMS41NDZsMy43MjcsNC4yMTlhMi4zODIsMi4zODIsMCwwLDAsMy4yMzQsMEw0OC42NDgsMjAuOWExLjAyNSwxLjAyNSwwLDAsMCwwLTEuNTQ2WiIvPjwvc3ZnPg==" alt="Icon for document-classification" width="80px" />
# Document Classification (technical name: **document-classification**

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/dc)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/document-classification)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  blocks_of_100  |  blocks_of_100  | eu10 - Europe (Frankfurt)  |
|  default  |  default  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **Document Classification** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **document-classification** by configuring your `usecase.json` file.

### Using the service plan **blocks_of_100**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "document-classification",
      "plan": "blocks_of_100"
    }
  ]
}
```

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "document-classification",
      "plan": "default"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency