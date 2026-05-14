

JUMP TO

Powered by

# CancelAllUnfreezeV2

post

https://api.shasta.trongrid.io/wallet/cancelallunfreezev2

Cancel unstakings, all unstaked funds still in the waiting period will be re-staked, all unstaked funds that exceeded the 14-day waiting period will be automatically withdrawn to the owner’s account

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

owner\_address

string

required

Owner address, in Base58Check format or HEX format.

Permission\_id

int32

Optional. Permission ID used for multi-signature.

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