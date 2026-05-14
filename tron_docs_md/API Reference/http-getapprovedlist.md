

JUMP TO

Powered by

# GetApprovedList

post

https://api.shasta.trongrid.io/wallet/getapprovedlist

Query the account address list which signed the transaction.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

signature

array of strings

required

The signature list of transaction. Example: `[ "50a252d1ffd1cf902fe4f7a3986697adf26a37c8193a86ce9ccc76adf5c05d26166c5e90d470a13708c48a76a766d2b2c68ffd733451ff1315040fb526e7ccde1b" ]`. Please note that when testing on this page, please enter the signature string directly into each input field. For example:
`50a252d1ffd1cf902fe4f7a3986697adf26a37c8193a86ce9ccc76adf5c05d26166c5e90d470a13708c48a76a766d2b2c68ffd733451ff1315040fb526e7ccde1b`

signature\*

ADD  string

raw\_data

json

required

The transaction's `raw_data`. Example: `{ "data": "74657374", "contract": [ { "parameter": { "value": { "resource": "ENERGY", "frozen_balance": 5000000, "owner_address": "TUoHaVjx7n5xz8LwPRDckgFrDWhMhuSuJM"}, "type_url": "type.googleapis.com/protocol.FreezeBalanceV2Contract" }, "type": "FreezeBalanceV2Contract"}], "ref_block_bytes": "dd1a", "ref_block_hash": "51a43e706d9ac33a", "expiration": 1767844938000, "timestamp": 1767844878000 }`

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format (Default: `false`). For example, when `raw_data` uses its sample value, this parameter should be set to `true`.

Response

# 200 200

Updated about 1 month ago

---

Language

JavaScript

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here!

Updated about 1 month ago

---