

# Statistics

## Get contract Energy consumption Data

Returns the contract’s Energy statistic data.

```
GET https://apilist.tronscanapi.com/api/energydailystatistic?limit=10&day=1680502490593
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/energydailystatistic?limit=10&day=1680502490593) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `day` | Current timestamp, accurate to milliseconds |
| `limit` | Number of items. Default: `10`. Max: `100` |

### Response

```
{
  "totalTrigger": 2438075,
  "totalCallerAmount": 594027,
  "totalEnergy": 94584946069,
  "total": 4739,
  "data": [
    {
      "contract_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "total_energy": 87064374864,
      "energy": 43402672527,
      "contract_supplied": 67499322,
      "trx": 43594203015,
      "tag1": "USDT Token",
      "tag1Url": "https://tron.network/usdt",
      "vip": true,
      "name": "TetherToken",
      "total_energy_percent": 0.92
    },
    {
      "contract_address": "TCb1jjfKYZkNWqNn2XYSDmYHCroWSQ8MJg",
      "total_energy": 922333833,
      "energy": 88381347,
      "contract_supplied": 0,
      "trx": 833952486,
      "tag1": "",
      "tag1Url": "",
      "vip": false,
      "name": "",
      "total_energy_percent": 0.01
    }
  ]
}
```

---

## Get Energy consumption distribution

Returns the contract’s Energy consumption distribution in a period.

```
GET https://apilist.tronscanapi.com/api/energystatistic
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/energystatistic) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start_timestamp` | Start timestamp, accurate to milliseconds |
| `end_timestamp` | End timestamp, accurate to milliseconds |
| `size` | Number of items. Max: `1000` |
| `type` | Statistic type. `0`: by day. `1`: by month. `2`: by quarter |

### Response

```
{
  "total": 2,
  "max": {
    "day": "2023-04-03",
    "total_energy": 94584946069,
    "energy": 45647460262,
    "contract_supplied": 432831626,
    "trx": 48504654181,
    "energy_ration": "0.4826",
    "contract_supplied_ration": "0.0046",
    "trx_ration": "0.5128"
  },
  "min": {
    "day": "2023-04-02",
    "total_energy": 75783855423,
    "energy": 37857994437,
    "contract_supplied": 531969952,
    "trx": 37393891034,
    "energy_ration": "0.4996",
    "contract_supplied_ration": "0.0070",
    "trx_ration": "0.4934"
  },
  "data": [
    {
      "day": "2023-04-02",
      "total_energy": 75783855423,
      "energy": 37857994437,
      "contract_supplied": 531969952,
      "trx": 37393891034,
      "energy_ration": "0.4996",
      "contract_supplied_ration": "0.0070",
      "trx_ration": "0.4934"
    },
    {
      "day": "2023-04-03",
      "total_energy": 94584946069,
      "energy": 45647460262,
      "contract_supplied": 432831626,
      "trx": 48504654181,
      "energy_ration": "0.4826",
      "contract_supplied_ration": "0.0046",
      "trx_ration": "0.5128"
    }
  ],
  "avg_consume_energy": "79678910056",
  "yesterday_energy_ratio": "0.483"
}
```

---

## Get top 10 statistic data

Returns top statistic data, including overview, accounts, tokens, contracts, and resources.

```
GET https://apilist.tronscanapi.com/api/top10?type=0&time=1
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/top10?type=0&time=1) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `time` | Time type. `0`: realtime. `1`: latest one hour. `2`: recent 24 hours. `3`: last week |
| `type` | Statistic data type. Value range: `0`–`17`. `0`: Overview `1`: Top accounts by total TRX sent `2`: Top accounts by TRX sending transactions `3`: Top accounts by total TRX received `4`: Top accounts by TRX receiving transactions `5`: Top accounts by frozen TRX `6`: Top accounts by votes `7`: Top tokens by holders `8`: Top tokens by transaction accounts `9`: Top tokens by total transaction count `10`: Top tokens by total transaction amount `11`: Top contracts by total TRX balance `12`: Top contracts by calling accounts `13`: Top contracts by number of calls `14`: Top accounts by Energy consumption `15`: Top accounts by Bandwidth consumption `16`: Top contracts by Energy consumption `17`: Top contracts by fee consumption |

### Response

```
{
  "token_record": "94382",
  "last_week_trx_transaction_number": "29433470",
  "last_day_trx_transaction_number": "4651179",
  "whole_vote": "39302920408",
  "last_hour_token20_sum_transaction": "155632",
  "last_day_token20_sum_transaction": "2324334",
  "last_day_whole_energy_use": "46468052002",
  "last_day_energy_usage": "96414035761",
  "last_day_net_usage": "2371520986",
  "last_day_whole_fee_burn": "21446630442140",
  "trc20_record": "89449",
  "trc10_record": "4933",
  "whole_freeze": "40058302788.652379",
  "contract_whole_balance": "30233868822.263364"
}
```

