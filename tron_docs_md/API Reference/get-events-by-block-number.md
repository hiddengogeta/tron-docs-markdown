

JUMP TO

Powered by

# Get events by block number

get

https://api.shasta.trongrid.io/v1/blocks/{block\_number}/events

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Path Params

block\_number

int32

required

The block number to query events for.
Example: `61840405`

Query Params

only\_confirmed

boolean

Set to `true` to return only confirmed events; set to `false` to return both confirmed and unconfirmed events. Cannot be used simultaneously with `only_unconfirmed`.

truefalse

limit

int32

The maximum number of events to return per page. (Default: 20, max:200)

fingerprint

string

The fingerprint for pagination, obtained from the `meta.fingerprint` field of a previous response. Note: When using `fingerprint`, all other parameters must remain the same.

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