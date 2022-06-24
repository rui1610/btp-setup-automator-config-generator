<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iY2xvdWQtZm9yLWFuYWx5dGljcyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNTYgNTYiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojMGE2ZWQxO30uY2xzLTJ7ZmlsbDojMDUzYjcwO308L3N0eWxlPjwvZGVmcz48dGl0bGU+Y2xvdWQtZm9yLWFuYWx5dGljczwvdGl0bGU+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjksMzMuNDcxLDQxLjk0Nyw0Ni40MjJBMjMuMywyMy4zLDAsMCwxLDI5LDUxLjg1N2EyOC4xMDUsMjguMTA1LDAsMCwxLTMuODk0LDBBMjMuMDc4LDIzLjA3OCwwLDAsMSw2LjgwOCwzOS45LDIyLjU0NywyMi41NDcsMCwwLDEsNCwyOC45NDMsMjIuNzQ1LDIyLjc0NSwwLDAsMSw5LjQzNCwxMy45MDlhMzYuNTcsMzYuNTcsMCwwLDEsMi43MTctMi42MjZBMjIuNzYsMjIuNzYsMCwwLDEsMjUuMSw1Ljg0OVYyOS42NjhaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNNTAuNjQxLDIwLjUyMSwzMC4zNTUsMjkuNDg3LDQ0LjU3Myw0My44bDEuNDQ5LDEuMjY4QTI0LjAzLDI0LjAzLDAsMCwwLDUyLDI4Ljk0MywyNi40NDgsMjYuNDQ4LDAsMCwwLDUwLjY0MSwyMC41MjFaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNNDkuMDExLDE2Ljk4OUEyNC44MDksMjQuODA5LDAsMCwwLDI5LDQuMDM4VjI1Ljg2NEw0Ny4yLDE3LjhaIi8+PC9zdmc+" alt="Icon for sap-analytics-cloud-embedded-edition" width="80px" />
# SAP Analytics Cloud, embedded edition

Technical name: **sap-analytics-cloud-embedded-edition**

Technical service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/SAC_EMBEDDED_EDITION/1.0/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-analytics-cloud-embedded-edition)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **SAP Analytics Cloud, embedded edition** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-analytics-cloud-embedded-edition** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-analytics-cloud-embedded-edition",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Experience