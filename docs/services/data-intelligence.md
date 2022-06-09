# data-intelligence (SERVICE)

SAP Data Intelligence

## Additional details

- [Documentation](https://help.sap.com/viewer/product/SAP_DATA_INTELLIGENCE/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-data-intelligence)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  enterprise  |  enterprise  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)  |
|  dedicated  |  Dedicated  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)  |
|  tenant  |  Tenant  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)  |

## Sample configuration of **SAP Data Intelligence** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **data-intelligence** by configuring your `usecase.json` file.

### Using the service plan **enterprise**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-intelligence",
      "plan": "enterprise"      
    }
  ]
}
```

### Using the service plan **dedicated** (Dedicated)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-intelligence",
      "plan": "dedicated"      
    }
  ]
}
```

### Using the service plan **tenant** (Tenant)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-intelligence",
      "plan": "tenant"      
    }
  ]
}
```

## Related categories

- Integration Suite