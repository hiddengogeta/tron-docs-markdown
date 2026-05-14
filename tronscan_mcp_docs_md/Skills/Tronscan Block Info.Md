

# Block Info

**Skill ID**: `tronscan-block-info`

**ClawHub**: [clawhub.ai/sshnii/tronscan-block-info](https://clawhub.ai/sshnii/tronscan-block-info)

Query block information on the TRON blockchain: latest block height, producing node, block time, transaction count, TRX burned, and network load statistics.

This skill applies to **block queries** only. For real-time TPS and network overview, use **tronscan-realtime-network**; to look up a transaction by hash, use **tronscan-transaction-info**.

---

## Use Cases

### Query the Latest Block

* `getLatestBlock` — Block number, hash, size, timestamp, producing node, and transaction count of the most recent confirmed block

`getLatestBlock` calls `/api/block/latest` under the hood and **does not return** fields such as `witnessName`, `fee`, `energyUsage`, `blockReward`, `voteReward`, `confirmations`, or `netUsage` — these will appear as `0` or `null` in the response and should be ignored. If you need those fields, use `getBlocks` instead.

Example prompts:

```
"What is the current block height on TRON?"
"What is the hash of the latest block?"
"How many transactions does the latest block contain?"
```

---

### Query Block List and Producing Nodes

* `getBlocks` — Paginated block list with filtering by producing node address, time range, and sort order

Example prompts:

```
"Which nodes produced the last 10 blocks?"
"Show the blocks produced by address TXxx..."
"How many blocks were produced in the past hour?"
"What is the block reward for this block?"
```

---

### Query Block Statistics and TRX Burned

* `getBlockStatistic` — 24-hour aggregated data: total fees paid, block count, and total TRX burned

Example prompts:

```
"How much TRX was burned in the past 24 hours?"
"What are today's block statistics?"
"What is the current network load?"
```

---

## Installation

### Confirm TronScan MCP Is Connected

Refer to [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-block-info)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-block-info
```