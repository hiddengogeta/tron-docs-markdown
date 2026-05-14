

JUMP TO

Powered by

# GetDelegatedResource

post

https://api.shasta.trongrid.io/walletsolidity/getdelegatedresource

Returns all resources delegations from an account to another account during stake1.0 phase. The fromAddress can be retrieved from the GetDelegatedResourceAccountIndex API. (Confirmed state)

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

fromAddress

string

required

The queried from account address. (Format: Base58 or Hex)

toAddress

string

required

The queried to account address. (Format: Base58 or Hex)

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