

JUMP TO

Powered by

# EstimateEnergy

post

https://api.shasta.trongrid.io/walletsolidity/estimateenergy

Estimate the energy required for the successful execution of smart contract transactions. (Confirmed state)

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

Contract address. (Format: Base58 or Hex)
Example: `TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs`

function\_selector

string

Function selector.
Example: `transfer(address,uint256)`.

parameter

string

ABI-encoded function parameters (Hex String).
Example: `000000000000000000000000a614f803b6fd780986a42c78ec9c7f77e6ded13c`

data

string

This field transmits the necessary `data` for smart contract interaction, including the function being called and its parameters. You may choose to use the data field, which contains the complete ABI-encoded information, or use the `function_selector` and `parameter` fields separately. Note that if both `data` and `function_selector` are present, the system will prioritize using the `function_selector` and `parameter` fields for the contract interaction.

call\_value

int64

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

Optional. Specifies whether the address is in Base58 format (default: false). Note: Set to true in this example for demonstration purposes.

truefalse

Responses

# 200 200

# 400 400

Updated 3 months ago

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

Updated 3 months ago

---