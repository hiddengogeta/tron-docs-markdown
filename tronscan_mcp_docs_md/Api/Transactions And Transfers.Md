

# Transactions and Transfers

## Get a list of transactions

Get a list of transactions.

```
GET https://apilist.tronscanapi.com/api/transaction?sort=-timestamp&count=true&limit=20&start=0&start_timestamp=1529856000000&end_timestamp=1680503191391
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/transaction?sort=-timestamp&count=true&limit=20&start=0&start_timestamp=1529856000000&end_timestamp=1680503191391) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0`. Max `start + limit` is `10000` |
| `limit` | Number of items per page. Default: `10`. Max: `50` |
| `start_timestamp` | Start time |
| `end_timestamp` | End time |
| `fromAddress` | Sender’s address |
| `toAddress` | Recipient’s address |
| `tokens` | Tokens involved |
| `block` | Block |
| `type` | Transaction type |
| `address` | Account address filter |
| `direction` | Transfer direction: `in` (incoming), `out` (outgoing), `all` (both) |
| `confirm` | Filter by confirmation status: `0` (confirmed only), `1` (unconfirmed only), `2` (reverted only), empty (all). Multiple values can be combined with a comma, e.g. `0,1` |

### Response

```
{
  "total": 10000,
  "rangeTotal": 10000,
  "data": [
    {
      "block": 49963474,
      "hash": "a211f0728aa129c17195322a38c3ca0917ab04af75c5f0934215e6447f4ef6d4",
      "timestamp": 1680503190000,
      "ownerAddress": "TWbdVwjHTNn2PXDPbtSNvvESDd8PpApFmX",
      "toAddressList": ["TAWE8B9DXDgTmfr3bhFsjZ4U8Jx4nFTTTT"],
      "toAddress": "TAWE8B9DXDgTmfr3bhFsjZ4U8Jx4nFTTTT",
      "contractType": 1,
      "confirmed": true,
      "revert": false,
      "contractData": {
        "amount": 93000000,
        "owner_address": "TWbdVwjHTNn2PXDPbtSNvvESDd8PpApFmX",
        "to_address": "TAWE8B9DXDgTmfr3bhFsjZ4U8Jx4nFTTTT"
      },
      "SmartCalls": "",
      "Events": "",
      "id": "",
      "fee": "",
      "contractRet": "SUCCESS",
      "result": "SUCCESS",
      "amount": "93000000",
      "cheatStatus": false,
      "riskTransaction": false,
      "noteLevel": 2,
      "cost": {
        "net_fee": 268000,
        "energy_penalty_total": 0,
        "energy_usage": 0,
        "fee": 268000,
        "energy_fee": 0,
        "energy_usage_total": 0,
        "origin_energy_usage": 0,
        "net_usage": 0
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
      "tokenType": "trc10"
    }
  ],
  "wholeChainTxCount": 5242347520,
  "contractMap": {
    "TAWE8B9DXDgTmfr3bhFsjZ4U8Jx4nFTTTT": false,
    "TWbdVwjHTNn2PXDPbtSNvvESDd8PpApFmX": false
  },
  "contractInfo": {},
  "normalAddressInfo": {
    "TAWE8B9DXDgTmfr3bhFsjZ4U8Jx4nFTTTT": { "risk": false },
    "TWbdVwjHTNn2PXDPbtSNvvESDd8PpApFmX": { "risk": false }
  }
}
```

---

## Get transaction detail information by transaction hash

Get transaction information.

