<img src="data:;base64, None" alt="Icon for edge-services" width="80px"/>
# **edge-services** (SAP Edge Services)

Service category: **APPLICATION**

## Additional details


## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  Enterprise  |  SAP Edge Services  | eu10 - Europe (Frankfurt)<br> us20 - US West (WA)  |
|  Standard  |  SAP Edge Services Cloud Standard Edition  | eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)  |

## Sample configuration of **SAP Edge Services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **edge-services** by configuring your `usecase.json` file.

### Using the service plan **Enterprise** (SAP Edge Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "edge-services",
      "plan": "Enterprise"
    }
  ]
}
```

### Using the service plan **Standard** (SAP Edge Services Cloud Standard Edition)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "edge-services",
      "plan": "Standard"
    }
  ]
}
```

## Related categories
