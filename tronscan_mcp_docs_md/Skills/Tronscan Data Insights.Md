

# Data Insights

**Skill ID**: `tronscan-data-insights`

**ClawHub**: [clawhub.ai/sshnii/tronscan-data-insights](https://clawhub.ai/sshnii/tronscan-data-insights)

Get global insights into the TRON network: daily new addresses, transaction volume statistics, transaction type distribution, popular tokens and contracts, and top account rankings (by transaction count or staked TRX).

This skill is not suitable for the following scenarios: for individual token details use **tronscan-token-scanner**; for single-address profiling use **tronscan-account-profiler**; for transfer count or transfer amount rankings of non-TRX tokens, use other skills.

---

## Use Cases

### Query Daily New Addresses

* `getDailyAccounts` — Daily new address count (`newAddressSeen`), supports queries up to 2,000 days back

`getDailyAccounts` returns the number of **new addresses seen per day** (`newAddressSeen`), which can serve as an activity reference only — **it is not equivalent to precise DAU (Daily Active Users)**. If a user asks about DAU, you must first clarify that this metric reflects new addresses and cannot be presented as an accurate DAU figure.

Example prompts:

```
"How many new addresses does TRON add each day over the past 30 days?"
"What is the trend of new account growth on the network over the past month?"
```

---

### Query Daily Transaction Volume and Contract Calls

* `getTransactionStatistics` — Aggregated statistics including total transaction count and token transaction volume
* `getTriggerStatistic` — Daily smart contract call counts within a specified time range
* `getTransferStatistics` — Transfer statistics categorized by token type

Example prompts:

```
"What was the total transaction count on TRON yesterday?"
"How did smart contract call volume change over the past 7 days?"
"What percentage of transfers are TRC20?"
```

---

### Query Popular Tokens and Contracts

* `getHotSearch` — Trending tokens and contracts with price and activity metrics

Example prompts:

```
"What are the most popular tokens on TRON right now?"
"Which contracts have seen a spike in call volume recently?"
```

---

### Query Top Account Rankings

* `getTop10` — Top 10 rankings across multiple dimensions (by transaction count, staked TRX, etc.)

Example prompts:

```
"Which are the top 10 addresses by transaction count?"
"What is the ranking of accounts with the most staked TRX?"
"Which addresses had the most TRX transfers yesterday?"
```

---

### Query Network Overview and TPS

* `getHomepageData` — Network overview including TPS, node count, TVL, and frozen amount
* `getCurrentTps` — Current TPS, latest block height, and all-time peak TPS

Example prompts:

```
"What is the current TPS on TRON?"
"How many nodes are on the network right now?"
"Give me an overall overview of the TRON network."
```

---

## Installation

### Confirm TronScan MCP Is Connected

Refer to [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-data-insights)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-data-insights
```