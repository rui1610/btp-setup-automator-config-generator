# hyperledger-fabric (SERVICE)

Hyperledger Fabric

## Additional details
- [Documentation](https://help.sap.com/viewer/p/HYPERLEDGER_FABRIC/)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  testnet  |  testnet  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  dev  |  dev  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  backbone  |  backbone  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  cyon  |  cyon  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  node  |  node  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  channel  |  channel  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **hyperledger-fabric** by configuring your `usecase.json` file.

### Using the service plan **testnet** (testnet)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "hyperledger-fabric",
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
      "name": "hyperledger-fabric",
      "plan: "dev"
  ]
}
````

### Using the service plan **backbone** (backbone)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan: "backbone"
  ]
}
````

### Using the service plan **cyon** (cyon)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan: "cyon"
  ]
}
````

### Using the service plan **node** (node)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan: "node"
  ]
}
````

### Using the service plan **channel** (channel)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan: "channel"
  ]
}
````


## Related categories
- Integration Suite