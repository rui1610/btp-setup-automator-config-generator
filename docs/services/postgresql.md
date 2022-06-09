# postgresql (SERVICE)

PostgreSQL

## Additional details
- [Documentation](https://help.sap.com/viewer/product/PostgreSQL/Cloud/en-US)
- [Tutorial](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/314e0968334d45ab855924497759671b.html)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  large  |  large  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us30 - US Central (IA)  |
|  xxsmall  |  xxsmall  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us30 - US Central (IA)  |
|  xsmall  |  xsmall  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  small  |  small  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  medium  |  medium  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **postgresql** by configuring your `usecase.json` file.

### Using the service plan **large** (large)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "postgresql",
      "plan: "large"
  ]
}
```

### Using the service plan **xxsmall** (xxsmall)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "postgresql",
      "plan: "xxsmall"
  ]
}
```

### Using the service plan **xsmall** (xsmall)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "postgresql",
      "plan: "xsmall"
  ]
}
```

### Using the service plan **small** (small)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "postgresql",
      "plan: "small"
  ]
}
```

### Using the service plan **medium** (medium)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "postgresql",
      "plan: "medium"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency