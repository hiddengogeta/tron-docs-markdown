

JUMP TO

Powered by

# GetContractInfo

post

https://api.shasta.trongrid.io/wallet/getcontractinfo

Queries a contract's information from the blockchain. The difference from the `wallet/getcontract` interface is that this interface returns not only the `bytecode` but also the `runtime bytecode` of the contract. Compared with `bytecode`, `runtime bytecode` does not contain constructor and constructor parameter information.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

value

string

Contract address (format: Base58 or Hex).
Example: `TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs`

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