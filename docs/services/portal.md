<img src="data:image/svg+xml;base64, PHN2ZyBpZD0icG9ydGFsIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NiA1NiI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiMwNTNiNzA7fS5jbHMtMntmaWxsOiMwYTZlZDE7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5wb3J0YWw8L3RpdGxlPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTQ1Ljg0LDIzLjk2MmE4LjQ4OSw4LjQ4OSwwLDAsMC0xMi43ODMtNS43MTNBMTAuNzQ3LDEwLjc0NywwLDAsMCwyMi40MSwxMUMxMCwxMSwxMS4wOSwyMy45ODgsMTEuMDksMjMuOTg4QTEwLjI1NywxMC4yNTcsMCwwLDAsMTQuMjg1LDQ0SDIyVjI5aDlWNDRINDEuNWExMC40ODYsMTAuNDg2LDAsMCwwLDQuMzQtMjAuMDM4Wk00MS41LDQxSDM0VjI2SDE5VjQxSDE0LjI4NWE3LjI1Nyw3LjI1NywwLDAsMS0yLjI1OC0xNC4xNjJsMi4yNzktLjc2OC0uMjMyLTIuMzg5YzAtLjA0Mi0uMzc5LTQuMjM3LDIuMDEtNy4wMTNDMTcuNDYxLDE1LjA2OCwxOSwxNCwyMi40NjUsMTRjMi41MzUsMCw2LjQxNywyLjE4Niw3Ljk5NCw1LjMzOWwxLjE3NiwyLjg3MSwyLjQyNC0xLjMxOEE3LjYsNy42LDAsMCwxLDM3LjQ0OSwyMGE1LjU0Niw1LjU0NiwwLDAsMSw1LjQ0Myw0LjUxOGwuMjg4LDEuNTI4LDEuNDE1LjY0NkE3LjQ4Niw3LjQ4NiwwLDAsMSw0MS41LDQxWiIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxOS4wMDYgNDQgMjIuMDA2IDQ0IDIyLjAwNiAyOSAzMS4wMDYgMjkgMzEuMDA2IDQ0IDM0LjAwNiA0NCAzNC4wMDYgMjYgMTkuMDA2IDI2IDE5LjAwNiA0NCIvPjwvc3ZnPg==" alt="Icon for portal" width="80px" />
# **portal** (Cloud Portal Service)

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/Portal_Service/latest/en-US)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Cloud Portal Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **portal** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "portal",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Experience