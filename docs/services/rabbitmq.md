<img src="data:image/svg+xml;base64, PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OCA0OCI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiNlYjYwMjI7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5yYWJiaXRtcTwvdGl0bGU+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNNDYuMDgsMTkuMkgzMC43MjNBMS45MTMsMS45MTMsMCwwLDEsMjguOCwxNy4yNzdWMS45MTNBMS45MSwxLjkxLDAsMCwwLDI2Ljg3NywwSDIxLjEyM0ExLjkwOSwxLjkwOSwwLDAsMCwxOS4yLDEuOTEzVjE3LjI3N0ExLjkxNCwxLjkxNCwwLDAsMSwxNy4yNzksMTkuMkgxMS41MjJBMS45MTQsMS45MTQsMCwwLDEsOS42LDE3LjI3N1YxLjkxM0ExLjkwNywxLjkwNywwLDAsMCw3LjY4MSwwSDEuOTIyQTEuOTA4LDEuOTA4LDAsMCwwLDAsMS45MTNWNDYuMDczQTEuOTE1LDEuOTE1LDAsMCwwLDEuOTIyLDQ4SDQ2LjA4QTEuOTE1LDEuOTE1LDAsMCwwLDQ4LDQ2LjA3M1YyMS4xMThhMS45MSwxLjkxLDAsMCwwLTEuOTItMS45Mk0zOC40LDM1LjUwOWEyLjg3NywyLjg3NywwLDAsMS0yLjg4MSwyLjg4M0gzMS42NzdBMi44NzQsMi44NzQsMCwwLDEsMjguOCwzNS41MDlWMzEuNjczYTIuODc0LDIuODc0LDAsMCwxLDIuODc2LTIuODg4aDMuODQ0QTIuODc3LDIuODc3LDAsMCwxLDM4LjQsMzEuNjczWiIvPjwvc3ZnPg==" alt="Icon for rabbitmq" width="80px" />
# RabbitMQ

Technical name: **rabbitmq**

Technical service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/RabbitMQ/Cloud/en-US)
- [Tutorial](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/bf757994794445ed904b97bf1907812a.html)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  virtualhost  |  virtualhost  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us30 - US Central (IA)  |
|  large  |  large  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  xsmall  |  xsmall  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)<br> us30 - US Central (IA)  |
|  medium  |  medium  | ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> ch20 - cf-ch20<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  small  |  small  | br10 - Brazil (Sao Paulo)  |

## Sample configuration of **RabbitMQ** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **rabbitmq** by configuring your `usecase.json` file.

### Using the service plan **virtualhost**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan": "virtualhost"
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
      "name": "rabbitmq",
      "plan": "large"
    }
  ]
}
```

### Using the service plan **xsmall**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "rabbitmq",
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
      "name": "rabbitmq",
      "plan": "medium"
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
      "name": "rabbitmq",
      "plan": "small"
    }
  ]
}
```

## Related categories

- Integration Suite