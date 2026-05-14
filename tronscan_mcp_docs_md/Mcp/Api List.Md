

## API Reference

### 1. Block - Block Queries (4)

| API Name | Description |
| --- | --- |
| `getLastestSolidityBlock` | Get the latest solidified block info, including block number, hash, size, timestamp, witness, transaction count, etc. |
| `getNewestBlock` | Get the newest block info, including block number, hash, size, timestamp, witness, transaction count, etc. |
| `getBlocks` | Get block list with pagination, sorting, and filtering by producer and time range |
| `getBlockStatistic` | Get block statistics including 24h total payments, block count, total burned amount, etc. |

### 2. Account - Account Queries (12)

| API Name | Description |
| --- | --- |
| `getAccountList` | Get account list with pagination and sorting, returning balance, voting power, transaction count, etc. |
| `getAccountDetail` | Get detailed info for a specific account, including TRX balance, activation status, total transactions, frozen amount, bandwidth/energy resources, etc. |
| `getAccountTokens` | Get tokens held by an account, filterable by type (TRC20/TRC721/TRC1155) with sorting |
| `getVoteList` | Get voting info: query voters for a specific SR or voting destinations for an address |
| `getAccountResource` | Get account Stake 1.0 resource info, including freeze records, bandwidth, and energy |
| `getAccountResourceV2` | Get account Stake 2.0 resource info, including staking records, delegated bandwidth and energy |
| `getApprovalList` | Get account token approval list, showing allowances granted to contracts |
| `getApprovalChangeRecords` | Get approval change records for a specific contract |
| `getAccountAnalysis` | Get daily account analysis data (balance changes, transfer count, energy/bandwidth consumption, transaction count) |
| `getParticipatedProjects` | Get list of DeFi projects the account participates in |
| `getTokenAssetOverview` | Get account token asset overview, including total assets, token count, balance and value per token |
| `getMultipleChainQuery` | Query corresponding addresses on other blockchains for a TRON address |

### 3. Contract - Contract Queries (10)

| API Name | Description |
| --- | --- |
| `getContractList` | Get smart contract list with search by name/address, sorting, and pagination |
| `getContractDetail` | Get detailed info for a specific contract, including balance, verification status, call count, method mapping, etc. |
| `getContractEvents` | Get contract event list, including transfer events and method calls |
| `getContractEnergyStatistic` | Get contract energy consumption statistics, including total consumption and daily breakdown |
| `getContractCallStatistic` | Get contract call statistics, including call count, top callers, top methods, etc. |
| `getContractCallerStatistic` | Get daily unique caller count for a contract within a specified time range |
| `getContractTriggerStatistic` | Get daily call count for a contract within a specified time range |
| `getContractAnalysis` | Get daily contract analysis data (balance, transfers, energy, bandwidth, call count, fees) |
| `getContractCallers` | Get all callers and their call counts for a contract on a specific day |
| `getContractTriggerTransactions` | Get contract trigger transaction list within a specified time range |

### 4. Transaction - Transaction Queries (9)

| API Name | Description |
| --- | --- |
| `getTransactionList` | Get transaction list with pagination, sorting, and various filter conditions |
| `getTransactionDetail` | Get transaction details by hash, including type, confirmation status, amount, energy/bandwidth consumption, etc. |
| `getTrc20Transfers` | Get TRC20/TRC721 token transfer records |
| `getTrc1155Transfers` | Get TRC1155 token transfer records |
| `getTransferList` | Get TRX native and TRC10 token transfer records |
| `getInternalTransactions` | Get smart contract internal transaction list |
| `getTrc20TransfersWithStatus` | Get TRC20 token transfer records with transaction status |
| `getTransactionStatistics` | Get transaction statistics including total volume, token transaction volume, and other aggregated info |
| `getTransferStatistics` | Get transfer statistics with activity distribution by token type |

### 5. Token - Token Queries (14)

