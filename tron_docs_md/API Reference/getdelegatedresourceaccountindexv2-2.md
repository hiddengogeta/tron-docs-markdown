

JUMP TO

Powered by

# GetDelegatedResourceAccountIndexV2

post

https://api.shasta.trongrid.io/walletsolidity/getdelegatedresourceaccountindexv2

Stake 2.0 API: query the resource delegation index by an account (confirmed state). Two lists will return, one is the list of addresses the account has delegated its resources(toAddress), and the other is the list of addresses that have delegated resources to the account(fromAddress).

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

value

string

required

Account address. (Format: Base58 or Hex)

visible

boolean

Set to `true` to format addresses in Base58Check; set to `false` for hex format. (Default: `false`)

truefalse

Responses

# 200 200

# 400 400

Updated about 1 month ago

---

Language

ShellNodeRubyPHPPython

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200 - Result400 - Result

Updated about 1 month ago

---