---

## Get contract called distribution

Returns the contract calling distribution of a specific day.

```
GET https://apilist.tronscanapi.com/api/triggeramountstatistic?limit=10&day=1680520472549
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/triggeramountstatistic?limit=10&day=1680520472549) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `day` | Data time, accurate to milliseconds |
| `limit` | Number of items. Max: `100` |

### Response

```
{
  "totalTrigger": 2438075,
  "totalCallerAmount": 594027,
  "totalEnergy": 94584946069,
  "total": 4739,
  "data": [
    {
      "contract_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "trigger_amount": 2163377,
      "caller_amount": 570447,
      "call_value": 0,
      "tag1": "USDT Token",
      "tag1Url": "https://tron.network/usdt",
      "vip": true,
      "name": "TetherToken",
      "trigger_amount_percent": 0.89,
      "caller_amount_percent": 0.96
    },
    {
      "contract_address": "THk5qH79SoAaUnUh8JVdRarSESTZpqPjSQ",
      "trigger_amount": 171253,
      "caller_amount": 56,
      "call_value": 0,
      "tag1": "",
      "tag1Url": "",
      "vip": false,
      "name": "",
      "trigger_amount_percent": 0.07,
      "caller_amount_percent": 0
    }
  ]
}
```

---

## Get TVC of Tokens

Returns the token’s total value on chain.

```
GET https://apilist.tronscanapi.com/api/tokenTvc?startTime=1586140919
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/tokenTvc?startTime=1586140919) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `startTime` | Start time. Default: 7 days ago, accurate to seconds |
| `endTime` | End time. Default: current time, accurate to seconds |

### Response

```
{
  "tvcLine": [
    { "value": 59225146570.410398, "time": 1680393600 },
    { "value": 59198156552.065324, "time": 1680480000 },
    { "value": 59237133080.098487, "time": 1680566400 }
  ],
  "stableCoinCountOfTopTen": 4,
  "totalTokenNum": 32,
  "tokens": [
    {
      "abbr": "USDT",
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "name": "Tether USD",
      "tokenType": "trc20",
      "priceInUsd": 1.0000509265752244,
      "marketcap": 664547644954.4063,
      "nrOfTokenHolders": 22342422,
      "supply": 44125091014.551106,
      "vip": true
    },
    {
      "abbr": "TRON",
      "contractAddress": "_",
      "name": "TRX",
      "tokenType": "trc10",
      "priceInUsd": 0.06640206836839435,
      "marketcap": 90950052502.455472,
      "nrOfTokenHolders": 76694242,
      "supply": 90950052502.455472,
      "vip": true
    }
  ]
}
```

---

## Get statistic data of contract called

Returns the statistic data of contract calling in a specific period.

```
GET https://apilist.tronscanapi.com/api/contract_caller_statistic?start_timestamp=1679961600000&end_timestamp=1680595504531
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/contract_caller_statistic?start_timestamp=1679961600000&end_timestamp=1680595504531) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `startTime` | Start time. Default: 7 days ago, accurate to seconds |
| `endTime` | End time. Default: current time, accurate to seconds |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "caller_count": 594027,
      "trigger_count": 2438075
    }
  ],
  "total": 1
}
```

---

## Get contract triggered data in period

Returns the contract trigger data by day in a specific period.

```
GET https://apilist.tronscanapi.com/api/triggerstatistic
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/triggerstatistic) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start_timestamp` | Start timestamp, accurate to milliseconds |
| `end_timestamp` | End timestamp, accurate to milliseconds |
| `limit` | Max number of data. Default: `1000` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-02",
      "trigger_count": 2531720,
      "active_address": 611253
    }
  ],
  "total": 1
}
```

---

## Get new increased user by day

Returns the number of new users added every day.

```
GET https://apilist.tronscanapi.com/api/overview/dailyaccounts?days=5
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/overview/dailyaccounts?days=5) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `days` | Data time range. Default: `15`. Max: `2000` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "new_account_count": 14823
    }
  ],
  "total": 1
}
```

---

## Get TRX supply, marketcap & destroy amount data

Returns TRX related data, like the real-time supply, market cap, and burning data.

```
GET https://apilist.tronscanapi.com/api/funds
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/funds) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "totalSupply": 90950052502,
  "circulatingSupply": 71234567890,
  "burnedAmount": 19715484612,
  "marketCap": 6038123456,
  "priceInUsd": 0.06640206836839435
}
```

---

## Get price source of TRX

Returns available sources of the TRX price.

```
GET https://apilist.tronscanapi.com/api/trx/volume/sourceList
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/trx/volume/sourceList) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "data": [
    "coinmarketcap",
    "coingecko",
    "binance"
  ]
}
```

---

## Get TRX turnover

Returns the statistic data of TRX, like supply, TRON protocol revenue, minting amount, and burning amount.

```
GET https://apilist.tronscanapi.com/api/turnover?from=issuance&start=1575129600000&end=1680753244454&type=0
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/turnover?from=issuance&start=1575129600000&end=1680753244454&type=0) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `size` | Number of data count |
| `start` | Start time, accurate to milliseconds |
| `end` | End time, accurate to milliseconds |
| `type` | Query type. `0`: by day. `1`: by month. `2`: by quarter. `3`: by block |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "supply": 90950052502,
      "protocol_revenue": 21446630442140,
      "mint_amount": 0,
      "burn_amount": 651750035
    }
  ],
  "total": 1
}
```

---

## Get records of TRX’s price, volume & marketcap

Returns the historical TRX data, such as the price, volume, and market cap.

```
GET https://apilist.tronscanapi.com/api/trx/volume?start_timestamp=1507564800000&limit=2004&end_timestamp=1680765305898&source=coinmarketcap
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/trx/volume?start_timestamp=1507564800000&limit=2004&end_timestamp=1680765305898&source=coinmarketcap) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `limit` | Number of data count |
| `start_timestamp` | Start time, accurate to milliseconds |
| `end_timestamp` | End time, accurate to milliseconds |
| `start` | Start index |
| `source` | Data source. Default: `coinmarketcap` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "priceInUsd": 0.06640206836839435,
      "volume": 419877875980.71,
      "marketcap": 6038123456789
    }
  ],
  "total": 1
}
```

---

## Get accounts with holding TRX

Returns the number of accounts that hold TRX, sorted by time in ascending order.

```
GET https://apilist.tronscanapi.com/api/overview/acountswithtrx?days=1000
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/overview/acountswithtrx?days=1000) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `days` | Number of query days |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "account_count": 76694242
    }
  ],
  "total": 1
}
```

---

## Get number of contract calls for a period, including maximum and minimum values

Returns the number of contract calls for a certain period of days, including the maximum and minimum values.

```
GET https://apilist.tronscanapi.com/api/calleraddressstatistic?start_timestamp=1680393600000&end_timestamp=1680652800000&limit=4
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/calleraddressstatistic?start_timestamp=1680393600000&end_timestamp=1680652800000&limit=4) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start_timestamp` | Start time, accurate to milliseconds |
| `end_timestamp` | End time, accurate to milliseconds |
| `limit` | Number of results returned. Max: `3000` |

### Response

```
{
  "max": {
    "day": "2023-04-03",
    "caller_count": 594027
  },
  "min": {
    "day": "2023-04-02",
    "caller_count": 511253
  },
  "data": [
    { "day": "2023-04-02", "caller_count": 511253 },
    { "day": "2023-04-03", "caller_count": 594027 }
  ],
  "total": 2
}
```

---

## Get TRX Staking Rate Data

Returns the TRX staking rate.

```
GET https://apilist.tronscanapi.com/api/freezeresource?start_day=2023-04-01&end_day=2023-04-06
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/freezeresource?start_day=2023-04-01&end_day=2023-04-06) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start_day` | Start time. Format: `yyyy-MM-dd` |
| `end_day` | End time. Format: `yyyy-MM-dd` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-01",
      "freeze_ratio": "0.4402",
      "total_freeze": 40058302788.652379,
      "total_supply": 90950052502.455472
    }
  ],
  "total": 1
}
```

---

## Get Average block size data

Returns the average block size per day, sorted by time in ascending order.

```
GET https://apilist.tronscanapi.com/api/overview/dailyavgblockSize?days=10
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/overview/dailyavgblockSize?days=10) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `days` | Number of query days. Default: `15` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "avg_block_size": 24567
    }
  ],
  "total": 1
}
```

---

## Get cost of Energy and Bandwidth data

Returns the cost of resources such as Energy and Bandwidth.

