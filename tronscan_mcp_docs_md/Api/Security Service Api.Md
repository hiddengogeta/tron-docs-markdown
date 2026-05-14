

# Security Service API

## Check account security

Returns risk flags for a specific account address, including fraud transaction history, fraud token creation, advertising spam, and stablecoin blacklist status.

```
GET https://apilist.tronscanapi.com/api/security/account/data?address=TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/security/account/data?address=TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Account address to check |

### Response

```
{
  "send_ad_by_memo": false,
  "has_fraud_transaction": false,
  "fraud_token_creator": false,
  "is_black_list": false
}
```

**Response field reference**

| Field | Description |
| --- | --- |
| `send_ad_by_memo` | Whether the account frequently sends advertising via memo |
| `has_fraud_transaction` | Whether the account has fraud transactions |
| `fraud_token_creator` | Whether the account is the creator of fraud tokens |
| `is_black_list` | Whether the account is in the stablecoin blacklist |

---

## Check token security

Returns security attributes for a TRC10, TRC20, TRC721, or TRC1155 token, including VIP status, blacklist capability, supply control, token level, and liquidity.

```
GET https://apilist.tronscanapi.com/api/security/token/data?address=TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/security/token/data?address=TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Token ID for TRC10, or token contract address for TRC20 / TRC721 / TRC1155 |

### Response

```
{
  "is_vip": true,
  "black_list_type": 2,
  "increase_total_supply": 1,
  "token_level": "2",
  "has_url": false,
  "swap_token": true,
  "sun_liquidity": "46004551.623228",
  "open_source": false,
  "is_proxy": false
}
```

**Response field reference**

| Field | Description |
| --- | --- |
| `is_vip` | Whether the token is issued by a well-known institution (in the VIP token list) |
| `black_list_type` | Whether the token contract has a blacklist. `0`: not recognized. `1`: has blacklist. `2`: no blacklist |
| `increase_total_supply` | Whether total supply can be increased. `0`: not recognized. `1`: increase allowed. `2`: increase not allowed |
| `token_level` | Token safety level. `0`: Unknown. `1`: Neutral. `2`: OK. `3`: Suspicious. `4`: Unsafe |
| `has_url` | Whether the token name or symbol contains a URL |
| `swap_token` | Whether the token is listed on sun.io |
| `sun_liquidity` | Token liquidity in USD |
| `open_source` | Whether the token contract is open source |
| `is_proxy` | Whether the token contract uses a proxy contract |

---

## Check URL security

Returns whether a given URL is flagged as a risk (phishing, scam, or malicious) URL.

```
GET https://apilist.tronscanapi.com/api/security/url/data?url=www.google.com.hk
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/security/url/data?url=www.google.com.hk) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `url` | Target URL to check |

### Response

```
{
  "cheat_url": false
}
```

**Response field reference**

| Field | Description |
| --- | --- |
| `cheat_url` | Whether the URL is flagged as a risk URL |

---

## Check transactions security

Returns a per-transaction risk analysis for one or more transaction hashes, identifying zero-value transfers, risk tokens, risk addresses, and same-tail address spoofing attacks.

```
GET https://apilist.tronscanapi.com/api/security/transaction/data?hashes=573fbca36c91193ef2385ff34ab96264f5ce84dd1a8aeef50e21cf46d9178945,fc72dedf9de595db345664a84cb5b9b07017c75989ec71bd0cc45da44bbd2e1a,7413fb017be53822a47d086a45632636e83f0c0bc1fe34f88f9328f167883e3e
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/security/transaction/data?hashes=573fbca36c91193ef2385ff34ab96264f5ce84dd1a8aeef50e21cf46d9178945,fc72dedf9de595db345664a84cb5b9b07017c75989ec71bd0cc45da44bbd2e1a,7413fb017be53822a47d086a45632636e83f0c0bc1fe34f88f9328f167883e3e) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `hashes` | One or more transaction hashes, separated by commas |

### Response

