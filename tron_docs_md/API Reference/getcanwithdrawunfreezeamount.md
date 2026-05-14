

JUMP TO

Powered by

# GetCanWithdrawUnfreezeAmount

post

https://api.shasta.trongrid.io/wallet/getcanwithdrawunfreezeamount

Query the withdrawable balance at the specified timestamp In Stake2.0

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

timestamp

int64

required

Timestamp to query. (Unit: millGisecond)

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