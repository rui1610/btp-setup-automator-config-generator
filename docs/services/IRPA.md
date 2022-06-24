<img src="data:image/svg+xml;base64, PHN2ZyBpZD0ic2FwLWludGVsbGlnZW50LXJvYm90aWMtcHJvY2Vzcy1hdXRvbWF0aW9uIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NiA1NiI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiMwNTNiNzA7fS5jbHMtMntmaWxsOiMwYTZlZDE7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5zYXAtaW50ZWxsaWdlbnQtcm9ib3RpYy1wcm9jZXNzLWF1dG9tYXRpb248L3RpdGxlPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTI4LDE1Ljk2MWM5LjkyNSwwLDE4LDcuNDEsMTgsMTYuNTE4UzM3LjkyNSw0OSwyOCw0OXMtMTgtNy40MS0xOC0xNi41MTgsOC4wNzUtMTYuNTE4LDE4LTE2LjUxOG0wLTNjLTExLjYsMC0yMSw4Ljc0LTIxLDE5LjUyMlMxNi40LDUyLDI4LDUyczIxLTguNzQsMjEtMTkuNTIxUzM5LjYsMTIuOTU3LDI4LDEyLjk1N1oiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0zNC44MSwyMy4zOTJIMjEuMTM3YTguMTcyLDguMTcyLDAsMCwwLDAsMTYuMzQ0SDM0LjgxYTguMTcyLDguMTcyLDAsMCwwLDAtMTYuMzQ0Wm0wLDEzLjM0MUgyMS4xMzdhNS4xNjksNS4xNjksMCwwLDEsMC0xMC4zMzhIMzQuODFhNS4xNjksNS4xNjksMCwwLDEsMCwxMC4zMzhaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMjIuMTk0LDI4Ljc5MWEyLjU0NywyLjU0NywwLDEsMCwyLjU1LDIuNTQ3QTIuNTQ4LDIuNTQ4LDAsMCwwLDIyLjE5NCwyOC43OTFaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMzMuODQxLDI4Ljc5MWEyLjU0NywyLjU0NywwLDEsMCwyLjU1LDIuNTQ3QTIuNTQ4LDIuNTQ4LDAsMCwwLDMzLjg0MSwyOC43OTFaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMjcuMjE4LDkuODQ4djMuMTQ2Yy4yNjEtLjAwOS41MTgtLjAzNy43ODItLjAzNy4yNDIsMCwuNDc3LjAyNy43MTguMDM0VjkuODYxQTIuOTYsMi45NiwwLDAsMCwzMSw3YTMsMywwLDEsMC02LDBBMi45NjEsMi45NjEsMCwwLDAsMjcuMjE4LDkuODQ4WiIvPjwvc3ZnPg==" alt="Icon for IRPA" width="80px" />
# SAP Intelligent Robotic Process Automation (technical name: **IRPA**

Service category: **APPLICATION**

## Additional details

- [Documentation](https://help.sap.com/viewer/p/IRPA)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-intelligent-rpa)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  SAP Intelligent Robotic Process Automation  | ap10 - Australia (Sydney)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |
|  free  |  Free  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |
|  concurrent  |  Concurrent  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **SAP Intelligent Robotic Process Automation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **IRPA** by configuring your `usecase.json` file.

### Using the service plan **default** (SAP Intelligent Robotic Process Automation)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "IRPA",
      "plan": "default"
    }
  ]
}
```

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "IRPA",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **concurrent** (Concurrent)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "IRPA",
      "plan": "concurrent"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Process Automation