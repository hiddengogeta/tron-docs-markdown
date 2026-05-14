

JUMP TO

Powered by

# GetCanDelegatedMaxSize

post

https://api.shasta.trongrid.io/wallet/getcandelegatedmaxsize

In Stake2.0, query the amount of delegatable resources share of the specified resource type for an address, unit is sun.

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

type

int32

required

Defaults to 0

Resource type, 0 is bandwidth, 1 is energy.

visible

boolean

Defaults to false

Optional. Set to `true` to format addresses in Base58Check; set to `false` for hex format. (Default: `false`)

truefalse

Responses

# 200 200

# 400 400

Updated 27 days ago

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

Updated 27 days ago

---