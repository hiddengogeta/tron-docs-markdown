

JUMP TO

Powered by

# Get TRC-20 token holder balances

get

https://api.shasta.trongrid.io/v1/contracts/{contractAddress}/tokens

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

fingerprint

string

The fingerprint for pagination, obtained from the `meta.fingerprint` field of a previous response. Note: When using `fingerprint`, all other parameters must remain the same.

limit

int32

The maximum number of transactions to return per page. (Default: 20，Max: 200)

order\_by

string

Specifies the sort order. balance,asc | balance,desc (default).

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

400 - Result

Updated 5 months ago

---