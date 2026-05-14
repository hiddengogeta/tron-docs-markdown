

JUMP TO

Powered by

# GetDelegatedResourceV2

post

https://api.shasta.trongrid.io/wallet/getdelegatedresourcev2

In Stake2.0, query the detail of resource share delegated from fromAddress to toAddress

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

Delegate account address, in Base58Check format or HEX format.

toAddress

string

required

Resource recipient address, in Base58Check format or HEX format.

visible

boolean

Defaults to false

Optional. Set to `true` to format addresses in Base58Check; set to `false` for hex format. (Default: `false`)

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