```
GET https://apilist.tronscanapi.com/api/acquisition_cost_statistic?limit=10
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/acquisition_cost_statistic?limit=10) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start_timestamp` | Start time, accurate to milliseconds |
| `end_timestamp` | End time, accurate to milliseconds |
| `limit` | Number of data returned. Default: `14`. Max: `3000` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "energy_cost": 420,
      "bandwidth_cost": 1000
    }
  ],
  "total": 1
}
```

---

## Get transfer amount of core tokens

Returns the transfer amount of core tokens.

```
GET https://apilist.tronscanapi.com/api/tokenTransfer/analysis?token=&days=10
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/tokenTransfer/analysis?token=&days=10) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `token` | Token ID or address. Set to `_` for TRX. Can be empty |
| `days` | Number of query days |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "transfer_count": 2050457,
      "transfer_amount": "419877875980.71"
    }
  ],
  "total": 1
}
```

---

## Get transaction trend data

Returns transaction trend data, sorted by time in ascending order.

```
GET https://apilist.tronscanapi.com/api/overview/dailytransactionnum?type=0&days=10
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/overview/dailytransactionnum?type=0&days=10) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `type` | Query type. `0`: by day. `1`: by week. `2`: by month. `3`: by quarter |
| `days` | Number of query days. Default: `15` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "transaction_count": 4651179
    }
  ],
  "total": 1
}
```

---

## Get active accounts statistic data

Returns active account data per day.

```
GET https://apilist.tronscanapi.com/api/account/active_statistic?type=day&start_timestamp=1680480000000
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/account/active_statistic?type=day&start_timestamp=1680480000000) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `type` | Query type. Values: `DAY`, `WEEK`, or `MONTH` |
| `start_timestamp` | Start time, accurate to milliseconds |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "active_address": 611253
    }
  ],
  "total": 1
}
```

---

## Get cumulative transactions data

Returns cumulative transactions per day, sorted by time.

```
GET https://apilist.tronscanapi.com/api/overview/transactionnum?days=20
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/overview/transactionnum?days=20) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `days` | Number of query days. Default: `15`. Max: `2000` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "cumulative_transaction_count": 5816219340
    }
  ],
  "total": 1
}
```

---

## Get Bandwidth consumption

Returns Bandwidth consumption per day.

```
GET https://apilist.tronscanapi.com/api/netstatistic?start_timestamp=1680307200000&end_timestamp=1680739200000&type=day
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/netstatistic?start_timestamp=1680307200000&end_timestamp=1680739200000&type=day) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start_timestamp` | Start time, accurate to milliseconds |
| `end_timestamp` | End time, accurate to milliseconds |
| `type` | Statistic type. Values: `day`, `month`, or `quarter` |
| `limit` | Max data count |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "total_net_use": 1719770951,
      "net_burn": 651750035,
      "net_usage": 2371520986
    }
  ],
  "total": 1
}
```

---

## Get DeFi TVL data

Returns statistic data of DeFi TVL per day.

```
GET https://apilist.tronscanapi.com/api/defiTvl?type=tvlline&startTime=1680660000&endTime=1680681600&project=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/defiTvl?type=tvlline&startTime=1680660000&endTime=1680681600&project=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `type` | If set to `tvlline`, the result includes tvlline data. Default value omits tvlline data |
| `startTime` | Start time, accurate to seconds. Default: 7 days ago |
| `endTime` | End time, accurate to seconds. Default: current time |
| `project` | TVL data for specific projects: `SUN`, `JustLend`, `JustStable`, `JustCryptos`, or `JustSwap`. Default: all projects |

### Response

```
{
  "tvlLine": [
    { "value": 5912514657.04, "time": 1680660000 },
    { "value": 5919815655.20, "time": 1680681600 }
  ],
  "projects": [
    {
      "name": "JustLend",
      "tvl": 2345678901.23
    },
    {
      "name": "SUN",
      "tvl": 1234567890.12
    }
  ],
  "total_tvl": 5912514657.04
}
```

---

## Get cumulative block size (on-chain size)

Returns the cumulative block size (on-chain size), sorted by time in ascending order.

```
GET https://apilist.tronscanapi.com/api/overview/totalblockchainsize?days=10
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/overview/totalblockchainsize?days=10) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `days` | Number of query days. Default: `15` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "total_size": 2345678901234
    }
  ],
  "total": 1
}
```

---

## Get token transaction data

Returns analysis data of token transactions, such as transfers and holders.

```
GET https://apilist.tronscanapi.com/api/token/analysis?token=TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn&start_day=2023-03-04&end_day=2023-04-06
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/token/analysis?token=TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn&start_day=2023-03-04&end_day=2023-04-06) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `token` | Token address |
| `start_day` | Start day. Format: `yyyy-MM-dd` |
| `end_day` | End day. Format: `yyyy-MM-dd` |
| `type` | Optional. Default: token transfer data. `1`: token holder data |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "transfer_count": 743,
      "transfer_amount": "312049537.29"
    }
  ],
  "total": 1
}
```

---

## Get statistics data of TRON

Returns statistic data of TRON per day, such as transfers, accounts, resources, and tokens.

```
GET https://apilist.tronscanapi.com/api/stats/overview?days=10
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/stats/overview?days=10) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `days` | Number of query days. Default: `15` |

### Response

```
{
  "data": [
    {
      "day": "2023-04-03",
      "transaction_count": 4651179,
      "new_account_count": 14823,
      "active_address": 611253,
      "trc20_transfer_count": 2324334,
      "trc10_transfer_count": 276,
      "trx_transfer_count": 1444329,
      "energy_usage": 96414035761,
      "net_usage": 2371520986,
      "contract_trigger_count": 2531720
    }
  ],
  "total": 1
}
```