

JUMP TO

Powered by

# UpdateSetting

post

https://api.shasta.trongrid.io/wallet/updatesetting

Update the consume\_user\_resource\_percent parameter of a smart contract

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

Transaction initiator address.(Format: Base58 or Hex).
Example: `TSNEe5Tf4rnc9zPMNXfaTF5fZfHDDH8oyW`

contract\_address

string

required

Contract address. (Format: Base58 or Hex).
Example: `TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs`

consume\_user\_resource\_percent

int32

required

Percentage of user Energy consumption for a smart contract. (Range: [0-100]).
Example: `10`

Permission\_id

int32

Optional. Permission ID used for multi-signature.

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