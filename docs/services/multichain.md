# multichain (SERVICE)

MultiChain

## Additional details

- [Documentation](https://help.sap.com/viewer/p/MULTICHAIN/)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  small  |  small  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  large  |  large  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  medium  |  medium  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  cyon  |  cyon  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration of **MultiChain** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **multichain** by configuring your `usecase.json` file.

### Using the service plan **small**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "multichain",
      "plan": "small"
    }
  ]
}
```

### Using the service plan **large**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "multichain",
      "plan": "large"
    }
  ]
}
```

### Using the service plan **medium**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "multichain",
      "plan": "medium"
    }
  ]
}
```

### Using the service plan **cyon**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "multichain",
      "plan": "cyon"
    }
  ]
}
```

## Related categories

- Integration Suite