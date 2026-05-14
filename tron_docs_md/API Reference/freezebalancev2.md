

JUMP TO

Powered by

# FreezeBalanceV2

post

https://api.shasta.trongrid.io/wallet/freezebalancev2

In Stake2.0, stake an amount of TRX to obtain bandwidth or energy, and obtain equivalent TRON Power(TP) according to the staked amount

Recipes

🔒

Stake and Delegate Resources

Open Recipe

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

Owner address, default hexString

frozen\_balance

int64

required

TRX stake amount, the unit is sun

resource

string

required

TRX stake type, 'BANDWIDTH' or 'ENERGY'

Permission\_id

int32

Optional. Specifies the permission ID used for multi-signature accounts.

visible

boolean

Defaults to false

Optional. Specifies whether the address is in Base58 format (default: false). Note: Set to true in this example for demonstration purposes.

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