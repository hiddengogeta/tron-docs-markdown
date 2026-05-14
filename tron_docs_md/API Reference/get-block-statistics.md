

JUMP TO

Powered by

# Get block statistics

get

https://api.shasta.trongrid.io/v1/blocks/{blockNum}/stats

Retrieves detailed statistical information for a specific block, including transaction counts and resource consumption.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Path Params

blockNum

int32

required

The specific block number to query.

Query Params

get\_tx\_detail

boolean

Set to `true` to include detailed transaction statistics (`txStat`) in the response. (Default: `false`)

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