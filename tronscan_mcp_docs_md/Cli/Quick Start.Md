

# Quick Start

## Basic Commands

After installation, run queries with these commands:

```
ts --version
ts help
ts tps --raw
ts block --raw
ts token usdt --raw
```

Expected behavior:

* `ts --version` prints the installed CLI version.
* `ts help` lists available commands and global options.
* Query commands return JSON data from TronScan API.
* Use `--raw` or `--json` for one-line JSON that is easier to parse in scripts.

## In the terminal

After installing `ts` globally, run commands directly:

```
ts help                         # list all subcommands
ts token-price trx              # token price by symbol
ts token usdt                   # token info
ts search usdt                  # search
ts block                        # latest block
ts tps                          # current TPS
ts account TXxx...              # account details
ts tx af949...                  # transaction by hash
ts transfer-trc20 TXxx...       # TRC20 transfers
ts security-account TXxx...     # account risk check
```

## Machine-readable output

All query commands print JSON. By default, the JSON is formatted for reading. Use `--raw` or `--json` for compact one-line JSON:

```
ts tps --raw
ts account TXxx... --json
```

Notes for scripts and AI agents:

* Prefer `--raw` or `--json`.
* Do not parse colorized or human-facing error text from stderr.
* Business fields come from TronScan API responses and can differ by endpoint.
* Pagination options are `--start N` and `--limit N`; defaults are `0` and `20`.