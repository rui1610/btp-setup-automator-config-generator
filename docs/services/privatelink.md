# privatelink (SERVICE)

Private Link Service

## Additional details
- [Documentation](https://help.sap.com/viewer/product/PRIVATE_LINK/CLOUD/en-US)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **privatelink** by configuring your `usecase.json` file.

### Using the service plan **standard** (standard)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "privatelink",
      "plan: "standard"
  ]
}
````


## Related categories
- Extension Suite - Development Efficiency