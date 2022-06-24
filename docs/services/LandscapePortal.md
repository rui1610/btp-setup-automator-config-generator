<img src="data:image/svg+xml;base64, CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNTYgNTYiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojMGE2ZWQxO30uY2xzLTJ7ZmlsbDojMDUzYjcwO308L3N0eWxlPjwvZGVmcz48ZyBpZD0ibGFuZHNjYXBlLXBvcnRhbCI+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMzEuMiwxN2ExLjU1MywxLjU1MywwLDAsMSwxLjM1OC44MTVMNDguNzc1LDQ2LjQ1N0ExLjY4MiwxLjY4MiwwLDAsMSw0Ny40MTYsNDlIOC41ODRhMS42ODEsMS42ODEsMCwwLDEtMS4zNzYtMi41MTJsOS44NTEtMTguMjczYTEuNTQ0LDEuNTQ0LDAsMCwxLDIuNzkzLjA4MmwuNTU0LDEuMTc0YTEuNTQzLDEuNTQzLDAsMCwwLDIuNzc2LjExM2w2LjY2Mi0xMS43NjlBMS41NTUsMS41NTUsMCwwLDEsMzEuMiwxN20wLTNhNC41OCw0LjU4LDAsMCwwLTMuOTcsMi4zMzhsLTUuNDA4LDkuNTUzYTQuNTExLDQuNTExLDAsMCwwLTMuMzkxLTEuNTIyLDQuNTY5LDQuNTY5LDAsMCwwLTQuMDE2LDIuNDIzTDQuNTY3LDQ1LjA2NGE0Ljc3OSw0Ljc3OSwwLDAsMCwuMSw0LjY5NEE0LjUzMiw0LjUzMiwwLDAsMCw4LjU4NCw1Mkg0Ny40MTZhNC41MjYsNC41MjYsMCwwLDAsMy45MzktMi4yODQsNC43Nyw0Ljc3LDAsMCwwLC4wMzEtNC43MzdMMzUuMTcyLDE2LjMzOEE0LjU4LDQuNTgsMCwwLDAsMzEuMiwxNFoiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0yOCw3QTE3LDE3LDAsMSwxLDExLDI0LDE3LjAxOSwxNy4wMTksMCwwLDEsMjgsN20wLTNBMjAsMjAsMCwxLDAsNDgsMjQsMjAsMjAsMCwwLDAsMjgsNFoiLz48L2c+PC9zdmc+" alt="Icon for LandscapePortal" width="80px" />
# Landscape Portal

Technical name: **LandscapePortal**

Technical service category: **APPLICATION**

## Additional details

- [Documentation](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/5eb70fb003954619b09224167a0afaa4.html)

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
|  standard  |  Standard  | eu10 - Europe (Frankfurt)  |

## Sample configuration of **Landscape Portal** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **LandscapePortal** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "LandscapePortal",
      "plan": "standard"
    }
  ]
}
```

## Related categories

- Extension Suite - Development Efficiency