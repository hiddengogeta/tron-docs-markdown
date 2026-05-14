

# Command Categories

TronScan CLI implements **86** query subcommands across the following categories:

| Category | Count | Commands | Scope |
| --- | --- | --- | --- |
| Token | 5 | `token` `token-holders` `token-price` `token-list` `token-distribution` | Token details, holders, prices, rankings, and position distribution. |
| Search | 2 | `search` `hot-token` | Keyword search and hot token rankings. |
| Overview | 3 | `tps` `overview` `nodes` | Network TPS, overview data, and node information. |
| Block | 1 | `block` | Latest block or a block by number. |
| Account | 10 | `account` `account-list` `account-tokens` `account-resource` `account-resource-v1` `account-approve` `account-votes` `account-analysis` `account-asset` `account-projects` | Account details, rankings, holdings, resources, approvals, votes, analysis, assets, and participated projects. |
| Super Representative | 4 | `sr` `sr-votes` `params` `proposal` | SR lists, voting details, chain parameters, and proposals. |
| Transaction | 10 | `tx` `tx-list` `tx-stats` `transfer` `transfer-stats` `transfer-trc20` `transfer-trc20-contract` `transfer-trc1155` `transfer-trc721` `internal-tx` | Transaction details, lists, statistics, transfers, and internal transactions. |
| Statistics | 20 | `trx-supply` `trx-turnover` `protocol-revenue` `burn-revenue` `stake-revenue` `tx-trend` `tx-total` `active-accounts` `new-accounts` `defi-tvl` `top10` `trx-price` `energy-daily` `energy-dist` `energy-cost` `bandwidth-daily` `trigger-stats` `token-tvc` `token-analysis` `token-transfer-analysis` | Supply, revenue, transactions, accounts, DeFi TVL, rankings, price, energy, bandwidth, contract triggers, and token analytics. |
| Contract | 9 | `contract` `contract-list` `contract-callers` `contract-energy` `contract-daily-callers` `contract-daily-calls` `contract-analysis` `contract-all-callers` `contract-triggers` | Contract details, lists, callers, energy usage, daily activity, analysis, and trigger transactions. |
| Security | 6 | `security-account` `security-token` `security-url` `security-tx` `security-auth` `security-sign` | Risk checks for accounts, tokens, URLs, transactions, approvals, and multisig settings. |
| Deep Analysis | 4 | `deep-related` `deep-flow` `deep-big-tx` `deep-token-transfer` | Related accounts, fund flow, large transactions, and token transfer counts. |
| Stablecoin | 11 | `stable-holders` `stable-change` `stable-top` `stable-big-tx` `stable-events` `stable-dist` `stable-liquidity` `stable-pool` `stable-pool-trend` `stable-pool-change` `stable-tvl` | Stablecoin holders, whale rankings, large transactions, events, distribution, liquidity, pools, and TVL. |
| Other | 1 | `api` | Call a TronScan API path directly. |

Run `ts help` in your terminal to see the full list of available commands.