```
{
  "573fbca36c91193ef2385ff34ab96264f5ce84dd1a8aeef50e21cf46d9178945": {
    "riskToken": false,
    "zeroTransfer": false,
    "riskAddress": false,
    "sameTailAttach": true,
    "riskTransaction": true
  },
  "7413fb017be53822a47d086a45632636e83f0c0bc1fe34f88f9328f167883e3e": {
    "riskToken": false,
    "zeroTransfer": true,
    "riskAddress": false,
    "sameTailAttach": false,
    "riskTransaction": true
  },
  "fc72dedf9de595db345664a84cb5b9b07017c75989ec71bd0cc45da44bbd2e1a": {
    "riskToken": false,
    "zeroTransfer": false,
    "riskAddress": true,
    "sameTailAttach": false,
    "riskTransaction": true
  }
}
```

The response is a map keyed by transaction hash. Each entry contains:

| Field | Description |
| --- | --- |
| `riskToken` | Whether the transaction involves a risk token |
| `zeroTransfer` | Whether the transfer amount is 0 |
| `riskAddress` | Whether a risk address is involved |
| `sameTailAttach` | Whether this is a same-tail address spoofing attack (attacker uses an address ending with the same characters as the victim’s) |
| `riskTransaction` | Whether the transaction is overall flagged as a risk |

---

## Check multi-sign security

Returns the multi-signature configuration for an account, including owner permissions, active permissions, and which addresses have been granted each permission type.

```
GET https://apilist.tronscanapi.com/api/security/sign/data?address=THSiB9MT2sCnAUgnYs9euMCY9aiZCD4HB5
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/security/sign/data?address=THSiB9MT2sCnAUgnYs9euMCY9aiZCD4HB5) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Account address to check |

### Response

```
{
  "multiSign": true,
  "multiSignOwnerPermissionAddress": [
    "TKNAHSPfXULFvhYz5YdYcXYitE9xhSkbyY"
  ],
  "multiSignActivePermissionAddress": [
    "TKNAHSPfXULFvhYz5YdYcXYitE9xhSkbyY"
  ],
  "multiSignWitnessPermissionAddress": [],
  "ownerPermission": {
    "permission_name": "owner",
    "threshold": 1,
    "keys": [
      { "address": "THSiB9MT2sCnAUgnYs9euMCY9aiZCD4HB5", "weight": 1 },
      { "address": "TKNAHSPfXULFvhYz5YdYcXYitE9xhSkbyY", "weight": 1 }
    ]
  },
  "activePermissions": [
    {
      "id": 2,
      "type": "Active",
      "permission_name": "active",
      "threshold": 1,
      "operations": "7fff1fc0033efb07000000000000000000000000000000000000000000000000",
      "keys": [
        { "address": "THSiB9MT2sCnAUgnYs9euMCY9aiZCD4HB5", "weight": 1 },
        { "address": "TKNAHSPfXULFvhYz5YdYcXYitE9xhSkbyY", "weight": 1 }
      ]
    }
  ]
}
```

**Response field reference**

| Field | Description |
| --- | --- |
| `multiSign` | Whether multi-signature is enabled on this account |
| `multiSignOwnerPermissionAddress` | Addresses granted owner permissions |
| `multiSignActivePermissionAddress` | Addresses granted active permissions |
| `multiSignWitnessPermissionAddress` | Addresses granted witness permissions |
| `ownerPermission` | Owner permission detail — includes `keys` (address + weight) and `threshold` |
| `activePermissions` | Active permission details — includes `operations`, `keys`, `threshold`, `id`, `type` |

---

## Check account authorization security

Returns a summary and detailed list of token authorizations for an account, highlighting any approvals granted to risk contracts or risk accounts.

```
GET https://apilist.tronscanapi.com/api/security/auth/data?address=THSiB9MT2sCnAUgnYs9euMCY9aiZCD4HB5
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/security/auth/data?address=THSiB9MT2sCnAUgnYs9euMCY9aiZCD4HB5) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Account address to check |

### Response

