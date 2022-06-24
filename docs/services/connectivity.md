<img src="data:image/svg+xml;base64, PHN2ZyBpZD0ic2FwLWhhbmEtY2xvdWQtY29ubmVjdG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NiA1NiI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiMwYTZlZDE7fS5jbHMtMntmaWxsOiMwNTNiNzA7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5zYXAtaGFuYS1jbG91ZC1jb25uZWN0b3I8L3RpdGxlPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTQxLjUsNDloLTlhMS41LDEuNSwwLDAsMCwwLDNoOWExLjUsMS41LDAsMCwwLDAtM1oiLz48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik00OC45OTEsMjVIMjUuMDA5QTMuMDA5LDMuMDA5LDAsMCwwLDIyLDI4LjAwOVY0Mi45OTFBMy4wMDksMy4wMDksMCwwLDAsMjUuMDA5LDQ2SDQ4Ljk5MUEzLjAwOSwzLjAwOSwwLDAsMCw1Miw0Mi45OTFWMjguMDA5QTMuMDA5LDMuMDA5LDAsMCwwLDQ4Ljk5MSwyNVptMCwxOEwyNSw0Mi45OTEsMjUuMDA5LDI4SDQ4Ljk5MWwuMDA5LjAwOVoiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0xOS4xMDksN2E2LjQ1NSw2LjQ1NSwwLDAsMSw1Ljg2NCw0LjAzM2wxLjMwNywzLjI5TDI5LjMxLDEyLjVhMy45MjIsMy45MjIsMCwwLDEsMi4wNDMtLjU5MSwzLjk4OCwzLjk4OCwwLDAsMSwzLjkxNCwzLjI0OWwuMjg4LDEuNTI5LDEuNDE1LjY0NmE1LjM1MSw1LjM1MSwwLDAsMSwzLDQuNjdINDNhOC4zNTUsOC4zNTUsMCwwLDAtNC43ODUtNy40QTYuOTQxLDYuOTQxLDAsMCwwLDI3Ljc2Miw5LjkyOCw5LjQ1Miw5LjQ1MiwwLDAsMCwxOS4wNTUsNEM4LjY1LDQsOS44LDE0LjYyMSw5LjgsMTQuNjIxQTguMzg3LDguMzg3LDAsMCwwLDEyLjQxLDMwLjk4NkgxOXYtM0gxMi40MWE1LjM4Nyw1LjM4NywwLDAsMS0xLjY3NS0xMC41MTVsMi4zMDgtLjc1OUwxMi43ODEsMTQuM2E4LjEsOC4xLDAsMCwxLDEuNS01LjI4NEE2LjUsNi41LDAsMCwxLDE5LjEwOSw3WiIvPjwvc3ZnPg==" alt="Icon for connectivity" width="80px"/>
# **connectivity** (Connectivity Service)

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/e54cc8fbbb571014beb5caaf6aa31280.html)
- [Documentation - Cloud Connector](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/e6c7616abb5710148cfcf3e75d96d596.html)
- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/connectivity-service)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  lite  |  lite  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> ch20 - cf-ch20<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  connectivity_proxy  |  connectivity_proxy  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> ch20 - cf-ch20<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Connectivity Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **connectivity** by configuring your `usecase.json` file.

### Using the service plan **lite**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "connectivity",
      "plan": "lite"
    }
  ]
}
```

### Using the service plan **connectivity_proxy**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "connectivity",
      "plan": "connectivity_proxy"
    }
  ]
}
```

## Related categories

- Integration Suite