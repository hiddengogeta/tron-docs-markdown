

JUMP TO

Powered by

# Get events by transaction id

get

https://api.shasta.trongrid.io/v1/transactions/{transactionID}/events

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Path Params

transactionID

string

required

The specific transaction hash to query.
Example: `aee87b7bb3e375c7e5e96f8b1a770c1fac60d483f56267fd77e663a3e9512a1a`

Query Params

only\_unconfirmed

boolean

Set to `true` to return only confirmed events; set to `false` to return both confirmed and unconfirmed events. Cannot be used simultaneously with `only_confirmed`.

truefalse

only\_confirmed

boolean

Set to `true` to return only confirmed events; set to `false` to return both confirmed and unconfirmed events. Cannot be used simultaneously with `only_unconfirmed`.

truefalse

Responses

# 200 200

# 400 400

Updated 4 months ago

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

Updated 4 months ago

---