```
GET https://apilist.tronscanapi.com/api/transaction-info?hash=3194a00c5cf427a931b908453588b2ca3f661dafa3860b76a6362d08b3b08583
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/transaction-info?hash=3194a00c5cf427a931b908453588b2ca3f661dafa3860b76a6362d08b3b08583) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `hash` | Transaction hash |

### Response

```
{
  "block": 49965114,
  "hash": "3194a00c5cf427a931b908453588b2ca3f661dafa3860b76a6362d08b3b08583",
  "timestamp": 1680508110000,
  "ownerAddress": "TLbAurUF5HC5rACqBygeE6c2UrzLuPRP7J",
  "contractType": 2,
  "toAddress": "TQA2Z63x5rN561gCZSEnNPK5A5HK4W813s",
  "confirmations": 35,
  "confirmed": true,
  "revert": false,
  "contractRet": "SUCCESS",
  "riskTransaction": false,
  "noteLevel": 3,
  "hashTag": [],
  "addressTag": {},
  "contractInfo": {},
  "normalAddressInfo": {
    "TLbAurUF5HC5rACqBygeE6c2UrzLuPRP7J": { "risk": false },
    "TQA2Z63x5rN561gCZSEnNPK5A5HK4W813s": { "risk": false }
  },
  "info": {},
  "internal_transactions": {},
  "signature_addresses": [],
  "trigger_info": {},
  "contractData": {
    "amount": 618000000,
    "asset_name": "1004917",
    "owner_address": "TLbAurUF5HC5rACqBygeE6c2UrzLuPRP7J",
    "to_address": "TQA2Z63x5rN561gCZSEnNPK5A5HK4W813s",
    "tokenInfo": {
      "tokenId": "1004917",
      "tokenAbbr": "btc618.com",
      "tokenName": "btc618.com",
      "tokenDecimal": 6,
      "tokenType": "trc10",
      "vip": false
    }
  },
  "cost": {
    "net_fee_cost": 1000,
    "fee": 0,
    "energy_fee_cost": 420,
    "net_usage": 283,
    "multi_sign_fee": 0,
    "net_fee": 0,
    "energy_penalty_total": 0,
    "energy_usage": 0,
    "energy_fee": 0,
    "energy_usage_total": 0,
    "memoFee": 0,
    "origin_energy_usage": 0,
    "account_create_fee": 0
  },
  "srConfirmList": [
    {
      "address": "TGyrSc9ZmTdbYziuk1SKEmdtCdETafewJ9",
      "name": "Luganodes",
      "block": 49965114,
      "url": "https://luganodes.com"
    },
    {
      "address": "TTxrh32VJveqiYRwbLEX2wLTMFCfbpAUQj",
      "name": "OKX Earn",
      "block": 49965115,
      "url": "https://www.okx.com/earn/home"
    },
    {
      "address": "TLyqzVGLV1srkB7dToTAEqgDSfPtXRJZYH",
      "name": "Binance Staking",
      "block": 49965124,
      "url": "https://www.binance.com/en/staking"
    }
  ],
  "contract_map": {
    "TLbAurUF5HC5rACqBygeE6c2UrzLuPRP7J": false,
    "TQA2Z63x5rN561gCZSEnNPK5A5HK4W813s": false
  }
}
```

---

## Get TRC20 & TRC721 transfers list

Get the transfer list of TRC20 and TRC721 tokens.

```
GET https://apilist.tronscanapi.com/api/token_trc20/transfers?limit=20&start=0&contract_address=TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT&start_timestamp=&end_timestamp=&confirm=&filterTokenValue=1
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/token_trc20/transfers?limit=20&start=0&contract_address=TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT&start_timestamp=&end_timestamp=&confirm=&filterTokenValue=1) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0`. Max `start + limit` is `10000` |
| `limit` | Number of items per page. Default: `10`. Max: `50` |
| `contract_address` | Contract address |
| `start_timestamp` | Start time |
| `end_timestamp` | End time |
| `confirm` | Filter by confirmation status: `0` (confirmed only), `1` (unconfirmed only), empty (all) |
| `relatedAddress` | Account address |
| `fromAddress` | Sender’s address |
| `toAddress` | Recipient’s address |
| `filterTokenValue` | Filter by token value threshold |

### Response

```
{
  "total": 10000,
  "rangeTotal": 27628,
  "totalHitsAccurate": true,
  "timeInterval": 0,
  "contractInfo": {
    "TL5x9MtSnDy537FXKx53yAaHRRNdg9TkkA": {
      "tag1": "jUSDJ Token",
      "tag1Url": "justlend.just.network",
      "name": "CErc20Delegator",
      "vip": false
    }
  },
  "normalAddressInfo": {
    "TH3N6kYXow3FUP8Giyjm344qpDgjpChQx7": { "risk": false }
  },
  "token_transfers": [
    {
      "transaction_id": "cc74c25b36ac29c0c22ae07955ebd93d2c58654ed976cd39af3224b4292dd4d1",
      "status": 0,
      "block_ts": 1680513705000,
      "from_address": "TH3N6kYXow3FUP8Giyjm344qpDgjpChQx7",
      "from_address_tag": {},
      "to_address": "TL5x9MtSnDy537FXKx53yAaHRRNdg9TkkA",
      "to_address_tag": {},
      "block": 49966979,
      "contract_address": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT",
      "quant": "11258727923280441931",
      "confirmed": true,
      "contractRet": "SUCCESS",
      "finalResult": "SUCCESS",
      "revert": false,
      "riskTransaction": false,
      "tokenInfo": {
        "tokenId": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT",
        "tokenAbbr": "USDJ",
        "tokenName": "JUST Stablecoin",
        "tokenDecimal": 18,
        "tokenCanShow": 1,
        "tokenType": "trc20",
        "tokenLogo": "https://static.tronscan.org/production/logo/usdj.png",
        "tokenLevel": "2",
        "issuerAddr": "THPvaUhoh2Qn2y9THCZML3H815hhFhn5YC",
        "vip": true
      },
      "contract_type": "trc20",
      "fromAddressIsContract": false,
      "toAddressIsContract": true
    }
  ]
}
```

---

## Get TRC1155 transfer list

Get the transfer list of TRC1155 tokens.

```
GET https://apilist.tronscanapi.com/api/token_trc1155/transfers?limit=20&start=0&contract_address=TXWLT4N9vDcmNHDnSuKv2odhBtizYuEMKJ&start_timestamp=&end_timestamp=&confirm=&filterTokenValue=0
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/token_trc1155/transfers?limit=20&start=0&contract_address=TXWLT4N9vDcmNHDnSuKv2odhBtizYuEMKJ&start_timestamp=&end_timestamp=&confirm=&filterTokenValue=0) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `relatedAddress` | Account address. When specified, TRC1155 transfers of that address are returned |
| `start` | Start index. Default: `0`. Max `start + limit` is `10000` |
| `limit` | Number of transfers per page. Default: `10`. Max: `50` |
| `start_timestamp` | Start time, accurate to milliseconds |
| `end_timestamp` | End time, accurate to milliseconds |
| `format` | Download format. Use `csv` to download transfer data |
| `block` | Block number |
| `confirm` | Filter by status. `0`: confirmed only, `1`: unconfirmed only, `0,1`: all |
| `direction` | `in`: transfer-in, `out`: transfer-out, `all`: both |
| `contract_address` | Contract address |
| `filterTokenValue` | Filter by token value threshold |

