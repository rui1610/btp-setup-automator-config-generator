<img src="data:image/svg+xml;base64, PHN2ZyBpZD0ic2VydmljZS10aWNrZXQtaW50ZWxsaWdlbmNlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NiA1NiI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiMwNTNiNzA7fS5jbHMtMntmaWxsOiMwYTZlZDE7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5zZXJ2aWNlLXRpY2tldC1pbnRlbGxpZ2VuY2U8L3RpdGxlPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTEzLjAwOCwyMmExLjUsMS41LDAsMCwwLTEuNS0xLjVoLTZhMS41LDEuNSwwLDAsMCwwLDNoNi4wMDVBMS41LDEuNSwwLDAsMCwxMy4wMDgsMjJaIi8+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMTQuNTA5LDE0LjUwOUg4LjVhMS41LDEuNSwwLDAsMCwwLDNoNi4wMDVhMS41LDEuNSwwLDAsMCwwLTNaIi8+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMTQuNTA5LDI2LjVIMTEuNDU1YTEuNSwxLjUsMCwxLDAsMCwzaDMuMDU0YTEuNSwxLjUsMCwwLDAsMC0zWiIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMSIgcG9pbnRzPSIzOS4zMjggMzkuNCAzNi44OCAzNi42MTQgMzUuMTkxIDM4LjMwMyAzOS4zMjggNDIuODYxIDQ3LjE3OCAzMy43NDQgNDUuNDkgMzIuMDU2IDM5LjMyOCAzOS40Ii8+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNNDEuNTExLDI2LjVBMTAuNDg5LDEwLjQ4OSwwLDEsMCw1MiwzNi45OSwxMC40ODgsMTAuNDg4LDAsMCwwLDQxLjUxMSwyNi41Wm0wLDE4LjcyOWE4LjI0MSw4LjI0MSwwLDEsMSw4LjI0MS04LjI0MUE4LjI1LDguMjUsMCwwLDEsNDEuNTExLDQ1LjIzMVoiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik00OS4wMDgsOC41MjFIMjIuMDI4YTIuOTkzLDIuOTkzLDAsMCwwLTIuOTkyLDIuOTkyVjI5LjUwNkEyLjk5MywyLjk5MywwLDAsMCwyMi4wMjgsMzIuNWg2Ljg3OUExMy40NjEsMTMuNDYxLDAsMCwxLDMwLjM1OSwyOS41aC02LjNsNS42NS0zLjc2N2ExLjEyMywxLjEyMywwLDEsMC0xLjI0Ny0xLjg2N2wtNi40Myw0LjI4NywwLTE0LjgzOCwxMS4zMzgsNy41NTdhMy44NjksMy44NjksMCwwLDAsNC4zLDBMNDksMTMuMzE5bDAsMTIuNDVBMTMuNDkxLDEzLjQ5MSwwLDAsMSw1MiwyOC41NTlWMTEuNTEzQTIuOTkzLDIuOTkzLDAsMCwwLDQ5LjAwOCw4LjUyMVptLTEzLDkuODYzYS44NzYuODc2LDAsMCwxLS45NzgsMGwtMTAuMy02Ljg2Nkg0Ni4zWiIvPjwvc3ZnPg==" alt="Icon for service-ticket-intelligence" width="80px"/>
# **service-ticket-intelligence** (Service Ticket Intelligence)

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/stint)
- [Support](https://help.sap.com/viewer/934ccff77ddb4fa2bf268a0085984db0/LATEST/en-US/76a77fbf8d3645978d98711450f0b8bc.html)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/service-ticket-intelligence)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  blocks_of_100  |  blocks_of_100  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> us10 - US East (VA)<br> us30 - US Central (IA)  |
|  free  |  Free  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> us10 - US East (VA)<br> us30 - US Central (IA)  |
|  standard  |  standard  | eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> us10 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Service Ticket Intelligence** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **service-ticket-intelligence** by configuring your `usecase.json` file.

### Using the service plan **blocks_of_100**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "service-ticket-intelligence",
      "plan": "blocks_of_100"
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
      "category": "SERVICE",
      "name": "service-ticket-intelligence",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "service-ticket-intelligence",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency