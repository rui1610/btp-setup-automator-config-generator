# personal-data-manager-service (SERVICE)

Personal Data Manager

## Additional details

- [Documentation](https://help.sap.com/viewer/product/PERSONAL_DATA_MANAGER/SHIP/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/personal-data-manager)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  free  |  free  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap21 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  standard  |  standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap21 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)  |

## Sample configuration of **Personal Data Manager** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **personal-data-manager-service** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "personal-data-manager-service",
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
      "name": "personal-data-manager-service",
      "plan": "standard"      
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency