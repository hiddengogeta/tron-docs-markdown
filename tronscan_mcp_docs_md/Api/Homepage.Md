

# Homepage & Search

## Get TRONSCAN home page data

Returns TRONSCAN home page data.

```
GET https://apilist.tronscanapi.com/api/system/homepage-bundle
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/system/homepage-bundle) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "tps": {
    "data": {
      "blockHeight": 49966049,
      "currentTps": 124,
      "maxTps": 1035
    },
    "type": "tps"
  },
  "node": {
    "total": 6113,
    "code": 0
  },
  "statsOverview": {
    "success": true,
    "data": [
      {
        "accountWithTrx": 95097822,
        "date": 1679270400000,
        "dateDayStr": "2023-03-20",
        "totalTransaction": 5110353723,
        "avgBlockTime": 3,
        "avgBlockSize": 65610,
        "totalBlockCount": 49581706,
        "newAddressSeen": 177313,
        "active_account_number": 2065546,
        "blockchainSize": 1480831494802,
        "totalAddress": 148010837,
        "newBlockSeen": 28791,
        "newTransactionSeen": 8049089,
        "newTrigger": 2096603,
        "newTrc10": 0,
        "newTrc20": 11,
        "totalTrc10": 4927,
        "totalTrc20": 89046,
        "triggers": 2464079621,
        "trx_transfer": 4682444,
        "trc10_transfer": 961498,
        "freeze_transaction": 138872,
        "unfreeze_transaction": 98995,
        "vote_transaction": 29139,
        "shielded_transaction": 0,
        "usdt_transaction": 1979362,
        "other_transaction": 41538,
        "energy_usage": 86213677685,
        "net_usage": 2312696315,
        "energy_usage_change_24h": 0.3071,
        "net_usage_change_24h": 0.2148,
        "active_account_number_rate": 0.1642,
        "newAddressSeenRate": 0.2406,
        "totalAddressRate": 0.0012
      }
    ],
    "avg_increase_accounts": 94546,
    "realTimeAccountNum": 150422638,
    "yesterday_total_address": 148010837,
    "yesterday_total_address_rate": 0.0012,
    "avg_active_account_for_one_month": 1950000,
    "avg_active_account_for_one_month_rate": 0.02,
    "avg_new_account_for_one_month": 170000,
    "avg_new_account_for_one_month_rate": 0.01,
    "new_account_for_one_month": 5100000
  },
  "freezeResource": {
    "total": 14,
    "data": [
      {
        "total_net_cost": 0.9075,
        "net_cost_change_24h": -0.0001,
        "total_energy_weight": 5318380207,
        "total_turn_over": "91174878410.695397",
        "energy_rate": 0.1195,
        "total_freeze_weight_change_24h": 0.002,
        "total_freeze_weight": 44522867669,
        "energy_cost_change_24h": 0.0172,
        "total_turnover_change_24h": -0.0002,
        "freezing_rate_change_24h": 0.0021,
        "freezing_rate": 0.4883,
        "net_rate": 0.8805,
        "total_net_weight": 39204487462,
        "day": "2023-03-20",
        "total_energy_cost": 0.0591,
        "freeze1Balance": 39204487462,
        "freeze2Balance": 5318380207,
        "freeze1Percent": 0.8805,
        "freeze2Percent": 0.1195
      }
    ],
    "freeze_rate_diff": 0,
    "freezing_rate": 0.4883,
    "total_freeze_weight": 44522867669,
    "total_freeze_weight_change_24h": 0.002,
    "freeze1Percent": 0.8805,
    "freeze2Percent": 0.1195,
    "yesterday_freezing_rate": 0.4862,
    "avg_freezing_rate_for_one_month": 0.4791
  },
  "triggerStatistic": {
    "total": 15,
    "min": {
      "triggers_amount_rate": -0.07031137219672139,
      "triggers_amount": 1616471,
      "dayStr": "2023-03-19",
      "day": 1679184000000
    },
    "max": {
      "triggers_amount_rate": 0.05825757475895665,
      "triggers_amount": 2167611,
      "dayStr": "2023-03-31",
      "day": 1680220800000
    },
    "data": [
      {
        "triggers_amount_rate": 0.29702481516835133,
        "triggers_amount": 2096603,
        "dayStr": "2023-03-20",
        "day": 1679270400000
      },
      {
        "triggers_amount_rate": -0.05922055820772936,
        "triggers_amount": 1972441,
        "dayStr": "2023-03-21",
        "day": 1679356800000
      }
    ],
    "avg_trigger_count": "989211",
    "trigger_ratio": "0.140"
  },
  "callerAddressStatistic": {
    "total": 15,
    "min": {
      "caller_amount_rate": -0.06234213617523721,
      "day": 1679788800000,
      "caller_amount": 462180
    },
    "max": {
      "caller_amount_rate": 0.013352945642836619,
      "day": 1680048000000,
      "caller_amount": 680656
    },
    "data": [
      {
        "caller_amount_rate": 0.22923921105902523,
        "day": 1679270400000,
        "caller_amount": 575059
      }
    ]
  },
  "accountList": {
    "total": 10000,
    "data": [],
    "rangeTotal": 150422638
  },
  "funds": {
    "genesisBlockIssue": 100000000000,
    "totalDonateBalance": 652719751205649,
    "totalFundBalance": 33177933703065630,
    "totalBlockPay": 1027115664,
    "totalNodePay": 5945630320,
    "burnPerDay": 1000000000,
    "burnUsddByCharge": 8997572047.566078,
    "burnByCharge": 5981458480.049072,
    "totalTurnOver": 90993715456.384852,
    "fundSumBalance": 33177933703065630,
    "donateBalance": 652719751205649,
    "fundTrx": 32525213951.85998,
    "turnOver": 67466073552.09094,
    "usddTrxBurnContractTransferTrx": 0
  },
  "stableCoin": [
    {
      "amount24h": 5385970884.857,
      "icon": "https://static.tronscan.org/production/logo/usdtlogo.png",
      "priceInUsd": 1.001476,
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "volumn24h": 5393920577.883,
      "transferCount": 967851969,
      "supply": 44125091015,
      "transferCount24h": 1778176,
      "holders": 22132393,
      "name": "Tether USD",
      "abbr": "USDT",
      "priceInTrx": 15.294038998856927208,
      "vip": true,
      "transfers": [
        {
          "date": 1679097600000,
          "amount": 6978301384.442,
          "transfer_count": 1649349,
          "day": "2023-03-18"
        },
        {
          "date": 1679184000000,
          "amount": 5727506520.235,
          "transfer_count": 1538489,
          "day": "2023-03-19"
        }
      ],
      "liquidity": [
        { "date": 1679097600000, "day": "2023-03-18", "liquidity": 44000000000 },
        { "date": 1679184000000, "day": "2023-03-19", "liquidity": 44100000000 }
      ]
    },
    {
      "amount24h": 1136777.229,
      "icon": "https://static.tronscan.org/production/upload/logo/TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn.png",
      "priceInUsd": 0.988515,
      "contractAddress": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn",
      "supply": 725332036,
      "transferCount24h": 923,
      "holders": 130781,
      "name": "Decentralized USD",
      "abbr": "USDD",
      "priceInTrx": 15.096104854093405586
    }
  ],
  "usdt": {
    "transfer_amount": "5385970884.857",
    "transfer_count": "1778176",
    "transfer_amount_percent": "0.0123",
    "transfer_count_percent": "0.0456",
    "active_account": "345678",
    "active_account_percent": "0.0789",
    "holders": "22132393",
    "holders_percent": "0.0012",
    "turnover": "5393920577.883",
    "turnover_percent": "0.0034"
  },
  "trx_volume_24h": "189819192.64816055",
  "trxPriceLine": {
    "total": 25,
    "data": [
      { "priceUsd": "0.0659888931388292", "time": "1680422400" },
      { "priceUsd": "0.06603902698700018", "time": "1680426000" },
      { "priceUsd": "0.06621545169710459", "time": "1680429600" }
    ]
  },
  "tvl": {
    "total": 1.19248935637809e10,
    "tvlLine": [
      { "t": "1680476400", "v": 1.19560536120805e10, "trxV": 2894427911.74 },
      { "t": "1680390000", "v": 1.21161034762574e10, "trxV": 2944857376.11 }
    ],
    "projects": [
      {
        "project": "JustLend DAO",
        "logo": "https://static.tronscan.org/production/upload/logo/justlend.png",
        "type": "Lending",
        "vip": "1",
        "locked": 3730739412.58,
        "url": "https://justlend.justnetwork.io/#/home",
        "gain": -0.034
      },
      {
        "project": "Just Cryptos",
        "logo": "https://static.tronscan.org/production/upload/logo/justcryptos.png",
        "type": "Cross Chain",
        "locked": 3355929591.96,
        "url": "https://justnetwork.io/token",
        "gain": -0.0026
      },
      {
        "project": "TRX Staking Governance",
        "logo": "https://static.tronscan.org/production/upload/logo/Staking.png",
        "type": "Governance",
        "locked": 2889443381.29,
        "url": "https://tronscan.org/#/data/charts/OverallFreezingRate",
        "gain": -0.0135
      },
      {
        "project": "SUN.io",
        "logo": "https://static.tronscan.org/production/upload/logo/sun10.png",
        "type": "DEX,Stablecoin,Farm",
        "locked": 761885844.19,
        "url": "https://sun.io/#/home",
        "gain": -0.0063
      }
    ]
  }
}
```

