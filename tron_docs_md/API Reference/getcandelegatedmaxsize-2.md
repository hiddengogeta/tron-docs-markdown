

JUMP TO

Powered by

# GetCanDelegatedMaxSize

post

https://api.shasta.trongrid.io/walletsolidity/getcandelegatedmaxsize

Stake2.0 API: query the amount of delegatable resources share of the specified resource type for an address, unit is sun. (Confirmed state)

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

type

int32

required

Defaults to 0

Resource type. `0` is Bandwidth, `1` is Energy.

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

400 - Result

Updated about 1 month ago

---