

# Contract Analysis

**Skill ID**: `tronscan-contract-analysis`

**ClawHub**: [clawhub.ai/sshnii/tronscan-contract-analysis](https://clawhub.ai/sshnii/tronscan-contract-analysis)

Perform a comprehensive analysis of any TRON contract address: deployment information, verification status, popular call methods, top callers, energy consumption, and historical contract activity.

This skill applies to **contract addresses** only. For token supply and holder distribution, use **tronscan-token-scanner**; for wallet balance queries, use **tronscan-account-profiler**.

---

## Use Cases

### Query Contract Details and Verification Status

* `getContractDetail` — Balance, verification status, call count, and method mappings

Example prompts:

```
"Is contract TXxx... open-source and verified?"
"What is the total number of calls to this contract?"
"What is the balance of this contract address?"
```

---

### Query Popular Methods and Top Callers

* `getContractCallStatistic` — Call count, top callers, and most-used methods
* `getContractCallers` — Full caller list with call counts for a specified date

Example prompts:

```
"What is the most frequently called method on this contract?"
"Who are the top 5 callers of this contract?"
"Which addresses called this contract today?"
```

---

### Query Contract Events and Triggered Transactions

* `getContractEvents` — Transfer events and method call records
* `getContractTriggerTransactions` — Contract-triggered transactions within a specified time range

Example prompts:

```
"What events has this contract triggered recently?"
"Which transactions called this contract in the past 24 hours?"
```

---

### Analyze Energy Consumption and Historical Activity

* `getContractEnergyStatistic` — Total energy consumed by the contract and daily consumption breakdown
* `getContractAnalysis` — Daily balance, transfer count, energy/bandwidth consumption, call count, and fees

Example prompts:

```
"How much energy has this contract consumed?"
"Show the activity trend for this contract over the past 30 days."
```

---

### Search Contract List

* `getContractList` — Search by name or address keyword, with sorting and pagination support

Example prompts:

```
"Search for contracts whose name contains 'swap'."
"List popular contracts ranked by call count."
```

---

## Installation

### Confirm TronScan MCP Is Connected

Refer to [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-contract-analysis)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-contract-analysis
```