---

## Get trending search information

Returns the trending search information.

```
GET https://apilist.tronscanapi.com/api/search/bar
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/search/bar) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
[
  {
    "token_id": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
    "vip_token": true,
    "name": "Tether USD",
    "icon": "https://static.tronscan.org/production/logo/usdtlogo.png",
    "type": 20,
    "abbr": "USDT"
  },
  {
    "token_id": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
    "vip_token": true,
    "name": "TrueUSD",
    "icon": "https://static.tronscan.org/production/logo/TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4.png",
    "type": 20,
    "abbr": "TUSD"
  },
  {
    "token_id": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn",
    "vip_token": true,
    "name": "Decentralized USD",
    "icon": "https://static.tronscan.org/production/upload/logo/TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn.png",
    "type": 20,
    "abbr": "USDD"
  },
  {
    "token_id": "TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR",
    "vip_token": true,
    "name": "Wrapped TRX",
    "icon": "https://static.tronscan.org/production/upload/logo/TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR.png?t=1598430824415",
    "type": 20,
    "abbr": "WTRX"
  },
  {
    "token_id": "TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8",
    "vip_token": true,
    "name": "USD Coin",
    "icon": "https://static.tronscan.org/production/upload/logo/TEkxiTehnzSmSe2XqrBj4w32RUN966rdz81.png",
    "type": 20,
    "abbr": "USDC"
  },
  {
    "token_id": "TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9",
    "vip_token": true,
    "name": "JUST",
    "icon": "https://static.tronscan.org/production/logo/just_icon.png",
    "type": 20,
    "abbr": "JST"
  }
]
```

