

JUMP TO

Powered by

# ExchangeCreate

post

https://api.shasta.trongrid.io/wallet/exchangecreate

Creates a trading pair.

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

Transaction initiator address (format: Base58 or Hex). Example: `4100776428620856AE1D71562812B734E356B68551`

first\_token\_id

string

required

ID of the first token in the DEX trading pair. Example:  `31303030343837`

first\_token\_balance

int32

required

Balance of the first token in the DEX trading pair. Example:  `100`

second\_token\_id

string

required

ID of the second token in the DEX trading pair. Example: `31303030303031`

second\_token\_balance

int32

required

Balance of the second token in the DEX trading pair. Example:  `100`

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