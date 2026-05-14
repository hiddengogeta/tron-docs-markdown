

# Contract

List of smart contract interfaces.

## Get list of contracts

The value sum of `start` and `limit` must be less than or equal to **10000**. The maximum value for `limit` is **50**.

Returns a list of contracts.

```
GET https://apilist.tronscanapi.com/api/contracts?limit=20&start=0&verified-only=true&open-source-only=false&sort=-trxCount
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/contracts?limit=20&start=0&verified-only=true&open-source-only=false&sort=-trxCount) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `search` | Search by contract name or contract address |
| `sort` | Sort fields: `-trxCount`, `-balance`, `-timestamp`. Default: `-trxCount` |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `10` |
| `open-source-only` | Whether to show only open source contracts |
| `verified-only` | Whether to show only verified contracts |
| `owner` | Filter by deployer address |

### Response

```
{
  "total": 10000,
  "triggerTop7": [
    {
      "tag1": "USDT Token",
      "tag1Url": "https://tron.network/usdt",
      "blueTagUrl": "tether.to",
      "contract": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "percentage": 0.8975886192776561,
      "name": "TetherToken",
      "risk": false,
      "triggers": 1970847,
      "publicTagDesc": ""
    }
  ],
  "data": [
    {
      "address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "name": "TetherToken",
      "verify_status": 2,
      "balance": 846378273694,
      "trxCount": 949991434,
      "date_created": 1555400628000,
      "license": "0",
      "compile_version": "tron-0.4.25_Odyssey_v3.2.3",
      "compile_settings": "{\"optimizer\":0,\"constructor_params\":\"...\"}",
      "verify_time": 1575472751000,
      "tag1": "USDT Token",
      "tag1Url": "https://tron.network/usdt",
      "risk": false,
      "publicTagDesc": "",
      "vip": true,
      "trc20token": {
        "icon_url": "https://static.tronscan.org/production/logo/usdtlogo.png",
        "symbol": "USDT",
        "total_supply": "44125091014551106",
        "level": "2",
        "contract_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
        "issuer_addr": "THPvaUhoh2Qn2y9THCZML3H815hhFhn5YC",
        "home_page": "https://tron.network/usdt",
        "token_desc": "USDT is the official stablecoin issued by Tether on the TRON network.",
        "holders_count": "22132393",
        "git_hub": "",
        "decimals": "6",
        "name": "Tether USD",
        "issue_time": "2019-04-16 20:41:20",
        "white_paper": "https://tether.to/wp-content/uploads/2016/06/TetherWhitePaper.pdf",
        "email": "",
        "social_media": "[{\"method\":\"Twitter\",\"link\":\"https://twitter.com/Tether_to\"}]",
        "status": "1",
        "token_type": "trc20"
      }
    }
  ],
  "contractCount": 2261713,
  "rangeTotal": 33980,
  "contractCount24h": 3431,
  "updateTime": 1680516000000,
  "totalTrigger": 2195713,
  "verifyContractCount": 33980,
  "verifyContractCount24h": 1,
  "status": {
    "code": 0,
    "message": "SUCCESS"
  }
}
```

---

## Get contract detail information

Returns contract detail information.

```
GET https://apilist.tronscanapi.com/api/contract?contract=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/contract?contract=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `contract` | Contract address |

### Response

```
{
  "type": "null",
  "count": 0,
  "status": {
    "code": 0,
    "message": "SUCCESS"
  },
  "data": [
    {
      "address": "TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S",
      "balance": 19957105809,
      "balanceInUsd": 0,
      "verify_status": 2,
      "is_proxy": false,
      "proxy_implementation": "",
      "old_proxy_implementation": "",
      "call_value": 0,
      "call_token_value": 0,
      "call_token_id": 0,
      "call_token_info": {
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
        }
      },
      "trxCount": 757116,
      "date_created": 1621864512000,
      "name": "SunToken",
      "description": "",
      "announcement": "",
      "license": "1",
      "tag1": "SUN Token",
      "tag1Url": "https://sun.io/",
      "vip": true,
      "feedbackRisk": false,
      "blueTag": "SUN",
      "blueTagUrl": "sun.io",
      "greyTag": "",
      "redTag": "",
      "publicTag": "SUN Token",
      "publicTagDesc": "",
      "activeDay": 1802,
      "creator": {
        "address": "TRX6Q82wMqWNbCCiLqejbZe43wk1h1zJHm",
        "addressTag": "",
        "address_is_contract": false,
        "txHash": "1836ff59e1f9c46dd1682ede7824d08db922ba10162b7f69feefd76fd83c017f",
        "token_balance": 0,
        "consume_user_resource_percent": 0,
        "energy_remaining": 0,
        "energy_limit": 0
      },
      "auditReportUrl": "",
      "auditDep": "",
      "auditDate": "",
      "methodMap": {
        "39509351": "increaseAllowance(address,uint256)",
        "23b872dd": "transferFrom(address,address,uint256)",
        "70a08231": "balanceOf(address)",
        "a9059cbb": "transfer(address,uint256)",
        "18160ddd": "totalSupply()",
        "95d89b41": "symbol()",
        "dd62ed3e": "allowance(address,address)",
        "095ea7b3": "approve(address,uint256)",
        "313ce567": "decimals()",
        "06fdde03": "name()"
      },
      "energy_factor": 0.0,
      "tokenInfo": {
        "tokenId": "TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S",
        "tokenAbbr": "SUN",
        "tokenName": "SUN",
        "tokenDecimal": 18,
        "tokenCanShow": 1,
        "tokenType": "trc20",
        "tokenLogo": "https://static.tronscan.org/production/logo/TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S.png",
        "tokenLevel": "2",
        "issuerAddr": "TRX6Q82wMqWNbCCiLqejbZe43wk1h1zJHm",
        "vip": true
      },
      "balanceWithTokens": 95414.58043381207,
      "balanceWithTokensInUsd": 6266.799813970157
    }
  ]
}
```

---

## Get event information of the contract

This is a **POST** request. Please use the POST method to get the data.

Returns a list of event information for the contract.

```
POST https://apilist.tronscanapi.com/api/contracts/smart-contract-triggers-batch
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/contracts/smart-contract-triggers-batch) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `contractAddress` | Contract address |
| `hashList` | A list of transaction hashes |
| `term` | Query content — supports block number and event name |
| `fields` | Comma-separated list of fields to return in `list[]`. Omit to return all fields. Example: `"hash,method"` |

**Example request body:**

```
{
  "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
}
```

### Response

```
{
  "event_list": [
    {
      "block_number": 49993470,
      "block_timestamp": 1680593202000,
      "caller_contract_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "contract_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "event_index": 0,
      "event_name": "Transfer",
      "result_type": {
        "from": "address",
        "to": "address",
        "value": "uint256"
      },
      "result_with_topic": {
        "index": [
          { "param": "from", "value": "0x3402bee3959dc631ede6693cd96d79d951127d54" },
          { "param": "to", "value": "0xb7814f473cb0f00ebd2f6b4423904ff587571906" }
        ],
        "topic": "ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "dataInArr": [
          { "param": "value", "value": "0" }
        ]
      },
      "result": {
        "0": "0x3402bee3959dc631ede6693cd96d79d951127d54",
        "1": "0xb7814f473cb0f00ebd2f6b4423904ff587571906",
        "2": "0",
        "from": "0x3402bee3959dc631ede6693cd96d79d951127d54",
        "to": "0xb7814f473cb0f00ebd2f6b4423904ff587571906",
        "value": "0"
      },
      "event": "Transfer(address indexed from, address indexed to, uint256 value)",
      "transaction_id": "ef062a62284f5dd0de9c598c2ae8c17dc8179113d6f716cc37a5d72758e75b0d"
    }
  ],
  "list": [
    {
      "owner_address": "TAUNgCkc9JQckDUpNntJHFfKQcXDqFaFaF",
      "block": 49993470,
      "hash": "ef062a62284f5dd0de9c598c2ae8c17dc8179113d6f716cc37a5d72758e75b0d",
      "date_created": 1680593202000,
      "contract_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "call_value": 0,
      "confirmed": false,
      "method": "transferFrom(address _from,address _to,uint256 _value)",
      "parameter": "{\"_from\":\"TEiDRohciqCzb6dwD5ANvXmg4dPuHZsjxM\",\"_value\":\"0\",\"_to\":\"TShVZkvV25hu1iTxBVxGY67duQ46hV2i2t\"}",
      "day": "2023-04-04",
      "token_id": 0,
      "token_value": 0,
      "data": ""
    }
  ]
}
```

---

## Get contract energy statistics

Returns Energy statistic data of a contract.

```
GET https://apilist.tronscanapi.com/api/onecontractenergystatistic?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/onecontractenergystatistic?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Contract address |

