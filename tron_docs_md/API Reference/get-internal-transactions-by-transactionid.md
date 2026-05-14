

JUMP TO

Powered by

# Get internal transactions by transaction ID

get

https://api.shasta.trongrid.io/v1/transactions/{transactionId}/internal-transactions

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Path Params

transactionId

string

required

The unique ID for the parent transaction.

Query Params

only\_confirmed

boolean

Set to `true` to return only confirmed transactions; set to false (or omit) to return both confirmed and unconfirmed transactions. Note: Cannot be used simultaneously with `only_unconfirmed`.

truefalse

only\_unconfirmed

boolean

Set to `true` to return only confirmed transactions; set to false (or omit) to return both confirmed and unconfirmed transactions. Note: Cannot be used simultaneously with `only_confirmed`.

truefalse

Responses

# 200 200

# 400 400

Updated 6 months ago

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

Updated 6 months ago

---