

# Transaction Info

**Skill ID**: `tronscan-transaction-info`

**ClawHub**: [clawhub.ai/sshnii/tronscan-transaction-info](https://clawhub.ai/sshnii/tronscan-transaction-info)

Look up TRON transaction details by transaction hash: transaction result, confirmation status, sender/receiver, energy/bandwidth consumption, and token transfer records.

This skill does not apply to address balance or token holder queries — use **tronscan-account-profiler** and **tronscan-token-scanner** respectively for those.

---

## Use Cases

### Query a Single Transaction

* `getTransactionDetail` — Transaction type, confirmation status, amount, energy/bandwidth consumption, sender/receiver, and token transfers within the transaction (`trc20TransferInfo`, `transfersAllList`)

When you have a transaction hash, **always use `getTransactionDetail` first** — token transfer information within the transaction is already included in the response, so there is no need to call `getTrc20Transfers` or similar tools separately.

**Unit conversions:**

* `net_fee`, `energy_fee`, `fee_limit`: unit is **sun** (1 TRX = 10⁶ sun) — divide by 1,000,000 to get TRX
* `amount_str` (TRC20): unit is the **smallest precision unit** — divide by 10^decimals to get a human-readable amount
* `contractData.amount` (TRX transfer): unit is **sun** — divide by 1,000,000 to get TRX

Example prompts:

```
"Did this transaction succeed? Hash is xxx..."
"How much energy did this transaction consume?"
"Who is the sender and receiver of this tx?"
"What token transfers are inside this transaction?"
```

---

### Query Transaction List by Address or Contract

* `getTransactionList` — Transaction list filtered by address, contract, or other conditions, with pagination and sorting support

Example prompts:

```
"What are the recent transactions for address TXxx...?"
"How many times has this contract been called recently?"
```

---

### Query Token Transfer Records (by Address / Contract / Time Range)

* `getTrc20Transfers` / `getTrc20TransfersWithStatus` — TRC20/TRC721 transfer records (including transaction status)
* `getTrc1155Transfers` — TRC1155 multi-token transfer records
* `getTransferList` — TRX and TRC10 native transfer records

The tools above are for querying transfer history by **address, contract, or time range** — they **do not support filtering by transaction hash**. Do not fabricate a tx hash as a filter parameter. For transfers within a single transaction, use `getTransactionDetail` instead.

Example prompts:

```
"What are the recent TRC20 transfers for address TXxx...?"
"What does the transfer activity look like for this contract over the past 7 days?"
"What is the TRX transfer history for this address?"
```

---

### Query Internal Transactions and Statistics

* `getInternalTransactions` — Internal call records triggered by smart contracts
* `getTransactionStatistics` — Total transaction count and aggregated token transaction volume
* `getTransferStatistics` — Transfer statistics categorized by token type

Example prompts:

```
"What internal transactions did this contract call trigger?"
"What is the total transaction volume on the TRON network?"
```

---

## Installation

### Confirm TronScan MCP Is Connected

Refer to [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-transaction-info)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-transaction-info
```