| API Name | Description |
| --- | --- |
| `getTokenList` | Get token list overview, filterable by type, sortable by price/change/volume/holders/market cap |
| `getTrc20TokenDetail` | Get TRC20/TRC721/TRC1155 token details (name, symbol, total supply, holders, price, etc.) |
| `getTrc10TokenDetail` | Get TRC10 token details (name, abbreviation, issuer, total supply, description, etc.) |
| `getTrc20TokenHolders` | Get TRC20/TRC721/TRC1155 token holder list (address, balance, percentage) |
| `getTrc10TokenHolders` | Get TRC10 token holder list |
| `getTokenPositionDistribution` | Get token holding amount distribution (holder count and percentage per range) |
| `getTokenPrice` | Get token price info (defaults to TRX price) |
| `getPricedTokenList` | Get list of all tokens with price information |
| `getTrc721Transfers` | Get transfer history for a specific TRC721 NFT token |
| `getAssetTransfer` | Get TRC10 or TRX transfer records |
| `getTrc1155Inventory` | Get TRC1155 contract inventory info |
| `getTrc1155TokenInventory` | Get holder info for a specific token ID in a TRC1155 contract |
| `getTrc20TotalSupply` | Get TRC20 token circulating/total supply |
| `getTrc721Inventory` | Get TRC721 NFT contract inventory info |

### 6. Witness - Witnesses / Super Representatives (6)

| API Name | Description |
| --- | --- |
| `getWitnessList` | Get witness (Super Representative) list, filterable by type (witness/partner/candidate) |
| `getAccountVotes` | Get account voting records, showing which SRs received votes and vote amounts |
| `getChainParameters` | Get all current TRON blockchain configuration parameters (transaction fees, energy/bandwidth prices, etc.) |
| `getProposals` | Get governance proposal list, including proposal content, voting info, and participant details |
| `getWitnessVoteInfo` | Get voting metrics and historical data for a specific witness (vote count, ranking changes, etc.) |
| `getWitnessGeneralInfo` | Get witness network aggregate statistics (total votes, block production stats, witness count) |

### 7. Homepage - Homepage / Search (6)

| API Name | Description |
| --- | --- |
| `getHomepageData` | Get homepage comprehensive data (TPS, node count, blockchain overview, frozen resources, TVL, etc.) |
| `getSearchBar` | Get trending search results (popular token list) |
| `search` | Search for tokens, contracts, accounts, transactions, or blocks on the TRON blockchain |
| `getCurrentTps` | Get current TPS, latest block height, and historical peak TPS |
| `getHotSearch` | Get trending tokens and contracts with trading metrics and price data |
| `getNodeMap` | Get current node info and geographic distribution data for all full nodes |

### 8. Wallet - Wallet Queries (5)

| API Name | Description |
| --- | --- |
| `getTrxTransfers` | Get account TRX transfer records, filterable by direction and time range |
| `getToken10Transfers` | Get account TRC10 token transfer records |
| `getWalletTrc20Transfers` | Get account TRC20 token transfer records |
| `getWalletTokens` | Get tokens held and watched in the account wallet |
| `getUnfreezableAmount` | Get the currently unfreezable TRX amount for an account |

### 9. Statistics - Statistical Data (26)

