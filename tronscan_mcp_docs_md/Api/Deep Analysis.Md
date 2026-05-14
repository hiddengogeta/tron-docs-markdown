

# Deep Analysis

## Get account data with transaction records with the current account

Returns accounts that have transaction records with a specific address, along with transfer-in/out amounts and counts.

```
GET https://apilist.tronscanapi.com/api/deep/account/relatedAccount?address=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/deep/account/relatedAccount?address=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Query address |
| `txNum` | Number of transactions range, separated by commas. e.g. `1,10` represents 1 to 10 |
| `txAmount` | Transaction amount range, separated by commas. e.g. `100,10000` represents 100 to 10000 |
| `direction` | Transfer type. `0`: all. `1`: transfer-in. `2`: transfer-out |
| `relatedAddress` | Filter by related address |
| `relatedToken` | Filter by related token |
| `startTime` | Start time in seconds |
| `endTime` | End time in seconds |
| `sortby` | Sorted field: `amountIn`, `amountOut`, `timesIn`, `timesOut` |
| `limit` | Max: `100` |

### Response

```
{
  "total": 4,
  "code": 0,
  "data": [
    {
      "inAmountUsd": 3130784970.9059763,
      "outAmountUsd": 0,
      "address": "TKHuVq1oKVruCGLvqVexFs6dawKv6fQgFs",
      "addressTag": "Tether Treasury",
      "outNum": 0,
      "inNum": 117
    },
    {
      "inAmountUsd": 1721903345.260201,
      "outAmountUsd": 0,
      "address": "TTd9qHyjqiUkfTxe3gotbuTMpjU8LEbpkN",
      "addressTag": "Kraken",
      "outNum": 0,
      "inNum": 169
    },
    {
      "inAmountUsd": 89488438.237212,
      "outAmountUsd": 0,
      "address": "TXFBqBbqJommqZf7BV8NNYzePh97UmJodJ",
      "addressTag": "Bitfinex",
      "outNum": 0,
      "inNum": 41
    },
    {
      "inAmountUsd": 158.68939300000002,
      "outAmountUsd": 0,
      "address": "TB3UZsVL7SdrrugRfeyXK5C75e7V3CDyty",
      "addressTag": "TB3UZsVL7SdrrugRfeyXK5C75e7V3CDyty",
      "outNum": 0,
      "inNum": 121
    }
  ],
  "refreshTimeInfo": {
    "timeToRefresh": 88200,
    "lastUpdateTime": "1680568641"
  }
}
```

---

## Get distribution of total market capitalization

Returns the balance distribution of all major stablecoins (USDT, USDC, TUSD, USDD, USDJ) across categories: Wallet, JustLend, SunSwap, SunCurve, and Other.

```
GET https://apilist.tronscanapi.com/api/stableCoin/holder/balance/overview
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/holder/balance/overview) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "data": [
    {
      "tokenAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "tokenName": "USDT",
      "decimal": 6,
      "statistic": [
        { "balance": "43809021504206608.0", "tokenName": "USDT", "category": "Wallet"   },
        { "balance": "161485597177868.0",   "tokenName": "USDT", "category": "JustLend" },
        { "balance": "93066779819482.0",    "tokenName": "USDT", "category": "SunSwap"  },
        { "balance": "28677547345688",      "tokenName": "USDT", "category": "SunCurve" },
        { "balance": "32839586001460.0",    "tokenName": "USDT", "category": "Other"    }
      ]
    },
    {
      "tokenAddress": "TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8",
      "tokenName": "USDC",
      "decimal": 6,
      "statistic": [
        { "balance": "490118517077022.0", "tokenName": "USDC", "category": "Wallet"   },
        { "balance": "2323284928085",     "tokenName": "USDC", "category": "JustLend" },
        { "balance": "5407502175133.0",   "tokenName": "USDC", "category": "SunSwap"  },
        { "balance": "733545818351.0",    "tokenName": "USDC", "category": "SunCurve" },
        { "balance": "6878671191409.0",   "tokenName": "USDC", "category": "Other"    }
      ]
    }
  ],
  "refreshTimeInfo": {
    "type": "realtime",
    "lastUpdateTime": 1680594293
  }
}
```

---

## Get chart of the number of accounts held (stablecoin holder change)

Returns daily stablecoin holder counts per token and the aggregate total over time.

```
GET https://apilist.tronscanapi.com/api/stableCoin/holder/change?startDay=2023-02-12
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/holder/change?startDay=2023-02-12) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `startDay` | Start date. Format: `yyyy-MM-dd` |
| `endDay` | End date. Format: `yyyy-MM-dd` |

### Response