---

## Search token/contract/account information

Returns the search results for tokens/accounts/contracts.

The maximum value for `limit` is **50**.

```
GET https://apilist.tronscanapi.com/api/search/v2?term=ethw&type=&start=&limit=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/search/v2?term=ethw&type=&start=&limit=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0`. Must be less than `50` |
| `limit` | Number of items per page. Default: `10` |
| `term` | **Required.** Search term. Returns a parameter-missing error if omitted |
| `type` | Search type. Options: `token`, `address`, `contract`, `transaction`, `block` |

### Response

```
{
  "address": [
    {
      "name": "AnthonyRethwill",
      "address": "TLr9uU2fPsKf7FnpQT2g9z8V3a58q33hLz",
      "date_created": 1531247445,
      "balance": 0,
      "totalBalance": 0,
      "total_transactions": 2234,
      "frozen": 0,
      "address_tag": "",
      "address_tag_logo": "",
      "witness_url": "",
      "activated": true
    },
    {
      "name": "ElizabethWarren",
      "address": "TLdfqXYJA1bETowS381WHt5KG8NtvnHFcA",
      "date_created": 1588222932,
      "balance": 2000000,
      "totalBalance": 2000000,
      "total_transactions": 6,
      "frozen": 0,
      "address_tag": "",
      "address_tag_logo": "",
      "witness_url": "",
      "activated": true
    }
  ],
  "token": [
    {
      "token_id": "TKqaZCWo6g4cY5P2pkykHQNBpo5GyVQrrn",
      "token_type": "trc20",
      "vip": false,
      "name": "Ethereum PoW",
      "abbr": "ETHW",
      "description": "ETHW (ETH1, Ethereum PoW) represents the token for the PoW chain that will potentially continue to exist.",
      "img_url": "https://static.tronscan.org/production/upload/logo/TKqaZCWo6g4cY5P2pkykHQNBpo5GyVQrrn.png",
      "url": "https://ethereum.org/",
      "holders": 11,
      "level": "1",
      "market_cap": 5196.111303094405153300,
      "volume24h": 0,
      "market_cap_trx": 5196.111303094405153300,
      "market_cap_usd": 341.58,
      "is_certificates": false,
      "market_info": {
        "fPrecision": 18,
        "fShortName": "ETHW",
        "fTokenAddr": "TKqaZCWo6g4cY5P2pkykHQNBpo5GyVQrrn",
        "filter": false,
        "gain": -0.0294,
        "marketCap24hGain": -0.0294,
        "pairUrl": "",
        "priceFrom": "CMC",
        "priceInTrx": 51.961113030944051533,
        "priceInUsd": "3.41581266352575",
        "sPrecision": 6,
        "sShortName": "TRX",
        "sTokenAddr": "T9yD14Nj9j7xAB4dbGeiX9h8unkKLxmGkn",
        "volume24hGain": 0,
        "volume24hInTrx": 99096290.62778482491637213914517628
      }
    },
    {
      "token_id": "TQGHTuTGKtSA9ocTG6E1ypSshFx16PtEUS",
      "token_type": "trc20",
      "vip": false,
      "name": "SUNSWAP-ETHW-TRX",
      "abbr": "S-ETHW-TRX",
      "description": "SUNSWAP ETHW-TRX pool TRC20 token.",
      "img_url": "",
      "url": "sunswap.com",
      "holders": 1,
      "level": "1",
      "is_certificates": true
    }
  ],
  "contract": [
    {
      "contract": "TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3",
      "name": "ExampleContract",
      "tag": "DeFi",
      "contract_address": "TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3",
      "verify_status": true,
      "official": false,
      "frozen": 0,
      "balance": 0,
      "total_transactions": 12345,
      "date_created": 1620000000,
      "description": "An example contract description."
    }
  ]
}
```