### Response

```
{
  "total": 1,
  "totalEnergy": 10881764450,
  "data": [
    {
      "day": 1621900800000,
      "total_energy": 97804,
      "energy": 75350,
      "contract_supplied": 0,
      "trx": 22454
    }
  ]
}
```

---

## Get contract call statistics

Returns contract call statistics.

```
GET https://apilist.tronscanapi.com/api/contracts/top_call?contract_address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/contracts/top_call?contract_address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `contract_address` | Contract address |

### Response

```
{
  "recentCallTimes": 8147,
  "timeLong": 1680480000000,
  "topAddress": [
    {
      "address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
      "addressTag": "Binance-Hot",
      "count": 628,
      "ratio": 0.0771
    },
    {
      "address": "TNaRAoLUyYEV2uF7GUrzSjRQTU8v5ZJ5VR",
      "addressTag": "Huobi",
      "count": 605,
      "ratio": 0.0743
    },
    {
      "address": "TETh4cVmVGXLBkGuKRDWnoz96rqoAop2aZ",
      "count": 410,
      "ratio": 0.0503
    },
    {
      "address": "TNXoiAJ3dct8Fjg4M9fkLFh9S2v9TXc32G",
      "addressTag": "Binance-Hot",
      "count": 384,
      "ratio": 0.0471
    }
  ],
  "totalAddress": 1429,
  "totalCallTimes": 756112,
  "topMethods": [
    { "times": 7164, "methodId": "a9059cbb", "ratio": 0.8793 },
    { "times": 866,  "methodId": "095ea7b3", "ratio": 0.1063 },
    { "times": 116,  "methodId": "23b872dd", "ratio": 0.0142 },
    { "times": 1,    "methodId": "d73dd623", "ratio": 0.0001 }
  ],
  "contractMap": {},
  "contractInfo": {}
}
```

---

## Get the number of unique addresses called per day for a contract over a certain period of time

Returns the number of unique addresses called per day for a contract over a certain period of time.

```
GET https://apilist.tronscanapi.com/api/onecontractcallerstatistic?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S&start_timestamp=1621900800000&end_timestamp=1621987200000
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/onecontractcallerstatistic?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S&start_timestamp=1621900800000&end_timestamp=1621987200000) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Contract address |
| `start_timestamp` | Start time, accurate to seconds |
| `end_timestamp` | End time, accurate to seconds |

### Response

```
{
  "total": 2,
  "totalCallerAmount": 143,
  "data": [
    {
      "day": 1621900800000,
      "amount": 2
    },
    {
      "day": 1621987200000,
      "amount": 141
    }
  ]
}
```

---

## Get the list of the number of calls per day of the contract

Returns a list of the number of calls per day of the contract.

```
GET https://apilist.tronscanapi.com/api/onecontracttriggerstatistic?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S&start_timestamp=1621900800000&end_timestamp=1621987200000
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/onecontracttriggerstatistic?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S&start_timestamp=1621900800000&end_timestamp=1621987200000) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Contract address |
| `start_timestamp` | Start time, accurate to seconds |
| `end_timestamp` | End time, accurate to seconds |

### Response

```
{
  "total": 2,
  "totalAmount": 166,
  "data": [
    {
      "day": 1621900800000,
      "amount": 6
    },
    {
      "day": 1621987200000,
      "amount": 160
    }
  ]
}
```

---

## Get the list of daily analysis data for the contract over a period of time

Returns a list of daily analysis data for the contract over a period of time.

```
GET https://apilist.tronscanapi.com/api/contract/analysis?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S&type=0&start_timestamp=1680430566127&end_timestamp=1680516966127
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/contract/analysis?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S&type=0&start_timestamp=1680430566127&end_timestamp=1680516966127) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Contract address |
| `type` | Query data type (see below) |
| `start_timestamp` | Start time, accurate to seconds |
| `end_timestamp` | End time, accurate to seconds |

**`type` values:**

| Value | Description |
| --- | --- |
| `0` | **Balance** — TRX balance, the price of TRX on that day (calculated using USDT) |
| `1` | **Token transfers** — number of TRC20 token transfers and number of tokens transferred |
| `2` | **Energy consumption** — from frozen TRX, from burning TRX, provided by contract deployers |
| `3` | **Bandwidth consumption** — from free Bandwidth or frozen TRX, from burning TRX |
| `4` | **Contract calling** — number of calls and number of calling accounts |
| `5` | **Fees** — Bandwidth and Energy consumed from burning TRX |