### Response

```
{
  "total": 288,
  "rangeTotal": 288,
  "contractMap": {
    "TXWLT4N9vDcmNHDnSuKv2odhBtizYuEMKJ": true
  },
  "contractInfo": {
    "TXWLT4N9vDcmNHDnSuKv2odhBtizYuEMKJ": {
      "tag1": "",
      "tag1Url": "",
      "name": "PHONFT1155",
      "vip": false
    }
  },
  "token_transfers": [
    {
      "transaction_id": "e3eb2a7a85d74e38bc4fa79c6b188039d95206f292c30a2b728df43d1eed5054",
      "block_ts": 1680257265000,
      "from_address": "TGgNvM6AF7upXu3qPkRhxh6N3zxCokwN6A",
      "from_address_tag": {},
      "to_address": "TShRA95pGcfHrJtY8c9v68P9jcHpfugMqp",
      "to_address_tag": {},
      "block": 49881524,
      "contract_address": "TXWLT4N9vDcmNHDnSuKv2odhBtizYuEMKJ",
      "trigger_info": {
        "method": "safeTransferFrom(address from,address to,uint256 id,uint256 amount,bytes data)",
        "parameter": {
          "amount": "4",
          "data": "",
          "from": "TGgNvM6AF7upXu3qPkRhxh6N3zxCokwN6A",
          "to": "TShRA95pGcfHrJtY8c9v68P9jcHpfugMqp",
          "id": "4822760016515516615649000000"
        },
        "methodName": "safeTransferFrom",
        "contract_address": "TXWLT4N9vDcmNHDnSuKv2odhBtizYuEMKJ",
        "call_value": 0
      },
      "quant": "4",
      "approval_amount": "0",
      "event_type": "Transfer",
      "contract_type": "trc1155",
      "token_id": "4822760016515516615649000000",
      "confirmed": true,
      "contractRet": "SUCCESS",
      "finalResult": "SUCCESS",
      "fromAddressIsContract": false,
      "toAddressIsContract": false,
      "tokenInfo": {
        "tokenId": "TXWLT4N9vDcmNHDnSuKv2odhBtizYuEMKJ",
        "tokenAbbr": "PHONFT",
        "tokenName": "PHONFT1155",
        "tokenDecimal": 0,
        "tokenCanShow": 1,
        "tokenType": "trc1155",
        "tokenLogo": "",
        "tokenLevel": "2",
        "issuerAddr": "TGgNvM6AF7upXu3qPkRhxh6N3zxCokwN6A",
        "vip": false
      },
      "revert": false
    }
  ]
}
```

