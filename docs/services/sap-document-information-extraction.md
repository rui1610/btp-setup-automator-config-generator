<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iZG9jdW1lbnQtaW5mb3JtYXRpb24tZXh0cmFjdGlvbiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNTYgNTYiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojMDUzYjcwO30uY2xzLTJ7ZmlsbDojMGE2ZWQxO308L3N0eWxlPjwvZGVmcz48dGl0bGU+ZG9jdW1lbnQtaW5mb3JtYXRpb24tZXh0cmFjdGlvbjwvdGl0bGU+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMzcsNDUuOTVWNDlhMi44ODgsMi44ODgsMCwwLDEtMywzSDdhMi44ODgsMi44ODgsMCwwLDEtMy0zVjE2TDE2LDRIMzRhMi45NjYsMi45NjYsMCwwLDEsMi4xMDkuODQzQTIuODQ5LDIuODQ5LDAsMCwxLDM3LDd2NkgzNFY3SDE5djlhMi44NDUsMi44NDUsMCwwLDEtLjg5MSwyLjE1NiwzLjA4NiwzLjA4NiwwLDAsMS0yLjIuODQ0SDdWNDlIMzRWNDUuOTVaIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSI0MyIgeT0iMTMuNjkzIiB3aWR0aD0iOSIgaGVpZ2h0PSIzIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSI0MyIgeT0iMTguMjY4IiB3aWR0aD0iOSIgaGVpZ2h0PSIzIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSI0MyIgeT0iMjUuNjkzIiB3aWR0aD0iOSIgaGVpZ2h0PSIzIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSI0MyIgeT0iMzAuMjY4IiB3aWR0aD0iOSIgaGVpZ2h0PSIzIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSI0MyIgeT0iMzcuNzI4IiB3aWR0aD0iOSIgaGVpZ2h0PSIzIi8+PHJlY3QgY2xhc3M9ImNscy0yIiB4PSI0MyIgeT0iNDIuMzAzIiB3aWR0aD0iOSIgaGVpZ2h0PSIzIi8+PHBvbHlnb24gY2xhc3M9ImNscy0yIiBwb2ludHM9IjM5Ljk4NCA0NS45ODIgMzkuOTg0IDEyLjk4MiAyNC45ODQgMjkuNDgyIDM5Ljk4NCA0NS45ODIiLz48L3N2Zz4=" alt="Icon for sap-document-information-extraction" width="80px" />
# Document Information Extraction (technical name: **sap-document-information-extraction**

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/dox)
- [Support](https://help.sap.com/viewer/5fa7265b9ff64d73bac7cec61ee55ae6/SHIP/en-US/7ddd52320bae4d539393a4365b9f6aa6.html)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/document-information-extraction)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | ap10 - Australia (Sydney)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |
|  blocks_of_100  |  blocks_of_100  | ap10 - Australia (Sydney)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **Document Information Extraction** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-document-information-extraction** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-document-information-extraction",
      "plan": "default"
    }
  ]
}
```

### Using the service plan **blocks_of_100**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-document-information-extraction",
      "plan": "blocks_of_100"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency