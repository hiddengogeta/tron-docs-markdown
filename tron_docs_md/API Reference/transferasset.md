

JUMP TO

Powered by

# TransferAsset

post

https://api.shasta.trongrid.io/wallet/transferasset

Transfer TRC10 token.

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

Transaction initiator address (Format: Base58 or Hex; Default: Hex). Example: `TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g`

to\_address

string

required

Recipient address (Format: Base58 or Hex; Default: Hex). Example: `TPswDDCAWhJAZGdHPidFg5nEf8TkNToDX1`

asset\_name

string

required

ID of the TRC-10 token (Format: Base58 or Hex; Default: Hex). Example: `31303030303031`

amount

int64

required

Defaults to null

Amount of TRX to transfer. (Unit: sun). Example: `1`

Permission\_id

int32

Permission ID used for multi-signature.

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

extra\_data

string

Notes on the transaction. (Format: Hex)

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