---

## Get TRX & TRC10 transfer list

Get account’s transfer list.

```
GET https://apilist.tronscanapi.com/api/transfer?sort=-timestamp&count=true&limit=20&start=0&address=TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7&filterTokenValue=1
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/transfer?sort=-timestamp&count=true&limit=20&start=0&address=TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7&filterTokenValue=1) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `sort` | Sort type |
| `start` | Start index. Default: `0`. Max `start + limit` is `10000` |
| `limit` | Number of transfers per page. Default: `10`. Max: `50` |
| `count` | Whether to return total transfer number |
| `address` | Address, like contract address |
| `fromAddress` | Sender’s address |
| `toAddress` | Recipient’s address |
| `tokens` | Specific tokens |
| `block` | Block number |
| `filterTokenValue` | Filter by token value threshold |
| `direction` | Transfer direction: `in` (incoming), `out` (outgoing), `all` (both) |
| `start_timestamp` | Start time |
| `end_timestamp` | End time |
| `confirm` | Filter by confirmation status: `0` (confirmed only), `1` (unconfirmed only), empty (all) |
| `token` | Single token filter |

### Response

```
{
  "total": 4,
  "rangeTotal": 4,
  "totalHitsAccurate": true,
  "timeInterval": 0,
  "data": [
    {
      "contractRet": "SUCCESS",
      "amount": 78963320,
      "data": "",
      "tokenName": "_",
      "confirmed": true,
      "transactionHash": "09f12a996caa106546b564b04b3adb8e5fed0091fc2006d6ee3ceb53b3ea359a",
      "id": "",
      "cheatStatus": false,
      "riskTransaction": false,
      "transferToTag": {},
      "tokenInfo": {
        "tokenId": "_",
        "tokenAbbr": "trx",
        "tokenName": "trx",
        "tokenDecimal": 6,
        "tokenCanShow": 1,
        "tokenType": "trc10",
        "tokenLogo": "https://static.tronscan.org/production/logo/trx.png",
        "vip": true
      },
      "transferFromAddress": "TKoCV62HPYYxghKQJV7bmW3g6KpWb1dGhQ",
      "transferToAddress": "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7",
      "block": 48132413,
      "timestamp": 1674997224000
    }
  ],
  "contractMap": {
    "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7": false
  },
  "contractInfo": {
    "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7": {
      "tag1": "WIN Token",
      "tag1Url": "https://winklink.org/",
      "name": "WINKLINK",
      "vip": true
    }
  },
  "normalAddressInfo": {
    "TKoCV62HPYYxghKQJV7bmW3g6KpWb1dGhQ": { "risk": false },
    "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7": { "risk": false }
  }
}
```

---

## Get internal transaction list for special address or block

Get internal transaction list.

```
GET https://apilist.tronscanapi.com/api/internal-transaction?limit=20&start=0&address=TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/internal-transaction?limit=20&start=0&address=TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start index. Default: `0`. Max `start + limit` is `10000` |
| `limit` | Number of transfers per page. Default: `10`. Max: `50` |
| `address` | Specific address. At least one of `address`, `block`, or `contract` must be specified |
| `contract` | Contract address to filter by |
| `block` | Block number |
| `start_timestamp` | Start time |
| `end_timestamp` | End time |
| `confirm` | Filter by confirmation status: `0` (confirmed only), `1` (unconfirmed only), empty (all) |

