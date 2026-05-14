

# Witness

List of witness interfaces.

## Get the list of witnesses

Returns a list of witnesses.

```
GET https://apilist.tronscanapi.com/api/pagewitness?witnesstype=0
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/pagewitness?witnesstype=0) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `witnesstype` | The type of value returned. `0` (or omitted): All types (default). `1`: Super Representative (top 27). `2`: Partner (rank 28–127). `3`: Candidate. Default: `0` |
| `start` | Offset from the beginning of the result set. Default: `0` |
| `limit` | Number of records to return. Default: `500` |
| `sort` | Sort direction. `0`: ascending (default). `1`: descending |
| `sortField` | Field to sort by. Valid values: `votes`, `latestBlock`, `producedTotal`, `missedTotal`, `producePercentage`, `annualizedRate`, `brokerage`, `voterBrokerage`. No sorting is applied when omitted or invalid |

### Response

```
{
  "total": 391,
  "lastBlock": {
    "hash": "0000000002fa75eec688726acae70af8a047f91e7d06d0c8801c167d0f38b562",
    "confirmed": true,
    "number": 49968622,
    "size": 56734,
    "timestamp": 1680518634000,
    "parentHash": "0000000002fa75ed0041c7b8b5e50d58b8a1a6f3073f9bccf60ad7d74f80f2a5",
    "witnessAddress": "TNaJADoq1u2atryP1ZzwvmEE4ZBELXfMqw",
    "nrOfTrx": 238,
    "txTrieRoot": "LQevPRnxfFyFmP8n4iMtkufQzVi7DVuauhTNo411oJGkzMsbU",
    "witnessId": 0
  },
  "data": [
    {
      "address": "TSMC4YzUSfySfqKuFnJbYyU3W6PBebBk2E",
      "name": "Smart Consensus",
      "url": "SmartConsensus",
      "producer": true,
      "latestBlockNumber": 49968605,
      "latestSlotNumber": 560172861,
      "missedTotal": 38,
      "producedTotal": 487865,
      "producedTrx": 0,
      "votes": 1903228100,
      "lastCycleVotes": 1903228100,
      "changeVotes": -919135,
      "realTimeVotes": 1902308965,
      "brokerage": 0,
      "voterBrokerage": 100,
      "annualizedRate": "4.628304",
      "producePercentage": 99.99221156664338,
      "version": 27,
      "witnessType": 1,
      "index": 1,
      "ranking": 1,
      "totalOutOfTimeTrans": 2738,
      "lastWeekOutOfTimeTrans": 0,
      "changedBrokerage": false,
      "lowestBrokerage": 100,
      "votesPercentage": 4.8305368093189225,
      "logoUrl": "https://example.com/logo.png"
    }
  ]
}
```

---

## Get the list of votes for the account

Returns a list of votes for the account.

```
GET https://apilist.tronscanapi.com/api/account/votes?address=TWSRE85rP7FydZKjHmmZgCYF5Dbw8AB91J
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/account/votes?address=TWSRE85rP7FydZKjHmmZgCYF5Dbw8AB91J) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Account address |

### Response

```
{
  "votes": {
    "TTW663tQYJTTCtHh6DWKAfexRhPMf2DxQ1": 10
  }
}
```

---

## Get the list of parameters in the chain

Returns the list of parameters in the chain.

```
GET https://apilist.tronscanapi.com/api/chainparameters
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/chainparameters) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "tronParameters": [
    {
      "key": "getMaintenanceTimeInterval",
      "value": 21600000,
      "initValue": 21600000,
      "relations": [
        {
          "id": 1,
          "key": 0,
          "value": 21600000,
          "expiration_time": 1680000000000,
          "state": "APPROVED"
        }
      ]
    },
    {
      "key": "getAccountUpgradeCost",
      "value": 9999000000,
      "initValue": 9999000000,
      "relations": []
    }
  ]
}
```

---

## Get the list of proposals

Returns the proposal details of the master chain based on the proposal ID and marks whether the address is the initiator or participant.

The maximum value for `limit` is **200**.

