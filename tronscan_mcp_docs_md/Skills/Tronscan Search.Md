

# Search

**Skill ID**: `tronscan-search`

**ClawHub**: [clawhub.ai/sshnii/tronscan-search](https://clawhub.ai/sshnii/tronscan-search)

Search for tokens, contracts, accounts, transactions, or blocks on the TRON blockchain by keyword, and quickly resolve names or symbols to on-chain addresses.

This skill is a prerequisite step before calling **tronscan-token-scanner** or **tronscan-contract-analysis** — when a user provides only a name or symbol, use this skill first to retrieve the on-chain address.

---

## Use Cases

### Look Up a Contract or Token Address by Name

* `search` — Enter a token symbol or contract name and get back matching addresses (`token_id` / contract address)

Example prompts:

```
"What is the contract address of USDT on TRON?"
"What is the contract address of BTT?"
"Search for contracts whose name contains 'swap'."
```

---

### Find an Account, Transaction, or Block

* `search` — Supports filtering by type: `token`, `address`, `contract`, `transaction`, `block`

Example prompts:

```
"Find account information for address TXxx..."
"What transaction corresponds to this transaction hash?"
"Search for block number 65000000."
```

---

### `search` Parameter Reference

| Parameter | Description |
| --- | --- |
| `term` | Required. Search keyword (e.g. USDT, BTT, or a contract name) |
| `type` | Optional. Filter by type: `token` / `address` / `contract` / `transaction` / `block` |
| `start` / `limit` | Optional. Pagination parameters |

---

## Installation

### Confirm TronScan MCP Is Connected

Refer to [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-search)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-search
```