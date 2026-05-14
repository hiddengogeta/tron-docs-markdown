

JUMP TO

Powered by

# WithdrawBalance

post

https://api.shasta.trongrid.io/wallet/withdrawbalance

Super Representative or user withdraw rewards, usable every 24 hours.
Super representatives can withdraw the balance from the account allowance into the account balance,
Users can claim the voting reward from the SRs and deposit into his account balance.

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

Super representative or user address(format: Base58 or Hex). Example: `TCuM8e98jmPwT1RU2jW7dekUC5HpXbGzFG`

Permission\_id

int32

Optional. Specifies the permission ID used for multi-signature accounts.

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

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