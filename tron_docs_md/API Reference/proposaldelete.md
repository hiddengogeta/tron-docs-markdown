

JUMP TO

Powered by

# ProposalDelete

post

https://api.shasta.trongrid.io/wallet/proposaldelete

Deletes Proposal Transaction.

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

Address of proposal owner (format: Base58 or Hex). Example: `TCuM8e98jmPwT1RU2jW7dekUC5HpXbGzFG`

proposal\_id

int32

required

Unique ID for the chain proposal. Example: `89`

Permission\_id

int32

Permission ID used for multi-signature.

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

Responses

# 200 200

# 400 400

Updated about 1 month ago

---

Language

JavaScript

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

Updated about 1 month ago

---