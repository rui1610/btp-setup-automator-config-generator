<img src="data:;base64, None" alt="Icon for sap-bigdataservices" width="80px" />
# Big Data Services

Technical name: **sap-bigdataservices**

Technical service category: **SERVICE**

## Additional details


## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Big Data Services  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **Big Data Services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-bigdataservices** by configuring your `usecase.json` file.

### Using the service plan **standard** (Big Data Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-bigdataservices",
      "plan": "standard"
    }
  ]
}
```

## Related categories
