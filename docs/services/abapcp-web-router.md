# abapcp-web-router (APPLICATION)

Web access for ABAP

## Additional details
- [Documentation](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/98928b0941294c74b946cdcefca9b047.html)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  Web Access for ABAP Environment  | eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **abapcp-web-router** by configuring your `usecase.json` file.

### Using the service plan **default** (Web Access for ABAP Environment)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "APPLICATION",
      "name": "abapcp-web-router",
      "plan: "default"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency