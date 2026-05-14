

JUMP TO

Powered by

# UpdateEnergyLimit

post

https://api.shasta.trongrid.io/wallet/updateenergylimit

Update the origin\_energy\_limit parameter of a smart contract

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

owner\_address

string

Transaction initiator address.(Format: Base58 or Hex).
Example: `TSNEe5Tf4rnc9zPMNXfaTF5fZfHDDH8oyW`

contract\_address

string

Contract address. (Format: Base58 or Hex).
Example: `TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs`

origin\_energy\_limit

int32

Maximum energy consumption allowed by the contract creator per transaction.
Example: `100000000`

Permission\_id

int32

Optional. Permission ID used for multi-signature. (Default: Owner Permission)

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