---

## Get the current TPS

Returns the latest block height, current TPS, and historical maximum TPS.

```
GET https://apilist.tronscanapi.com/api/system/tps
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/system/tps) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "data": {
    "blockHeight": 49966616,
    "currentTps": 138,
    "maxTps": 1035
  },
  "type": "tps"
}
```

---

## Get hot search info

Returns popular search results.

```
GET https://apilist.tronscanapi.com/api/search/hot
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/search/hot) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "hot_tokens": [
    {
      "id": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "type": "20",
      "vip_token": true,
      "icon": "https://static.tronscan.org/production/logo/usdtlogo.png",
      "name": "Tether USD",
      "abbr": "USDT",
      "priceInUsd": 0.9999464376419606,
      "holders": 22132393
    },
    {
      "id": "TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4",
      "type": "20",
      "vip_token": true,
      "icon": "https://static.tronscan.org/production/logo/TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4.png",
      "name": "TrueUSD",
      "abbr": "TUSD",
      "priceInUsd": 1.001244006534014,
      "holders": 309660
    },
    {
      "id": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn",
      "type": "20",
      "vip_token": true,
      "icon": "https://static.tronscan.org/production/upload/logo/TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn.png",
      "name": "Decentralized USD",
      "abbr": "USDD",
      "priceInUsd": 1.0,
      "holders": 130781
    },
    {
      "id": "TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR",
      "type": "20",
      "vip_token": true,
      "icon": "https://static.tronscan.org/production/upload/logo/TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR.png?t=1598430824415",
      "name": "Wrapped TRX",
      "abbr": "WTRX",
      "priceInUsd": 0.0657378655744259,
      "holders": 8820
    },
    {
      "id": "TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8",
      "type": "20",
      "vip_token": true,
      "icon": "https://static.tronscan.org/production/upload/logo/TEkxiTehnzSmSe2XqrBj4w32RUN966rdz81.png",
      "name": "USD Coin",
      "abbr": "USDC",
      "priceInUsd": 0.999652675542019,
      "holders": 369057
    },
    {
      "id": "TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9",
      "type": "20",
      "vip_token": true,
      "icon": "https://static.tronscan.org/production/logo/just_icon.png",
      "name": "JUST",
      "abbr": "JST",
      "priceInUsd": 0.026699405135209707,
      "holders": 450893
    },
    {
      "id": "TN3W4H6rK2ce4vX9YnFQHwKENnHjoxb3m9",
      "type": "20",
      "vip_token": true,
      "icon": "https://static.tronscan.org/production/logo/TN3W4H6rK2ce4vX9YnFQHwKENnHjoxb3m9.png",
      "name": "Bitcoin",
      "abbr": "BTC",
      "priceInUsd": 28327.246303324384,
      "holders": 35539
    }
  ],
  "hot_contracts": [
    {
      "tag": "FTH-DC Token",
      "tagUrl": "",
      "triggers": 535219,
      "trigger7day": 3746533,
      "contract_address": "TVp4VW5DdC6YxTTU6kgzKDRjKu8Aj3dpNH",
      "name": "FintochPool",
      "verify_status": 0
    },
    {
      "tag": "S-USDT-TRX Token",
      "tagUrl": "https://sunswap.com",
      "triggers": 9800661,
      "trigger7day": 68604627,
      "contract_address": "TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE",
      "name": "CreatedByContract",
      "verify_status": 2
    },
    {
      "tag": "",
      "tagUrl": "",
      "triggers": 2849741,
      "trigger7day": 19948187,
      "contract_address": "TARciDTaL5Bpsqf5YeLzNkyj9zj7Uctfpb",
      "name": "ToCandy",
      "verify_status": 0
    },
    {
      "tag": "SUN: USDD Pool",
      "tagUrl": "",
      "triggers": 75935,
      "trigger7day": 531545,
      "contract_address": "TNTfaTpkdd4AQDeqr8SGG7tgdkdjdhbP5c",
      "name": "StableSwap2Pool",
      "verify_status": 0
    }
  ],
  "hot_sum_all": {
    "click": 0,
    "search": 0,
    "holder": 0,
    "transfer": 0,
    "activeAddress": 0,
    "justswapLiquidity": 0,
    "justswapVolume": 0,
    "totalScore": 0
  },
  "hot_c_sum_all": {
    "caller": 0,
    "click": 0,
    "search": 0,
    "trigger": 0,
    "tokenAmount": 0,
    "projectId": 0,
    "verified": 0,
    "totalScore": 0
  }
  // Note: a `weight` object is also returned when `detail=1`, containing scoring weight configuration
}
```

---

## Get node information

Returns the current node information of TRON fullnodes.

```
GET https://apilist.tronscanapi.com/api/nodemap
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/nodemap) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "total": 1,
  "code": 0,
  "data": [
    {
      "country": "United States",
      "lng": -77.4903,
      "province": "Virginia",
      "city": "Ashburn",
      "ip": "100.24.113.233",
      "lat": 39.0469
    }
  ]
}
```