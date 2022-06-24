<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iYmxvY2tjaGFpbi1zZXJ2aWNlcyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNTYgNTYiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojMDUzYjcwO30uY2xzLTJ7ZmlsbDojMGE2ZWQxO308L3N0eWxlPjwvZGVmcz48dGl0bGU+YmxvY2tjaGFpbi1zZXJ2aWNlczwvdGl0bGU+PHBvbHlnb24gY2xhc3M9ImNscy0xIiBwb2ludHM9IjQwIDM3LjYwNSA0MCA0MS43MDYgMzYuMzIgNDMuNzk3IDM2LjMyIDQ3LjI0OCA0MyA0My40NTIgNDMgMzUuOTAxIDQwIDM3LjYwNSIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMSIgcG9pbnRzPSIyMy42MTYgMjMuMTU4IDE5LjgwOCAyNS4zMjIgMTYgMjMuMTU4IDE2IDE5LjAzNyAxMyAxNy4zMzMgMTMgMjQuOTA0IDE5LjgwOCAyOC43NzIgMjYuNjE2IDI0LjkwNCAyNi42MTYgMTcuMzMzIDIzLjYxNiAxOS4wMzcgMjMuNjE2IDIzLjE1OCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMSIgcG9pbnRzPSIxNiAzNy42MDUgMTMgMzUuOTAxIDEzIDQzLjQ1MiAxOS43MDEgNDcuMjU5IDE5LjcwMSA0My44MDkgMTYgNDEuNzA2IDE2IDM3LjYwNSIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMSIgcG9pbnRzPSIyNy45OTUgMjAuOTU5IDMxLjc5MiAyMy4zNDMgMzQuNjE3IDIxLjczNyAyNy45OTUgMTcuMzMzIDI3Ljk5NSAyMC45NTkiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0yNi42MTYsMTUuNjA3VjcuODY4TDE5LjgwOCw0LDEzLDcuODY4djcuNzM5bDYuODA4LDMuODY5Wk0xNiw5LjYxNCwxOS44MDgsNy40NWwzLjgwOCwyLjE2NHY0LjI0OGwtMy44MDgsMi4xNjNMMTYsMTMuODYyWiIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIyNi42MTYgMjYuNjI5IDIzLjYxNiAyOC4zMzQgMjMuNjE2IDMyLjQzIDE5LjgwOCAzNC41OTMgMTYgMzIuNDMgMTYgMjguMzM0IDEzIDI2LjYyOSAxMyAzNC4xNzUgMTkuODA4IDM4LjA0NCAyNi42MTYgMzQuMTc1IDI2LjYxNiAyNi42MjkiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0yMS4yLDQwLjM5M3Y3LjczNkwyOC4wMDksNTJsNi44MTEtMy44NzFWNDAuMzkzbC02LjgxMS0zLjg2OVpNMzEuODIsNDIuMTM5djQuMjQ0bC0zLjgxMSwyLjE2NkwyNC4yLDQ2LjM4NFY0Mi4xMzhsMy44MDgtMi4xNjRaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMzYuMTkyLDIyLjU2OGwtNi44MDgsMy44Njh2Ny43MzlsNi44MDgsMy44NjlMNDMsMzQuMTc1VjI2LjQzNlpNNDAsMzIuNDNsLTMuODA4LDIuMTYzTDMyLjM4NCwzMi40M1YyOC4xODJsMy44MDgtMi4xNjRMNDAsMjguMTgyWiIvPjwvc3ZnPg==" alt="Icon for blockchain-services" width="80px" />
# Blockchain Application Enablement

Technical name: **blockchain-services**

Technical service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/p/BLOCKCHAIN_APPLICATION_ENABLEMENT/)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  blockchain-proof-of-state  |  blockchain-proof-of-state  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  blockchain-proof-of-history  |  blockchain-proof-of-history  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  blockchain-timestamp  |  blockchain-timestamp  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  blockchain-hana-integration  |  Blockchain Services  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **Blockchain Application Enablement** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **blockchain-services** by configuring your `usecase.json` file.

### Using the service plan **blockchain-proof-of-state**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan": "blockchain-proof-of-state"
    }
  ]
}
```

### Using the service plan **blockchain-proof-of-history**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan": "blockchain-proof-of-history"
    }
  ]
}
```

### Using the service plan **blockchain-timestamp**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan": "blockchain-timestamp"
    }
  ]
}
```

### Using the service plan **blockchain-hana-integration** (Blockchain Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan": "blockchain-hana-integration"
    }
  ]
}
```

## Related categories

- Integration Suite