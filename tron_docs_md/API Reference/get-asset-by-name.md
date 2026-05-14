

JUMP TO

Powered by

# Get assets by name

get

https://api.shasta.trongrid.io/v1/assets/{name}/list

NOTE: Multiple assets may have the same name.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Path Params

name

string

required

Name of the asset(s). Example: `btt`

Query Params

limit

int32

number of assets per page, default 20, max 200

fingerprint

string

fingerprint of the last asset returned by the previous page; when using it, the other parameters and filters should remain the same

order\_by

string

order\_by = total\_supply,asc | total\_supply,desc | start\_time,asc | start\_time,desc | end\_time,asc | end\_time,desc | id,asc | id,desc (default)

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