

JUMP TO

Powered by

# CreateAccount

post

https://api.shasta.trongrid.io/wallet/createaccount

Activate an account. Uses an already activated account to activate a new account. Users have to generate an account locally with wallet-cli or others SDKs like TronWeb, and then use this API to activate the account generated, or just simply transfer TRX to it.

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

Transaction initiator address (format: Base58 or Hex). Example: `TUoHaVjx7n5xz8LwPRDckgFrDWhMhuSuJM`

account\_address

string

required

Address of the account to be activated (format: Base58 or Hex). Example: `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ`

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Permission\_id

int32

Permission ID used for multi-signature.

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