

JUMP TO

Powered by

# Get internal transactions by address

get

https://api.shasta.trongrid.io/v1/accounts/{address}/internal-transactions

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

The account address. (Format: Base58 or hex)

Query Params

only\_confirmed

boolean

Set to `true` to return only confirmed transactions; set to false to return both confirmed and unconfirmed transactions. Cannot be used simultaneously with `only_unconfirmed`. (Default: `false`)

truefalse

only\_unconfirmed

boolean

Set to `true` to return only confirmed transactions; set to false to return both confirmed and unconfirmed transactions. Cannot be used simultaneously with `only_confirmed`. (Default: `false`)

truefalse

only\_to

boolean

Set to `true` to return only transactions sent to the address specified in the path. (Default: `false`)

truefalse

only\_from

boolean

Set to `true` to return only transactions sent from the address specified in the path. (Default: `false`)

truefalse

limit

int32

The maximum number of transactions to return per page. (Default: 20, Max: 200)

fingerprint

string

The fingerprint for pagination, obtained from the `meta.fingerprint` field of a previous response. Note: When using `fingerprint`, all other parameters must remain the same.

order\_by

string

Specifies the sort order. block\_timestamp,asc | block\_timestamp,desc (default).

min\_timestamp

date

The minimum block timestamp to filter by. (Unit: milliseconds, Default: 0)

max\_timestamp

date

The maximum block timestamp to filter by. (Unit: milliseconds, Default: current time)

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