

# TronScan CLI

A CLI tool built on [TronScan API](https://docs.tronscan.org/). Besides the global `setup` command, it implements **86** `ts <command>` query subcommands: tokens, search, overview, blocks, accounts, governance, transactions, statistics, contracts, security, deep analysis, stablecoins, and raw `api` access.

## Install

### Install from npm

```
npm install -g @tronscanteam/cli
```

This registers the global command **`ts`** for use in any directory. Run `ts setup` to configure your API Key, and `ts help` to see all commands.

**API Key**:

Get your API Key: <https://docs.tronscan.org/zh/api/api-keys>

```
ts setup YOUR_API_KEY    # replace with your actual API Key
```

### Upgrade and uninstall

```
npm update -g @tronscanteam/cli
npm uninstall -g @tronscanteam/cli
```

## Dependencies

* [Node.js](https://nodejs.org/) >= 18

## Safety model

TronScan CLI is a read-only data query tool for TronScan API. It does not manage wallets, read private keys, sign messages, broadcast transactions, or submit transactions.