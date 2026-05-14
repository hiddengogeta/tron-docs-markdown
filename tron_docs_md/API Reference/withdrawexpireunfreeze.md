

JUMP TO

Powered by

# WithdrawExpireUnfreeze

post

https://api.shasta.trongrid.io/wallet/withdrawexpireunfreeze

Withdraw unfrozen balance in Stake2.0, the user can call this API to get back their funds after executing /wallet/unfreezebalancev2 transaction and waiting N days, N is a network parameter

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

visible

boolean

Defaults to false

Optional. Set to `true` to format addresses in Base58Check; set to `false` for hex format. (Default: `false`)

truefalse

Permission\_id

int32

Optional. Permission ID used for multi-signature.

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