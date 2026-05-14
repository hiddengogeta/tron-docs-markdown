

JUMP TO

Powered by

# CreateAssetIssue

post

https://api.shasta.trongrid.io/wallet/createassetissue

Issues a TRC-10 token. An account can only issue a TRC-10 token once.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

owner\_address

string

Transaction initiator address (Default: Hex). Example: `TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g`

name

string

Token name (Default: Hex). Example: `0x6173736574497373756531353330383934333132313538`

abbr

string

Token's abbreviation or symbol. Example: `0x6162627231353330383934333132313538`

total\_supply

int64

Total supply of the TRC-10 token.

trx\_num

int64

Defines the price ratio as `trx_num / num`. (Unit of 'trx\_num': sun)

num

int64

Defines the price ratio as `trx_num / num`. (Unit of 'trx\_num': sun)

start\_time

int64

ICO start time. (Unit: millisecond)

end\_time

int64

ICO End time. (Unit: millisecond)

description

string

Description of the TRC-10 token (Default: Hex). Example: `0x4578616d706c654465736372697074696f6e`

url

string

URL of the official website (Default: Hex). Example: `0x7777772e6578616d706c652e636f6d`

free\_asset\_net\_limit

int64

Free Bandwidth limit for TRC-10 token transfers.

public\_free\_asset\_net\_limit

int64

Total public free Bandwidth limit for a TRC-10 token.

frozen\_supply

json

List of frozen supply objects for the TRC-10 token. Example: `{"frozen_amount":1,"frozen_days":2}`

precision

int32

Token precision (number of decimal places).

visible

boolean

(Optional) Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Permission\_id

int32

(Optional) Specifies the permission ID used for multi-signature accounts.

Updated 3 months ago

---

Language

ShellNodeRubyPHPPython

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here!

Updated 3 months ago

---