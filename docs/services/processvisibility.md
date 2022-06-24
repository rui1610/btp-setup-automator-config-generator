<img src="data:image/svg+xml;base64, PHN2ZyBpZD0icHJvY2Vzcy12aXNpYmlsaXR5IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NiA1NiI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiMwNTNiNzA7fS5jbHMtMntmaWxsOiMwYTZlZDE7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5wcm9jZXNzLXZpc2liaWxpdHk8L3RpdGxlPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTUxLjA2Miw0Ni45MzgsMzkuMjE4LDM1LjAwN0ExOS41NTUsMTkuNTU1LDAsMSwwLDM1LDM5LjIyNEw0Ni44NDQsNTEuMTU2QTMuMTIyLDMuMTIyLDAsMCwwLDQ5LDUyYTIuOCwyLjgsMCwwLDAsMi4wNjItLjg0NCwyLjg0LDIuODQsMCwwLDAsMC00LjIxOFpNNywyMy41QTE2LjUsMTYuNSwwLDEsMSwyMy41LDQwLDE2LjUxOSwxNi41MTksMCwwLDEsNywyMy41WiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTI2LjM1MSwxOC45MTFoNi4zMTNhMS4zNDMsMS4zNDMsMCwwLDAsMS4zNDMtMS4zNDNWMTQuMjU0YTEuMzQzLDEuMzQzLDAsMCwwLTEuMzQzLTEuMzQzSDI2LjM1MWExLjM0NCwxLjM0NCwwLDAsMC0xLjM0NCwxLjM0M3YuOTA4aC0zLjU5YS43NTIuNzUyLDAsMCwwLS43NS43NXY1LjI1MWwtMi4wNzYsMi4wNzZIMTcuNTA3di0uOUExLjM0MSwxLjM0MSwwLDAsMCwxNi4xNjYsMjFoLTYuM2ExLjM0MSwxLjM0MSwwLDAsMC0xLjM0MSwxLjM0MXYzLjMwOGExLjM0MSwxLjM0MSwwLDAsMCwxLjM0MSwxLjM0MWg2LjNhMS4zNDEsMS4zNDEsMCwwLDAsMS4zNDEtMS4zNDF2LS45aDEuMUwyMC42NjcsMjYuOHY0Ljc3NWEuNzUyLjc1MiwwLDAsMCwuNzUuNzVoMy41OXYuOTA4YTEuMzQzLDEuMzQzLDAsMCwwLDEuMzQ0LDEuMzQzaDYuMzEzYTEuMzQzLDEuMzQzLDAsMCwwLDEuMzQzLTEuMzQzVjI5LjkxNWExLjM0MywxLjM0MywwLDAsMC0xLjM0My0xLjM0M0gyNi4zNTFhMS4zNDQsMS4zNDQsMCwwLDAtMS4zNDQsMS4zNDN2LjkwNmgtMi44NFYyNi44OHMuMDEzLS4wMDYuMDE4LS4wMTJMMjQuMzQ5LDI0LjdhMS4wMjEsMS4wMjEsMCwwLDAsMC0xLjQ0NmwtMi4xNjUtMi4xNjZjLS4wMDUsMC0uMDEyLS4wMDYtLjAxNy0uMDExVjE2LjY2MmgyLjg0di45MDZBMS4zNDMsMS4zNDMsMCwwLDAsMjYuMzUxLDE4LjkxMVoiLz48L3N2Zz4=" alt="Icon for processvisibility" width="80px" />
# **processvisibility** (Process Visibility)

Service category: **SERVICE**

## Additional details

- [Documentation](https://help.sap.com/viewer/product/VISIBILITY_SERVICE/Cloud/en-US)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  standard  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu20 - Europe (Netherlands)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)  |
|  workflow  |  workflow  | ap10 - Australia (Sydney)<br> ap11 - Singapore<br> ap12 - South Korea (Seoul)<br> ap20 - Australia (Sydney) Azure<br> ap21 - Singapore<br> br10 - Brazil (Sao Paulo)<br> ca10 - Canada (Montreal)<br> eu10 - Europe (Frankfurt)<br> eu11 - Europe (Frankfurt) EU Access - AWS<br> eu20 - Europe (Netherlands)<br> eu30 - Europe (Frankfurt)<br> jp10 - Japan (Tokyo)<br> jp20 - Japan (Tokyo)<br> us10 - US East (VA)<br> us20 - US West (WA)<br> us21 - US East (VA)<br> us30 - US Central (IA)  |

## Sample configuration of **Process Visibility** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **processvisibility** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "processvisibility",
      "plan": "standard"
    }
  ]
}
```

### Using the service plan **workflow**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "processvisibility",
      "plan": "workflow"
    }
  ]
}
```

## Related categories

- Extension Suite - Digital Process Automation