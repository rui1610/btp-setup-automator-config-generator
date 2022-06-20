# one-mds (SERVICE)

Master Data Integration

## Additional details

- [Documentation](https://help.sap.com/viewer/product/SAP_MASTER_DATA_INTEGRATION/CLOUD/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/master-data-integration?region=all)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  sap-integration  |  sap-integration  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  s4hana-onpremise  |  s4hana-onpremise  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **Master Data Integration** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **one-mds** by configuring your `usecase.json` file.

### Using the service plan **sap-integration**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "one-mds",
      "plan": "sap-integration"
    }
  ]
}
```

### Using the service plan **s4hana-onpremise**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "one-mds",
      "plan": "s4hana-onpremise"
    }
  ]
}
```

## Related categories

- Integration Suite