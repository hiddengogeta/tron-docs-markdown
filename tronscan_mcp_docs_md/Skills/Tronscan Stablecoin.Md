

# Stablecoin Analysis

**Skill ID**: `tronscan-stablecoin`  
**ClawHub**: [clawhub.ai/sshnii/tronscan-stablecoin](https://clawhub.ai/sshnii/tronscan-stablecoin)

This skill covers comprehensive analysis of the stablecoin ecosystem on the TRON network, supporting USDT, USDC, USDD, and TUSD. You can query supply and circulation trends, holder structures, large transaction monitoring, blacklisted frozen addresses, liquidity pool status, and TVL distribution, as well as track key on-chain events such as minting, burning, and freezing.

This skill is designed for comprehensive stablecoin ecosystem queries and analysis. For in-depth analysis of a single token, use **tronscan-token-scanner**. For browsing general token lists, use **tronscan-token-list**.

---

## Use Cases

### Stablecoin Overview & Supply

* `getStableCoinOverview` — Get the supply and holder count overview for a specific stablecoin; token address is optional
* `getStableCoinTotalSupply` — Get the current total circulating supply of all stablecoins on TRON combined
* `getStableCoinTotalSupplyChange` — Get a historical chart of total supply changes, filterable by time range
* `getStableCoinTokenSupplyTurnover` — Get the supply and circulation trend for a specific stablecoin (USDD / USDC / TUSD)

Example prompts:

```
"How much USDT is currently on TRON?"
"What is the trend of total stablecoin supply over the past month?"
"Show me the historical supply and circulation trend for USDD."
```

---

### Holder Analysis

* `getStableCoinTopHolders` — Get the top holder leaderboard for each stablecoin, sortable by USDT / USDC / USDD / TUSD, with optional contract address inclusion
* `getStableCoinHolderChange` — Get the daily change trend in the number of stablecoin holders
* `getStableCoinHolderBalanceOverview` — Get the total market cap distribution across all stablecoins for a clear comparison of market share
* `getStableCoinDistribution` — Get the holding concentration distribution for a specific stablecoin
* `getStableCoinDistributionChange` — Get the historical change chart of holding concentration distribution

Example prompts:

```
"Who holds the most USDT?"
"Has the number of stablecoin holders grown this month?"
"What is the market share of USDT versus USDC?"
```

---

### Transfer Activity & Large Transactions

* `getStableCoinTransferAmount` — Get the time-series trend of stablecoin transfer amounts, with optional line chart data overlay
* `getStableCoinBigAmount` — Get large stablecoin transaction records (up to 50), filterable by transaction type including transfers, swaps, adding/removing liquidity, deposits, loans, repayments, and withdrawals

The `types` parameter is required when using `getStableCoinBigAmount`. Pass `types: "0"` to query all types. Other values: 1=transfer in, 2=transfer out, 3=swap, 4=add liquidity, 5=remove liquidity, 6=deposit, 7=loan, 8=repayment, 9=withdrawal.

Example prompts:

```
"What are the largest USDT transfers recently?"
"Has swap activity for stablecoins been active lately?"
"What large stablecoin lending transactions occurred in the last 24 hours?"
```

---

### Blacklist & Key Events

* `getStableCoinBlackList` — Get the list of frozen stablecoin addresses and amounts, sortable by token address or frozen amount
* `getStableCoinKeyEvents` — Get important on-chain events for stablecoins including minting, burning, and freezing, with multi-dimensional filtering by token type, amount range, and time range

Example prompts:

```
"Which USDT addresses are currently frozen?"
"Have there been any large USDT minting events recently?"
"What key operations have occurred for USDC recently?"
```

---

### Liquidity Pools & TVL

* `getStableCoinPoolInfo` — Get detailed information for all stablecoin liquidity pools
* `getStableCoinPoolOverview` — Get a basic overview for a specific pool; pool contract address can be provided
* `getStableCoinPoolChange` — Get the liquidity change chart for a specific pool
* `getStableCoinPoolTrend` — Get trend data for liquidity changes in a specific pool with a custom time range (start time must be after 2022-11-21)
* `getStableCoinTvl` — Get the TVL distribution of stablecoins across liquidity pools, filterable by token address

Note that time parameter units differ by tool: `getStableCoinPoolTrend` uses milliseconds (`startTimestamp` / `endTimestamp`), while other tools use seconds (`startTime` / `endTime`). Please verify the relevant tool documentation before calling.

Example prompts:

```
"What are the main stablecoin liquidity pools on TRON right now?"
"How much TVL is locked in stablecoin DeFi pools?"
"How has liquidity changed in this pool over the past month?"
```

---

## Installation

### Confirm TronScan MCP is Connected

Refer to the [Getting Started](/en/skills/getting-started) guide.

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-stablecoin)

Copy the page link and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-stablecoin
```