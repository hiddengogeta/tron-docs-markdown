

JUMP TO

Powered by

# GetContract

post

https://api.shasta.trongrid.io/wallet/getcontract

Queries a contract's information from the blockchain, including the bytecode of the contract, ABI, configuration parameters, etc.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

value

string

required

The contract address. (Format: Base58 or hex).
Example: TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs

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