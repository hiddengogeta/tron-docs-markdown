

# Tokens

## Get token list

Returns the token info.

The maximum value for `limit` is **500**.

```
GET https://apilist.tronscanapi.com/api/tokens/overview?start=0&limit=2&verifier=all&order=desc&filter=top&sort=&showAll=1&field=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/tokens/overview?start=0&limit=2&verifier=all&order=desc&filter=top&sort=&showAll=1&field=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `20` |
| `order` | Default descending. Optional: `desc`, `asc` |
| `filter` | Token filtering. Default: `all`. Optional: `trc10`, `trc20`, `trc721`, `trc1155`, `all`, `top` |
| `sort` | Sorting field. Default: `marketcap`. Optional: `priceInTrx`, `gain`, `volume24hInTrx`, `holderCount`, `marketcap`, `createTime`, `hot`, `init`, `top` |
| `field` | Field names to return, separated by commas. If blank, all fields are returned |
| `verifier` | By default, tokens with `type=auto` are not returned. Set to `all` to return all tokens |

### Response

```
{
  "all": 82625,
  "currentWeekAll": 81,
  "currentWeekTotalAll": 57,
  "tokens": [
    {
      "abbr": "USDT",
      "contractAddress": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "dateCreated": 1555400628,
      "decimal": 6,
      "description": "USDT is the official stablecoin issued by Tether on the TRON network.",
      "gain": -0.0001,
      "imgUrl": "https://static.tronscan.org/production/logo/usdtlogo.png",
      "isTop": true,
      "level": "2",
      "marketcap": 676296055758.162651744384498500774922,
      "name": "Tether USD",
      "nrOfTokenHolders": 22119750,
      "ownerAddress": "THPvaUhoh2Qn2y9THCZML3H815hhFhn5YC",
      "priceInTrx": 15.326791179538664037,
      "priceInUsd": 1.000177699841053200,
      "projectSite": "https://tron.network/usdt",
      "supply": 44125091014.551106,
      "tokenType": "trc20",
      "transferCount": 967552226,
      "verifier": "robot",
      "vip": true,
      "volume24hInTrx": 352411988502.470404503170441975634585
    },
    {
      "abbr": "TRON",
      "contractAddress": "_",
      "dateCreated": 1529891469,
      "decimal": 6,
      "description": "Official Token of TRON Protocol",
      "gain": -0.008,
      "imgUrl": "https://static.tronscan.org/production/logo/trx.png",
      "isTop": true,
      "level": "2",
      "marketcap": 90995853639.549692,
      "name": "TRX",
      "nrOfTokenHolders": 76422658,
      "priceInTrx": 1.0,
      "priceInUsd": 0.06525682304436267,
      "supply": 90995853639.549692,
      "tokenType": "trc10",
      "transferCount": 1856514990,
      "vip": true
    }
  ],
  "total": 21,
  "total10": 3638,
  "total1155": 20,
  "total20": 77411,
  "total721": 1556,
  "totalAllCount": 82625,
  "updateTime": 1680502383192,
  "valueAtLeast": 10000
}
```

---

## Get details of all TRC20/TRC721/TRC1155 tokens or specified tokens

Returns the detail information of TRC20/TRC721/TRC1155 tokens.

The maximum value for `limit` is **50**.

```
GET https://apilist.tronscanapi.com/api/token_trc20?contract=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&showAll=1&start=&limit=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/token_trc20?contract=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&showAll=1&start=&limit=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `contract` | TRC20/TRC721/TRC1155 contract address |
| `showAll` | Returned data type. `0`: only whitelist (default). `1`: all. `2`: exclude blacklist |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `30` |

### Response

```
{
  "total": 1,
  "rangeTotal": 1,
  "trc20_tokens": [
    {
      "symbol": "USDT",
      "contract_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
      "token_desc": "USDT is the official stablecoin issued by Tether on the TRON network.",
      "home_page": "https://tron.network/usdt",
      "icon_url": "https://static.tronscan.org/production/logo/usdtlogo.png",
      "vip": true,
      "level": "2",
      "decimals": 6,
      "name": "Tether USD",
      "issue_address": "THPvaUhoh2Qn2y9THCZML3H815hhFhn5YC",
      "transfer_num": 967710206,
      "holders_count": 22126100,
      "volume24h": 21231115612.35,
      "transfer24h": 2193222,
      "market_info": {
        "priceInTrx": 15.323038898864725314,
        "priceInUsd": 1.000116842294540100,
        "gain": -0.0001,
        "liquidity": 46903104.780281,
        "volume24hInTrx": 352344274662.928904839525251926296585,
        "pairUrl": "https://sunswap.com/#/scanv2/detail/TFGDbUyP8xez44C77fin3bn3Ss6jugoUwJ"
      },
      "tokenPriceLine": {
        "total": 25,
        "data": [
          { "priceUsd": "1.0002796372275067", "time": "1680415200" },
          { "priceUsd": "1.0000974872551347", "time": "1680418800" }
        ]
      },
      "tokenType": "trc20",
      "white_paper": "https://tether.to/wp-content/uploads/2016/06/TetherWhitePaper.pdf"
    }
  ]
}
```

---

## Get details of all TRC10 tokens or specified TRC10 tokens

Returns the detail information of TRC10 tokens.

```
GET https://apilist.tronscanapi.com/api/token?id=1002000&showAll=1&order=0&owner=&start=&limit=&id_gt=&totalAll=&name=&field=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/token?id=1002000&showAll=1&order=0&owner=&start=&limit=&id_gt=&totalAll=&name=&field=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `10` |
| `owner` | TRC10 issuer address |
| `id` | TRC10 token ID. If set to `0`, the token is TRX |
| `id_gt` | The ID of the returned token must be greater than this value |
| `showAll` | Returned data type. `0`: only whitelist (default). `1`: all. `2`: exclude blacklist |
| `fields` | Field names to return, separated by commas. If blank, all fields are returned |
| `totalAll` | When `totalAll=1`, the `totalAll` in the response is the total number of all tokens; otherwise it is the filtered count |
| `name` | TRC10 token name |

### Response

```
{
  "total": 1,
  "totalAll": 1,
  "data": [
    {
      "tokenID": 1002000,
      "abbr": "BTTOLD",
      "name": "BitTorrent Old",
      "description": "Official Token of BitTorrent Protocol",
      "precision": 6,
      "totalSupply": 990000000000000000,
      "nrOfTokenHolders": 16419593,
      "ownerAddress": "TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg",
      "dateCreated": 1547950149000,
      "imgUrl": "https://static.tronscan.org/production/logo/1002000.png",
      "vip": true,
      "level": "2",
      "website": "www.bittorrent.com",
      "github": "https://github.com/bittorrent",
      "market_info": {
        "priceInTrx": 0.009235322096783673,
        "priceInUsd": 0.000602778680780651,
        "gain": -0.0409,
        "volume24hInTrx": 2207585.19516434931338253853651861
      },
      "transfer24h": 24,
      "volume24h": 161311.88,
      "tokenPriceLine": {
        "total": 25,
        "data": [
          { "priceUsd": "0.0006316053556967662", "time": "1680415200" },
          { "priceUsd": "0.0006308130697251012", "time": "1680418800" }
        ]
      }
    }
  ]
}
```

---

## Get the holder of a TRC20/TRC721/TRC1155 token

Returns the holder information of TRC20/TRC721/TRC1155 tokens.

The value sum of `start` and `limit` must be less than or equal to **10000**. The maximum value for `limit` is **50**.

```
GET https://apilist.tronscanapi.com/api/token_trc20/holders?start=0&limit=5&contract_address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&holder_address=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/token_trc20/holders?start=0&limit=5&contract_address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&holder_address=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `contract_address` | TRC20/TRC721/TRC1155 contract address. At least one of `contract_address` or `holder_address` is required |
| `holder_address` | Token holder address. See `contract_address` note above |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `10` |

### Response

```
{
  "total": 10000,
  "rangeTotal": 22127141,
  "contractMap": {},
  "contractInfo": {},
  "trc20_tokens": [
    {
      "holder_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
      "balance": "9873546646139600",
      "addressTag": "Binance-Cold 2",
      "addressTagLogo": "https://coin.top/production/upload/logo/Binance.png",
      "updateBlock": 49750607,
      "updateTime": 1679864391000,
      "srTag": false,
      "srName": "",
      "foundationTag": false,
      "analysisShow": true,
      "publicTagDesc": ""
    },
    {
      "holder_address": "TMuA6YqfCeX8EhbfYEg5y7S4DqzSJireY9",
      "balance": "3999333220555150",
      "addressTag": "Binance-Cold 1",
      "addressTagLogo": "https://coin.top/production/upload/logo/Binance.png",
      "updateBlock": 47774475,
      "updateTime": 1673921982000,
      "srTag": false,
      "foundationTag": false,
      "analysisShow": true
    },
    {
      "holder_address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
      "balance": "2061340659212102",
      "addressTag": "Binance-Hot",
      "addressTagLogo": "https://coin.top/production/upload/logo/Binance.png",
      "updateBlock": 49963704,
      "updateTime": 1680503880000,
      "srTag": false,
      "foundationTag": false,
      "analysisShow": true
    }
  ]
}
```

---

## Get the holder of a TRC10 token

Returns the holder information of TRC10 tokens.

The value sum of `start` and `limit` must be less than or equal to **10000**. The maximum value for `limit` is **50**.

```
GET https://apilist.tronscanapi.com/api/tokenholders?sort=-balance&limit=20&start=0&address=TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg&holder_address=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/tokenholders?sort=-balance&limit=20&start=0&address=TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg&holder_address=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `10` |
| `sort` | Sort by holder balance. Use `-` prefix for descending order. Default: `-balance` |
| `address` | TRC10 issuer address (required) |
| `holder_address` | TRC10 holder address |

### Response

```
{
  "total": 10000,
  "rangeTotal": 16419593,
  "contractMap": {},
  "contractInfo": {},
  "data": [
    {
      "address": "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb",
      "name": "BitTorrent",
      "balance": "598625477691368189",
      "updateTime": 1680485589000,
      "index": 1,
      "addressTag": "Black hole: Address(0) without private key, often used for token burn.",
      "addressTagLogo": "",
      "srTag": false,
      "srName": "",
      "foundationTag": false,
      "analysisShow": false
    },
    {
      "address": "TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5",
      "name": "BitTorrent",
      "balance": "136571760289947896",
      "updateTime": 1661146485000,
      "index": 2,
      "srTag": false,
      "foundationTag": false,
      "analysisShow": false
    },
    {
      "address": "TV9p7kGr2JNiBYfuyyem6CuHrbfJXEQpFj",
      "name": "BitTorrent",
      "balance": "36748380903107404",
      "updateTime": 1656886977000,
      "index": 3,
      "srTag": false,
      "foundationTag": false,
      "analysisShow": false
    }
  ]
}
```

---

## Get the distribution of token amounts held by holders

Returns the distribution of token holdings among token holders.

```
GET https://apilist.tronscanapi.com/api/tokens/position-distribution?tokenId=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/tokens/position-distribution?tokenId=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `tokenId` | Token address or token ID |

### Response

```
{
  "expire": 1680505803648,
  "rank1-10": "21339396114270443",
  "rank11-50": "2762355558731794",
  "rank51-100": "963739140448814",
  "rank101-500": "2949416190422246",
  "other": "12345678901234567",
  "rank1-10_ratio": 0.68,
  "rank11-50_ratio": 0.09,
  "rank51-100_ratio": 0.03,
  "rank101-500_ratio": 0.09,
  "other_ratio": 0.11
}
```

---

## Get the price information of a specific token

Returns token price information.

Only some tokens have price information.

```
GET https://apilist.tronscanapi.com/api/token/price?token=trx
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/token/price?token=trx) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `token` | Token abbreviation. Default: `trx` |

### Response

```
{
  "price_in_trx": "1.000000000000000000",
  "percent_change_24h": "-1.32633933",
  "market_cap": "5924627157.48",
  "volume_percent_change_24h": "-14.5509",
  "price_in_usd": "0.06510875200109231",
  "volume_24h": "185091667.4531934",
  "market_cap_percent_change_24h": "-1.3392",
  "from": "coinmarketcap",
  "time": 1680505501491,
  "token": "trx",
  "rank": 1
}
```

---

## Get a list of priced tokens

Returns the list of tokens that have a price.

```
GET https://apilist.tronscanapi.com/api/getAssetWithPriceList
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/getAssetWithPriceList) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "number": 1,
  "data": [
    {
      "name": "Wrapped TRX",
      "logo": "https://static.tronscan.org/production/upload/logo/TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR.png?t=1598430824415",
      "id": "TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR",
      "abbr": "WTRX",
      "type": "trc20",
      "vip": true,
      "priceInUsd": 0.065
    }
  ]
}
```

---

## Get the transfer list of one TRC721 tokenId

Returns the transfer list of a specific TRC721 token.

The value sum of `start` and `limit` must be less than or equal to **10000**. The maximum value for `limit` is **50**.

```
GET https://apilist.tronscanapi.com/api/trc721/transfers?limit=20&start=0&contract=THjYwnDDN6aYxrzKb88CSMTEYjBuHpoYxS&tokenId=965650
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/trc721/transfers?limit=20&start=0&contract=THjYwnDDN6aYxrzKb88CSMTEYjBuHpoYxS&tokenId=965650) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `20` |
| `contract` | TRC721 contract address (required) |
| `tokenId` | The ID of a TRC721 token (required; must be a numeric ID) |

### Response

```
{
  "total": 1,
  "rangeTotal": 1,
  "contractMap": {},
  "contractInfo": {},
  "token_id_info": {
    "tokenIdName": "965650",
    "tokenIdImage": "https://static.tronscan.org/production/upload/logo/00/0078186f4893cb0b57c5799da8bec800.png"
  },
  "token_transfers": [
    {
      "transaction_id": "6e857404b7b3b8fed973442e0e2f58c3179e04893deb7a341873fa4160d5e27f",
      "block_ts": 1670256540000,
      "from_address": "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb",
      "from_address_tag": "Black hole: Address(0) without private key, often used for token burn.",
      "to_address": "TNLjmMrKwAxPXabtgdLGdF1DG17kQKHZg2",
      "to_address_tag": "",
      "block": 46556208,
      "contract_address": "THjYwnDDN6aYxrzKb88CSMTEYjBuHpoYxS",
      "token_id": "965650",
      "event_type": "Transfer",
      "confirmed": true,
      "contractRet": "SUCCESS",
      "finalResult": "SUCCESS",
      "revert": false,
      "tokenInfo": {
        "tokenId": "THjYwnDDN6aYxrzKb88CSMTEYjBuHpoYxS",
        "tokenAbbr": "DVKNFT",
        "tokenName": "Devikins NFT",
        "tokenDecimal": 0,
        "tokenType": "trc721",
        "vip": false
      }
    }
  ]
}
```

---

## Get one TRC10/TRX transfer information

Returns the transfer list of a TRC10 token or TRX.

The value sum of `start` and `limit` must be less than or equal to **10000**.

```
GET https://apilist.tronscanapi.com/api/asset/transfer?limit=2&start=0&name=&issueAddress=TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg&start_timestamp=1680480000000&end_timestamp=1680566400000&address=&relatedAddress=&confirm=&filterTokenValue=0
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/asset/transfer?limit=2&start=0&name=&issueAddress=TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg&start_timestamp=1680480000000&end_timestamp=1680566400000&address=&relatedAddress=&confirm=&filterTokenValue=0) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `10`, max: `50` |
| `name` | When querying TRX transfers, fill in `trx` |
| `issueAddress` | TRC10 issuer address |
| `start_timestamp` | Start time |
| `end_timestamp` | End time. Must be ≥ `start_timestamp` |
| `address` | Query address |
| `relatedAddress` | Same as `address` parameter |
| `confirm` | `0`: solidified transactions. `1`: non-solidified transactions. Omit for all |
| `filterTokenValue` | Whether to hide small amount transactions. `1`: hide. `0`: do not hide |

### Response

```
{
  "total": 6,
  "rangeTotal": 6,
  "contractMap": {},
  "contractInfo": {},
  "normalAddressInfo": {},
  "Data": [
    {
      "blockId": 49964543,
      "transactionHash": "16fc1528f314ed9d346f7a6087ae95d7cc484ab1d57af48c3e5e50679cd0c0b3",
      "timestamp": 1680506397000,
      "transferFromAddress": "TK3C7dJN9dh1nG8PzVJYJjCiunah99y1Pt",
      "transferToAddress": "TKXFJ1ucjo1eeNE12SU7Sw94qQGF9ogHwR",
      "amount": 429322766,
      "tokenName": "1002000",
      "finalResult": "SUCCESS",
      "contractRet": "SUCCESS",
      "confirmed": true,
      "cheatStatus": false,
      "riskTransaction": false,
      "fromAddressIsContract": false,
      "toAddressIsContract": false,
      "tokenInfo": {
        "tokenId": "1002000",
        "tokenAbbr": "BTTOLD",
        "tokenName": "BitTorrent Old",
        "tokenDecimal": 6,
        "tokenType": "trc10",
        "vip": true
      }
    },
    {
      "blockId": 49964306,
      "transactionHash": "b79781695a314c030e4bdcbb088666b91c7661bc23142e7181d12955da88ddf4",
      "timestamp": 1680505686000,
      "transferFromAddress": "TMG43Y5LnnT8sfU98oXYcUSKsvXFuUMac8",
      "transferToAddress": "TCRnxaac1TbdGMy3RtArZeFQdEL3GWfj14",
      "amount": 4300000000,
      "tokenName": "1002000",
      "finalResult": "SUCCESS",
      "contractRet": "SUCCESS",
      "confirmed": true,
      "cheatStatus": false,
      "riskTransaction": false,
      "fromAddressIsContract": false,
      "toAddressIsContract": false,
      "tokenInfo": {
        "tokenId": "1002000",
        "tokenAbbr": "BTTOLD",
        "tokenName": "BitTorrent Old",
        "tokenDecimal": 6,
        "tokenType": "trc10",
        "vip": true
      }
    }
  ]
}
```

---

## Get inventory information of a TRC1155

Returns TRC1155 inventory information.

The value sum of `start` and `limit` must be less than or equal to **10000**. The maximum value for `limit` is **50**.

```
GET https://apilist.tronscanapi.com/api/trc1155/inventory?contract=TREYLQ3i56GTQnaQn68woKHtDkVTcFKHjN&tokenId=&limit=2&start=0&sort=-tokenId
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/trc1155/inventory?contract=TREYLQ3i56GTQnaQn68woKHtDkVTcFKHjN&tokenId=&limit=2&start=0&sort=-tokenId) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `20` |
| `contract` | TRC1155 contract address (required) |
| `tokenId` | The ID of a token in TRC1155 |
| `sort` | `-tokenId`: descending by tokenId. `tokenId`: ascending by tokenId |

### Response

```
{
  "total": 2,
  "rangeTotal": 2,
  "page_size": 2,
  "code": 200,
  "data": [
    {
      "token_id": "2",
      "holders_count": 1,
      "token_name": "Mutant Ape #2",
      "token_description": "Number one Bored Ape Club bringing Mutant Apes on Tron Network",
      "token_image": "https://ipfs.io/ipfs/QmdsxYwtbDKmx6fz6CP5FLCH3hkkuZ3EDBFBTcHHRrsSRM",
      "token_imageInnerUrl": "https://static.tronscan.org/production/upload/logo/98/988e5fe9cc0c7b50e795d3f7f87a2978.png",
      "latest_transfer_timestamp": 1657090707000,
      "token_url": ""
    },
    {
      "token_id": "1",
      "holders_count": 5,
      "token_name": "Mutant Ape #1",
      "token_description": "Number one Bored Ape Club bringing Mutant Apes on Tron Network",
      "token_image": "https://ipfs.io/ipfs/QmVFPvu8aeJHXyNVxpfftVHaKjRsbtH6dXWscJ2TukM3xi",
      "token_imageInnerUrl": "https://static.tronscan.org/production/upload/logo/75/75d37b177b9a7c60d5a80f463ba624f2.png",
      "latest_transfer_timestamp": 1661310345000,
      "token_url": ""
    }
  ]
}
```

---

## Get the holding information of a certain tokenId in TRC1155

Returns the holding information of a token in TRC1155.

The value sum of `start` and `limit` must be less than or equal to **10000**. The maximum value for `limit` is **50**.