```
{
  "statistics": [
    {
      "date": 1680307200,
      "aggrHolder": "22937264",
      "category": [
        { "tokenName": "USDT", "tokenAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t", "holderNum": "22108346", "date": "2023-04-01" },
        { "tokenName": "USDD", "tokenAddress": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn", "holderNum": "130780",   "date": "2023-04-01" },
        { "tokenName": "TUSD", "tokenAddress": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4", "holderNum": "309639",   "date": "2023-04-01" },
        { "tokenName": "USDC", "tokenAddress": "TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8", "holderNum": "369013",   "date": "2023-04-01" },
        { "tokenName": "USDJ", "tokenAddress": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT", "holderNum": "19486",    "date": "2023-04-01" }
      ]
    }
  ],
  "latest": [
    { "tokenAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t", "tokenName": "USDT", "holderNum": 22128346 },
    { "tokenAddress": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn", "tokenName": "USDD", "holderNum": 130779   },
    { "tokenAddress": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4", "tokenName": "TUSD", "holderNum": 309650   },
    { "tokenAddress": "TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8", "tokenName": "USDC", "holderNum": 369044   },
    { "tokenAddress": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT", "tokenName": "USDJ", "holderNum": 19487    }
  ],
  "totalHolder": "22957306"
}
```

---

## Get the transfer quantity of a TRC20 token held by an account

Returns the transfer-in and transfer-out quantity of a specific TRC20 token for a given account.

```
GET https://apilist.tronscanapi.com/api/deep/account/holderToken/basicInfo/trc20/transfer?accountAddress=TRxvWuBAkQgV2XCfVfkykYBzKe4vS4Kqsh&tokenAddress=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/deep/account/holderToken/basicInfo/trc20/transfer?accountAddress=TRxvWuBAkQgV2XCfVfkykYBzKe4vS4Kqsh&tokenAddress=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `accountAddress` | Account address to query |
| `tokenAddress` | TRC20 token contract address |

### Response

```
{
  "transferIn": 0,
  "transferOut": 0
}
```

---

## Get list of transactions involving liquidity

Returns a list of liquidity transactions (add/remove/exchange) filtered by various criteria.

The maximum interval between `startTimestamp` and `endTimestamp` is **60 days**. If `endTimestamp` exceeds the current time, `startTimestamp` is automatically set to 60 days before `endTimestamp`.

```
GET https://apilist.tronscanapi.com/api/deep/stableCoin/liquidity/transaction?token=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&project=sunswap&type=AddLiquidity&operator=TLnW8ZBqqTPweLyKHpg1LGNj2v9kx8N3rh&startTimestamp=1680503760000
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/deep/stableCoin/liquidity/transaction?token=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&project=sunswap&type=AddLiquidity&operator=TLnW8ZBqqTPweLyKHpg1LGNj2v9kx8N3rh&startTimestamp=1680503760000) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `sort` | Sorting method: `timestamp`, `value`, or `tokenValue`. Prefix with `-` for descending order |
| `minValue` | Minimum total USD value. Default: `1000` |
| `maxValue` | Maximum total USD value. Default: no upper limit |
| `type` | Liquidity operations: `AddLiquidity`, `RemoveLiquidity`, `TokenExchange`. Default: all. Multiple values separated by commas |
| `operator` | Filter by operator address |
| `startTimestamp` | Start timestamp in milliseconds. Default: 60 days before current time |
| `endTimestamp` | End timestamp in milliseconds |
| `token` | Filter by token address. Multiple tokens separated by commas |
| `pool` | Filter by liquidity pool address |
| `project` | `sunswap` or `suncurve` |
| `influence` | Impact on a specific token. `+` for increase, `-` for decrease |
| `minTokenValue` | Minimum value for a single token filter |
| `maxTokenValue` | Maximum value for a single token filter |

### Response

```
{
  "total": 1,
  "data": [
    {
      "project": "SunSwap",
      "type": "AddLiquidity",
      "value": "2583.3694",
      "operation": [
        {
          "tokenId": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
          "tokenName": "Tether USD",
          "tokenAbbr": "USDT",
          "tokenDecimal": 6,
          "tokenAmount": "1293.684385",
          "tokenValue": "1293.7082"
        },
        {
          "tokenId": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
          "tokenName": "TrueUSD",
          "tokenAbbr": "TUSD",
          "tokenDecimal": 18,
          "tokenAmount": "1290.0",
          "tokenValue": "1289.6612"
        }
      ],
      "operator": "TLnW8ZBqqTPweLyKHpg1LGNj2v9kx8N3rh",
      "dateCreated": 1680503760000,
      "hash": "6d0fb572aabb5b2a0187a173c81b17fba2139f23b7901dc973d3df460c485a1d"
    }
  ],
  "refreshTimeInfo": {
    "type": "realtime",
    "lastUpdateTime": 1680507417
  }
}
```

---

## Get all tags of an account

Returns all on-chain behavioral tags associated with an account, including asset, activity, DeFi, NFT, and governance categories.

```
GET https://apilist.tronscanapi.com/api/account/tag?address=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/account/tag?address=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Account address to query |

### Response

```
{
  "blueTag": "",
  "greyTag": "",
  "redTag": "",
  "publicTag": "",
  "chainTags": {
    "Assets": [
      { "tagName": "High Balance", "tagDesc": "Total assets over $10k" },
      { "tagName": "Whale",        "tagDesc": "Total assets over $1m"  }
    ],
    "Activity": [
      { "tagName": "Block Sale",    "tagDesc": "Have made large transactions over $10k"      },
      { "tagName": "High Activity", "tagDesc": "Over 100 transactions in the last 6 months"  }
    ],
    "DeFi": [
      { "tagName": "Lender on JustLend",         "tagDesc": "Have undrawn deposits at JustLend"    },
      { "tagName": "SunSwap Liquidity Provider",  "tagDesc": "Providing liquidity at SunSwap"       },
      { "tagName": "SUN Farming",                 "tagDesc": "Participating in farming at SUN.io"   },
      { "tagName": "SunCurve Liquidity Provider", "tagDesc": "Providing liquidity at SunCurve"      }
    ],
    "NFT": [
      { "tagName": "NFT Collector", "tagDesc": "Currently holding at least one NFT" }
    ],
    "Governance": [
      { "tagName": "TRX Governance", "tagDesc": "Participating in TRX staking" }
    ]
  },
  "refreshTimeInfo": {
    "type": "realtime",
    "lastUpdateTime": 1680507588
  }
}
```

---

## Get transfer amount change chart with a statistical period of 24 hours

Returns stablecoin transfer amounts over time, with optional line chart data per token.

```
GET https://apilist.tronscanapi.com/api/stableCoin/transferAmount
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/transferAmount) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `startTime` | Start time in seconds |
| `endTime` | End time in seconds |
| `type` | Set to `addLine` to include line chart data in response. Default: line chart excluded |

### Response

```
{
  "stableAmountLine": [
    {
      "tokenAbbr": "USDT",
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "lineData": [{ "t": 1680393600000, "v": 5385970884.857 }]
    },
    {
      "tokenAbbr": "USDC",
      "contractAddress": "TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8",
      "lineData": [{ "t": 1680393600000, "v": 56155327.430 }]
    },
    {
      "tokenAbbr": "TUSD",
      "contractAddress": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
      "lineData": [{ "t": 1680393600000, "v": 7755550.490 }]
    },
    {
      "tokenAbbr": "USDD",
      "contractAddress": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn",
      "lineData": [{ "t": 1680393600000, "v": 1136777.229 }]
    },
    {
      "tokenAbbr": "USDJ",
      "contractAddress": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT",
      "lineData": [{ "t": 1680393600000, "v": 338142.765 }]
    }
  ],
  "stableAmount24h": [
    { "amount24h": 5385970884.857, "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t", "tokenAbbr": "USDT" },
    { "amount24h": 56155327.430,   "contractAddress": "TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8", "tokenAbbr": "USDC" },
    { "amount24h": 7755550.490,    "contractAddress": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4", "tokenAbbr": "TUSD" },
    { "amount24h": 1136777.229,    "contractAddress": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn", "tokenAbbr": "USDD" },
    { "amount24h": 338142.765,     "contractAddress": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT", "tokenAbbr": "USDJ" }
  ]
}
```

---

## Get the chart of the top holders of stablecoins

Returns the top 50 stablecoin holders with their USDT, USDC, USDD, TUSD, and USDJ balances.

```
GET https://apilist.tronscanapi.com/api/stableCoin/holder/top
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/holder/top) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `viewContract` | Whether to include contract data. `1`: include. `2`: exclude |
| `sort` | Sort field: `USDT`, `USDC`, `USDJ`, `USDD`, or `TUSD` |
| `direction` | Sort direction. `1`: ascending. `2`: descending |

### Response

```
{
  "total": 50,
  "data": [
    {
      "address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
      "addressType": 1,
      "accountTag": "Binance-Cold 2",
      "usdtAmount": 9873632775.224686,
      "tusdAmount": 1244717298.236131619743863419,
      "usddAmount": 0.000431736076562944,
      "usdcAmount": 61665303.553071
    },
    {
      "address": "TMuA6YqfCeX8EhbfYEg5y7S4DqzSJireY9",
      "addressType": 1,
      "accountTag": "Binance-Cold 1",
      "usdtAmount": 3999368107.604717,
      "usddAmount": 0.000264701265386571
    },
    {
      "address": "TKHuVq1oKVruCGLvqVexFs6dawKv6fQgFs",
      "addressType": 1,
      "accountTag": "Tether Treasury",
      "usdtAmount": 962565110.636746,
      "usddAmount": 0.000177042212446563
    }
  ],
  "refreshTimeInfo": {
    "type": "realtime",
    "lastUpdateTime": 1680510563
  }
}
```

---

## Get basic information of the stable currency pool

Returns pool composition, TVL, 24h volume, and per-token liquidity percentages for a specific pool.

```
GET https://apilist.tronscanapi.com/api/stableCoin/pool/overview?pool=TKcEU8ekq2ZoFzLSGFYCUY6aocJBX9X31b
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/pool/overview?pool=TKcEU8ekq2ZoFzLSGFYCUY6aocJBX9X31b) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `pool` | Contract address of the pool to query |

### Response

```
{
  "tokens": [
    {
      "tokenId": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT",
      "tokenAbbr": "USDJ",
      "tokenName": "JUST Stablecoin",
      "tokenDecimal": 18,
      "tokenType": "trc20",
      "vip": true,
      "liquidity": "237607.7104",
      "liquidityPercent": "0.068796"
    },
    {
      "tokenId": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
      "tokenAbbr": "TUSD",
      "tokenName": "TrueUSD",
      "tokenDecimal": 18,
      "tokenType": "trc20",
      "vip": true,
      "liquidity": "1605100.6987",
      "liquidityPercent": "0.464733"
    },
    {
      "tokenId": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "tokenAbbr": "USDT",
      "tokenName": "Tether USD",
      "tokenDecimal": 6,
      "tokenType": "trc20",
      "vip": true,
      "liquidity": "1611101.2545",
      "liquidityPercent": "0.466471"
    }
  ],
  "volume24Hours": "1430692.368843",
  "tvl": "3453429.9181",
  "poolUrl": "https://sun.io/?lang=en-US#/3pool",
  "refreshTimeInfo": {
    "timeToRefresh": 3900,
    "lastUpdateTime": "1680509735"
  }
}
```

---

## Get large transactions of stablecoins

Returns large stablecoin transactions filtered by type, amount, address, and time.

```
GET https://apilist.tronscanapi.com/api/deep/stableCoin/bigAmount?limit=2&types=0
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/deep/stableCoin/bigAmount?limit=2&types=0) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Filter by address |
| `txUsd` | Transaction value range in USD, separated by commas. e.g. `1,10` |
| `txAmount` | Transaction amount range, separated by commas. e.g. `100,10000` |
| `relatedAddress` | Filter by related address |
| `relatedToken` | Filter by related token |
| `startTime` | Start time in seconds |
| `endTime` | End time in seconds |
| `limit` | Max: `50` |
| `types` | Transfer type, separated by commas. `0`: all. `1`: transfer-in. `2`: transfer-out. `3`: exchange. `4`: add liquidity. `5`: remove liquidity. `6`: deposit. `7`: loan. `8`: repayment. `9`: withdraw money |
| `sortBy` | Sorted field: `time`, `amount`, `usd` (total value) |
| `asc` | `true` or `false` |

### Response

```
{
  "total": 17248681,
  "code": 0,
  "data": [
    {
      "amount": 11000.0,
      "amountUsd": 11001.839364,
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "dateTime": 1680479976000,
      "fromAddress": "TC9jeJeGwHYXjSXkf1JR6WA6kuLzQeLPKD",
      "fromAddressTag": "TC9jeJeGwHYXjSXkf1JR6WA6kuLzQeLPKD",
      "toAddress": "TJsxVp1hGbt4U5gGHfdfXjnL9pVbsxpk66",
      "toAddressTag": "TJsxVp1hGbt4U5gGHfdfXjnL9pVbsxpk66",
      "hash": "07af6a299e0b7a62c39acd06bde1053cb28faf853750dcedac1866603c1cd371",
      "transferType": "1"
    },
    {
      "amount": 63640.0,
      "amountUsd": 63650.641555,
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "dateTime": 1680479976000,
      "fromAddress": "TFZ57tTAJBR1f6KZj97mXYB7iUJUGxp9pn",
      "fromAddressTag": "TFZ57tTAJBR1f6KZj97mXYB7iUJUGxp9pn",
      "toAddress": "TCdep4hMANtJfHWts31tcWWDEzUEFHNxKA",
      "toAddressTag": "TCdep4hMANtJfHWts31tcWWDEzUEFHNxKA",
      "hash": "42bba7828f169232b3c60063b212221c125a483d3dde5eeead90c6e693a05849",
      "transferType": "1"
    }
  ],
  "refreshTimeInfo": {
    "timeToRefresh": 88200,
    "lastUpdateTime": "1680481089"
  }
}
```

---

## Get a graph of all stablecoin issuance changes

Returns the total supply change trend for all stablecoins over a specified time range.

```
GET https://apilist.tronscanapi.com/api/stableCoin/totalSupply/change
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/totalSupply/change) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `startTime` | Start time in seconds |
| `endTime` | End time in seconds |

### Response

```
{
  "data": [
    {
      "date": "2023-04-03",
      "tokenName": "USDT",
      "totalSupply": "44125091014551106",
      "increaseSupply": "500000000000",
      "destroySupply": "0"
    }
  ]
}
```

---

## Get key events of TRON stablecoin

Returns key smart contract events (e.g. mint, burn, blacklist additions) for TRON stablecoins.

