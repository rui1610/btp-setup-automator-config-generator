# objectstore (SERVICE)

Object Store

## Additional details

- [Documentation](https://help.sap.com/viewer/product/ObjectStore/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/object-store)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  azure-standard  |  azure-standard  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  s3-standard  |  s3-standard  | br10 - Brazil (Sao Paulo)  |
|  gcs-standard  |  gcs-standard  | eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> us30 - US Central (IA)  |

## Sample configuration of **Object Store** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **objectstore** by configuring your `usecase.json` file.

### Using the service plan **azure-standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "objectstore",
      "plan": "azure-standard"
    }
  ]
}
```

### Using the service plan **s3-standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "objectstore",
      "plan": "s3-standard"
    }
  ]
}
```

### Using the service plan **gcs-standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "objectstore",
      "plan": "gcs-standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency