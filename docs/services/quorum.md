# quorum (SERVICE)

Quorum

## Additional details
- [Documentation](https://help.sap.com/viewer/p/QUORUM)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  cyon  |  cyon  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  testnet  |  testnet  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  dev  |  dev  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **quorum** by configuring your `usecase.json` file.

### Using the service plan **cyon** (cyon)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "quorum",
      "plan: "cyon"
  ]
}
````

### Using the service plan **testnet** (testnet)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "quorum",
      "plan: "testnet"
  ]
}
````

### Using the service plan **dev** (dev)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "quorum",
      "plan: "dev"
  ]
}
````


## Related categories
- Integration Suite