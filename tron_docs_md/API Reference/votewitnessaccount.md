

JUMP TO

Powered by

# VoteWitnessAccount

post

https://api.shasta.trongrid.io/wallet/votewitnessaccount

Vote for super representatives

Recipes

🗳️

Vote for Super Representatives

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

Transaction initiator address (format: Base58 or Hex). Example: `TLUebU4tkfr4pxm2R5wZjrjQtqyKsV6Vab`

votes

array of objects

required

List of `vote` objects, each containing an SR address (`vote_address`) and vote count (`vote_count`).

votes\*

ADD  object

Permission\_id

int32

Permission ID used for multi-signature.

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Responses

# 200 200

# 400 400

Updated 16 days ago

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

Updated 16 days ago

---