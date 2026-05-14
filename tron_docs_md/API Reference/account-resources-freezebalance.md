

JUMP TO

Powered by

# FreezeBalance

post deprecated

https://api.shasta.trongrid.io/wallet/freezebalance

This interface has been deprecated, please use [FreezeBalanceV2](/reference/freezebalancev2-1) to stake TRX to obtain resources.

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

frozen\_duration

int32

Defaults to 3

Lock-up duration for this stake, now the value can only be 3 days. It is not allowed to unstake within 3 days after the stake. You can unstake TRX after the 3 lock-up days

resource

string

required

Type of resource. (Enum: "BANDWIDTH" or "ENERGY")

receiver\_address

string

Optional,the address that will receive the resource, default hexString

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