```
GET https://apilist.tronscanapi.com/api/deep/stableCoin/totalSupply/keyEvents?limit=10&direction=1&sort=1&start=1
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/deep/stableCoin/totalSupply/keyEvents?limit=10&direction=1&sort=1&start=1) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start index |
| `limit` | Number of results |
| `sort` | Sorting: `1`: by quantity. `2`: by time |
| `operatorAddress` | Filter by operator address |
| `direction` | `1`: ascending. `2`: descending |
| `startTime` | Start time |
| `endTime` | End time |
| `startAmount` | Minimum amount filter |
| `endAmount` | Maximum amount filter |
| `USDT` | Key events for USDT, multiple events separated by commas |
| `USDC` | Key events for USDC, multiple events separated by commas |
| `USDD` | Key events for USDD, multiple events separated by commas |
| `USDJ` | Key events for USDJ, multiple events separated by commas |
| `TUSD` | Key events for TUSD, multiple events separated by commas |

### Response

```
{
  "total": 96539,
  "data": [
    {
      "tokenName": "USDT",
      "tokenAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "eventName": "AddedBlackList",
      "count": "0.0",
      "operatorAddress": "TRLi4KskHxfACnxKzLrf2wNHauWUQpwziN",
      "time": "1674226986000",
      "hash": "1517cc610a8868903ac0aca0742b81a8e9db48ce1fc6a346b5fafece886c4562"
    },
    {
      "tokenName": "USDJ",
      "tokenAddress": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT",
      "eventName": "LogSetOwner",
      "count": "0.0",
      "operatorAddress": "TJ9JS5iALDDP89kwYqJd4eaWcoQneobLU5",
      "time": "1670749374000",
      "hash": "ec7257c313b9d4f81ce5f09c44d988581aac2d14acdb233fd1eda4fcf6a4ccdf"
    }
  ],
  "refreshTimeInfo": {
    "type": "realtime",
    "lastUpdateTime": 1680512082
  }
}
```

---

## Get the total circulation of all stablecoins

Returns the current total supply for USDT, USDD, TUSD, USDC, and USDJ.

```
GET https://apilist.tronscanapi.com/api/stableCoin/totalSupply
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/totalSupply) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "data": [
    { "tokenName": "USDT", "address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t", "totalSupply": "44125091014551106",          "tokenDecimal": 6  },
    { "tokenName": "USDD", "address": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn", "totalSupply": "725332035842248000000000000",   "tokenDecimal": 18 },
    { "tokenName": "TUSD", "address": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4", "totalSupply": "1304918613500000000000000000", "tokenDecimal": 18 },
    { "tokenName": "USDC", "address": "TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8", "totalSupply": "513902529550000",               "tokenDecimal": 6  },
    { "tokenName": "USDJ", "address": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT", "totalSupply": "273145279475423432037979793",   "tokenDecimal": 18 }
  ],
  "refreshTimeInfo": {
    "type": "realtime",
    "lastUpdateTime": 1680513319
  }
}
```

---

## Get all stablecoin liquidity pool information

Returns a list of all stablecoin liquidity pools with their TVL, constituent tokens, and pool names.

```
GET https://apilist.tronscanapi.com/api/stableCoin/pool/info
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/pool/info) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
[
  {
    "poolAddress": "TNTfaTpkdd4AQDeqr8SGG7tgdkdjdhbP5c",
    "poolName": "2pool",
    "tvl": "55851695.9987",
    "tokens": [
      {
        "tokenId": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn",
        "tokenAbbr": "USDD",
        "tokenName": "Decentralized USD",
        "tokenDecimal": 18,
        "tokenType": "trc20",
        "vip": true
      },
      {
        "tokenId": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
        "tokenAbbr": "USDT",
        "tokenName": "Tether USD",
        "tokenDecimal": 6,
        "tokenType": "trc20",
        "vip": true
      }
    ]
  }
]
```

---

## Get a list of all blacklist transactions

Returns transactions where addresses were added to or removed from the stablecoin blacklist.

```
GET https://apilist.tronscanapi.com/api/stableCoin/blackList
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/blackList) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `tokenAddress` | Filter by stablecoin contract address |
| `blackAddress` | Filter by blacklisted address |
| `sort` | `1`: by quantity. `2`: by time |
| `direction` | `1`: ascending. `2`: descending |
| `start` | Start index |
| `limit` | Number of results |

### Response

```
{
  "total": 513,
  "data": [
    {
      "blackAddress": "TNmk2SAgpFu2xEKHEuyJrSrMTBweSuUVBu",
      "tokenName": "USDT",
      "num": "0",
      "time": 1665081543,
      "transHash": "d3fb3cf3e422f7a85b11e8f0ac927b9097604a178cacc1abf9a169febccaf410",
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
    },
    {
      "blackAddress": "TSvQBQVm6ZVQFQdSZqg2KGbpjtJ8h4fPFd",
      "tokenName": "USDT",
      "num": "0",
      "time": 1665081918,
      "transHash": "ad2be9ae507dbc504372de1f959284cdaa10aeb66e11d8b7c625b1791aba1dfb",
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
    }
  ]
}
```

---

## Obtain a graph of changes in holdings of a stablecoin

Returns a chart showing how the holder distribution of a stablecoin has changed over time across categories (exchange, wallet, contract).

