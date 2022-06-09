# redis (SERVICE)

Redis

## Additional details

- [Documentation](https://help.sap.com/viewer/product/Redis/Cloud/en-US)
- [Tutorial](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/971730b26c93492e980a03c4619f9916.html)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  xsmall  |  xsmall  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  medium  |  medium  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  large  |  large  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  small  |  small  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Redis** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **redis** by configuring your `usecase.json` file.

### Using the service plan **xsmall**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "redis",
      "plan": "xsmall"      
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
      "name": "redis",
      "plan": "medium"      
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
      "name": "redis",
      "plan": "large"      
    }
  ]
}
```

### Using the service plan **small**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "redis",
      "plan": "small"      
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency