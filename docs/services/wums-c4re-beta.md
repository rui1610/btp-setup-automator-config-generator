<img src="data:image/svg+xml;base64, PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDIzLjAuNiwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkViZW5lXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCAxNiAxNiIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTYgMTY7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDojMDA5MkQxO30KCS5zdDF7ZmlsbDojNUE3QTk0O30KCS5zdDJ7ZmlsbDojNDI3Q0FDO30KCS5zdDN7Y2xpcC1wYXRoOnVybCgjU1ZHSURfMl8pO30KCS5zdDR7Y2xpcC1wYXRoOnVybCgjU1ZHSURfNl8pO30KCS5zdDV7ZmlsbDpub25lO3N0cm9rZTojMDA5MkQxO3N0cm9rZS13aWR0aDoxNTtzdHJva2UtbWl0ZXJsaW1pdDoxMDt9Cgkuc3Q2e2ZpbGw6bm9uZTt9Cgkuc3Q3e2ZpbGw6IzAwOTJEMTtzdHJva2U6IzAwOTJEMTtzdHJva2Utd2lkdGg6MjtzdHJva2UtbWl0ZXJsaW1pdDoxMDt9Cjwvc3R5bGU+CjxwYXRoIGNsYXNzPSJzdDEiIGQ9Ik04LDBMMSwzLjM3djkuMjZMOCwxNmw3LTMuMzdWMy4zN0w4LDB6IE0xNCwxMmwtNiwyLjZ2LTFsLTYtMi41M3YtMC45OGw1LDEuNjR2LTEuMjVMMiw5LjM2VjguMzJMNyw4LjdWNy40NQoJTDIsNy42di0xTDcsNS42VjQuMzdsLTUsMS41VjQuOTRMOCwyLjZWMS4yNkwxNCw0VjEyeiIvPgo8Zz4KCTxnPgoJCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik0xMC40OSwxMS43M0w5LjYsMTIuMDdDOS41OSwxMSw4Ljg4LDEwLjMzLDgsMTAuNTdsMC0xLjMzQzkuNCw4Ljk0LDEwLjQ3LDEwLjA2LDEwLjQ5LDExLjczeiIvPgoJCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik0xMy40MSwxMC42M2wtMC42MiwwLjI0QzEyLjcxLDcuNjcsMTAuODIsNS4xOSw4LDUuMjRsMC0xLjI2QzExLjIzLDQuMTEsMTMuMzIsNy4wMywxMy40MSwxMC42M3oiLz4KCQk8cGF0aCBjbGFzcz0ic3QwIiBkPSJNMTIuMDgsMTEuMTNsLTAuNzQsMC4yOEMxMS4zLDkuMTgsOS45MSw3LjU5LDgsNy44N2wwLTEuM0MxMC4zNyw2LjM4LDEyLjAyLDguNDEsMTIuMDgsMTEuMTN6Ii8+Cgk8L2c+Cgk8cGF0aCBjbGFzcz0ic3QwIiBkPSJNOC44MiwxMi4zMmMwLDAuMzctMC4xOSwwLjY3LTAuNDIsMC42OGMtMC4yNCwwLjAxLTAuNDMtMC4yOS0wLjQzLTAuNjZjMC0wLjM3LDAuMTktMC42NywwLjQyLTAuNjcKCQlDOC42MywxMS42Nyw4LjgyLDExLjk2LDguODIsMTIuMzJ6Ii8+CjwvZz4KPC9zdmc+Cg==" alt="Icon for wums-c4re-beta" width="80px" />
# Workspace Utilization (technical name: **wums-c4re-beta**

Service category: **APPLICATION**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/SAP_CLOUD_FOR_REAL_ESTATE/2/en-US)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  default  |  SAP Cloud for Real Estate Workspace Utilization Management (BETA)  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **Workspace Utilization** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **wums-c4re-beta** by configuring your `usecase.json` file.

### Using the service plan **default** (SAP Cloud for Real Estate Workspace Utilization Management (BETA))

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "wums-c4re-beta",
      "plan": "default"
    }
  ]
}
```

## Related categories

- Integration Suite