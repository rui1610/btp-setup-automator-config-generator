<img src="data:image/svg+xml;base64, PHN2ZyBpZD0ibWVzc2FnaW5nLXNlcnZpY2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDU2IDU2Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6IzA1M2I3MDt9LmNscy0ye2ZpbGw6IzBhNmVkMTt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPm1lc3NhZ2luZy1zZXJ2aWNlPC90aXRsZT48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik0xOSwzOS4zMTJIMTQuMjg1QTcuMjU3LDcuMjU3LDAsMCwxLDEyLjAyNywyNS4xNWwyLjI3OS0uNzY3LS4yMzItMi4zOWMwLS4wNDItLjM3OS00LjIzNiwyLjAxLTcuMDEyLDEuMzc3LTEuNiwzLjUyNC0yLjUsNi4zODEtMi42NjdhOC41NjMsOC41NjMsMCwwLDEsNy44LDUuMzU1bDEuMzA2LDMuMjg5LDMuMDMxLTEuODI3YTUuNDUxLDUuNDUxLDAsMCwxLDIuODQzLS44MTksNS41NDYsNS41NDYsMCwwLDEsNS40NDMsNC41MThsLjI4OCwxLjUyOUw0NC42LDI1YzIuMiwxLDIuOCwzLjAxLDMuMjg1LDUuMzA4SDUxLjFjLS41MTctMy41OS0yLjA2OS02LjU4Mi01LjI2LTguMDM3YTguNDg3LDguNDg3LDAsMCwwLTEyLjc4My01LjcxM0ExMS41NTgsMTEuNTU4LDAsMCwwLDIyLjQxLDkuMzEyQzkuNzUzLDkuOTgzLDExLjA5LDIyLjMsMTEuMDksMjIuM2ExMC4yNTcsMTAuMjU3LDAsMCwwLDMuMiwyMC4wMTJIMTkiLz48cG9seWxpbmUgY2xhc3M9ImNscy0xIiBwb2ludHM9IjQ2Ljc1NiA0Mi4zNjkgNDMuNjU3IDQ1LjQ2OCA0NS41NjQgNDcuMzc1IDUyIDQwLjkzOSA0NS41NjQgMzQuNTAzIDQzLjY1NyAzNi40MSA0Ni42MzYgMzkuMzEzIDM3LjAzOCAzOS4zMTMgMzcuMDIyIDQyLjMyNiIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxOS4wMDEgNDIuMzEgMjIuMDAxIDQyLjMxIDIyLjAwMSAzMS43IDI3Ljk4IDM2LjMxIDM0LjAwMSAzMS43IDM0LjAwMSA0Mi4zMSAzNy4wMjIgNDIuMzI2IDM3LjEwMyAyNy4zMSAzNC4wMDEgMjcuMzEgMjcuOTMyIDMxLjkwMyAyMi4wMDEgMjcuMzEgMTkuMDAxIDI3LjMxIDE5LjAwMSA0Mi4zMSIvPjwvc3ZnPg==" alt="Icon for integration-suite-advanced-event-mesh" width="80px" />
# **integration-suite-advanced-event-mesh** (SAP Integration Suite, advanced event mesh)

Service category: **APPLICATION**

## Additional details

- [Documentation](https://help.sap.com/docs/SAP_ADVANCED_EVENT_MESH/728c56cd25854f0fad611eb26ae17152/0d4bcd5a2be744688039160b9bb289ae.html)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **SAP Integration Suite, advanced event mesh** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **integration-suite-advanced-event-mesh** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "integration-suite-advanced-event-mesh",
      "plan": "default"
    }
  ]
}
```

## Related categories

- Integration Suite