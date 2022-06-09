# enterprise-messaging (SERVICE)

Event Mesh

## Additional details
- [Documentation](https://help.sap.com/viewer/product/SAP_ENTERPRISE_MESSAGING/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/event-mesh)
- [Support](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5dd739823b824b539eee47b7860a00be.html)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  event-mesh-connectivity  |  Event Mesh Connectivity  | eu10 - Europe (Frankfurt)  |
|  event-mesh-connectivity-beta  |  event-mesh-connectivity-beta  | eu10 - Europe (Frankfurt)<br> us20 - US West (WA)  |
|  default  |  default  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> in30 - cf-in30<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **enterprise-messaging** by configuring your `usecase.json` file.

### Using the service plan **event-mesh-connectivity** (Event Mesh Connectivity)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "enterprise-messaging",
      "plan: "event-mesh-connectivity"
  ]
}
```

### Using the service plan **event-mesh-connectivity-beta** (event-mesh-connectivity-beta)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "enterprise-messaging",
      "plan: "event-mesh-connectivity-beta"
  ]
}
```

### Using the service plan **default** (default)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
      "category": "SERVICE",
      "name": "enterprise-messaging",
      "plan: "default"
  ]
}
```


## Related categories
- Integration Suite