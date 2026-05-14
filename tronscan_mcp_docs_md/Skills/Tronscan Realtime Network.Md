

# Realtime Network Data

**Skill ID**: `tronscan-realtime-network`

**ClawHub**: [clawhub.ai/sshnii/tronscan-realtime-network](https://clawhub.ai/sshnii/tronscan-realtime-network)

Query the TRON network status in real time: confirmed block height, current TPS, node count, TVL, total transaction count, and Super Representative vote tallies.

This skill is for **real-time data** queries only. For historical trend analysis use **tronscan-data-insights**; for block details use **tronscan-block-info**.

---

## Use Cases

### Query the Latest Confirmed Block Height

* `getLatestBlock` — Returns the latest **solidified block**, not the chain-head block
* `getCurrentTps` — Returns the chain-head block height

`getLatestBlock` returns the **solidified block**, which may lag behind the chain-head. If a user asks for the “latest block height” or “current block,” clarify that the result is the solidified block and may differ from the chain head. For the chain-head height, use `getCurrentTps` instead.

In addition, fields such as `witnessName`, `fee`, `energyUsage`, `blockReward`, `voteReward`, `confirmations`, and `netUsage` from `getLatestBlock` may return `0` or `null` — this is expected behavior. If you need those fields, use `getBlocks` from **tronscan-block-info** instead.

Example prompts:

```
"What is the current confirmed block height on TRON?"
"What is the hash of the latest solidified block?"
"What is the current chain-head block height?"
```

---

### Query Real-Time TPS

* `getCurrentTps` — Current TPS, latest block height, and all-time peak TPS
* `getHomepageData` — TPS data as part of the network overview

Example prompts:

```
"What is the current TPS on TRON?"
"What is the all-time peak TPS?"
"What is the network throughput right now?"
```

---

### Query Node Count and Distribution

* `getHomepageData` — Total node count across the network
* `getNodeMap` — Real-time node information and geographic distribution

Example prompts:

```
"How many nodes does TRON currently have?"
"What regions are nodes mainly distributed in?"
```

---

### Query TVL and Network Overview

* `getHomepageData` — Full network overview including TPS, node count, TVL, and frozen amount

Example prompts:

```
"What is the current TVL on TRON?"
"Give me a real-time overview of the TRON network."
```

---

### Query Total Transaction Count and Live Votes

* `getTransactionStatistics` — Total network transaction count and aggregated token transaction volume
* `getWitnessGeneralInfo` — Total vote count, block statistics, and number of Super Representatives

Example prompts:

```
"What is the all-time total transaction count on TRON?"
"What is the current total vote count across the network?"
"How many Super Representatives are there right now?"
```

---

## Installation

### Confirm TronScan MCP Is Connected

Refer to [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-realtime-network)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-realtime-network
```