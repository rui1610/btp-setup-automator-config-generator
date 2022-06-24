<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iZG9jdW1lbnQtc2VydmljZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNTYgNTYiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojMGE2ZWQxO30uY2xzLTJ7ZmlsbDojMDUzYjcwO30uY2xzLTN7ZmlsbDojMDA5MmQxO308L3N0eWxlPjwvZGVmcz48dGl0bGU+ZG9jdW1lbnQtc2VydmljZTwvdGl0bGU+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNNDksMjBoLS4yTDQzLDhIMTNMNy4yLDIwSDdhMi45NDYsMi45NDYsMCwwLDAtMywzVjQ0YTIuOTQ2LDIuOTQ2LDAsMCwwLDMsM0g0OWEyLjk0NiwyLjk0NiwwLDAsMCwzLTNWMjNBMi45NDYsMi45NDYsMCwwLDAsNDksMjBabS0zLjItLjFIMTAuMWw0LjYtOS42SDQxLjNNNyw0NFYyM0g0OVY0NFoiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMzQgMzggMjIgMzggMjIgMzYuNSAxOSAzNi41IDE5IDM4IDE5IDQxIDM3IDQxIDM3IDM4IDM3IDM2LjUgMzQgMzYuNSAzNCAzOCIvPjxsaW5lIGNsYXNzPSJjbHMtMyIgeDE9IjQxLjMiIHkxPSIxMC4zIiB4Mj0iNDUuOCIgeTI9IjE5LjkiLz48cmVjdCBjbGFzcz0iY2xzLTIiIHg9IjE0LjEiIHk9IjE2LjEiIHdpZHRoPSIyNy44IiBoZWlnaHQ9IjEuNSIvPjxyZWN0IGNsYXNzPSJjbHMtMiIgeD0iMTYiIHk9IjEyLjQiIHdpZHRoPSIyNCIgaGVpZ2h0PSIxLjUiLz48L3N2Zz4=" alt="Icon for sdm" width="80px"/>
# **sdm** (Document Management Service, Integration Option)

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/p/DOCUMENT_MANAGEMENT)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/document-management-service-integration-option)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  free  |  free  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Document Management Service, Integration Option** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sdm** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sdm",
      "plan": "standard"
    }
  ]
}
```

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sdm",
      "plan": "free"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Experience