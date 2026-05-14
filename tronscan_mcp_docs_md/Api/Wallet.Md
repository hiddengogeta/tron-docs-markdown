

# Wallet

## Get the list of TRX transfers related to a specific address

Returns the list of TRX transfers for a specific address.

The value sum of `start` and `limit` must be less than or equal to **10000**.

```
GET https://apilist.tronscanapi.com/api/transfer/trx?address=TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7&start=0&limit=20&direction=0&reverse=true&fee=true&db_version=1&start_timestamp=&end_timestamp=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/transfer/trx?address=TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7&start=0&limit=20&direction=0&reverse=true&fee=true&db_version=1&start_timestamp=&end_timestamp=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `20`. Max: `50` |
| `address` | Query address (required) |
| `direction` | Default: `1`. `1`: inbound transfers. `2`: outbound transfers. `0`: both |
| `start_timestamp` | **Millisecond timestamp**. Start time. Default: earliest block time `1529769600000` |
| `end_timestamp` | **Millisecond timestamp**. End time. Default: current time |
| `db_version` | Default: `0`, which filters out transfers with invalid `to` or `from` addresses |
| `reverse` | Sort the data in descending order. Default: `true` |
| `fee` | Whether to return data of TRX burning for resource consumption. Default: `false` |

### Response

```
{
  "contractMap": {
    "TGXD5vRuCng2k8Ei51u4fmLxYzAUcJngGP": false,
    "TTnsU2TZPH2napsioPhCcZfuTNpRmujVRp": false,
    "TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7": false
  },
  "tokenInfo": {
    "tokenId": "_",
    "tokenAbbr": "trx",
    "tokenName": "trx",
    "tokenDecimal": 6,
    "tokenCanShow": 1,
    "tokenType": "trc10",
    "tokenLogo": "https://static.tronscan.org/production/logo/trx.png",
    "tokenLevel": "2",
    "vip": true
  },
  "page_size": 2,
  "code": 200,
  "data": [
    {
      "amount": "40",
      "block_timestamp": 1670818821000,
      "block": 46743525,
      "from": "TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7",
      "to": "TGXD5vRuCng2k8Ei51u4fmLxYzAUcJngGP",
      "hash": "eb62c9a87f3be46a883459b30b58fc940dba485c44981a2cfeb5f5d7d2702745",
      "confirmed": 1,
      "contract_type": "TransferContract",
      "contractType": 1,
      "revert": 0,
      "contract_ret": "SUCCESS",
      "symbol": "",
      "issue_address": "",
      "decimals": 6,
      "token_name": "",
      "direction": 1,
      "cheatStatus": false
    },
    {
      "amount": "100000",
      "block_timestamp": 1625827647000,
      "block": 31784460,
      "from": "TTnsU2TZPH2napsioPhCcZfuTNpRmujVRp",
      "to": "TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7",
      "hash": "3401fc4929fb41750971c65a79333d116b7fc00cb2d8ed1a629e6ebefd8a928f",
      "confirmed": 1,
      "contract_type": "TransferContract",
      "contractType": 1,
      "revert": 0,
      "contract_ret": "SUCCESS",
      "symbol": "",
      "issue_address": "",
      "decimals": 6,
      "token_name": "",
      "direction": 2,
      "cheatStatus": false
    }
  ]
}
```

---

## Get the transfer list of a specific TRC10 token for a certain address

Returns the transfer list of a TRC10 token for a specific account.

The value sum of `start` and `limit` must be less than or equal to **10000**.

```
GET https://apilist.tronscanapi.com/api/transfer/token10?address=TK1AgzEiqiAuvnPVACvjJexwV4svyBxBdW&trc10Id=1002000&start=0&limit=2&direction=0&reverse=true&db_version=1&start_timestamp=&end_timestamp=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/transfer/token10?address=TK1AgzEiqiAuvnPVACvjJexwV4svyBxBdW&trc10Id=1002000&start=0&limit=2&direction=0&reverse=true&db_version=1&start_timestamp=&end_timestamp=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `20`. Max: `50` |
| `address` | Query address (required) |
| `trc10Id` | TRC10 token ID (required) |
| `direction` | Default: `1`. `1`: inbound transfers. `2`: outbound transfers. `0`: both |
| `start_timestamp` | **Millisecond timestamp**. Start time. Default: earliest block time `1529769600000` |
| `end_timestamp` | **Millisecond timestamp**. End time. Default: current time |
| `db_version` | Default: `0`, which filters out transfers with invalid `to` or `from` addresses |
| `reverse` | Sort the data in descending order. Default: `true` |

### Response

```
{
  "contractMap": {
    "TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg": false,
    "TSyGCe17oMDc9AQdHYec69jYob2GcF3fwj": false,
    "TKHtoE7js6DP3T8tKtYaATygvUHJCCrTLS": false,
    "TK1AgzEiqiAuvnPVACvjJexwV4svyBxBdW": false
  },
  "tokenInfo": {
    "tokenId": "1002000",
    "tokenAbbr": "BTTOLD",
    "tokenName": "BitTorrent Old",
    "tokenDecimal": 6,
    "tokenCanShow": 1,
    "tokenType": "trc10",
    "tokenLogo": "https://static.tronscan.org/production/logo/1002000.png",
    "tokenLevel": "2",
    "vip": true
  },
  "page_size": 2,
  "code": 200,
  "data": [
    {
      "amount": "218498000000",
      "block_timestamp": 1668238866000,
      "block": 45885595,
      "from": "TSyGCe17oMDc9AQdHYec69jYob2GcF3fwj",
      "to": "TK1AgzEiqiAuvnPVACvjJexwV4svyBxBdW",
      "hash": "aee0a620b754f82068ee1316efb70703308e5be4acb1e2a40bea775b639e12e8",
      "confirmed": 1,
      "contract_type": "TransferAssetContract",
      "contractType": 2,
      "revert": 0,
      "contract_ret": "SUCCESS",
      "id": 1002000,
      "symbol": "BTTOLD",
      "issue_address": "TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg",
      "decimals": 6,
      "token_name": "BitTorrent Old",
      "direction": 2
    },
    {
      "amount": "1234",
      "block_timestamp": 1657593534000,
      "block": 42339925,
      "from": "TKHtoE7js6DP3T8tKtYaATygvUHJCCrTLS",
      "to": "TK1AgzEiqiAuvnPVACvjJexwV4svyBxBdW",
      "hash": "6c0b76f20f0f84abb9dc6fc12d797e77414fcc993e0ecca74f2b6cc007de6d5e",
      "confirmed": 1,
      "contract_type": "TransferAssetContract",
      "contractType": 2,
      "revert": 0,
      "contract_ret": "SUCCESS",
      "id": 1002000,
      "symbol": "BTTOLD",
      "issue_address": "TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg",
      "decimals": 6,
      "token_name": "BitTorrent Old",
      "direction": 2
    }
  ]
}
```

---

## Get the transfer list of a specific TRC20 token for a certain address

Returns the transfer list of a TRC20 token for a specific account.

The value sum of `start` and `limit` must be less than or equal to **10000**.