### Response

> **Note:** `voteCount`, `voteDetail`, and `voteToAddress` are conditional returns — only present for vote-type internal transactions.

```
{
  "total": 5901,
  "rangeTotal": 5901,
  "contractMap": {
    "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7": false
  },
  "contractInfo": {
    "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7": {
      "tag1": "WIN Token",
      "tag1Url": "https://winklink.org/",
      "name": "WINKLINK",
      "vip": true
    }
  },
  "normalAddressInfo": {
    "TC1GhhC5iGFLuuUthriuUu183P8YWPmQsK": { "risk": false },
    "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7": { "risk": false }
  },
  "data": [
    {
      "from": "TC1GhhC5iGFLuuUthriuUu183P8YWPmQsK",
      "to": "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7",
      "block": 49969040,
      "hash": "487c71e5e377852fe9e415b4a808bf383a7f990f402487155f5bd967eab9259b",
      "internal_hash": "38fb7717806abb5d6f4f1ac58fa94fdea350c9bf49c1b6cdbf327f528cce0fbf",
      "timestamp": 1680519888000,
      "rejected": false,
      "confirmed": true,
      "result": "SUCCESS",
      "revert": false,
      "note": "call",
      "call_value": 0,
      "token_id": "_",
      "valueInfoList": [],
      "token_list": {
        "token_id": "_",
        "call_value": 0,
        "tokenInfo": {
          "tokenId": "_",
          "tokenAbbr": "trx",
          "tokenName": "trx",
          "tokenDecimal": 6,
          "tokenType": "trc10",
          "vip": true
        }
      }
    }
  ]
}
```

---

## Get account’s transaction data

Get account’s transaction data.

