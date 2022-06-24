<img src="data:;base64, None" alt="Icon for hana-tenant-db" width="80px" />
# **hana-tenant-db** (SAP HANA Tenant Database)

Service category: **SERVICE**

## Additional details


## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  SAP HANA Tenant Database  | ap21 - Singapore<br> eu20 - Europe (Netherlands)<br> jp20 - Japan (Tokyo)<br> us20 - US West (WA)<br> us21 - US East (VA)  |

## Sample configuration of **SAP HANA Tenant Database** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **hana-tenant-db** by configuring your `usecase.json` file.

### Using the service plan **standard** (SAP HANA Tenant Database)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-tenant-db",
      "plan": "standard"
    }
  ]
}
```

## Related categories
