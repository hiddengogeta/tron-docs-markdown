

JUMP TO

Powered by

# GetDelegatedResourceAccountIndexV2

post

https://api.shasta.trongrid.io/wallet/getdelegatedresourceaccountindexv2

In Stake2.0, query the resource delegation index by an account. Two lists will return, one is the list of addresses the account has delegated its resources(toAddress), and the other is the list of addresses that have delegated resources to the account(fromAddress).

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

Account address, in Base58Check format or HEX format.

visible

boolean

Defaults to false

Optional. Set to `true` to format addresses in Base58Check; set to `false` for hex format. (Default: `false`)

truefalse

Responses

# 200 200

# 400 400

Updated 6 days ago

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

Updated 6 days ago

---