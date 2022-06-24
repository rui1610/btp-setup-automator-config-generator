<img src="data:image/svg+xml;base64, PHN2ZyBpZD0icHJpbnQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDU2IDU2Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6IzA1M2I3MDt9LmNscy0ye2ZpbGw6IzBhNmVkMTt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPnByaW50PC90aXRsZT48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik01MS4xMDksMTMuODkxQTIuODc5LDIuODc5LDAsMCwwLDQ5LDEzSDQzVjdhMi44OTEsMi44OTEsMCwwLDAtLjg5MS0yLjEwOUEyLjg3OSwyLjg3OSwwLDAsMCw0MCw0SDE2YTIuODMzLDIuODMzLDAsMCwwLTIuMTU2Ljg5MUEyLjk2MiwyLjk2MiwwLDAsMCwxMyw3djZIN2EyLjgzMywyLjgzMywwLDAsMC0yLjE1Ni44OTFBMi45NjIsMi45NjIsMCwwLDAsNCwxNlYzMWEyLjg4OSwyLjg4OSwwLDAsMCwzLDNoNlYzMUg3VjE2SDQ5VjMxSDQzdjNoNmEyLjk2MiwyLjk2MiwwLDAsMCwyLjEwOS0uODQ0QTIuODQ0LDIuODQ0LDAsMCwwLDUyLDMxVjE2QTIuODkxLDIuODkxLDAsMCwwLDUxLjEwOSwxMy44OTFaTTQwLDEzSDE2VjdINDBaIi8+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNNDYsMjAuNWExLjUxMSwxLjUxMSwwLDAsMC0uNDIyLTEuMDMxQTEuMzgxLDEuMzgxLDAsMCwwLDQ0LjUsMTloLTZhMS4zNzgsMS4zNzgsMCwwLDAtMS4wNzguNDY5QTEuNTExLDEuNTExLDAsMCwwLDM3LDIwLjUsMS4zMjUsMS4zMjUsMCwwLDAsMzguNSwyMmg2QTEuMzI3LDEuMzI3LDAsMCwwLDQ2LDIwLjVaIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSIxOSIgeT0iMzEiIHdpZHRoPSIxOCIgaGVpZ2h0PSIzIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSIxOSIgeT0iMzciIHdpZHRoPSIxOCIgaGVpZ2h0PSIzIi8+PHBvbHlnb24gY2xhc3M9ImNscy0yIiBwb2ludHM9IjM3IDQzIDE5IDQzIDI4IDQ3LjEwMiAzNyA0MyIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTQyLjEwOSwyNS44OTFBMi44NzksMi44NzksMCwwLDAsNDAsMjVIMTZhMi44MzMsMi44MzMsMCwwLDAtMi4xNTYuODkxQTIuOTYyLDIuOTYyLDAsMCwwLDEzLDI4VjQ5YTIuODg5LDIuODg5LDAsMCwwLDMsM0g0MGEyLjk2MiwyLjk2MiwwLDAsMCwyLjEwOS0uODQ0QTIuODQ4LDIuODQ4LDAsMCwwLDQzLDQ5VjI4QTIuODkxLDIuODkxLDAsMCwwLDQyLjEwOSwyNS44OTFaTTQwLDQ5SDE2VjI4SDQwWiIvPjwvc3ZnPg==" alt="Icon for print-app" width="80px" />
# **print-app** (Print Service)

Service category: **APPLICATION**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/SCP_PRINT_SERVICE/SHIP/en-US)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> us10 - US East (VA)<br> us20 - US West (WA)  |

## Sample configuration of **Print Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **print-app** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "print-app",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Experience