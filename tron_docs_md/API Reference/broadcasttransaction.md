

JUMP TO

Powered by

# BroadcastTransaction

post

https://api.shasta.trongrid.io/wallet/broadcasttransaction

Broadcasts a signed transaction to the network.

Recipes

📡

API Signature and Broadcast Flow

Open Recipe

✍️

Offline Sign the Transaction

Open Recipe

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

RAW\_BODY

json

required

Transaction object(Singed). See [here](/docs/tron-protocol-transaction) for details.
e.g., {"visible": false, "txID": "6db783c4142b3749a4b598db4644155455c9206e2eca4b31efbd48e46773d9d5", "raw\_data": {"contract": [{"parameter": {"value": {"amount": 1000000, "owner\_address": "411320a6fb4dcd4ff8e91392a8cb98378633cf7dd8", "to\_address": "414c8967080d86f3d0e1352a42f9213c7b9dd03b0f"}, "type\_url": "type.googleapis.com/protocol.TransferContract"}, "type": "TransferContract"}], "ref\_block\_bytes": "f69b", "ref\_block\_hash": "7d4a3b02495f2320", "expiration": 1762502739000, "timestamp": 1762502681856}, "raw\_data\_hex": "0a02f69b22087d4a3b02495f232040b888e6eaa5335a67080112630a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412320a15411320a6fb4dcd4ff8e91392a8cb98378633cf7dd81215414c8967080d86f3d0e1352a42f9213c7b9dd03b0f18c0843d7080cae2eaa533", "signature": ["2a3743f40d53a124c1597256b155bf286bd8874afe6997ec0a7e63405dea78cd914d9aa9adb8f84dc8d1ef4b1827dd9e8960a40a4ad11e619d06e9601e8b27c000"]}

Response

# 200 200

Updated 16 days ago

---

Language

ShellNodeRubyPHPPython

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200 - Example API Call Response

Updated 16 days ago

---