```
GET https://apilist.tronscanapi.com/api/proposal?limit=20&start=0&address=TWSRE85rP7FydZKjHmmZgCYF5Dbw8AB91J
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/proposal?limit=20&start=0&address=TWSRE85rP7FydZKjHmmZgCYF5Dbw8AB91J) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `start` | Start number. Default: `0` |
| `limit` | Number of items per page. Minimum: `20`. Default: `20` |
| `address` | Shows whether the address is an initiator or a participant |
| `id` | Proposal ID |
| `state` | Filter by proposal state. Valid values: `PENDING`, `APPROVED`, `DISAPPROVED`, `CANCELED` |

### Response

```
{
  "total": 51,
  "data": [
    {
      "proposalId": 83,
      "proposer": {
        "address": "TVFKwzE8qeETLaZEHMx2tjEsdnujAgAWaA",
        "name": "BlockchainOrg",
        "url": "http://blockchain.org",
        "producer": true,
        "votes": 1510416677,
        "producedTotal": 1607459,
        "missedTotal": 2978,
        "producePercentage": 99.81508124813327,
        "votesPercentage": 3.833551719658652,
        "latestBlockNumber": 49969313,
        "latestSlotNumber": 560173569,
        "producedTrx": 0
      },
      "proposalHash": "0bce347c6c5cae85d3f6eb3830afa5077068c2acfa57ad4ea495cb009056b8b9",
      "paramters": [
        { "key": 72, "value": 1 },
        { "key": 73, "value": 3000000000 },
        { "key": 74, "value": 2000 },
        { "key": 75, "value": 12000 }
      ],
      "expirationTime": 1675576800000,
      "createTime": 1675315965000,
      "approveSelf": false,
      "state": "APPROVED",
      "totalVotes": 27,
      "validVotes": 22,
      "createSelf": false,
      "typeApprovals": {
        "candidate": [],
        "partner": [],
        "sr": [
          {
            "address": "TDpt9adA6QidL1B1sy3D8NC717C6L5JxFo",
            "name": "Chain Cloud",
            "url": "http://chaincloud.org",
            "producer": true,
            "votes": 1421479679,
            "producedTotal": 1234567,
            "missedTotal": 123,
            "producePercentage": 99.9,
            "votesPercentage": 3.6078228947483204,
            "latestBlockNumber": 49969300,
            "latestSlotNumber": 560173500,
            "producedTrx": 0
          },
          {
            "address": "TCEo1hMAdaJrQmvnGTCcGT2LqrGU4N7Jqf",
            "name": "TRONScan",
            "url": "https://tronscan.org",
            "producer": true,
            "votes": 1095956900,
            "producedTotal": 987654,
            "missedTotal": 456,
            "producePercentage": 99.95,
            "votesPercentage": 2.7816214708458,
            "latestBlockNumber": 49969310,
            "latestSlotNumber": 560173510,
            "producedTrx": 0
          },
          {
            "address": "TLyqzVGLV1srkB7dToTAEqgDSfPtXRJZYH",
            "name": "Binance Staking",
            "url": "https://www.binance.com",
            "producer": true,
            "votes": 1421491682,
            "producedTotal": 876543,
            "missedTotal": 789,
            "producePercentage": 99.91,
            "votesPercentage": 3.6078533592697943,
            "latestBlockNumber": 49969320,
            "latestSlotNumber": 560173520,
            "producedTrx": 0
          }
        ]
      },
      "approvals": [
        {
          "address": "TDpt9adA6QidL1B1sy3D8NC717C6L5JxFo",
          "name": "Chain Cloud",
          "url": "http://chaincloud.org",
          "producer": true,
          "votes": 1421479679,
          "producedTotal": 1234567,
          "missedTotal": 123,
          "producePercentage": 99.9,
          "votesPercentage": 3.6078228947483204,
          "latestBlockNumber": 49969300,
          "latestSlotNumber": 560173500,
          "producedTrx": 0
        },
        {
          "address": "TCEo1hMAdaJrQmvnGTCcGT2LqrGU4N7Jqf",
          "name": "TRONScan",
          "url": "https://tronscan.org",
          "producer": true,
          "votes": 1095956900,
          "producedTotal": 987654,
          "missedTotal": 456,
          "producePercentage": 99.95,
          "votesPercentage": 2.7816214708458,
          "latestBlockNumber": 49969310,
          "latestSlotNumber": 560173510,
          "producedTrx": 0
        }
      ],
      "veto": [
        {
          "address": "TWvncFqyDfMcKfjsx4hvoWwhJfF5yKMZcU",
          "name": "http://foo.bar",
          "url": "http://foo.bar",
          "producer": true,
          "votes": 996631644,
          "producedTotal": 765432,
          "missedTotal": 321,
          "producePercentage": 99.96,
          "votesPercentage": 2.5295264617383655,
          "latestBlockNumber": 49969330,
          "latestSlotNumber": 560173530,
          "producedTrx": 0
        },
        {
          "address": "TBsyKdNsCKNXLgvneeUJ3rbXgWSgk6paTM",
          "name": "StakedTron",
          "url": "https://stakedtron.com",
          "producer": true,
          "votes": 705558329,
          "producedTotal": 654321,
          "missedTotal": 654,
          "producePercentage": 99.9,
          "votesPercentage": 1.790760381982617,
          "latestBlockNumber": 49969340,
          "latestSlotNumber": 560173540,
          "producedTrx": 0
        }
      ]
    }
  ]
}
```

---

## Get the current voting information of witness

Returns the current voting information of a witness.

```
GET https://apilist.tronscanapi.com/api/vote/witness?address=TSMC4YzUSfySfqKuFnJbYyU3W6PBebBk2E
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/vote/witness?address=TSMC4YzUSfySfqKuFnJbYyU3W6PBebBk2E) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `address` | Account address |

### Response

```
{
  "success": "true",
  "data": {
    "lastRanking": 1,
    "realTimeRanking": 1,
    "address": "TSMC4YzUSfySfqKuFnJbYyU3W6PBebBk2E",
    "name": "Smart Consensus",
    "url": "SmartConsensus",
    "hasPage": false,
    "lastCycleVotes": 1926023286,
    "realTimeVotes": 1923188661,
    "changeVotes": -2834625,
    "brokerage": 0,
    "voterBrokerage": 100,
    "logoUrl": "https://example.com/logo.png",
    "votesPercentage": 4.895789412784719,
    "lastCycleVotesPercentage": 4.875509336280341,
    "change_cycle": 0,
    "witnessType": 1,
    "annualizedRate": "4.599307",
    "producedTotal": 488739,
    "producedEfficiency": 99.99222549342542,
    "blockReward": 7819824,
    "version": 27,
    "totalOutOfTimeTrans": 2738,
    "lastWeekOutOfTimeTrans": 0,
    "changedBrokerage": false,
    "lowestBrokerage": 100,
    "realtimeVoteLine": [
      { "time": 1680480000000, "vote": 1926023286 },
      { "time": 1680501600000, "vote": 1918600587 },
      { "time": 1680523200000, "vote": 1917205073 },
      { "time": 1680544800000, "vote": 1916617107 },
      { "time": 1680566400000, "vote": 1903228100 },
      { "time": 1680588000000, "vote": 1902605691 }
    ]
  },
  "totalWitness": 391,
  "changedBrokerage": false,
  "lowestBrokerage": 100,
  "brokerageHistory": [
    {
      "from": 100,
      "to": 100,
      "time": 1640850534,
      "hash": "67e9fd98b4952b0bdde0abc4d321fc4efad4847060911be61b3c730c01526ee3"
    }
  ],
  "brokerageChangeNum": 1
}
```

---

## Get statistics for the witness homepage

Returns statistics for the witness homepage.

```
GET https://apilist.tronscanapi.com/api/witness/general-info
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/witness/general-info) ↗ 🔗

RequestResponse

### Request

No parameters required.

### Response

```
{
  "total": 391,
  "increaseOf30Day": 2,
  "totalRealtimeVotes": 39351582658,
  "minBlocksCount": {
    "address": "TAQpCTFeJvwdWf6MQZtXXkzWrTS9aymshb",
    "name": "Valkyrie_Investments",
    "url": "https://valkyrieinvest.com",
    "missedTotal": 0,
    "producedTotal": 46928,
    "producePercentage": 100,
    "currentProducePercentage": 100      },
  "highestEfficiency": {
    "address": "TAQpCTFeJvwdWf6MQZtXXkzWrTS9aymshb",
    "name": "Valkyrie_Investments",
    "url": "https://valkyrieinvest.com",
    "missedTotal": 0,
    "producedTotal": 46928,
    "producePercentage": 100,
    "currentProducePercentage": 100      },
  "lowestEfficiency": {
    "address": "TN2W4cc7a4dsYyTLiLMWa9m7jVpdLjGvYs",
    "name": "Huobi_Wallet",
    "url": "https://www.huobiwallet.com/",
    "missedTotal": 9519,
    "producedTotal": 644571,
    "producePercentage": 98.54469568408018,
    "currentProducePercentage": 98.54469568408018      },
  "maxBlocksCount": {
    "address": "TTcYhypP8m4phDhN6oRexz2174zAerjEWP",
    "name": "CryptoGuyInZA",
    "url": "https://www.cryptoguyinza.co.za/",
    "missedTotal": 3074,
    "producedTotal": 1828518,
    "producePercentage": 99.83216786271178,
    "currentProducePercentage": 99.83216786271178      }
}
```