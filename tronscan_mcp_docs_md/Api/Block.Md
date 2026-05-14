

# Block

## Get the list of blocks or details of one block

Returns the blocks info.

The value sum of `start` and `limit` must be less than or equal to **10000**.

```
GET https://apilist.tronscanapi.com/api/block?sort=-number&start=0&limit=20&producer=&number=&start_timestamp=&end_timestamp=
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/block?sort=-number&start=0&limit=20&producer=&number=&start_timestamp=&end_timestamp=) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Default: `10`, Max: `50` |
| `number` | Optional. Block number. When provided, returns details of that single block and ignores `start_timestamp` / `end_timestamp` |
| `producer` | Super representative address |
| `sort` | Sort fields, only supports sorting by block number. Use `-` prefix for descending order. Default: `-number` |
| `start_timestamp` | Start timestamp (in milliseconds). Default: `0` |
| `end_timestamp` | End timestamp (in milliseconds). Defaults to current time |

### Response

```
{
  "total": 10000,
  "rangeTotal": 49853230,
  "data": [
    {
      "number": 49853229,
      "hash": "0000000002f8b32dc29f7bae3878395dfebbb7b6cdb907275fa34d62d4f7f4c1",
      "size": 112407,
      "timestamp": 1680172356000,
      "txTrieRoot": "4zHkjDXP6949NPAEFETxtcpRj1TdpqBwUPYfEQDsF6PdERsAM",
      "parentHash": "0000000002f8b32c3594a370e65928480f1e5a9368a68d4c12d636c0b394a470",
      "witnessId": 0,
      "witnessAddress": "TMafrJCuNoYq3mg9dDThfg7c9VP6enZN6j",
      "nrOfTrx": 446,
      "witnessName": "metaverse home",
      "version": "27",
      "fee": 3010.57726,
      "confirmed": false,
      "confirmations": 1,
      "netUsage": 136470,
      "energyUsage": 7962299,
      "OtherFeeTrx": 0,
      "otherFeeMap": {
        "accountActivationFee": "0.1"
      },
      "bandwidthConsumedFromBurnCnt": 0,
      "freeBandwidthUsageCnt": 136470,
      "bandwidthBurnFeeSunAmt": 0,
      "energyConsumedFromOwnerBurnCnt": 0,
      "freeEnergyUsageCnt": 7962299,
      "energyBurnFeeSunAmt": 0,
      "blockReward": 16,
      "voteReward": 160,
      "revert": false
    },
    {
      "number": 49853228,
      "hash": "0000000002f8b32c3594a370e65928480f1e5a9368a68d4c12d636c0b394a470",
      "size": 77408,
      "timestamp": 1680172353000,
      "txTrieRoot": "uFM3tvLH9MWiSVvs7Sea1qPxinUsizracPji7bBuYYHVAjRKt",
      "parentHash": "0000000002f8b32be841a2381555f0f204f0b70ee58c77bba7911dd80ddc952f",
      "witnessId": 0,
      "witnessAddress": "TDpt9adA6QidL1B1sy3D8NC717C6L5JxFo",
      "nrOfTrx": 334,
      "witnessName": "Chain Cloud",
      "version": "27",
      "fee": 691.76672,
      "confirmed": false,
      "confirmations": 2,
      "netUsage": 95603,
      "energyUsage": 3482059,
      "OtherFeeTrx": 0,
      "bandwidthConsumedFromBurnCnt": 0,
      "freeBandwidthUsageCnt": 95603,
      "bandwidthBurnFeeSunAmt": 0,
      "energyConsumedFromOwnerBurnCnt": 0,
      "freeEnergyUsageCnt": 3482059,
      "energyBurnFeeSunAmt": 0,
      "blockReward": 16,
      "voteReward": 160,
      "revert": false
    }
  ]
}
```

---

## Get statistical information of blocks

Returns the statistic information of blocks.

```
GET https://apilist.tronscanapi.com/api/block/statistic
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/block/statistic) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "last_day_pay": 5067392,
  "last_day_block_count": 28792,
  "last_day_total_burn": 5.901546129160072e9,
  "whole_block_count": 49852969,
  "whole_pay": 6952840208,
  "last_day_burn": 2.0858019799059868e7
}
```