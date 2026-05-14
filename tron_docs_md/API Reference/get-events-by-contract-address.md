

JUMP TO

Powered by

# Get events by contract address

get

https://api.shasta.trongrid.io/v1/contracts/{address}/events

Recipes

👂

Listen to Contract Events

Open Recipe

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

Contract address in `base58` or `hex` format.
Example: `TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs`

Query Params

event\_name

string

Defaults to Transfer

The event name to filter by.
Example: `Transfer`

block\_number

int64

The specific block number to query.
Example: `61840405`

only\_unconfirmed

boolean

Set to `true` to return only confirmed events; set to `false` to return both confirmed and unconfirmed events. Cannot be used simultaneously with `only_confirmed`.

truefalse

only\_confirmed

boolean

Set to `true` to return only confirmed events; set to `false` to return both confirmed and unconfirmed events. Cannot be used simultaneously with `only_unconfirmed`.

truefalse

min\_timestamp

date-time

The minimum block timestamp to filter by. (Unit: milliseconds, Default: 0)

max\_timestamp

date-time

The maximum block timestamp to filter by. (Unit: milliseconds, Default: current time)

order\_by

string

Specifies the sort order. block\_timestamp,asc | block\_timestamp,desc (default).

fingerprint

string

The fingerprint for pagination, obtained from the `meta.fingerprint` field of a previous response. Note: When using `fingerprint`, all other parameters must remain the same.

limit

int32

The maximum number of events to return per page. (Default: 20, Max:200)

Responses

# 200 200

# 400 400

Updated 16 days ago

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

Updated 16 days ago

---