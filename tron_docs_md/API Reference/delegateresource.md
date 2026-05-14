

JUMP TO

Powered by

# DelegateResource

post

https://api.shasta.trongrid.io/wallet/delegateresource

Delegate bandwidth or energy resources to other accounts in Stake2.0.

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

Owner address, in Base58Check format or HEX format.

receiver\_address

string

required

Resource receiver address, in Base58Check format or HEX format.

balance

int64

required

Amount of TRX to delegate or undelegate for resources. (Unit: sun)

resource

string

required

Type of resource. (Enum: "BANDWIDTH" or "ENERGY")

lock

boolean

Defaults to false

Optional. Whether to lock the resource delegation. If `true`, the delegation cannot be canceled during the `lock_period`.

truefalse

lock\_period

int64

Lock duration in blocks (1 block ≈ 3 seconds). Only valid if `lock` is `true`. (e.g., 1 day = 28800)

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