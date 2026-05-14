

# Account Profiler

**Skill ID**: `tronscan-account-profiler`

**ClawHub**: [clawhub.ai/sshnii/tronscan-account-profiler](https://clawhub.ai/sshnii/tronscan-account-profiler)

Perform a complete profile of any wallet address: TRX balance, token holdings, total asset value, DeFi participation, Stake 1.0/2.0 energy and bandwidth resources, voting records, and transaction statistics.

This skill applies to **wallet addresses** only. If your primary question involves contract identification, verification status, or frequently called methods, switch to the **tronscan-contract-analysis** skill instead.

---

## Use Cases

### Query TRX Balance and Resource Status

* `getAccountDetail` — TRX balance, total transaction count, free and staked bandwidth/energy, activation status
* `getAccountResource` / `getAccountResourceV2` — Detailed staking records broken down by resource type

Example prompts:

```
"What is the TRX balance of address TLv...?"
"How much energy and bandwidth does this address have left?"
"Is this address activated on TRON?"
```

---

### List Token Holdings and Total Asset Value

* `getAccountTokens` — Paginated token list (supports filtering by TRC20/TRC721/TRC1155)
* `getTokenAssetOverview` — Summary view: total asset value, individual token balances, and USD estimates

`getAccountTokens` only returns tokens with a balance greater than 0. Use the `show` parameter to filter by type: `1` = TRC20, `2` = TRC721, `4` = TRC1155, `3` = All.

Example prompts:

```
"What tokens does address TXxx... hold?"
"What is the total USD value of this wallet?"
"Show all NFTs held by this address."
```

---

### View DeFi Participation and SR Votes

* `getParticipatedProjects` — List of DeFi protocols with position type, currency, and USD value
* `getVoteList` — Target Super Representatives and vote counts

Example prompts:

```
"Which DeFi projects is this address participating in?"
"Which Super Representatives has this address voted for?"
"How much TRX does this wallet have staked in DeFi?"
```

---

### Analyze Historical Account Activity

* `getAccountAnalysis` — Daily time series of balance, transfer count, energy/bandwidth consumption, and transaction count

| `type` Value | Data Returned |
| --- | --- |
| `0` | Daily TRX balance and day’s price |
| `1` | Daily transfer count and number of unique tokens involved |
| `2` | Daily energy consumption breakdown |
| `3` | Daily bandwidth consumption breakdown |
| `4` | Daily initiated and received transaction counts |

Example prompts:

```
"Show the TRX balance changes for this address over the past 30 days."
"How much energy did this address consume last week?"
```

---

## Installation

### Confirm TronScan MCP Is Connected

Refer to [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-account-profiler)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-account-profiler
```