

JUMP TO

Powered by

# AccountPermissionUpdate

post

https://api.shasta.trongrid.io/wallet/accountpermissionupdate

Update the account's permission.

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

Account address (format: Base58 or Hex). Example: `TJZuV6A9QRdtVeJBvewCF9fLF2qnRSEv3y`

actives

json

required

List of active permissions for the account. Example: `[{ "type": 2, "permission_name": "active0", "threshold": 2, "operations": "7fff1fc0037e0000000000000000000000000000000000000000000000000000", "keys": [{ "address": "TJZuV6A9QRdtVeJBvewCF9fLF2qnRSEv3y", "weight": 1 }, { "address": "TPswDDCAWhJAZGdHPidFg5nEf8TkNToDX1", "weight": 1 }] }]`

owner

json

required

Owner permission object of the account. Example: `{ "type": 0, "permission_name": "owner", "threshold":1, "keys": [{ "address": "TJZuV6A9QRdtVeJBvewCF9fLF2qnRSEv3y", "weight": 1 }] }`

witness

json

Witness permission object (for Super Representatives). Example: `{"type": 1, "permission_name": "witness", "threshold": 1, "keys": [{ "address": "TJZuV6A9QRdtVeJBvewCF9fLF2qnRSEv3y", "weight": 1 }]}`

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Permission\_id

string

Permission ID used for multi-signature.

Responses

# 200 200

# 400 400

Updated 3 months ago

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

Updated 3 months ago

---