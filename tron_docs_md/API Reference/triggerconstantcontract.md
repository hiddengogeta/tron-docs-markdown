

JUMP TO

Powered by

# TriggerConstantContract

post

https://api.shasta.trongrid.io/wallet/triggerconstantcontract

Invoke the readonly function (modified by the `view` or `pure` modifier) of a contract for contract data query; or Invoke the non-readonly function of a contract for predicting whether the transaction can be successfully executed and estimating the energy consumption; or estimate the energy consumption of contract deployment

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
Example: `TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g`

contract\_address

string

Contract address. (Format: Base58 or Hex).
Example: `TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs`

function\_selector

string

Function selector.
Example: `transfer(address,uint256)`

parameter

string

ABI-encoded function parameters (Hex String).
Example: `000000000000000000000000a614f803b6fd780986a42c78ec9c7f77e6ded13c`

data

string

This field transmits the necessary data for smart contract interaction, including the function being called and its parameters. You may choose to use the `data` field, which contains the complete ABI-encoded information, or use the `function_selector` and `parameter` fields separately. Note that if both `data` and `function_selector` are present, the system will prioritize using the `function_selector` and `parameter` fields for the contract interaction.

call\_value

int64

Amount of TRX transferred into the contract. (Unit: sun)

call\_token\_value

int64

Amount of TRC-10 token transferred into the contract.

token\_id

int64

TRC-10 token id

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

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200 - Result400 - Result

Updated about 1 month ago

---