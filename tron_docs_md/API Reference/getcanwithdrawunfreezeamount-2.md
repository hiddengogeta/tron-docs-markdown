

JUMP TO

Powered by

# GetCanWithdrawUnfreezeAmount

post

https://api.shasta.trongrid.io/walletsolidity/getcanwithdrawunfreezeamount

Stake2.0 API: query the withdrawable balance at the specified timestamp (confirmed state)

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

Owner address. (Format: Base58 or Hex)

timestamp

int64

required

Timestamp to query. (Unit: millGisecond)

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