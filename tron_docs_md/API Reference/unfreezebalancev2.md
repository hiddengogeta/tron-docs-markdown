

JUMP TO

Powered by

# UnfreezeBalanceV2

post

https://api.shasta.trongrid.io/wallet/unfreezebalancev2

Unstake some TRX staked in Stake2.0, release the corresponding amount of bandwidth or energy, and voting rights (TP)

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

unfreeze\_balance

int64

required

Amount of TRX to unstake. (Unit: sun)

resource

string

required

Type of resource. (Enum: "BANDWIDTH" or "ENERGY")

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