

# Getting Started

This guide covers the available installation methods for TronScan Skills. All methods require configuring the TronScan MCP service first.

---

## Installation Methods

ClawHub One-ClickAgent Bulk InstallSKILL Link (No Install)

### ClawHub One-Click

### Method 1: ClawHub One-Click Install (Recommended)

Search and install skills directly from the [ClawHub](https://clawhub.ai) marketplace:

### Open the ClawHub Marketplace

Visit [clawhub.ai](https://clawhub.ai), search for `TronScan`, and find the skill you want (e.g. `tronscan-token-scanner`).

### Open the Skill Detail Page

Copy the skill page link into the OpenClaw chat and ask it to install.

**Command-line install** (if the `clawhub` CLI is already installed):

```
# Install a single skill
clawhub install tronscan-token-scanner
 
# Install multiple skills at once
clawhub install tronscan-token-scanner tronscan-account-profiler tronscan-search
```

### Agent Bulk Install

### Method 2: Bulk Install via AI Agent (OpenClaw / Cursor, etc.)

Send the skills list page URL to an AI Agent and ask it to install each skill one by one.

### Copy the following prompt and send it to your AI Agent

```
Please install all TronScan skills listed at https://mcpdoc.tronscan.org/en/skills, one by one.
```

### Agent Completes the Installation

The Agent will read the list and install each skill to the skills directory (e.g. `.cursor/skills/`).

**Best for**: Installing all skills at once in a single session.

### SKILL Link (No Install)

### Method 3: Use via SKILL Link (No Installation Required)

Send a skill’s `SKILL.md` link directly to an AI Agent. The Agent can use the content as context without copying anything to the skills directory.

```
Please load and use this skill: https://clawhub.ai/sshnii/tronscan-token-scanner
```

| Feature | Details |
| --- | --- |
| ✅ Pros | No installation needed, great for quick trials |
| ⚠️ Limits | The Agent may not persist the skill — you may need to re-provide it each session; some Agents may not auto-load it as a skill |

**Best for**: Quickly trying out a skill, or when your Agent supports loading skills by link.

---

## Skills List

| Skill | Slug | Description | ClawHub |
| --- | --- | --- | --- |
| Token Scanner | `tronscan-token-scanner` | TRX/token price, supply, market cap, rating, holdings | [Install](https://clawhub.ai/sshnii/tronscan-token-scanner) |
| Account Profiler | `tronscan-account-profiler` | Address assets, tokens, DeFi, energy, votes | [Install](https://clawhub.ai/sshnii/tronscan-account-profiler) |
| Contract Analysis | `tronscan-contract-analysis` | Contract verification, popular methods, top callers | [Install](https://clawhub.ai/sshnii/tronscan-contract-analysis) |
| Transaction Info | `tronscan-transaction-info` | Transaction result, confirmation status, resource usage | [Install](https://clawhub.ai/sshnii/tronscan-transaction-info) |
| Block Info | `tronscan-block-info` | Latest block, block producer, TRX burned | [Install](https://clawhub.ai/sshnii/tronscan-block-info) |
| Token List | `tronscan-token-list` | TRC20 list, trending tokens, 24h volume | [Install](https://clawhub.ai/sshnii/tronscan-token-list) |
| Data Insights | `tronscan-data-insights` | Daily active accounts, top accounts, trending tokens/contracts | [Install](https://clawhub.ai/sshnii/tronscan-data-insights) |
| Realtime Network | `tronscan-realtime-network` | TPS, node count, TVL, total transactions | [Install](https://clawhub.ai/sshnii/tronscan-realtime-network) |
| Search | `tronscan-search` | Resolve token/contract address by name | [Install](https://clawhub.ai/sshnii/tronscan-search) |
| SR Governance | `tronscan-sr-governance` | Super Representatives (SR), candidates, votes, chain parameters & proposals | [Install](https://clawhub.ai/sshnii/tronscan-sr-governance) |
| Stablecoin Analysis | `tronscan-stablecoin` | Supports USDT, USDC, USDD, and TUSD | [Install](https://clawhub.ai/sshnii/tronscan-stablecoin) |

---

## Troubleshooting

**MCP connection failed**: Go to **Settings → Extensions** and verify that the TronScan MCP is successfully connected.

**Rate limited / 429 error**: Without an API Key, TronScan applies request rate limits. Visit [TronScan Developer API](https://tronscan.org/#/developer/api) to apply for a key, then pass it via the `TRON-PRO-API-KEY` header in your MCP configuration.