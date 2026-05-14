

JUMP TO

Powered by

# ParticipateAssetIssue

post

https://api.shasta.trongrid.io/wallet/participateassetissue

Participate in an asset issue.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

to\_address

string

required

Issuer's address. Example: `TPswDDCAWhJAZGdHPidFg5nEf8TkNToDX1`

owner\_address

string

required

Participant address (Default: Hex). Example: `TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g`

amount

int64

required

Amount of TRX to participate in token issuance. (Unit: sun)

asset\_name

string

required

Token id, default hexString. Example: `1000001031303030303031`

visible

boolean

Defaults to true

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Permission\_id

int32

Permission ID used for multi-signature.

Responses

# 200 200

# 400 400

Updated 3 months ago

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

Updated 3 months ago

---