```
GET https://apilist.tronscanapi.com/api/stableCoin/distribution/change?token=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/distribution/change?token=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `token` | Stablecoin contract address |

### Response

```
{
  "data": [
    {
      "date": "2023-04-03",
      "exchange": "0.46828375",
      "wallet": "0.52457996",
      "contract": "0.00713629"
    }
  ]
}
```

---

## Obtain the basic information of a token held by an account

Returns the holding amount, first hold time, wallet/project breakdown, and latest transfer time for a token held by an account.

```
GET https://apilist.tronscanapi.com/api/account/holderToken/basicInfo?tokenAddress=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&accountAddress=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/account/holderToken/basicInfo?tokenAddress=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&accountAddress=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `accountAddress` | Account address to query |
| `tokenAddress` | TRC20 address or TRC10 token ID. Set to `0` for TRX |

### Response

```
{
  "data": {
    "holdCount": "156528709608684.000000",
    "holdAmount": 156551611.113586,
    "firstHoldTime": 1622123499,
    "latestTransferTime": 1680511902,
    "tokenDecimal": 6,
    "walletValue": "9845557.885079",
    "walletRatio": "0.062890",
    "projectValue": "146706053.228507",
    "projectRatio": "0.937110",
    "projects": [
      { "name": "wallet",       "value": 9845557.885079,   "ratio": "0.062890" },
      { "name": "JustLend DAO", "value": "146706053.2285", "ratio": "0.937110" }
    ],
    "projectNum": 2
  },
  "refreshTimeInfo": {
    "type": "realtime",
    "lastUpdateTime": 1680514013
  }
}
```

---

## Get the distribution of holders of a stablecoin

Returns detailed holder distribution across exchanges, wallets, and DeFi protocols (JustLend, SunSwap, SunCurve, etc.).

```
GET https://apilist.tronscanapi.com/api/stableCoin/distribution?token=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/distribution?token=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `token` | Stablecoin contract address |

### Response

```
{
  "addresses": {
    "exchange": {
      "data": [
        { "address": "Binance",  "percent": "0.44515271", "value": "19642403643836642" },
        { "address": "KuCoin",   "percent": "0.00698337", "value": "308141828261099"   },
        { "address": "Kraken",   "percent": "0.00448365", "value": "197841498897643"   },
        { "address": "Bitfinex", "percent": "0.00294634", "value": "130007587022640"   },
        { "address": "Okex",     "percent": "0.00116254", "value": "51297265458110"    }
      ],
      "percent": "0.46828375",
      "value": "20663063072655609.0"
    },
    "otherAccount": {
      "data": [
        { "address": "TKHuVq1oKVruCGLvqVexFs6dawKv6fQgFs", "percent": "0.02181427", "value": "962556714046129" }
      ],
      "percent": "0.52457996",
      "value": "23147138633971927.0"
    }
  },
  "contract": {
    "JustLend":      { "percent": "0.00365885", "value": "161446940798547.0" },
    "SunSwap":       { "percent": "0.00209795", "value": "92572067643057.0"  },
    "SunCurve":      { "percent": "0.00064664", "value": "28532995861673"    },
    "otherContract": { "percent": "0.00073286", "value": "32337303620293.0"  }
  },
  "tokenName": "Tether USD",
  "tokenAbbr": "USDT",
  "tokenDecimal": 6,
  "refreshTimeInfo": {
    "timeToRefresh": 5400,
    "lastUpdateTime": "1680512709"
  }
}
```

---

## Get the asset value chart of a token in an account

Returns daily price, balance, and USD value for a token held by an account over time.

```
GET https://apilist.tronscanapi.com/api/account/holderToken/asset/valueInfo?startTime=1680364800000&accountAddress=TRxvWuBAkQgV2XCfVfkykYBzKe4vS4Kqsh&tokenAddress=0
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/account/holderToken/asset/valueInfo?startTime=1680364800000&accountAddress=TRxvWuBAkQgV2XCfVfkykYBzKe4vS4Kqsh&tokenAddress=0) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `accountAddress` | Account address to query |
| `tokenAddress` | TRC20 address or TRC10 token ID. Set to `0` for TRX |
| `startTime` | Start time in milliseconds |
| `endTime` | End time in milliseconds |

### Response

```
{
  "data": [
    {
      "date": "2023-04-01",
      "statistics": {
        "date": "2023-04-01",
        "balance": "137634221",
        "price": "0.06645341943116789",
        "value": "9.146265"
      }
    },
    {
      "date": "2023-04-02",
      "statistics": {
        "date": "2023-04-02",
        "balance": "137634221",
        "price": "0.06587720099451715",
        "value": "9.066957"
      }
    }
  ],
  "tokenDecimal": 6
}
```

---

## Obtain the balance flow of the asset value of a token in an account

Returns the balance change flow (inflows and outflows) for a token in an account up to a specified end time.

