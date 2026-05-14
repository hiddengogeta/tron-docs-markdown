

JUMP TO

Powered by

# TriggerSmartContract

post

https://api.shasta.trongrid.io/wallet/triggersmartcontract

Returns TransactionExtention, which contains the unsigned Transaction

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
Example: `TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g`

contract\_address

string

required

Contract address. (Format: Base58 or Hex).
Example: `TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs`

function\_selector

string

Function selector.
Example: `transfer(address,uint256)`

parameter

string

ABI-encoded function parameters (Hex String).
e.g., 00000000000000000000004115208EF33A926919ED270E2FA61367B2DA3753DA0000000000000000000000000000000000000000000000000000000000000032

data

string

This field transmits the necessary data for smart contract interaction, including the function being called and its parameters. You may choose to use the `data` field, which contains the complete ABI-encoded information, or use the `function_selector` and `parameter` fields separately. Note that if both `data` and `function_selector` are present, the system will prioritize using the `function_selector` and `parameter` fields for the contract interaction.

fee\_limit

int32

required

Maximum fee (in TRX) allowed for this transaction. (Unit: sun).
Example: `1000000000`

call\_value

int64

Defaults to 0

Amount of TRX transferred into the contract. (Unit: sun)

call\_token\_value

int64

Amount of TRC-10 token transferred into the contract.

token\_id

int64

TRC-10 token ID

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