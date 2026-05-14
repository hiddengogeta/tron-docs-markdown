

* Release Note
Version: 6.3.0

On this page

# Release Note

## New Features[​](#new-features "Direct link to New Features")

* **Added `trx.getContractInfo`**

  Added `trx.getContractInfo(contractAddress)` method that retrieves detailed contract information via the `wallet/getcontractinfo` node API endpoint.
* **Extended `deserializeTx` with full contract type coverage**

  Added deserialization support for all remaining `TransactionBuilder` contract types via `raw_data_hex`:

  + Account: `AccountCreateContract`, `AccountUpdateContract`, `SetAccountIdContract`, `AccountPermissionUpdateContract`
  + Stake / Vote: `FreezeBalanceContract`, `UnfreezeBalanceContract`, `VoteWitnessContract`
  + Proposal: `ProposalCreateContract`, `ProposalApproveContract`, `ProposalDeleteContract`
  + Smart contract: `CreateSmartContract`, `UpdateSettingContract`, `UpdateEnergyLimitContract`, `ClearABIContract`
  + DEX: `ExchangeCreateContract`, `ExchangeInjectContract`, `ExchangeWithdrawContract`, `ExchangeTransactionContract`
  + `UpdateBrokerageContract`

## Improvements[​](#improvements "Direct link to Improvements")

* **Plugin restrictions**

  + Added `PROTECTED_MODULES` to prevent plugins from overriding 2 modules: `transactionBuilder`, `plugin`.
  + Added `PROTECTED_METHODS` to block plugins from overriding critical signing/key methods: `sign`, `signMessage`, `signMessageV2`, `signTransaction`, `signTypedData`, `multiSign`, `setPrivateKey`, `ecRecover`.
  + ⚠️ Note: Plugin support will be removed in the next major version.
* **Bug fix**

  + Corrected the return type of the `getDelegatedResourceV2` in `trx.ts` to consistently return an array.

## Changes[​](#changes "Direct link to Changes")

* Remove dev dependency @eslint/eslintrc.
* Bump serialize-javascript from 7.0.3 to 7.0.5.