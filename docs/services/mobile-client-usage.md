# mobile-client-usage (SERVICE)

Mobile Client Usage Service

## Additional details


## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Mobile Client Usage Service allows mobile application to upload client usage information and to analyze them on the server  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> br10 - Brazil (Sao Paulo)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **Mobile Client Usage Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **mobile-client-usage** by configuring your `usecase.json` file.

### Using the service plan **standard** (Mobile Client Usage Service allows mobile application to upload client usage information and to analyze them on the server)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "mobile-client-usage",
      "plan": "standard"      
    }
  ]
}
```

## Related categories
