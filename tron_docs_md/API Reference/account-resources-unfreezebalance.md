

JUMP TO

Powered by

# UnfreezeBalance

post

https://api.shasta.trongrid.io/wallet/unfreezebalance

Unstake the TRX staked during Stake1.0, release the obtained bandwidth or energy and TP. This operation will cause automatically cancel all votes.

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

resource

string

required

Type of resource. (Enum: "BANDWIDTH" or "ENERGY")

receiver\_address

string

Optional, in Base58Check format or HEX format.

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