```
GET https://apilist.tronscanapi.com/api/transfer/trc20?address=TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7&trc20Id=TCmSR8UYWvsZkZmprGKaudTuWUZ62ycnnN&start=0&limit=2&direction=0&reverse=true&db_version=1&start_timestamp=&end_timestamp=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/transfer/trc20?address=TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7&trc20Id=TCmSR8UYWvsZkZmprGKaudTuWUZ62ycnnN&start=0&limit=2&direction=0&reverse=true&db_version=1&start_timestamp=&end_timestamp=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `20`. Max: `50` |
| `address` | Query address (required) |
| `trc20Id` | TRC20 token ID (required) |
| `direction` | Default: `1`. `1`: inbound transfers. `2`: outbound transfers. `0`: both |
| `start_timestamp` | **Millisecond timestamp**. Start time. Default: earliest block time `1529769600000` |
| `end_timestamp` | **Millisecond timestamp**. End time. Default: current time |
| `db_version` | Default: `0`, which filters out transfers with invalid `to` or `from` addresses |
| `reverse` | Sort the data in descending order. Default: `true` |

### Response

```
{
  "contractMap": {
    "TQRj3keAZdS9mUWqReMFuYRhAZdEZuPoHc": false,
    "TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7": false
  },
  "tokenInfo": {
    "tokenId": "TCmSR8UYWvsZkZmprGKaudTuWUZ62ycnnN",
    "tokenAbbr": "SSH",
    "tokenName": "SSH",
    "tokenDecimal": 6,
    "tokenCanShow": 1,
    "tokenType": "trc20",
    "tokenLogo": "https://static.tronscan.org/production/upload/logo/TCmSR8UYWvsZkZmprGKaudTuWUZ62ycnnN.jpeg?t=1651809163740",
    "tokenLevel": "0",
    "issuerAddr": "TQRj3keAZdS9mUWqReMFuYRhAZdEZuPoHc",
    "vip": false
  },
  "page_size": 1,
  "code": 200,
  "data": [
    {
      "amount": "1000000000000",
      "status": 0,
      "approval_amount": "0",
      "block_timestamp": 1630984188000,
      "block": 33491701,
      "from": "TQRj3keAZdS9mUWqReMFuYRhAZdEZuPoHc",
      "to": "TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7",
      "hash": "59eb32557ed6b96fa61d466fd54e1282acbb526205ca8cbf539885ccb11d91f9",
      "confirmed": 1,
      "contract_type": "TriggerSmartContract",
      "contractType": 31,
      "revert": 0,
      "contract_ret": "SUCCESS",
      "event_type": "Transfer",
      "issue_address": "TQRj3keAZdS9mUWqReMFuYRhAZdEZuPoHc",
      "decimals": 6,
      "token_name": "ADApp",
      "id": "TCmSR8UYWvsZkZmprGKaudTuWUZ62ycnnN",
      "direction": 2
    }
  ]
}
```

---

## Get the information of tokens held and followed in the account’s web wallet

Returns a list of tokens held and followed by an account.

```
GET https://apilist.tronscanapi.com/api/account/wallet?address=TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/account/wallet?address=TSTVYwFDp7SBfZk7Hrz3tucwQVASyJdwC7) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Query address (required) |

### Response

```
{
  "code": 200,
  "status": "1",
  "message": "request ok",
  "lastUpdateSeconds": 1714514400000,
  "count": 3,
  "data": [
    {
      "token_id": "_",
      "token_abbr": "trx",
      "token_name": "trx",
      "token_type": 0,
      "token_decimal": 6,
      "balance": "0.000000",
      "token_value": "0.000000",
      "token_value_in_usd": "0",
      "token_price_in_usd": "0.06561",
      "token_price": "1",
      "frozen_token_value_in_usd": "0",
      "frozenV2_token_value_in_usd": "0",
      "level": 2,
      "frozen": 0,
      "frozenV2": 0,
      "pair_id": 48,
      "vip": false,
      "token_url": "https://static.tronscan.org/production/logo/trx.png"
    },
    {
      "token_id": "1002486",
      "token_abbr": "BDC",
      "token_name": "BlockDance",
      "token_type": 10,
      "token_decimal": 6,
      "balance": "10000",
      "token_value": "0",
      "token_value_in_usd": "0",
      "token_price_in_usd": "0",
      "token_price": "0",
      "level": "1",
      "transferCount": 44,
      "nrOfTokenHolders": 26,
      "vip": false,
      "token_url": "https://static.tronscan.org/production/upload/logo/1002486.png?t=1584951708472"
    },
    {
      "token_id": "TCmSR8UYWvsZkZmprGKaudTuWUZ62ycnnN",
      "token_abbr": "SSH",
      "token_name": "SSH",
      "token_type": 20,
      "token_decimal": 6,
      "balance": "1000000",
      "token_value": "0",
      "token_value_in_usd": "0",
      "token_price_in_usd": "0",
      "token_price": "0",
      "level": "0",
      "transferCount": 6,
      "nrOfTokenHolders": 6,
      "vip": false,
      "token_url": "https://static.tronscan.org/production/upload/logo/TCmSR8UYWvsZkZmprGKaudTuWUZ62ycnnN.jpeg?t=1651809163740"
    }
  ],
  "totalValueInUsd": "0"
}
```

---

## Get the amount of unfreezable TRX in address

Returns the amount of unfreezable TRX in one address.

```
GET https://apilist.tronscanapi.com/api/account/resource/unfreeze?address=TGXD5vRuCng2k8Ei51u4fmLxYzAUcJngGP
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/account/resource/unfreeze?address=TGXD5vRuCng2k8Ei51u4fmLxYzAUcJngGP) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Query address (required) |

### Response

```
{
  "balance": 0,
  "message": "SUCCESS"
}
```