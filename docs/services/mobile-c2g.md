<img src="data:;base64, None" alt="Icon for mobile-c2g" width="80px" />
# Mobile Content

Technical name: **mobile-c2g**

Technical service category: **SERVICE**

## Additional details


## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Mobile Content to Go Service, the back-end for the corresponding iPhone application  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> br10 - Brazil (Sao Paulo)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **Mobile Content** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **mobile-c2g** by configuring your `usecase.json` file.

### Using the service plan **standard** (Mobile Content to Go Service, the back-end for the corresponding iPhone application)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "mobile-c2g",
      "plan": "standard"
    }
  ]
}
```

## Related categories
