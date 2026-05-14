

JUMP TO

Powered by

# Get internal transactions by contract address

get

https://api.shasta.trongrid.io/v1/contracts/{contractAddress}/internal-transactions

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Path Params

contractAddress

string

required

The address of contract (format: Base58 or Hex). Example: `TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs`

Query Params

only\_confirmed

boolean

Set to `true` to return only confirmed [items]; set to `false` to return both confirmed and unconfirmed [items]. Cannot be used simultaneously with `only_unconfirmed`. (Default: `false`)

truefalse

only\_unconfirmed

boolean

Set to `true` to return only unconfirmed [items]; set to `false` to return both confirmed and unconfirmed [items]. Cannot be used simultaneously with `only_confirmed`. (Default: `false`)

truefalse

limit

int32

The maximum number of transactions to return per page. (Default: 20，Max: 200)

fingerprint

string

The fingerprint for pagination, obtained from the `meta.fingerprint` field of a previous response. Note: When using `fingerprint`, all other parameters must remain the same.

min\_timestamp

date

The minimum block timestamp to filter by. (Unit: milliseconds, Default: 0)

max\_timestamp

date

The maximum block timestamp to filter by. (Unit: milliseconds, Default: current time)

order\_by

string

Specifies the sort order. block\_timestamp,asc | block\_timestamp,desc (default).

Responses

# 200 200

# 400 400

Updated 5 months ago

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

Updated 5 months ago

---