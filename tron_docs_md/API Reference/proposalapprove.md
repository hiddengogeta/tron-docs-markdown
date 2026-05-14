

JUMP TO

Powered by

# ProposalApprove

post

https://api.shasta.trongrid.io/wallet/proposalapprove

Approves proposed transaction.

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

Approver address (format: Base58 or Hex). Example: `TUeTYVYJFfmBj3hVyopAZB97yc432Aay4N`

proposal\_id

int32

required

Unique ID for the chain proposal. Example: `89`

is\_add\_approval

boolean

required

Whether to approve the proposal.

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