# document-information-extraction-application (APPLICATION)

Document Information Extraction UI

## Additional details

- [Documentation](https://help.sap.com/viewer/product/DOCUMENT_INFORMATION_EXTRACTION)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  default  | ap10 - Australia (Sydney)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **Document Information Extraction UI** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **document-information-extraction-application** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "document-information-extraction-application",
      "plan": "default"      
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency