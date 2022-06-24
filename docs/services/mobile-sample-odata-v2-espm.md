<img src="data:;base64, None" alt="Icon for mobile-sample-odata-v2-espm" width="80px" />
# Mobile Sample OData

Technical name: **mobile-sample-odata-v2-espm**

Technical service category: **SERVICE**

## Additional details


## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Mobile Sample OData v2 ESPM Service is a sample OData service used for development and testing  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> br10 - Brazil (Sao Paulo)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **Mobile Sample OData** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **mobile-sample-odata-v2-espm** by configuring your `usecase.json` file.

### Using the service plan **standard** (Mobile Sample OData v2 ESPM Service is a sample OData service used for development and testing)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "mobile-sample-odata-v2-espm",
      "plan": "standard"
    }
  ]
}
```

## Related categories
