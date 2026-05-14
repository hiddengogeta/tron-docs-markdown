

JUMP TO

Powered by

# ExchangeInject

post

https://api.shasta.trongrid.io/wallet/exchangeinject

Injects capital into the transaction. The purpose of injecting capital into the trading pair is to prevent price fluctuation from affecting the transaction.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

owner\_address

string

Transaction creator address (format: Base58 or Hex). Example: `4100776428620856AE1D71562812B734E356B68551`

exchange\_id

int64

ID of the DEX trading pair. Example: `12`

token\_id

string

ID of the token, usually is the token name (format: Hex). Example: `31303030343837`

quant

int64

Amount of tokens to inject from a DEX trading pair. Example: `100`

Permission\_id

int64

Permission ID used for multi-signature.

visible

boolean

Set to `true` to include detailed transaction statistics (`txStat`) in the response. (Default: `false`)

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