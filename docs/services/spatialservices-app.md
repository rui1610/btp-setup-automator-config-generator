# spatialservices-app (APPLICATION)

HANA Spatial Services

## Additional details


## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  professional  |  HANA Spatial Services  | eu10 - Europe (Frankfurt)  |
|  starter  |  HANA Spatial Services  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **HANA Spatial Services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **spatialservices-app** by configuring your `usecase.json` file.

### Using the service plan **professional** (HANA Spatial Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "spatialservices-app",
      "plan": "professional"
    }
  ]
}
```

### Using the service plan **starter** (HANA Spatial Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "spatialservices-app",
      "plan": "starter"
    }
  ]
}
```

## Related categories