```
GET https://apilist.tronscanapi.com/api/trc1155/token/inventory?contract=TREYLQ3i56GTQnaQn68woKHtDkVTcFKHjN&limit=2&start=0&tokenId=1
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/trc1155/token/inventory?contract=TREYLQ3i56GTQnaQn68woKHtDkVTcFKHjN&limit=2&start=0&tokenId=1) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `contract` | TRC1155 contract address (required) |
| `tokenId` | The ID of a token in TRC1155 (required) |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `20` |

### Response

```
{
  "total": 5,
  "rangeTotal": 5,
  "page_size": 2,
  "code": 200,
  "data": [
    {
      "token_id": "1",
      "holder_count": "2",
      "owner_address": "TLwiP6eaAvjmPcETN99qZMoPZ65EDK74BH",
      "token_name": "Mutant Ape #1",
      "token_description": "Number one Bored Ape Club bringing Mutant Apes on Tron Network",
      "token_image": "https://ipfs.io/ipfs/QmVFPvu8aeJHXyNVxpfftVHaKjRsbtH6dXWscJ2TukM3xi",
      "token_imageInnerUrl": "https://static.tronscan.org/production/upload/logo/75/75d37b177b9a7c60d5a80f463ba624f2.png",
      "token_url": ""
    },
    {
      "token_id": "1",
      "holder_count": "5",
      "owner_address": "TJezP5s9U1SN44qM1JyzdAyQ3dmZATcogF",
      "token_name": "Mutant Ape #1",
      "token_description": "Number one Bored Ape Club bringing Mutant Apes on Tron Network",
      "token_image": "https://ipfs.io/ipfs/QmVFPvu8aeJHXyNVxpfftVHaKjRsbtH6dXWscJ2TukM3xi",
      "token_imageInnerUrl": "https://static.tronscan.org/production/upload/logo/75/75d37b177b9a7c60d5a80f463ba624f2.png",
      "token_url": ""
    }
  ]
}
```

---

## Get the circulation of a TRC20 token

Returns the circulation of a TRC20 token.

```
GET https://apilist.tronscanapi.com/api/token_trc20/totalSupply?address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/token_trc20/totalSupply?address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | TRC20 contract address |

### Response

```
44125091014.551106
```

---

## Get inventory information of a TRC721

Returns the inventory information of tokens in TRC721.

The value sum of `start` and `limit` must be less than or equal to **10000**. The maximum value for `limit` is **50**.

```
GET https://apilist.tronscanapi.com/api/trc721/token?contract=THjYwnDDN6aYxrzKb88CSMTEYjBuHpoYxS&tokenId=&limit=2&start=0&ownerAddress=&sort=-tokenId
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/trc721/token?contract=THjYwnDDN6aYxrzKb88CSMTEYjBuHpoYxS&tokenId=&limit=2&start=0&ownerAddress=&sort=-tokenId) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `contract` | TRC721 contract address (required) |
| `tokenId` | The ID of a token in TRC721 |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `20` |
| `ownerAddress` | TRC721 token holder address |
| `sort` | `tokenId`: ascending order. `-tokenId`: descending order |

### Response

```
{
  "total": 10000,
  "rangeTotal": 856684,
  "page_size": 2,
  "code": 200,
  "data": [
    {
      "token_id": "965650",
      "owner_address": "TNLjmMrKwAxPXabtgdLGdF1DG17kQKHZg2",
      "owner_address_tag": "",
      "token_name": "965650",
      "token_description": "Devikin are the playable characters of the blockchain game Devikins.",
      "token_image": "https://img.devikins.com/9/965650.png",
      "token_url": "https://marketplace.devikins.com/devikin/965650",
      "token_imageInnerUrl": "https://static.tronscan.org/production/upload/logo/00/0078186f4893cb0b57c5799da8bec800.png",
      "latest_transfer_timestamp": 1670256540000
    },
    {
      "token_id": "965649",
      "owner_address": "TERfaJdmMPQEAsDjVcnwUUFxDgRAfqucaP",
      "owner_address_tag": "",
      "token_name": "965649",
      "token_description": "Devikin are the playable characters of the blockchain game Devikins.",
      "token_image": "https://img.devikins.com/9/965649.png",
      "token_url": "https://marketplace.devikins.com/devikin/965649",
      "token_imageInnerUrl": "https://static.tronscan.org/production/upload/logo/11/11748026721660209d0f007329ea09dd.png",
      "latest_transfer_timestamp": 1670254638000
    }
  ]
}
```