```
GET https://apilist.tronscanapi.com/api/token_trc20/transfers-with-status?limit=1&start=0&trc20Id=TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4&address=TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/token_trc20/transfers-with-status?limit=1&start=0&trc20Id=TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4&address=TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start index. Default: `0`. Max `start + limit` is `10000` |
| `limit` | Number of transfers per page. Default: `20`. Max: `50` |
| `trc20Id` | TRC20 token address. **Required** |
| `address` | Account address. **Required** |
| `direction` | `1`: transfer-out (default), `2`: transfer-in, `0`: approval events |
| `db_version` | Whether to include approval transfers. `1`: include, `0`: exclude |
| `reverse` | Sort by creation time. Valid values: `true` / `false` |

### Response

```
{
  "tokenInfo": {
    "tokenId": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
    "tokenAbbr": "TUSD",
    "tokenName": "TrueUSD",
    "tokenDecimal": 18,
    "tokenCanShow": 1,
    "tokenType": "trc20",
    "tokenLogo": "https://static.tronscan.org/production/logo/tusd.png",
    "tokenLevel": "2",
    "issuerAddr": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
    "vip": true
  },
  "page_size": 1,
  "code": 200,
  "contractMap": {
    "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4": true
  },
  "data": [
    {
      "amount": "2531319816832000000000000",
      "status": 0,
      "approval_amount": "0",
      "block_timestamp": 1680520824000,
      "block": 49969352,
      "from": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
      "to": "TNXoiAJ3dct8Fjg4M9fkLFh9S2v9TXc32G",
      "hash": "09e76a0a358c205cfaaf366f340982024bdc9184c46fbad340003fdd34b8178d",
      "contract_address": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
      "confirmed": 0,
      "contract_type": "TriggerSmartContract",
      "contractType": 31,
      "revert": 0,
      "contract_ret": "SUCCESS",
      "final_result": "SUCCESS",
      "event_type": "Transfer",
      "decimals": 18,
      "token_name": "TrueUSD",
      "id": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
      "issue_address": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
      "direction": 1
    }
  ]
}
```

---

## Get transaction’s statistic data

Query statistic data of transactions.

```
GET https://apilist.tronscanapi.com/api/transaction/statistics
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/transaction/statistics) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "trc20Proportion": 23.904067997171442,
  "votesCount": 13665750,
  "trxTransferAmount": 3946775930194.08,
  "trc1155Count": 376,
  "trc10TransferCount": 785874652,
  "trxTransferCount": 1841578276,
  "trc20Amount": 108824880186574.28,
  "lastDayTxAmount": 347638651873.549499,
  "triggerProportion": 47.7588363752856,
  "othersCount": 48964240,
  "trc10TransferProportion": 15.011257854324562,
  "triggerTop10": [
    {
      "symbol": "USDT",
      "amount": 92661947704424.51,
      "address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "proportion": 18.180335008021615,
      "count": 951783294,
      "name": "Tether USD",
      "tokenType": "trc20"
    }
  ],
  "txCount": 5219303424,
  "trc20Top10": [
    {
      "symbol": "USDT",
      "address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "proportion": 18.180335008021615,
      "count": 951783294,
      "name": "Tether USD",
      "tokenType": "trc20"
    }
  ],
  "trc10TransferAmount": 1082262192353854.55,
  "lastDayTxCount": 7958199,
  "triggerCount": 2500287403,
  "triggerAmount": 213095775970664.94,
  "txAmount": 1314967143168462.47,
  "trc20Count": 1251434177,
  "trc721Count": 2905463,
  "trxTransferProportion": 35.17661027697644,
  "freezeBalanceCount": 33496818,
  "freezeBalanceAmount": 405867982280.2,
  "freezeBalanceProportion": 0.24274313630394778,
  "votesAmount": 44851381692,
  "votesProportion": 0.12883478074086357,
  "othersAmount": 1780849027067.26,
  "othersProportion": 15.445482928104257,
  "updateTime": 1680566400000
}
```

---

## Get statistic distribution data of transfer

Query statistic data of transfers.

```
GET https://apilist.tronscanapi.com/api/transfer/statistics
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/transfer/statistics) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "trc1155Proportion": 0.000008553422441506424,
  "trc20Proportion": 32.14427980066043,
  "trxTransferAmount": 3946775930194.07547,
  "trc1155Count": 333,
  "trc10TransferCount": 785874652,
  "lastDayTransfersCount": 7690674,
  "trxTransferCount": 1852963834,
  "transfersCount": 3893178459,
  "trc20Amount": 108824880186574.280532,
  "trc721Proportion": 0.07462958686836811,
  "trc10TransferProportion": 20.18593959347703,
  "trc20Count": 1251434177,
  "trc721Count": 2905463,
  "trc10TransferAmount": 1082262192353854.553791,
  "transfersAmount": 1195033848470622.909793,
  "trxTransferProportion": 47.595142465571726,
  "lastDayTransfersAmount": 174159162949.283275,
  "vip_core_token_amount_his_total": 26507614475524.355,
  "vip_core_token_1day_add": 29326432600.097733
}
```