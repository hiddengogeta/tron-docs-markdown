

# Token List

**Skill ID**: `tronscan-token-list`

**ClawHub**: [clawhub.ai/sshnii/tronscan-token-list](https://clawhub.ai/sshnii/tronscan-token-list)

Browse the token list on TRON: sort by price, 24h change, volume, market cap, or holder count to quickly discover trending and high-quality projects.

This skill is for **list browsing and discovery**. For in-depth analysis of a single token, use **tronscan-token-scanner**.

---

## Use Cases

### Browse the TRC20 Token List

* `getTokenList` — Supports filtering by token type and sorting by price, change, volume, market cap, or holder count
* `getPricedTokenList` — Returns all tokens that have price data

Example prompts:

```
"List TRC20 tokens on TRON ranked by market cap."
"Which tokens have the highest 24h trading volume?"
"What is the ranking of tokens by holder count?"
```

---

### Query Hot and Trending Tokens

* `getHotSearch` — Trending tokens and contracts with price and activity metrics
* `getSearchBar` — Current hot search terms and trending token list

Example prompts:

```
"What are the most popular tokens on TRON right now?"
"Which tokens are currently trending upward?"
"What tokens are people searching for lately?"
```

---

### Query Individual Token Details

* `getTrc20TokenDetail` — Full details for TRC20/TRC721/TRC1155 tokens (name, symbol, supply, holders, price, etc.)

Example prompts:

```
"What are the token details for this contract address?"
"What is the 24h trading volume and holder count for this token?"
```

---

## Installation

### Confirm TronScan MCP Is Connected

Refer to [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-token-list)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-token-list
```