| API Name | Description |
| --- | --- |
| `getEnergyDailyStatistic` | Get daily energy consumption statistics for contracts (ranked by consumption) |
| `getEnergyStatistic` | Get energy consumption distribution for a specified time range (aggregated by day/month/quarter) |
| `getTop10` | Get Top 10 ranking statistics across various time and category dimensions |
| `getTriggerAmountStatistic` | Get contract call volume distribution data for a specific date |
| `getTokenTvc` | Get token total on-chain value (TVC) data |
| `getContractCallerStatisticOverview` | Get contract caller statistics (default: last 7 days) |
| `getTriggerStatistic` | Get daily contract trigger data within a specified time range |
| `getDailyNewAccounts` | Get daily new account data (default: last 15 days, max: 2000 days) |
| `getFunds` | Get TRX real-time supply, market cap, and burn data |
| `getTrxVolumeSourceList` | Get TRX price data source list |
| `getTurnover` | Get TRX turnover rate, supply, revenue, minting and burn statistics |
| `getTrxVolume` | Get TRX historical price, volume, and market cap data |
| `getAccountsWithHoldingTrx` | Get the number of accounts that hold TRX (ascending by time) |
| `getCallerAddressStatistic` | Get contract call count statistics including max and min values |
| `getFreezeResource` | Get historical TRX staking rate data |
| `getDailyAvgBlockSize` | Get daily average block size data |
| `getAcquisitionCostStatistic` | Get cost statistics for acquiring resources (Energy and Bandwidth) |
| `getTokenTransferAnalysis` | Get transfer amount analysis data for core tokens |
| `getDailyTransactionNum` | Get transaction trend data with day/week/month/quarter aggregation |
| `getActiveStatistic` | Get active account statistics per day/week/month |
| `getTransactionNum` | Get cumulative daily transaction count data |
| `getNetStatistic` | Get daily Bandwidth consumption statistics |
| `getDefiTvl` | Get daily Defi TVL statistics |
| `getTotalBlockchainSize` | Get cumulative block size (on-chain size) data |
| `getTokenAnalysis` | Get analysis data for token transactions (transfers, holders, etc.) |
| `getStatsOverview` | Get comprehensive daily statistics for TRON (transfers, accounts, resources, tokens) |

### 10. Deep Analysis (27)

| API Name | Description |
| --- | --- |
| `getRelatedAccount` | Get related accounts and transaction data (filterable by transaction count, amount, direction) |
| `getStableCoinHolderBalanceOverview` | Get market cap distribution across stablecoins |
| `getStableCoinHolderChange` | Get chart data for stablecoin holder count changes over time |
| `getTrc20TransferCount` | Get transfer count statistics for a specific TRC20 token held by an account |
| `getLiquidityTransactions` | Get stablecoin liquidity pool transaction list (filterable by project/operation type/token) |
| `getAccountTag` | Get account tag info (exchange tags, project tags, risk tags, etc.) |
| `getStableCoinTransferAmount` | Get stablecoin transfer amount change chart data (24h statistical period) |
| `getStableCoinTopHolders` | Get stablecoin top holder rankings (sortable by different stablecoins) |
| `getStableCoinPoolOverview` | Get stablecoin liquidity pool basic info |
| `getStableCoinBigAmount` | Get large stablecoin transaction list (filterable by address/amount/transaction type) |
| `getStableCoinTotalSupplyChange` | Get chart data for total stablecoin supply changes |
| `getStableCoinKeyEvents` | Get stablecoin key events (issuance/burn/freeze and other major operations) |
| `getStableCoinTotalSupply` | Get current total circulating supply for all stablecoins |
| `getStableCoinPoolInfo` | Get detailed info for all stablecoin liquidity pools |
| `getStableCoinBlackList` | Get stablecoin blacklist (frozen addresses and transaction records) |
| `getStableCoinDistributionChange` | Get chart data for holding distribution changes of a stablecoin |
| `getHolderTokenBasicInfo` | Get basic info about a token held by an account (balance, holding time, etc.) |
| `getStableCoinDistribution` | Get holder distribution data for a stablecoin |
| `getTokenAssetValueInfo` | Get chart data for asset value changes of a token in an account |
| `getTokenBalanceFlow` | Get balance flow change records for a token in an account |
| `getStableCoinTokenSupplyTurnover` | Get supply circulation trend chart data for a stablecoin |
| `getStableCoinPoolTrend` | Get stablecoin liquidity pool change trend data |
| `getStableCoinPoolChange` | Get liquidity change chart data for stablecoin liquidity pools |
| `getStableCoinOverview` | Get stablecoin basic overview (supply, holder count) |
| `getStableCoinTvl` | Get stablecoin distribution (TVL) across liquidity pools |
| `getAccountTransferAmount` | Get account inflow and outflow fund distribution data |
| `getAccountTokenBigAmount` | Get large token transaction list for an account |

---