# blockchain-services (SERVICE)

Blockchain Application Enablement

## Additional details
- [Documentation](https://help.sap.com/viewer/p/BLOCKCHAIN_APPLICATION_ENABLEMENT/)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  blockchain-proof-of-state  |  blockchain-proof-of-state  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  blockchain-proof-of-history  |  blockchain-proof-of-history  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  blockchain-timestamp  |  blockchain-timestamp  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |
|  blockchain-hana-integration  |  Blockchain Services  | eu10 - Europe (Frankfurt)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **blockchain-services** by configuring your `usecase.json` file.

### Using the service plan **blockchain-proof-of-state** (blockchain-proof-of-state)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan: "blockchain-proof-of-state"
  ]
}
````

### Using the service plan **blockchain-proof-of-history** (blockchain-proof-of-history)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan: "blockchain-proof-of-history"
  ]
}
````

### Using the service plan **blockchain-timestamp** (blockchain-timestamp)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan: "blockchain-timestamp"
  ]
}
````

### Using the service plan **blockchain-hana-integration** (Blockchain Services)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan: "blockchain-hana-integration"
  ]
}
````


## Related categories
- Integration Suite