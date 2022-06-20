# COMPUTE_UNIT (SERVICE)

Java Quota

## Additional details

- [Documentation](https://help.sap.com/viewer/product/VIRTUAL_MACHINES/Cloud/en-US)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  PRO  |  Professional Edition for VMs: 2 CPUs, 4096 MB Memory  | ae1 - UAE (Dubai)<br> ru1 - Russia (Moscow)<br> sa1 - KSA (Riyadh)  |
|  PREMIUM_PLUS  |  Premium Plus Edition for VMs: 8 CPUs, 16384 MB Memory  | ae1 - UAE (Dubai)<br> ru1 - Russia (Moscow)<br> sa1 - KSA (Riyadh)  |
|  PREMIUM  |  Premium Edition for VMs: 4 CPUs, 8192 MB Memory  | ap1 - Australia (Sydney)<br> ap2 - Australia (Sydney DR)<br> br1 - Brazil (Sao Paulo)<br> ca1 - Canada (Toronto)<br> ca2 - Canada (Toronto DR)<br> cn1 - China (Shanghai)<br> eu1 - Europe (Rot)<br> eu2 - Europe (Frankfurt)<br> eu3 - Europe (Amsterdam)<br> jp1 - Japan (Tokyo)<br> us1 - US East (Ashburn)<br> us2 - US West (Chandler)<br> us3 - US East (Sterling)<br> us4 - US West (Colorado Springs)  |

## Sample configuration of **Java Quota** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **COMPUTE_UNIT** by configuring your `usecase.json` file.

### Using the service plan **PRO** (Professional Edition for VMs: 2 CPUs, 4096 MB Memory)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "COMPUTE_UNIT",
      "plan": "PRO"
    }
  ]
}
```

### Using the service plan **PREMIUM_PLUS** (Premium Plus Edition for VMs: 8 CPUs, 16384 MB Memory)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "COMPUTE_UNIT",
      "plan": "PREMIUM_PLUS"
    }
  ]
}
```

### Using the service plan **PREMIUM** (Premium Edition for VMs: 4 CPUs, 8192 MB Memory)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "COMPUTE_UNIT",
      "plan": "PREMIUM"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency