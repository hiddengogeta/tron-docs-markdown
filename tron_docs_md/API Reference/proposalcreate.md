

JUMP TO

Powered by

# ProposalCreate

post

https://api.shasta.trongrid.io/wallet/proposalcreate

Creates a proposal transaction.

Recipes

📝

Create a Governance Proposal

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

Transaction initiator address (format: Base58 or Hex). Example: `TCuM8e98jmPwT1RU2jW7dekUC5HpXbGzFG`

parameters

json

required

Map of chain parameter IDs and their new values.
For example:  `[{"key": 0,"value": 100000},{"key": 1,"value": 2}]`

Permission\_id

int32

Permission ID used for multi-signature.

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

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