```
GET https://apilist.tronscanapi.com/api/account/holderToken/asset/changeBalance?accountAddress=TRxvWuBAkQgV2XCfVfkykYBzKe4vS4Kqsh&tokenAddress=0&endTime=1680364800000
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/account/holderToken/asset/changeBalance?accountAddress=TRxvWuBAkQgV2XCfVfkykYBzKe4vS4Kqsh&tokenAddress=0&endTime=1680364800000) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `accountAddress` | Account address to query |
| `tokenAddress` | TRC20 address or TRC10 token ID. Set to `0` for TRX |
| `endTime` | End time in milliseconds |

### Response

```
{
  "data": [
    {
      "date": "2023-04-02",
      "inflow": "5000000",
      "outflow": "2000000",
      "balance": "137634221"
    }
  ],
  "tokenDecimal": 6
}
```

---

## Obtain a trend chart of the circulation of a certain stablecoin

Returns the total supply, mint amount, and burn amount per day for a specific stablecoin.

Supported stablecoins: **USDD**, **USDC**, **USDJ**, **TUSD**

```
GET https://apilist.tronscanapi.com/api/stableCoin/tokenSupply/turnover?startTime=1680278400&tokenAddress=TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/tokenSupply/turnover?startTime=1680278400&tokenAddress=TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `startTime` | Start time in seconds |
| `endTime` | End time in seconds |
| `tokenAddress` | Stablecoin contract address |

### Response

```
{
  "statistics": [
    {
      "date": "2023-04-02",
      "totalSupply": 273145279475423432037979793,
      "increaseSupply": "0",
      "destroySupply": "0"
    },
    {
      "date": "2023-04-01",
      "totalSupply": 273145279475423432037979793,
      "increaseSupply": "0",
      "destroySupply": "0"
    }
  ],
  "tokenDecimal": 18
}
```

---

## Obtain information on the trend of liquidity pool changes

Returns a Sankey-diagram-style data structure showing how liquidity has flowed in and out of a pool between two time points.

`startTimstamp` must be later than **2022-11-21 08:00:00** and `endTimestamp` must be earlier than the current time.

```
GET https://apilist.tronscanapi.com/api/stableCoin/pool/trend?pool=TQx6CdLHqjwVmJ45ecRzodKfVumAsdoRXH
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/pool/trend?pool=TQx6CdLHqjwVmJ45ecRzodKfVumAsdoRXH) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `startTimstamp` | Start timestamp in milliseconds. Must be later than 2022-11-21 08:00:00 |
| `endTimestamp` | End timestamp in milliseconds. Must be earlier than current time |
| `pool` | Liquidity pool contract address |

### Response

```
{
  "data": [
    { "name": "in" },
    { "name": "out" },
    { "name": "USDC 2022-11-22", "value": "591349.5137" },
    { "name": "USDC 2023-04-02" },
    { "name": "3SUN 2022-11-22", "value": "425478.2888" },
    { "name": "3SUN 2023-04-02" }
  ],
  "links": [
    { "source": "USDC 2022-11-22", "target": "USDC 2023-04-02", "value": "1150523.9396" },
    { "source": "in",              "target": "USDC 2023-04-02", "value": "92.4864"      },
    { "source": "USDC 2022-11-22", "target": "3SUN 2023-04-02", "value": "416297.7966"  },
    { "source": "in",              "target": "3SUN 2023-04-02", "value": "10.0169"       }
  ],
  "refreshTimeInfo": {
    "timeToRefresh": 36300,
    "lastUpdateTime": "1680515730"
  }
}
```

---

## Obtain the liquidity change graph of the liquidity pool

Returns the liquidity change history for a specific pool address.

```
GET https://apilist.tronscanapi.com/api/stableCoin/pool/change?pool=TKVsYedAY23WFchBniU7kcx1ybJnmRSbGt
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/pool/change?pool=TKVsYedAY23WFchBniU7kcx1ybJnmRSbGt) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `pool` | Liquidity pool contract address |

### Response

```
{
  "data": [
    {
      "date": "2023-04-03",
      "liquidity": "3453429.9181",
      "addLiquidity": "50000.00",
      "removeLiquidity": "10000.00"
    }
  ]
}
```

---

## Obtain basic information on stablecoins

Returns market cap, holder count, total supply, 24h transfer count, and 24h liquidity data for a specific stablecoin.

```
GET https://apilist.tronscanapi.com/api/stableCoin/overview?tokenAddress=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/overview?tokenAddress=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `tokenAddress` | Stablecoin contract address |

### Response

```
{
  "data": {
    "marketCap": "44110731044.538503",
    "holderCnt": "22149409",
    "supply": "44125091014.551106",
    "transferCntIn24h": "2688823",
    "transferCntIn24hChange": "0.531773",
    "liquidityIn24h": "244242750.2350",
    "liquidityIn24hChange": "-0.000660"
  },
  "refreshTimeInfo": {
    "type": "realtime",
    "lastUpdateTime": 1680517235
  }
}
```

---

## Obtain the distribution of the stablecoin liquidity pool

Returns all liquidity pools (SunSwap v1/v2, SunCurve) containing a specific stablecoin, with TVL and token compositions.

```
GET https://apilist.tronscanapi.com/api/stableCoin/tvl?token=TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/tvl?token=TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `token` | Stablecoin contract address |

### Response

