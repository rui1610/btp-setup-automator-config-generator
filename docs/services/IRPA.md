# IRPA (APPLICATION)

SAP Intelligent Robotic Process Automation

## Additional details

- [Documentation](https://help.sap.com/viewer/p/IRPA)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-intelligent-rpa)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  SAP Intelligent Robotic Process Automation  | ap10 - Australia (Sydney)<br> eu10 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |
|  free  |  Free  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |
|  concurrent  |  Concurrent  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> jp10 - Japan (Tokyo)<br> us10 - US East (VA)  |

## Sample configuration of **SAP Intelligent Robotic Process Automation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **IRPA** by configuring your `usecase.json` file.

### Using the service plan **default** (SAP Intelligent Robotic Process Automation)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "IRPA",
      "plan": "default"
    }
  ]
}
```

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "IRPA",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **concurrent** (Concurrent)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "IRPA",
      "plan": "concurrent"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Process Automation