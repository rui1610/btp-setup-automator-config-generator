<img src="data:;base64, None" alt="Icon for mobile-app-update" width="80px"/>
# **mobile-app-update** (Mobile App Update)

Service category: **SERVICE**

## Additional details


## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Mobile App Update Service is used to update new versions of an App Modeler application  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> br10 - Brazil (Sao Paulo)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **Mobile App Update** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **mobile-app-update** by configuring your `usecase.json` file.

### Using the service plan **standard** (Mobile App Update Service is used to update new versions of an App Modeler application)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "mobile-app-update",
      "plan": "standard"
    }
  ]
}
```

## Related categories
