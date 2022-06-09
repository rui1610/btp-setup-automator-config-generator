# rabbitmq (SERVICE)

RabbitMQ

## Additional details
- [Documentation](https://help.sap.com/viewer/product/RabbitMQ/Cloud/en-US)
- [Tutorial](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/bf757994794445ed904b97bf1907812a.html)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  virtualhost  |  virtualhost  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us30 - US Central (IA)  |
|  large  |  large  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  xsmall  |  xsmall  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us30 - US Central (IA)  |
|  medium  |  medium  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  small  |  small  | br10 - Brazil (Sao Paulo)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **rabbitmq** by configuring your `usecase.json` file.

### Using the service plan **virtualhost** (virtualhost)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan: "virtualhost"
  ]
}
````

### Using the service plan **large** (large)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan: "large"
  ]
}
````

### Using the service plan **xsmall** (xsmall)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan: "xsmall"
  ]
}
````

### Using the service plan **medium** (medium)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan: "medium"
  ]
}
````

### Using the service plan **small** (small)

````
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan: "small"
  ]
}
````


## Related categories
- Integration Suite