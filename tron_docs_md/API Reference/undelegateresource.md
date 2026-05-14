

JUMP TO

Powered by

# UnDelegateResource

post

https://api.shasta.trongrid.io/wallet/undelegateresource

Cancel the delegation of bandwidth or energy resources to other accounts in Stake2.0

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