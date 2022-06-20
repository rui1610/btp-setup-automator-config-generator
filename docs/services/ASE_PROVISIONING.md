# ASE_PROVISIONING (SERVICE)

SAP ASE Service

## Additional details

- [Documentation](https://help.sap.com/viewer/product/ASE_SERVICE/Cloud/en-US)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-ase-service)

## Service availability

| Plan Name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  XLARGE  |  ASE 640GB  | ae1 - UAE (Dubai)<br> ap1 - Australia (Sydney)<br> ap2 - Australia (Sydney DR)<br> br1 - Brazil (Sao Paulo)<br> ca1 - Canada (Toronto)<br> ca2 - Canada (Toronto DR)<br> cn1 - China (Shanghai)<br> eu1 - Europe (Rot)<br> eu2 - Europe (Frankfurt)<br> eu3 - Europe (Amsterdam)<br> jp1 - Japan (Tokyo)<br> ru1 - Russia (Moscow)<br> sa1 - KSA (Riyadh)<br> us1 - US East (Ashburn)<br> us2 - US West (Chandler)<br> us3 - US East (Sterling)<br> us4 - US West (Colorado Springs)  |
|  MEDIUM  |  ASE 160GB  | ae1 - UAE (Dubai)<br> ap1 - Australia (Sydney)<br> ap2 - Australia (Sydney DR)<br> br1 - Brazil (Sao Paulo)<br> ca1 - Canada (Toronto)<br> ca2 - Canada (Toronto DR)<br> cn1 - China (Shanghai)<br> eu1 - Europe (Rot)<br> eu2 - Europe (Frankfurt)<br> eu3 - Europe (Amsterdam)<br> jp1 - Japan (Tokyo)<br> ru1 - Russia (Moscow)<br> sa1 - KSA (Riyadh)<br> us1 - US East (Ashburn)<br> us2 - US West (Chandler)<br> us3 - US East (Sterling)<br> us4 - US West (Colorado Springs)  |
|  SMALL  |  ASE 80GB  | ae1 - UAE (Dubai)<br> ap1 - Australia (Sydney)<br> ap2 - Australia (Sydney DR)<br> br1 - Brazil (Sao Paulo)<br> ca1 - Canada (Toronto)<br> ca2 - Canada (Toronto DR)<br> cn1 - China (Shanghai)<br> eu1 - Europe (Rot)<br> eu2 - Europe (Frankfurt)<br> eu3 - Europe (Amsterdam)<br> jp1 - Japan (Tokyo)<br> ru1 - Russia (Moscow)<br> sa1 - KSA (Riyadh)<br> us1 - US East (Ashburn)<br> us2 - US West (Chandler)<br> us3 - US East (Sterling)<br> us4 - US West (Colorado Springs)  |
|  XSMALL  |  ASE 40GB  | ae1 - UAE (Dubai)<br> ap1 - Australia (Sydney)<br> ap2 - Australia (Sydney DR)<br> br1 - Brazil (Sao Paulo)<br> ca1 - Canada (Toronto)<br> ca2 - Canada (Toronto DR)<br> cn1 - China (Shanghai)<br> eu1 - Europe (Rot)<br> eu2 - Europe (Frankfurt)<br> eu3 - Europe (Amsterdam)<br> jp1 - Japan (Tokyo)<br> ru1 - Russia (Moscow)<br> sa1 - KSA (Riyadh)<br> us1 - US East (Ashburn)<br> us2 - US West (Chandler)<br> us3 - US East (Sterling)<br> us4 - US West (Colorado Springs)  |
|  LARGE  |  ASE 320GB  | ae1 - UAE (Dubai)<br> ap1 - Australia (Sydney)<br> ap2 - Australia (Sydney DR)<br> br1 - Brazil (Sao Paulo)<br> ca1 - Canada (Toronto)<br> ca2 - Canada (Toronto DR)<br> cn1 - China (Shanghai)<br> eu1 - Europe (Rot)<br> eu2 - Europe (Frankfurt)<br> eu3 - Europe (Amsterdam)<br> jp1 - Japan (Tokyo)<br> ru1 - Russia (Moscow)<br> sa1 - KSA (Riyadh)<br> us1 - US East (Ashburn)<br> us2 - US West (Chandler)<br> us3 - US East (Sterling)<br> us4 - US West (Colorado Springs)  |

## Sample configuration of **SAP ASE Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ASE_PROVISIONING** by configuring your `usecase.json` file.

### Using the service plan **XLARGE** (ASE 640GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "XLARGE"
    }
  ]
}
```

### Using the service plan **MEDIUM** (ASE 160GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "MEDIUM"
    }
  ]
}
```

### Using the service plan **SMALL** (ASE 80GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "SMALL"
    }
  ]
}
```

### Using the service plan **XSMALL** (ASE 40GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "XSMALL"
    }
  ]
}
```

### Using the service plan **LARGE** (ASE 320GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "LARGE"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency