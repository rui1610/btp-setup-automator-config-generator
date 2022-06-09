# kymaruntime (ENVIRONMENT)

Kyma runtime

## Additional details
- [Documentation](https://help.sap.com/viewer/3504ec5ef16548778610c7e89cc0eac3/Cloud/en-US/468c2f3c3ca24c2c8497ef9f83154c44.html)
- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  azure  |  Kyma Runtime Azure  | ap21 - Singapore<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  aws  |  Kyma Runtime AWS  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |
|  gcp  |  Kyma Runtime GCP  | us30 - US Central (IA)  |
|  free  |  free  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **kymaruntime** by configuring your `usecase.json` file.

### Using the service plan **azure** (Kyma Runtime Azure)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "ENVIRONMENT",
      "name": "kymaruntime",
      "plan: "azure"
  ]
}
```

### Using the service plan **aws** (Kyma Runtime AWS)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "ENVIRONMENT",
      "name": "kymaruntime",
      "plan: "aws"
  ]
}
```

### Using the service plan **gcp** (Kyma Runtime GCP)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "ENVIRONMENT",
      "name": "kymaruntime",
      "plan: "gcp"
  ]
}
```

### Using the service plan **free** (free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "ENVIRONMENT",
      "name": "kymaruntime",
      "plan: "free"
  ]
}
```


## Related categories
- Extension Suite - Development Efficiency