

JUMP TO

Powered by

# GetAccountBalance

post

https://api.shasta.trongrid.io/wallet/getaccountbalance

Get the account balance in a specific block.(Note: At present, the interface data can only be queried through the following official nodes 13.228.119.63 & 18.139.193.235 & 18.141.79.38 & 18.139.248.26)

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

account\_identifier

json

required

Object containing the account address. Example: `{ "address": "TLLM21wteSPs4hKjbxgmH1L6poyMjeTbHm" }`

block\_identifier

json

required

Object containing the block number and hash. Example: `{ "hash": "0000000000010c4a732d1e215e87466271e425c86945783c3d3f122bfa5affd9", "number": 68682 }`

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Responses

# 200 200

# 400 400

Updated about 1 month ago

---

Language

ShellNodeRubyPHPPython

Credentials

Header

Header

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200 - Result400 - Result

Updated about 1 month ago

---