```
{
  "sunswapv1": [
    {
      "liquidity": "14583756.5482",
      "poolAddress": "TQcia2H2TU3WrFk9sKtdK9qCfkW8XirfPQ",
      "poolName": "V1-USDJ-TRX",
      "project": "SunSwap",
      "tokens": [
        {
          "tokenId": "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT",
          "tokenAbbr": "USDJ",
          "tokenName": "JUST Stablecoin",
          "tokenDecimal": 18,
          "tokenType": "trc20",
          "vip": true
        },
        {
          "tokenId": "_",
          "tokenAbbr": "trx",
          "tokenName": "TRX",
          "tokenDecimal": 6,
          "tokenType": "trc10",
          "vip": true
        }
      ]
    }
  ]
}
```

---

## Obtain account transfer-in and transfer-out fund distribution

Returns an aggregated breakdown of inbound and outbound fund flows for a specific account.

```
GET https://apilist.tronscanapi.com/api/deep/account/transferAmount?address=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5&limit=10
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/deep/account/transferAmount?address=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5&limit=10) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Account address to query |
| `startTime` | Start time in seconds |
| `endTime` | End time in seconds |
| `direction` | Transfer type. `0`: all. `1`: transfer-in. `2`: transfer-out |
| `relatedToken` | Filter by related token |
| `sortBy` | Sorted field: `amountIn`, `amountOut`, `timesIn`, `timesOut` |
| `limit` | Number of results |

### Response

```
{
  "total": 4,
  "code": 0,
  "data": [
    {
      "inAmountUsd": 3130784970.9059763,
      "outAmountUsd": 0,
      "address": "TKHuVq1oKVruCGLvqVexFs6dawKv6fQgFs",
      "addressTag": "Tether Treasury",
      "outNum": 0,
      "inNum": 117
    },
    {
      "inAmountUsd": 1721903345.260201,
      "outAmountUsd": 0,
      "address": "TTd9qHyjqiUkfTxe3gotbuTMpjU8LEbpkN",
      "addressTag": "Kraken",
      "outNum": 0,
      "inNum": 169
    }
  ]
}
```

---

## Get large transactions

Returns large transactions for a specific account, filtered by token, type, and amount.

```
GET https://apilist.tronscanapi.com/api/deep/account/token/bigAmount?address=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5&relatedToken=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&types=4
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/deep/account/token/bigAmount?address=TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5&relatedToken=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&types=4) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Account address to query |
| `txUsd` | Transaction value range in USD, separated by commas. e.g. `1,10` |
| `txAmount` | Transaction amount range, separated by commas. e.g. `100,10000` |
| `relatedAddress` | Filter by related address |
| `relatedToken` | Filter by related token address |
| `startTime` | Start time in seconds |
| `endTime` | End time in seconds |
| `limit` | Number of results |
| `types` | Transfer type, separated by commas. `0`: all. `1`: transfer-in. `2`: transfer-out. `3`: exchange. `4`: add liquidity. `5`: remove liquidity. `6`: deposit. `7`: loan. `8`: repayment. `9`: withdraw money |
| `sortBy` | Sorted field: `time`, `amount`, `usd` (total value) |
| `asc` | `true` or `false` |

### Response

```
{
  "total": 17248681,
  "code": 0,
  "data": [
    {
      "amount": 63640.0,
      "amountUsd": 63650.641555,
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "dateTime": 1680479976000,
      "fromAddress": "TFZ57tTAJBR1f6KZj97mXYB7iUJUGxp9pn",
      "fromAddressTag": "TFZ57tTAJBR1f6KZj97mXYB7iUJUGxp9pn",
      "toAddress": "TCdep4hMANtJfHWts31tcWWDEzUEFHNxKA",
      "toAddressTag": "TCdep4hMANtJfHWts31tcWWDEzUEFHNxKA",
      "hash": "42bba7828f169232b3c60063b212221c125a483d3dde5eeead90c6e693a05849",
      "transferType": "1"
    }
  ],
  "refreshTimeInfo": {
    "timeToRefresh": 88200,
    "lastUpdateTime": "1680481089"
  }
}
```

---

## Chart of the number of accounts held and balance overview

Returns stablecoin balance distribution across holder categories (Wallet, JustLend, SunSwap, SunCurve, Other) for all major stablecoins.

```
GET https://apilist.tronscanapi.com/api/stableCoin/holder/balance/overview
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stableCoin/holder/balance/overview) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "data": [
    {
      "tokenAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "tokenName": "USDT",
      "decimal": 6,
      "statistic": [
        { "balance": "43809021504206608.0", "tokenName": "USDT", "category": "Wallet"   },
        { "balance": "161485597177868.0",   "tokenName": "USDT", "category": "JustLend" },
        { "balance": "93066779819482.0",    "tokenName": "USDT", "category": "SunSwap"  },
        { "balance": "28677547345688",      "tokenName": "USDT", "category": "SunCurve" },
        { "balance": "32839586001460.0",    "tokenName": "USDT", "category": "Other"    }
      ]
    }
  ],
  "refreshTimeInfo": {
    "type": "realtime",
    "lastUpdateTime": 1680594293
  }
}
```