

JUMP TO

Powered by

# DeployContract

post

https://api.shasta.trongrid.io/wallet/deploycontract

Deploys a contract. Returns TransactionExtention, which contains an unsigned transaction.

Recipes

🪙

Deploy a TRC-20 Token with TronWeb

Open Recipe

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
Example: `TJmmqjb1DK9TTZbQXzRQ2AuA94z4gKAPFh`

abi

json

Smart contract ABI.
Example: `"[{"constant":false,"inputs":[{"name":"key","type":"uint256"},{"name":"value","type":"uint256"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"key","type":"uint256"}],"name":"get","outputs":[{"name":"value","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]"`

bytecode

string

Bytecode of the smart contract.
Example: `608060405234801561001057600080fd5b5060de8061001f6000396000f30060806040526004361060485763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416631ab06ee58114604d5780639507d39a146067575b600080fd5b348015605857600080fd5b506065600435602435608e565b005b348015607257600080fd5b50607c60043560a0565b60408051918252519081900360200190f35b60009182526020829052604090912055565b600090815260208190526040902054905600a165627a7a72305820fdfe832221d60dd582b4526afa20518b98c2e1cb0054653053a844cf265b25040029`

fee\_limit

int32

Maximum fee (in TRX) allowed for this transaction. (Unit: sun).
Example: `1000000000`

parameter

string

The parameters passed to the contract's constructor function.(ABI-encoded format)

origin\_energy\_limit

int32

Maximum energy consumption allowed by the contract creator per transaction.

name

string

Contract name

call\_value

int32

Amount of TRX transferred into the contract at deployment. (Unit: sun)

consume\_user\_resource\_percent

int32

Percentage of user Energy consumption for a smart contract. (Range: [0-100])

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Responses

# 200 200

# 400 400

Updated 16 days ago

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

Updated 16 days ago

---