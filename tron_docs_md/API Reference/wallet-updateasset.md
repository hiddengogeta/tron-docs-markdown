

JUMP TO

Powered by

# UpdateAsset

post

https://api.shasta.trongrid.io/wallet/updateasset

Update basic TRC10 token information.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

owner\_address

string

Token issuer's address (default: Hex). Example: `TPswDDCAWhJAZGdHPidFg5nEf8TkNToDX1`

description

string

Description of the TRC-10 token. (Default: Hex)

url

string

URL of the official website. (Default: Hex)

new\_limit

int32

New free Bandwidth limit for each caller.

new\_public\_limit

int32

New total free Bandwidth limit for all callers.

Permission\_id

int32

Permission ID used for multi-signature.

visible

boolean

Defaults to true

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

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