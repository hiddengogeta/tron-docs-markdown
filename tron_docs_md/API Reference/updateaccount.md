

JUMP TO

Powered by

# UpdateAccount

post

https://api.shasta.trongrid.io/wallet/updateaccount

Modify account name

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

Account address (format: Base58 or Hex). Example: `TUoHaVjx7n5xz8LwPRDckgFrDWhMhuSuJM`

account\_name

string

required

Account name. Example: `testAccountName`

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Permission\_id

int32

Permission ID used for multi-signature.

Responses

# 200 200

# 400 400

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

200 - Result400 - Result

Updated about 1 month ago

---