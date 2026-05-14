

JUMP TO

Powered by

# CreateTransaction

post

https://api.shasta.trongrid.io/wallet/createtransaction

Creates a TRX transfer transaction. If the recipient account (to\_address) does not exist, it will be automatically activated.

Recipes

💸

Send Your First Transaction

Open Recipe

📡

API Signature and Broadcast Flow

Open Recipe

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

Sender address. (Format: Base58 or Hex).
e.g., 41FD49EDA0F23FF7EC1D03B52C3A45991C24CD440E

to\_address

string

required

Recipient address. (Format: Base58 or Hex).
e.g., 4198927FFB9F554DC4A453C64B2E553A02D6DF514B

amount

int64

required

Defaults to -1

Amount of TRX to transfer. (Unit: sun).
e.g., 1000

Permission\_id

int32

The permission ID of the account. Defaults to owner permission if unspecified. Check [More info](/docs/multi-signature).

visible

boolean

Defaults to false

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

extra\_data

string

Remarks or notes for the transaction, in Hex format.

Responses

# 200 200

# 400 400

Updated 16 days ago

---

Language

JavaScript

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200 - Result400 - Result

Updated 16 days ago

---