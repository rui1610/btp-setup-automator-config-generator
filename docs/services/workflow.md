<img src="data:image/svg+xml;base64, PHN2ZyBpZD0id29ya2Zsb3ctc2VydmljZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNTYgNTYiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojNWE3YTk0O30uY2xzLTJ7ZmlsbDojMDA5MmQxO308L3N0eWxlPjwvZGVmcz48dGl0bGU+d29ya2Zsb3ctc2VydmljZTwvdGl0bGU+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMzYuNjg3LDE2SDQ5LjMxM0EyLjY4NywyLjY4NywwLDAsMCw1MiwxMy4zMTNWNi42ODdBMi42ODcsMi42ODcsMCwwLDAsNDkuMzEzLDRIMzYuNjg3QTIuNjg3LDIuNjg3LDAsMCwwLDM0LDYuNjg3VjEwbC01LjA2OCwwVjIzLjU1MWExLjQ0OSwxLjQ0OSwwLDAsMC0uMzEzLjIwOEwyNS40NCwyNi45MzhhMS40NDYsMS40NDYsMCwwLDAtLjIwOC4zMTJIMjJWMjQuNjg3QTIuNjg3LDIuNjg3LDAsMCwwLDE5LjMxMywyMkg2LjY4N0EyLjY4NywyLjY4NywwLDAsMCw0LDI0LjY4N3Y2LjYyN0EyLjY4NywyLjY4NywwLDAsMCw2LjY4NywzNEgxOS4zMTNBMi42ODcsMi42ODcsMCwwLDAsMjIsMzEuMzEzVjI4Ljc1aDMuMjMzYTEuNDQ4LDEuNDQ4LDAsMCwwLC4yMDcuMzExbDMuMTgsMy4xOGExLjQ0NCwxLjQ0NCwwLDAsMCwuMzEyLjIwN1Y0Ni4xMjVsNS4wNjgsMHYzLjE5M0EyLjY4NywyLjY4NywwLDAsMCwzNi42ODcsNTJINDkuMzEzQTIuNjg3LDIuNjg3LDAsMCwwLDUyLDQ5LjMxM1Y0Mi42ODdBMi42ODcsMi42ODcsMCwwLDAsNDkuMzEzLDQwSDM2LjY4N0EyLjY4NywyLjY4NywwLDAsMCwzNCw0Mi42ODdWNDQuNjJIMzAuNDMyVjMyLjQ0OGExLjQ0NiwxLjQ0NiwwLDAsMCwuMzExLS4yMDdsMy4xNzktMy4xNzlhMS41LDEuNSwwLDAsMCwwLTIuMTIzbC0zLjE4LTMuMThhMS40NDYsMS40NDYsMCwwLDAtLjMxLS4yMDZWMTEuNUgzNHYxLjgwOUEyLjY4NywyLjY4NywwLDAsMCwzNi42ODcsMTZaIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSIzNCIgeT0iNCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjEyIiByeD0iMi42ODciIHJ5PSIyLjY4NyIvPjxyZWN0IGNsYXNzPSJjbHMtMiIgeD0iMzQiIHk9IjQwIiB3aWR0aD0iMTgiIGhlaWdodD0iMTIiIHJ4PSIyLjY4NyIgcnk9IjIuNjg3Ii8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSI0IiB5PSIyMiIgd2lkdGg9IjE4IiBoZWlnaHQ9IjEyIiByeD0iMi42ODciIHJ5PSIyLjY4NyIvPjwvc3ZnPg==" alt="Icon for workflow" width="80px" />
# **workflow** (Workflow)

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/p/WORKFLOW_SERVICE)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Workflow** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **workflow** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "workflow",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Process Automation