### Response

**`type=0` — Balance:**

```
{
  "size": 1,
  "data": [
    {
      "day": "2023-04-02",
      "trx_amount": "19957.105809",
      "usdt_amount": "1303.445448",
      "price": 0.06531234843567024
    }
  ]
}
```

**`type=1` — Token transfers:**

```
{
  "size": 1,
  "data": [
    {
      "day": "2023-04-02",
      "transfer_count": 0,
      "token_count": 0
    }
  ]
}
```

**`type=2` — Energy consumption:**

```
{
  "size": 1,
  "data": [
    {
      "day": "2023-04-02",
      "energy_usage": 2499257,
      "energy_burn": 969003,
      "origin_energy_usage": 0,
      "energy_usage_total": 3468260,
      "energy_usage_as_deploy": 0,
      "energy_total": 3468260
    }
  ]
}
```

**`type=3` — Bandwidth consumption:**

```
{
  "size": 1,
  "data": [
    {
      "day": "2023-04-02",
      "net_usage": 71287,
      "net_burn": 13439,
      "net_usage_total": 84726
    }
  ]
}
```

**`type=4` — Contract calling:**

```
{
  "size": 1,
  "data": [
    {
      "day": "2023-04-02",
      "trigger_count": 243,
      "account_count": 93
    }
  ]
}
```

**`type=5` — Fees:**

```
{
  "size": 1,
  "data": [
    {
      "day": "2023-04-02",
      "burn_trx": "420.420260"
    }
  ]
}
```

---

## Get the list of all callers of the contract and the statistics of the number of calls

Returns a list of all callers of the contract and the statistics of the number of calls.

```
GET https://apilist.tronscanapi.com/api/onecontractcallers?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S&day=1680429735649&limit=2&start=0
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/onecontractcallers?address=TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S&day=1680429735649&limit=2&start=0) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Contract address |
| `day` | Query the number of days, counted backwards from current time. Default: yesterday |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `10` |

### Response

```
{
  "total": 93,
  "totalCallerAmount": 243,
  "data": [
    {
      "caller_address": "TZDSbKHtAF7UJPZmTgbx7EvFCpgKHX295g",
      "amount": 36
    },
    {
      "caller_address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
      "callerAddressTag": "Binance-Hot",
      "amount": 20
    }
  ],
  "contractMap": {
    "TZDSbKHtAF7UJPZmTgbx7EvFCpgKHX295g": false,
    "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi": false
  },
  "contractInfo": {}
}
```

---

## Get the list of trigger transactions for a certain time period

The maximum value for `limit` is **50**. The value sum of `start` and `limit` must be less than or equal to **10000**.

Returns a list of trigger transactions for a certain time period.

```
GET https://apilist.tronscanapi.com/api/contracts/trigger?limit=1&start=0&start_timestamp=1680430566127&end_timestamp=1680508302533
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/contracts/trigger?limit=1&start=0&start_timestamp=1680430566127&end_timestamp=1680508302533) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `10` |
| `start_timestamp` | Start time, accurate to milliseconds |
| `end_timestamp` | End time, accurate to milliseconds |

### Response

```
{
  "total": 10000,
  "data": [
    {
      "block": 49965178,
      "callData": "23b872dd000000000000000000000041acd40aa681afe4fed382a8883f1300277c650c8f...",
      "callValue": 0,
      "confirmed": true,
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "contractType": "IntendedLeaveEmpty",
      "hash": "5d8b9023513dd8e13c0d3b282133661c05654a4808d731c678ea298d9eace5a7",
      "ownerAddress": "TGwaLG8wsB9UHytN5WKzdHn5KiMV8cCccC",
      "ownerAddressTag": "",
      "timestamp": 1680508302000,
      "result": "IntendedLeaveEmpty",
      "token": ""
    }
  ],
  "contractMap": {
    "TGwaLG8wsB9UHytN5WKzdHn5KiMV8cCccC": false,
    "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t": true
  },
  "rangeTotal": 3059619,
  "contractInfo": {
    "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t": {
      "isToken": true,
      "tag1": "USDT Token",
      "tag1Url": "https://tron.network/usdt",
      "name": "TetherToken",
      "risk": false,
      "publicTagDesc": "",
      "publicTag": "USDT Token",
      "vip": true
    }
  }
}
```