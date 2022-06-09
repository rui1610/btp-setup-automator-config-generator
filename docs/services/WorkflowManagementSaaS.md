# WorkflowManagementSaaS (APPLICATION)

Workflow Management

## Additional details

- [Documentation](https://help.sap.com/viewer/product/WORKFLOW_MANAGEMENT/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/workflow-management)

## Service availability

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  saas-application  |  saas-application  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Workflow Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **WorkflowManagementSaaS** by configuring your `usecase.json` file.

### Using the service plan **saas-application**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "WorkflowManagementSaaS",
      "plan": "saas-application"      
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Process Automation