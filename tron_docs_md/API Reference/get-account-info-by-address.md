

JUMP TO

Powered by

# Get account info by address

get

https://api.shasta.trongrid.io/v1/accounts/{address}

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Path Params

address

string

required

The account address (Format: Base58Check or Hex). Example: `TFtbBrsWw5DGHoKQE8VY2WzTY3VnanQ2hz`

Query Params

only\_confirmed

boolean

Set to `true` to return only confirmed results; set to `false` to return both confirmed and unconfirmed results. Cannot be used simultaneously with `only_unconfirmed`. (Default: `false`)

truefalse

only\_unconfirmed

boolean

Set to `true` to return only unconfirmed results; set to `false` to return both confirmed and unconfirmed results. Cannot be used simultaneously with `only_confirmed`. (Default: `false`)

truefalse

Responses

# 200 200

# 400 400

Updated 5 months ago

---

Language

ShellNodeRubyPHPPython

Credentials

Header

Header

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200 - Result400 - Result

Updated 5 months ago

---