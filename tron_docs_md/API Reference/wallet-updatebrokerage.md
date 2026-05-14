

JUMP TO

Powered by

# UpdateBrokerage

post

https://api.shasta.trongrid.io/wallet/updateBrokerage

Update the SR's brokerage setting.

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

Super representative's account address (format: Base58 or Hex). Example:  `TCuM8e98jmPwT1RU2jW7dekUC5HpXbGzFG`

brokerage

int32

required

The brokerage ratio of the super representative, for example: 20 means 20%, 100 means 100%

visible

boolean

Optional. Specifies whether the address is in Base58 format (default: false). Note: Set to true in this example for demonstration purposes.

truefalse

Permission\_id

int32

Permission ID used for multi-signature.

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