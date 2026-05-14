

JUMP TO

Powered by

# GetDelegatedResource

post

https://api.shasta.trongrid.io/wallet/getdelegatedresource

Returns all resources delegations during stake1.0 phase from an account to another account. The fromAddress can be retrieved from the GetDelegatedResourceAccountIndex API.

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

The queried from account address, in Base58Check format or HEX format.

toAddress

string

required

The queried to account address, in Base58Check format or HEX format.

visible

boolean

Defaults to false

Optional. Set to `true` to format addresses in Base58Check; set to `false` for hex format. (Default: `false`)

truefalse

Responses

# 200 200

# 400 400

Updated 3 months ago

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

Updated 3 months ago

---