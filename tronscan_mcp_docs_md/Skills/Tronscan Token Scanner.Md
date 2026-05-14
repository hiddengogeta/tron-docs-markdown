

# Token Scanner

**Skill ID**: `tronscan-token-scanner`

**ClawHub**: [clawhub.ai/sshnii/tronscan-token-scanner](https://clawhub.ai/sshnii/tronscan-token-scanner)

Perform a deep scan of any individual token on TRON: supply, market cap, price, security rating, launch date, and holder distribution. Supports full information queries for the native TRX token.

This skill is for **single token in-depth analysis**. For token list browsing or trend rankings, use **tronscan-token-list** or **tronscan-data-insights**.

---

## Use Cases

### Query TRX Price, Supply, and Market Cap

* `getTokenPrice` — Current TRX price (default token is TRX)
* `getFunds` — Real-time TRX supply, market cap, and burned amount
* `getTrxVolume` — TRX historical price, trading volume, and market cap data
* `getTurnover` — TRX circulating supply, total supply, and mint/burn statistics

Example prompts:

```
"What is the current price of TRX?"
"What is the total market cap of TRX?"
"What does the historical price trend of TRX look like?"
"How much TRX was minted and burned over the past 30 days?"
```

---

### Query Token Overview

* `getTrc20TokenDetail` — TRC20/TRC721/TRC1155 token details (name, symbol, supply, holders, price, etc.)
* `getTrc10TokenDetail` — TRC10 native asset details (name, issuer, supply, description, etc.)

TRC20/TRC721/TRC1155 tokens use a **contract address**; TRC10 tokens use an **asset ID** — do not mix them up. If the user provides only a token name or symbol, use **tronscan-search** first to resolve it to a contract address.

Example prompts:

```
"What is the total supply of USDT?"
"What token corresponds to this contract address?"
"When did this token launch?"
```

---

### Query Holder Distribution

* `getTrc20TokenHolders` / `getTrc10TokenHolders` — Holder list with address, balance, and percentage
* `getTokenPositionDistribution` — Number and percentage of holders broken down by balance range

Example prompts:

```
"Which addresses are the top holders of this token?"
"Is the holder distribution highly concentrated?"
"What is the holder list for this TRC10 token?"
```

---

### Query Supply and NFT Inventory

* `getTrc20TotalSupply` — TRC20 circulating supply and total supply
* `getTrc721Inventory` — NFT contract inventory
* `getTrc1155Inventory` — Multi-token contract inventory

Example prompts:

```
"What is the circulating supply of this TRC20 token?"
"How many tokens does this NFT contract have in total?"
```

---

## Installation

### Confirm TronScan MCP Is Connected

Refer to [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-token-scanner)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-token-scanner
```