```
{
  "approveProjectCount": 1,
  "approveTokenCount": 1,
  "approveAddressCount": 1,
  "approveRiskContractCount": 0,
  "approveRiskAccountCount": 1,
  "approveRiskAddressCount": 1,
  "riskApprove": [
    {
      "amount": "1",
      "unlimited": false,
      "from_address": "THSiB9MT2sCnAUgnYs9euMCY9aiZCD4HB5",
      "to_address": "TKNAHSPfXULFvhYz5YdYcXYitE9xhSkbyY",
      "contract_address": "TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf",
      "operate_time": 1689221733000,
      "project_id": "TKNAHSPfXULFvhYz5YdYcXYitE9xhSkbyY",
      "project_sort": 2147483647,
      "tokenInfo": {
        "tokenId": "TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf",
        "tokenAbbr": "USDT",
        "tokenName": "Tether USD",
        "tokenDecimal": 6,
        "tokenCanShow": 1,
        "tokenType": "trc20",
        "tokenLogo": "https://static.tronscan.org/production/logo/usdtlogo.png",
        "tokenLevel": "1",
        "issuerAddr": "THPvaUhoh2Qn2y9THCZML3H815hhFhn5YC",
        "vip": false
      },
      "project": {
        "id": "TKNAHSPfXULFvhYz5YdYcXYitE9xhSkbyY"
      }
    }
  ]
}
```

**Response field reference**

| Field | Description |
| --- | --- |
| `approveProjectCount` | Number of authorized projects |
| `approveTokenCount` | Number of authorized tokens |
| `approveAddressCount` | Number of authorized addresses |
| `approveRiskContractCount` | Number of authorized risk contracts |
| `approveRiskAccountCount` | Number of authorized risk accounts |
| `approveRiskAddressCount` | Total number of authorized risk addresses (`approveRiskContractCount` + `approveRiskAccountCount`) |
| `riskApprove` | List of risk authorizations — each entry contains the approved amount, token info, from/to addresses, contract address, and operation timestamp |

Any address appearing in `riskApprove` has been granted token spending rights to a known risk address or contract. Review and revoke these approvals promptly to protect your assets.

---

## Get all tokens in TronScan

Returns a paginated list of all tokens indexed by TronScan, including TRC10 and TRC20 tokens with metadata, reputation level, price, holder count, transfer stats, and which aggregator platforms they appear on.

```
GET https://apilist.tronscan.org/api/token/all?start=0&limit=50
```

> Try this endpoint in your [**browser**](https://apilist.tronscan.org/api/token/all?start=0&limit=50) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start index |
| `limit` | Number of tokens per page |

### Response

```
{
  "total": 96396,
  "page_size": 2,
  "data": [
    {
      "type": "trc20",
      "contract": "TKU5qFEKRRjx86dWKRYHkZgvxrSoHAbPVX",
      "project": "",
      "symbol": "PKER",
      "name": "PKER",
      "logo": "",
      "decimals": 18,
      "reputation": "1",
      "price": "",
      "total supply": 100000000000,
      "token holders": 3,
      "total transfers": 8,
      "24h transfers": 0,
      "occurrences": 2,
      "aggregators": ["TronScan", "Sunswap"]
    },
    {
      "type": "trc20",
      "contract": "TTe98BF3yQV4fmvGY7fAkfazTNr2dhFUTZ",
      "project": "SunSwap",
      "symbol": "S-TONK-TRX",
      "name": "SUNSWAP-TONK-TRX",
      "logo": "",
      "decimals": 6,
      "reputation": "1",
      "price": "",
      "total supply": 3000,
      "token holders": 1,
      "total transfers": 2,
      "24h transfers": 0,
      "occurrences": 1,
      "aggregators": ["TronScan"]
    }
  ]
}
```

**Response field reference**

| Field | Description |
| --- | --- |
| `total` | Total token count |
| `page_size` | Number of items in this page |
| `type` | Token type (e.g. `trc20`, `trc10`) |
| `contract` | Token contract address or TRC10 token ID |
| `project` | Token’s associated project name |
| `symbol` | Token symbol |
| `name` | Token name |
| `logo` | Token logo URL |
| `decimals` | Token decimal places |
| `reputation` | Token level / reputation score |
| `price` | Token price in USD |
| `total supply` | Total token supply |
| `token holders` | Number of token holders |
| `total transfers` | Total number of transfer transactions |
| `24h transfers` | Number of transfers in the last 24 hours |
| `occurrences` | Number of aggregator platforms the token appears on |
| `aggregators` | List of platforms the token is listed on (e.g. `TronScan`, `Sunswap`, `Coingecko`, `Coinmarketcap`) |