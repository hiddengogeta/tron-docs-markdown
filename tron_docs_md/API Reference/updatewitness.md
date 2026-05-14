

JUMP TO

Powered by

# UpdateWitness

post

https://api.shasta.trongrid.io/wallet/updatewitness

Edit the URL of the SR's official website.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

owner\_address

string

required

Transaction initiator address (format: Base58 or Hex). Example: `TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g`

update\_url

string

required

New official website URL for the Super Representative (SR).

Permission\_id

int32

Permission ID used for multi-signature.

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Response

# 200 200

Updated about 1 month ago

---

Language

ShellNodeRubyPHPPython

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200 - Result

Updated about 1 month ago

---