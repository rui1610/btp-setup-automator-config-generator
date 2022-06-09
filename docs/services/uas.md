# uas (SERVICE)

Usage Data Management

## Additional details

- [Documentation](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/bf2b3043d0474ea0a2c11c0390460d85.html)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/usage-data-management-service)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  reporting-ga-admin  |  reporting-ga-admin  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |
|  reporting-directory  |  reporting-directory  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Usage Data Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **uas** by configuring your `usecase.json` file.

### Using the service plan **reporting-ga-admin**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "uas",
      "plan": "reporting-ga-admin"      
    }
  ]
}
```

### Using the service plan **reporting-directory**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "uas",
      "plan": "reporting-directory"      
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency