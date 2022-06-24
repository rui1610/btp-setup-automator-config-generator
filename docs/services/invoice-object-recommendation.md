<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iaW52b2ljZS1vYmplY3QtcmVjb21tZW5kYXRpb24iIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDU2IDU2Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6IzA1M2I3MDt9LmNscy0ye2ZpbGw6IzBhNmVkMTt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPmludm9pY2Utb2JqZWN0LXJlY29tbWVuZGF0aW9uPC90aXRsZT48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik0yMiwyMkgxM2ExLjUsMS41LDAsMCwwLDAsM2g5YTEuNSwxLjUsMCwwLDAsMC0zWiIvPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTIyLDI4SDEzYTEuNSwxLjUsMCwwLDAsMCwzaDlhMS41LDEuNSwwLDAsMCwwLTNaIi8+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjIsMzRIMTNhMS41LDEuNSwwLDAsMCwwLDNoOWExLjUsMS41LDAsMCwwLDAtM1oiLz48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik0yNi41LDdIMTQuNTk0TDUuNSwxNlY0NmEyLjg4OSwyLjg4OSwwLDAsMCwzLDNoMThWNDZIOC41VjE5aDZhMy4wODQsMy4wODQsMCwwLDAsMi4yLS44NDRBMi44NDQsMi44NDQsMCwwLDAsMTcuNTk0LDE2VjEwSDI2LjVaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNNDkuNjA5LDcuODQ0QTIuOTYyLDIuOTYyLDAsMCwwLDQ3LjUsN2gtMThWNGgtM1Y1MmgzVjQ5aDE4YTIuODg5LDIuODg5LDAsMCwwLDMtM1YxMEEyLjg0OCwyLjg0OCwwLDAsMCw0OS42MDksNy44NDRaTTQ3LjUsNDZoLTE4VjEwaDE4WiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTMxLjIsMzAuM2w1LjUzOCw2LjUwOWEuNTc4LjU3OCwwLDAsMCwuNTMyLjE4Ny41NTMuNTUzLDAsMCwwLC40NDMtLjMyOGw4LjItMTIuNzM2YS42LjYsMCwwLDAtLjA4OS0uNzVsLS45NzUtLjk4M2EuNTQ4LjU0OCwwLDAsMC0uNTA5LS4xODcuNTQyLjU0MiwwLDAsMC0uNDIxLjMyOGwtNi40NjgsOS42OTNhLjUzOC41MzgsMCwwLDEtLjkzLjE4N0wzMi45NzEsMjguNDdhLjUuNSwwLDAsMC0uODQxLDBsLS45MzEuOTgzQS41NDYuNTQ2LDAsMCwwLDMxLjIsMzAuM1oiLz48L3N2Zz4=" alt="Icon for invoice-object-recommendation" width="80px" />
# Invoice Object Recommendation (technical name: **invoice-object-recommendation**

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/Invoice_Object_Recommendation)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **Invoice Object Recommendation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **invoice-object-recommendation** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "invoice-object-recommendation",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency