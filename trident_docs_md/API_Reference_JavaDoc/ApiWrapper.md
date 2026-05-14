

org.tron.trident.core

## Class ApiWrapper

* java.lang.Object
* + org.tron.trident.core.ApiWrapper

* All Implemented Interfaces:
  :   [Api](../../../../org/tron/trident/core/Api.html "interface in org.tron.trident.core")

  ---

    

  ```
  public class ApiWrapper
  extends java.lang.Object
  implements Api
  ```

  A `ApiWrapper` object is the entry point for calling the functions.

  A `ApiWrapper` object is bind with a private key and a full node.
  [`broadcastTransaction(org.tron.trident.proto.Chain.Transaction)`](../../../../org/tron/trident/core/ApiWrapper.html#broadcastTransaction-org.tron.trident.proto.Chain.Transaction-), [`signTransaction(org.tron.trident.proto.Response.TransactionExtention, org.tron.trident.core.key.KeyPair)`](../../../../org/tron/trident/core/ApiWrapper.html#signTransaction-org.tron.trident.proto.Response.TransactionExtention-org.tron.trident.core.key.KeyPair-) and other transaction related
  operations can be done via a `ApiWrapper` object.

  Since:
  :   java version 1.8.0\_231

  See Also:
  :   [`Contract`](../../../../org/tron/trident/core/contract/Contract.html "class in org.tron.trident.core.contract"),
      [`Chain.Transaction`](../../../../org/tron/trident/proto/Chain.Transaction.html "class in org.tron.trident.proto"),
      [`Contract`](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `WalletGrpc.WalletBlockingStub` | `blockingStub` |
    | `WalletSolidityGrpc.WalletSolidityBlockingStub` | `blockingStubSolidity` |
    | `io.grpc.ManagedChannel` | `channel` |
    | `io.grpc.ManagedChannel` | `channelSolidity` |
    | `KeyPair` | `keyPair` |
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `ApiWrapper(java.lang.String grpcEndpoint, java.lang.String grpcEndpointSolidity, java.lang.String hexPrivateKey)` |
    | `ApiWrapper(java.lang.String grpcEndpoint, java.lang.String grpcEndpointSolidity, java.lang.String hexPrivateKey, int timeout)` |
    | `ApiWrapper(java.lang.String grpcEndpoint, java.lang.String grpcEndpointSolidity, java.lang.String hexPrivateKey, java.util.List<io.grpc.ClientInterceptor> clientInterceptors)` |
    | `ApiWrapper(java.lang.String grpcEndpoint, java.lang.String grpcEndpointSolidity, java.lang.String hexPrivateKey, java.util.List<io.grpc.ClientInterceptor> clientInterceptors, int timeout)` |
    | `ApiWrapper(java.lang.String grpcEndpoint, java.lang.String grpcEndpointSolidity, java.lang.String hexPrivateKey, java.lang.String apiKey)` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionExtention` | `accountPermissionUpdate(Contract.AccountPermissionUpdateContract accountPermissionUpdateContract)` Update account permissions for multiSign |
    | `Response.TransactionExtention` | `accountPermissionUpdate(java.lang.String ownerAddress, AccountPermissions accountPermissions)` update account permissions with new owner/witness/active permissions |
    | `Response.TransactionExtention` | `approveProposal(java.lang.String ownerAddress, long proposalId, boolean isAddApproval)` ProposalApprove Approves proposed transaction. |
    | `Contract.AssetIssueContract.Builder` | `assetIssueContractBuilder(java.lang.String ownerAddress, java.lang.String name, java.lang.String abbr, long totalSupply, int trxNum, int icoNum, long startTime, long endTime, java.lang.String url, long freeAssetNetLimit, long publicFreeAssetNetLimit, int precision, java.lang.String description)` |
    | `java.lang.String` | `broadcastTransaction(Chain.Transaction txn)` broadcast a transaction with the binding account. |
    | `static byte[]` | `calculateTransactionHash(Chain.Transaction txn)` |
    | `Response.TransactionExtention` | `cancelAllUnfreezeV2(java.lang.String ownerAddress)` Stake2.0 API Cancel all the unstaking transactions in the waiting period |
    | `Response.TransactionExtention` | `clearContractABI(java.lang.String ownerAddress, java.lang.String contractAddress)` ClearABIContract |
    | `void` | `close()` |
    | `Response.TransactionExtention` | `constantCall(java.lang.String ownerAddress, java.lang.String contractAddress, Function function)` Deprecated. Since 0.9.2, scheduled for removal in future versions. Use [`triggerConstantContract(String, String, Function, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-org.tron.trident.abi.datatypes.Function-org.tron.trident.core.NodeType...-) instead. |
    | `Response.TransactionExtention` | `constantCallV2(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData)` Deprecated. Since 0.9.2, scheduled for removal in future versions. Use [`triggerConstantContract(String, String, String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-java.lang.String-org.tron.trident.core.NodeType...-) instead. |
    | `Response.TransactionExtention` | `createAccount(java.lang.String ownerAddress, java.lang.String accountAddress)` Create an account. |
    | `static Contract.AccountCreateContract` | `createAccountCreateContract(com.google.protobuf.ByteString owner, com.google.protobuf.ByteString address)` |
    | `static Contract.AccountUpdateContract` | `createAccountUpdateContract(com.google.protobuf.ByteString accountName, com.google.protobuf.ByteString address)` |
    | `Response.TransactionExtention` | `createAssetIssue(java.lang.String ownerAddress, java.lang.String name, java.lang.String abbr, long totalSupply, int trxNum, int icoNum, long startTime, long endTime, java.lang.String url, long freeAssetNetLimit, long publicFreeAssetNetLimit, int precision, java.util.HashMap<java.lang.String,java.lang.String> frozenSupply, java.lang.String description)` Issue a token |
    | `Response.TransactionExtention` | `createAssetIssue(java.lang.String ownerAddress, java.lang.String name, java.lang.String abbr, long totalSupply, int trxNum, int icoNum, long startTime, long endTime, java.lang.String url, long freeAssetNetLimit, long publicFreeAssetNetLimit, int precision, java.lang.String description)` Issue a token |
    | `static Contract.SetAccountIdContract` | `createSetAccountIdContract(com.google.protobuf.ByteString accountId, com.google.protobuf.ByteString address)` |
    | `Contract.CreateSmartContract` | `createSmartContract(java.lang.String contractName, java.lang.String address, java.lang.String ABI, java.lang.String code, long callValue, long consumeUserResourcePercent, long originEnergyLimit, long tokenValue, java.lang.String tokenId)` |
    | `Contract.CreateSmartContract` | `createSmartContract(java.lang.String contractName, java.lang.String address, java.lang.String ABI, java.lang.String code, long callValue, long consumeUserResourcePercent, long originEnergyLimit, long tokenValue, java.lang.String tokenId, java.lang.String libraryAddressPair, java.lang.String compilerVersion)` |
    | `Response.TransactionExtention` | `createTransactionExtention(com.google.protobuf.Message request, Chain.Transaction.Contract.ContractType contractType)` build Transaction Extention in local. |
    | `static Contract.UnfreezeAssetContract` | `createUnfreezeAssetContract(com.google.protobuf.ByteString address)` |
    | `static Contract.UpdateAssetContract` | `createUpdateAssetContract(com.google.protobuf.ByteString address, com.google.protobuf.ByteString description, com.google.protobuf.ByteString url, long newLimit, long newPublicLimit)` |
    | `static Contract.VoteWitnessContract` | `createVoteWitnessContract(com.google.protobuf.ByteString ownerAddress, java.util.Map<java.lang.String,java.lang.String> votes)` |
    | `Response.TransactionExtention` | `createWitness(java.lang.String ownerAddress, java.lang.String url)` CreateWitness Apply to become a witness. |
    | `Response.TransactionExtention` | `delegateResource(java.lang.String ownerAddress, long balance, int resourceCode, java.lang.String receiverAddress, boolean lock)` Stake2.0 API Delegate bandwidth or energy resources to other accounts |
    | `Response.TransactionExtention` | `delegateResourceV2(java.lang.String ownerAddress, long balance, int resourceCode, java.lang.String receiverAddress, boolean lock, long lockPeriod)` Stake2.0 API Delegate bandwidth or energy resources to other accounts |
    | `Response.TransactionExtention` | `deleteProposal(java.lang.String ownerAddress, long proposalId)` ProposalDelete Deletes Proposal Transaction. |
    | `Response.TransactionExtention` | `deployContract(java.lang.String contractName, java.lang.String abiStr, java.lang.String bytecode, java.util.List<Type<?>> constructorParams, long feeLimit, long consumeUserResourcePercent, long originEnergyLimit, long callValue, java.lang.String tokenId, long tokenValue)` Deploy a smart contract - no broadcasting |
    | `void` | `disableLocalCreate()` |
    | `void` | `enableLocalCreate(BlockId blockId, long expireTime)` enable local create transaction. |
    | `long` | `estimateBandwidth(Chain.Transaction txn)` Estimate the bandwidth consumption of the transaction. |
    | `Response.EstimateEnergyMessage` | `estimateEnergy(java.lang.String ownerAddress, java.lang.String contractAddress, Function function, NodeType... nodeType)` Estimate the energy required for the successful execution of smart contract transactions This API is closed by default in tron node. |
    | `Response.EstimateEnergyMessage` | `estimateEnergy(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData, long callValue, long tokenValue, java.lang.String tokenId, NodeType... nodeType)` Estimate the energy required for the successful execution of smart contract transactions This API is closed by default in tron node. |
    | `Response.EstimateEnergyMessage` | `estimateEnergyV2(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData)` Deprecated. Since 0.9.2, scheduled for removal in future versions. Use [`estimateEnergy(String, String, String, long, long, String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#estimateEnergy-java.lang.String-java.lang.String-java.lang.String-long-long-java.lang.String-org.tron.trident.core.NodeType...-) instead. |
    | `Response.TransactionExtention` | `exchangeCreate(java.lang.String ownerAddress, java.lang.String firstToken, long firstBalance, java.lang.String secondToken, long secondBalance)` exchangeCreate |
    | `Response.TransactionExtention` | `exchangeInject(java.lang.String ownerAddress, long exchangeId, java.lang.String tokenId, long amount)` exchangeInject |
    | `Response.TransactionExtention` | `exchangeTransaction(java.lang.String ownerAddress, long exchangeId, java.lang.String tokenId, long amount, long expected)` create exchangeTransaction. |
    | `Response.TransactionExtention` | `exchangeWithdraw(java.lang.String ownerAddress, long exchangeId, java.lang.String tokenId, long quant)` create ExchangeWithdrawContract with parameters |
    | `Response.TransactionExtention` | `freezeBalance(java.lang.String ownerAddress, long frozenBalance, int frozenDuration, int resourceCode)` Freeze balance to get energy or bandwidth, for 3 days |
    | `Response.TransactionExtention` | `freezeBalance(java.lang.String ownerAddress, long frozenBalance, int frozenDuration, int resourceCode, java.lang.String receiveAddress)` Freeze balance to get energy or bandwidth, for 3 days |
    | `Response.TransactionExtention` | `freezeBalanceV2(java.lang.String ownerAddress, long frozenBalance, int resourceCode)` Stake2.0 API Stake an amount of TRX to obtain bandwidth or energy, and obtain equivalent TRON Power(TP) according to the staked amount |
    | `static KeyPair` | `generateAddress()` Generate random address |
    | `Response.Account` | `getAccount(java.lang.String address, NodeType... nodeType)` Get account info by address |
    | `long` | `getAccountBalance(java.lang.String address)` |
    | `Response.Account` | `getAccountById(java.lang.String id, NodeType... nodeType)` |
    | `Response.AccountNetMessage` | `getAccountNet(java.lang.String address)` Query bandwidth information |
    | `AccountPermissions` | `getAccountPermissions(java.lang.String address, NodeType... nodeType)` Retrieves the permissions of a TRON account. |
    | `Response.AccountResourceMessage` | `getAccountResource(java.lang.String address)` Query the resource information of an account(bandwidth,energy,etc) |
    | `Response.Account` | `getAccountSolidity(java.lang.String address)` Deprecated. Since 0.10.0, scheduled for removal in future versions. use [`getAccount(String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getAccount-java.lang.String-org.tron.trident.core.NodeType...-) instead |
    | `Response.AssetIssueList` | `getAssetIssueByAccount(java.lang.String address)` Query the TRC10 token information issued by an account |
    | `Contract.AssetIssueContract` | `getAssetIssueById(java.lang.String assetId, NodeType... nodeType)` Query a token by token id |
    | `Contract.AssetIssueContract` | `getAssetIssueByName(java.lang.String name, NodeType... nodeType)` Query a token by token name |
    | `Response.AssetIssueList` | `getAssetIssueList(NodeType... nodeType)` Query the list of all the TRC10 tokens |
    | `Response.AssetIssueList` | `getAssetIssueListByName(java.lang.String name, NodeType... nodeType)` Query the list of all the TRC10 tokens by token name |
    | `long` | `getAvailableUnfreezeCount(java.lang.String ownerAddress, NodeType... nodeType)` Stake2.0 API query remaining times of executing unstake operation |
    | `Response.PricesResponseMessage` | `getBandwidthPrices(NodeType... nodeType)` GetBandwidthPrices Query historical bandwidth unit price. |
    | `Response.PricesResponseMessage` | `getBandwidthPricesOnSolidity()` Deprecated. Since 0.10.0, scheduled for removal in future versions. use [`getBandwidthPrices(NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getBandwidthPrices-org.tron.trident.core.NodeType...-) instead |
    | `Response.BlockExtention` | `getBlock(boolean detail, NodeType... nodeType)` get latest block extension |
    | `Response.BlockExtention` | `getBlock(java.lang.String blockIDOrNum, boolean detail, NodeType... nodeType)` get block of one specified block |
    | `Response.BlockBalanceTrace` | `getBlockBalance(java.lang.String blockId, long blockNum)` GetBlockBalance Get all balance change operations in a block(Note: At present, the interface data can only be queried through the following official nodes 47.241.20.47; 161.117.85.97; 161.117.224.116; 161.117.83.38) |
    | `Chain.Block` | `getBlockById(java.lang.String blockID)` GetBlockById Query block by ID(block hash). |
    | `Chain.Block` | `getBlockByIdOrNum(java.lang.String blockIDOrNum)` GetBlockByIdOrNum |
    | `Response.BlockListExtention` | `getBlockByLatestNum(long num)` Get some latest blocks |
    | `Response.BlockListExtention` | `getBlockByLimitNext(long startNum, long endNum)` Returns the list of Block Objects included in the 'Block Height' range specified |
    | `Response.BlockExtention` | `getBlockByNum(long blockNum, NodeType... nodeType)` Query block information by block height, it called getBlockByNum2 rpc |
    | `long` | `getBrokerageInfo(java.lang.String address, NodeType... nodeType)` Query the ratio of brokerage of the witness. |
    | `long` | `getBurnTRX(NodeType... nodeType)` GetBurnTRX Query the amount of TRX burned due to on-chain transaction fees since No. |
    | `long` | `getCanDelegatedMaxSize(java.lang.String ownerAddress, int type, NodeType... nodeType)` Stake2.0 API query the amount of delegatable resources share of the specified resource type for an address, unit is sun. |
    | `long` | `getCanWithdrawUnfreezeAmount(java.lang.String ownerAddress, long timestamp, NodeType... nodeType)` Stake2.0 API query the withdrawable balance at the specified timestamp |
    | `long` | `getCanWithdrawUnfreezeAmount(java.lang.String ownerAddress, NodeType... nodeType)` Stake2.0 API query the withdrawable balance at the latest block timestamp |
    | `Response.ChainParameters` | `getChainParameters()` All parameters that the blockchain committee can set |
    | `Contract` | `getContract(java.lang.String contractAddress)` Obtain a `Contract` object via an address |
    | `Response.SmartContractDataWrapper` | `getContractInfo(java.lang.String contractAddress)` getContractInfo |
    | `Response.DelegatedResourceList` | `getDelegatedResource(java.lang.String fromAddress, java.lang.String toAddress, NodeType... nodeType)` Returns all resources delegations from an account to another account. |
    | `Response.DelegatedResourceAccountIndex` | `getDelegatedResourceAccountIndex(java.lang.String address, NodeType... nodeType)` Query the energy delegation by an account. |
    | `Response.DelegatedResourceAccountIndex` | `getDelegatedResourceAccountIndexV2(java.lang.String address, NodeType... nodeType)` Stake2.0 API query the delegated resource index of an account. |
    | `Response.DelegatedResourceList` | `getDelegatedResourceV2(java.lang.String fromAddress, java.lang.String toAddress, NodeType... nodeType)` Stake2.0 API query the detail of resource share delegated from fromAddress to toAddress |
    | `Response.PricesResponseMessage` | `getEnergyPrices(NodeType... nodeType)` GetEnergyPrices Query historical energy unit price. |
    | `Response.PricesResponseMessage` | `getEnergyPricesOnSolidity()` Deprecated. Since 0.10.0, scheduled for removal in future versions. use [`getEnergyPrices(NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getEnergyPrices-org.tron.trident.core.NodeType...-) instead |
    | `Response.Exchange` | `getExchangeById(java.lang.String id, NodeType... nodeType)` Query exchange pair based on id |
    | `Response.MarketOrderList` | `getMarketOrderByAccount(java.lang.String address, NodeType... nodeType)` getMarketOrderByAccount |
    | `Response.MarketOrder` | `getMarketOrderById(java.lang.String txn, NodeType... nodeType)` getMarketOrderById |
    | `Response.MarketOrderList` | `getMarketOrderListByPair(java.lang.String sellTokenId, java.lang.String buyTokenId, NodeType... nodeType)` getMarketOrderListByPair |
    | `Response.MarketOrderPairList` | `getMarketPairList(NodeType... nodeType)` getMarketPairList |
    | `Response.MarketPriceList` | `getMarketPriceByPair(java.lang.String sellTokenId, java.lang.String buyTokenId, NodeType... nodeType)` getMarketPriceByPair |
    | `Response.PricesResponseMessage` | `getMemoFee()` GetMemoFee Query historical memo fee. |
    | `long` | `getNextMaintenanceTime()` GetNextMaintenanceTime Returns the timestamp of the next voting time in milliseconds. |
    | `Response.NodeInfo` | `getNodeInfo()` Get current API node info |
    | `Chain.Block` | `getNowBlock(NodeType... nodeType)` Query the latest block information |
    | `Response.BlockExtention` | `getNowBlock2(NodeType... nodeType)` Query the latest block information |
    | `Response.BlockExtention` | `getNowBlockSolidity()` Deprecated. Since 0.10.0, scheduled for removal in future versions. use [`getNowBlock2(NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getNowBlock2-org.tron.trident.core.NodeType...-) instead |
    | `Response.AssetIssueList` | `getPaginatedAssetIssueList(long offset, long limit, NodeType... nodeType)` Query the list of all the tokens by pagination. |
    | `Response.ExchangeList` | `getPaginatedExchangeList(long offset, long limit)` get paginated exchange list |
    | `Response.WitnessList` | `getPaginatedNowWitnessList(long offset, long limit, NodeType... nodeType)` Get a paginated list of real-time witnesses ordered by vote count Note: This method may throw an exception when FullNode is in the maintenance period. |
    | `Response.ProposalList` | `getPaginatedProposalList(long offset, long limit)` get paginated proposal list |
    | `long` | `getPendingSize()` GetPendingSize Get the size of the pending pool queue |
    | `Response.Proposal` | `getProposalById(java.lang.String id)` Query proposal based on ID |
    | `GrpcAPI.NumberMessage` | `getRewardInfo(java.lang.String address, NodeType... nodeType)` Get the rewards that the voter has not received |
    | `GrpcAPI.NumberMessage` | `getRewardSolidity(java.lang.String address)` Deprecated. Since 0.10.0, scheduled for removal in future versions. use [`getRewardInfo(String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getRewardInfo-java.lang.String-org.tron.trident.core.NodeType...-) instead |
    | `Common.SmartContract` | `getSmartContract(java.lang.String contractAddress)` |
    | `Response.TransactionApprovedList` | `getTransactionApprovedList(Chain.Transaction trx)` Query transaction approvedList |
    | `Chain.Transaction` | `getTransactionById(java.lang.String txID, NodeType... nodeType)` Query transaction information by transaction id |
    | `Chain.Transaction` | `getTransactionByIdSolidity(java.lang.String txID)` Deprecated. Since 0.10.0, scheduled for removal in future versions. use [`getTransactionById(String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getTransactionById-java.lang.String-org.tron.trident.core.NodeType...-) instead |
    | `long` | `getTransactionCountByBlockNum(long blockNum, NodeType... nodeType)` getTransactionCountByBlockNum |
    | `Chain.Transaction` | `getTransactionFromPending(java.lang.String txId)` GetTransactionFromPending Get transaction details from the pending pool |
    | `Response.TransactionInfoList` | `getTransactionInfoByBlockNum(long blockNum, NodeType... nodeType)` Get transactionInfo from block number |
    | `Response.TransactionInfoList` | `getTransactionInfoByBlockNumSolidity(long blockNum)` Deprecated. Since 0.10.0, scheduled for removal in future versions. use [`getTransactionInfoByBlockNum(long, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getTransactionInfoByBlockNum-long-org.tron.trident.core.NodeType...-) instead |
    | `Response.TransactionInfo` | `getTransactionInfoById(java.lang.String txID, NodeType... nodeType)` Query the transactionInfo by transaction id |
    | `GrpcAPI.TransactionIdList` | `getTransactionListFromPending()` GetTransactionListFromPending Get transaction list information from pending pool |
    | `Response.TransactionSignWeight` | `getTransactionSignWeight(Chain.Transaction trx)` Query transaction sign weight |
    | `Response.ExchangeList` | `listExchanges(NodeType... nodeType)` List all exchange pairs |
    | `Response.NodeList` | `listNodes()` List all nodes that current API node is connected to |
    | `Response.ProposalList` | `listProposals()` List all proposals |
    | `Response.WitnessList` | `listWitnesses(NodeType... nodeType)` List all witnesses that current API node is connected to |
    | `Response.TransactionExtention` | `marketCancelOrder(java.lang.String ownerAddress, java.lang.String orderId)` crete MarketCancelOrderContract with parameters |
    | `Response.TransactionExtention` | `marketSellAsset(java.lang.String ownerAddress, java.lang.String sellTokenId, long sellTokenQuantity, java.lang.String buyTokenId, long buyTokenQuantity)` create MarketSellAssetContract with parameters |
    | `static ApiWrapper` | `ofMainnet(java.lang.String hexPrivateKey)` Deprecated. Since 0.9.2, scheduled for removal in future versions. This method will only be available before TronGrid prohibits the use without API key |
    | `static ApiWrapper` | `ofMainnet(java.lang.String hexPrivateKey, java.lang.String apiKey)` The constructor for main net. |
    | `static ApiWrapper` | `ofNile(java.lang.String hexPrivateKey)` The constructor for Nile test net. |
    | `static ApiWrapper` | `ofShasta(java.lang.String hexPrivateKey)` The constructor for Shasta test net. |
    | `static com.google.protobuf.ByteString` | `parseAddress(java.lang.String address)` The function receives addresses in any formats. |
    | `static com.google.protobuf.ByteString` | `parseHex(java.lang.String hexString)` |
    | `Response.TransactionExtention` | `participateAssetIssue(java.lang.String toAddress, java.lang.String ownerAddress, java.lang.String assertName, long amount)` Participate a token |
    | `Response.TransactionExtention` | `proposalCreate(java.lang.String ownerAddress, java.util.Map<java.lang.Long,java.lang.Long> parameters)` ProposalCreate Creates a proposal transaction. |
    | `Chain.Transaction` | `setAccountId(java.lang.String id, java.lang.String address)` |
    | `Response.TransactionExtention` | `setAccountId2(java.lang.String id, java.lang.String address)` |
    | `void` | `setExpireTimeStamp(long expireTime)` |
    | `void` | `setReferHeadBlockId(BlockId blockId)` |
    | `Chain.Transaction` | `signTransaction(Chain.Transaction txn)` |
    | `Chain.Transaction` | `signTransaction(Chain.Transaction txn, KeyPair keyPair)` |
    | `Chain.Transaction` | `signTransaction(Response.TransactionExtention txnExt)` |
    | `Chain.Transaction` | `signTransaction(Response.TransactionExtention txnExt, KeyPair keyPair)` |
    | `static java.lang.String` | `toHex(byte[] raw)` |
    | `static java.lang.String` | `toHex(com.google.protobuf.ByteString raw)` |
    | `Response.TransactionExtention` | `transfer(java.lang.String fromAddress, java.lang.String toAddress, long amount)` Transfer TRX. |
    | `Response.TransactionExtention` | `transferTrc10(java.lang.String fromAddress, java.lang.String toAddress, int tokenId, long amount)` Transfers TRC10 Asset |
    | `TransactionBuilder` | `triggerCall(java.lang.String ownerAddress, java.lang.String contractAddress, Function function)` Deprecated. Since 0.9.2, scheduled for removal in future versions. Use [`triggerConstantContract(String, String, Function, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-org.tron.trident.abi.datatypes.Function-org.tron.trident.core.NodeType...-) instead. |
    | `TransactionBuilder` | `triggerCallV2(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData)` Deprecated. Since 0.9.2, scheduled for removal in future versions. Use [`triggerConstantContract(String, String, String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-java.lang.String-org.tron.trident.core.NodeType...-) instead. |
    | `Response.TransactionExtention` | `triggerConstantContract(java.lang.String ownerAddress, java.lang.String contractAddress, Function function, NodeType... nodeType)` |
    | `Response.TransactionExtention` | `triggerConstantContract(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData, long callValue, long tokenValue, java.lang.String tokenId, NodeType... nodeType)` make a constant call - no broadcasting, no need to broadcast |
    | `Response.TransactionExtention` | `triggerConstantContract(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData, NodeType... nodeType)` |
    | `Response.TransactionExtention` | `triggerContract(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData, long callValue, long tokenValue, java.lang.String tokenId, long feeLimit)` make a TriggerSmartContract, - no broadcasting. |
    | `Response.TransactionExtention` | `undelegateResource(java.lang.String ownerAddress, long balance, int resourceCode, java.lang.String receiverAddress)` Stake2.0 API unDelegate resource |
    | `Response.TransactionExtention` | `unfreezeAsset(java.lang.String ownerAddress)` Unfreeze a token that has passed the minimum freeze duration |
    | `Response.TransactionExtention` | `unfreezeBalance(java.lang.String ownerAddress, int resourceCode)` Unfreeze balance to get TRX back |
    | `Response.TransactionExtention` | `unfreezeBalance(java.lang.String ownerAddress, int resourceCode, java.lang.String receiveAddress)` Unfreeze balance to get TRX back |
    | `Response.TransactionExtention` | `unfreezeBalanceV2(java.lang.String ownerAddress, long unfreezeBalance, int resourceCode)` Stake2.0 API Unstake some TRX, release the corresponding amount of bandwidth or energy, and voting rights (TP) |
    | `Response.TransactionExtention` | `updateAccount(java.lang.String address, java.lang.String accountName)` Modify account name |
    | `Response.TransactionExtention` | `updateAsset(java.lang.String ownerAddress, java.lang.String description, java.lang.String url, long newLimit, long newPublicLimit)` Update basic TRC10 token information |
    | `Response.TransactionExtention` | `updateBrokerage(java.lang.String address, int brokerage)` |
    | `Response.TransactionExtention` | `updateEnergyLimit(java.lang.String ownerAddress, java.lang.String contractAddress, long originEnergyLimit)` create UpdateEnergyLimitContract with parameters |
    | `Response.TransactionExtention` | `updateSetting(java.lang.String ownerAddress, java.lang.String contractAddress, long consumeUserResourcePercent)` create UpdateSettingContract with parameters |
    | `Response.TransactionExtention` | `updateWitness(java.lang.String ownerAddress, java.lang.String updateUrl)` UpdateWitness Edit the URL of the witness's official website. |
    | `Response.TransactionExtention` | `voteWitness(java.lang.String ownerAddress, java.util.HashMap<java.lang.String,java.lang.String> votes)` Vote for witnesses |
    | `Response.TransactionExtention` | `withdrawBalance(java.lang.String ownerAddress)` WithdrawBalance Super Representative or user withdraw rewards, usable every 24 hours. |
    | `Response.TransactionExtention` | `withdrawExpireUnfreeze(java.lang.String ownerAddress)` Stake2.0 API withdraw unfrozen balance |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### blockingStub

      ```
      public final WalletGrpc.WalletBlockingStub blockingStub
      ```
    - #### blockingStubSolidity

      ```
      public final WalletSolidityGrpc.WalletSolidityBlockingStub blockingStubSolidity
      ```
    - #### keyPair

      ```
      public final KeyPair keyPair
      ```
    - #### channel

      ```
      public final io.grpc.ManagedChannel channel
      ```
    - #### channelSolidity

      ```
      public final io.grpc.ManagedChannel channelSolidity
      ```
  + ### Constructor Detail

    - #### ApiWrapper

      ```
      public ApiWrapper(java.lang.String grpcEndpoint,
                        java.lang.String grpcEndpointSolidity,
                        java.lang.String hexPrivateKey)
      ```
    - #### ApiWrapper

      ```
      public ApiWrapper(java.lang.String grpcEndpoint,
                        java.lang.String grpcEndpointSolidity,
                        java.lang.String hexPrivateKey,
                        java.lang.String apiKey)
      ```
    - #### ApiWrapper

      ```
      public ApiWrapper(java.lang.String grpcEndpoint,
                        java.lang.String grpcEndpointSolidity,
                        java.lang.String hexPrivateKey,
                        java.util.List<io.grpc.ClientInterceptor> clientInterceptors)
      ```
    - #### ApiWrapper

      ```
      public ApiWrapper(java.lang.String grpcEndpoint,
                        java.lang.String grpcEndpointSolidity,
                        java.lang.String hexPrivateKey,
                        int timeout)
      ```
    - #### ApiWrapper

      ```
      public ApiWrapper(java.lang.String grpcEndpoint,
                        java.lang.String grpcEndpointSolidity,
                        java.lang.String hexPrivateKey,
                        java.util.List<io.grpc.ClientInterceptor> clientInterceptors,
                        int timeout)
      ```
  + ### Method Detail

    - #### ofMainnet

      ```
      public static ApiWrapper ofMainnet(java.lang.String hexPrivateKey,
                                         java.lang.String apiKey)
      ```

      The constructor for main net. Use TronGrid as default

      Parameters:
      :   `hexPrivateKey` - the binding private key. Operations require private key will all use this unless the private key is specified elsewhere.
      :   `apiKey` - this function works with TronGrid, an API key is required.

      Returns:
      :   a ApiWrapper object
    - #### ofMainnet

      ```
      @Deprecated
      public static ApiWrapper ofMainnet(java.lang.String hexPrivateKey)
      ```

      Deprecated. Since 0.9.2, scheduled for removal in future versions.
      This method will only be available before TronGrid prohibits the use without API key

      The constructor for main net.

      Parameters:
      :   `hexPrivateKey` - the binding private key. Operations require private key will all use this unless the private key is specified elsewhere.

      Returns:
      :   a ApiWrapper object
    - #### ofShasta

      ```
      public static ApiWrapper ofShasta(java.lang.String hexPrivateKey)
      ```

      The constructor for Shasta test net. Use TronGrid as default.

      Parameters:
      :   `hexPrivateKey` - the binding private key. Operations require private key will all use this unless the private key is specified elsewhere.

      Returns:
      :   a ApiWrapper object
    - #### ofNile

      ```
      public static ApiWrapper ofNile(java.lang.String hexPrivateKey)
      ```

      The constructor for Nile test net.

      Parameters:
      :   `hexPrivateKey` - the binding private key. Operations require private key will all use this unless the private key is specified elsewhere.

      Returns:
      :   a ApiWrapper object
    - #### enableLocalCreate

      ```
      public void enableLocalCreate(BlockId blockId,
                                    long expireTime)
      ```

      enable local create transaction.

      Parameters:
      :   `blockId` - refer blockId used in createTransaction. It will be invalid after 65535 blocks
          so remember to update it timely.
      :   `expireTime` - transaction's absolute expire timestamp in createTransaction, milliseconds.
    - #### disableLocalCreate

      ```
      public void disableLocalCreate()
      ```
    - #### setReferHeadBlockId

      ```
      public void setReferHeadBlockId(BlockId blockId)
      ```
    - #### setExpireTimeStamp

      ```
      public void setExpireTimeStamp(long expireTime)
      ```
    - #### generateAddress

      ```
      public static KeyPair generateAddress()
      ```

      Generate random address

      Returns:
      :   A list, inside are the public key and private key
    - #### parseAddress

      ```
      public static com.google.protobuf.ByteString parseAddress(java.lang.String address)
      ```

      The function receives addresses in any formats.

      Parameters:
      :   `address` - account or contract address in any allowed formats.

      Returns:
      :   hex address
    - #### calculateTransactionHash

      ```
      public static byte[] calculateTransactionHash(Chain.Transaction txn)
      ```
    - #### parseHex

      ```
      public static com.google.protobuf.ByteString parseHex(java.lang.String hexString)
      ```
    - #### toHex

      ```
      public static java.lang.String toHex(byte[] raw)
      ```
    - #### toHex

      ```
      public static java.lang.String toHex(com.google.protobuf.ByteString raw)
      ```
    - #### createVoteWitnessContract

      ```
      public static Contract.VoteWitnessContract createVoteWitnessContract(com.google.protobuf.ByteString ownerAddress,
                                                                           java.util.Map<java.lang.String,java.lang.String> votes)
      ```
    - #### createAccountUpdateContract

      ```
      public static Contract.AccountUpdateContract createAccountUpdateContract(com.google.protobuf.ByteString accountName,
                                                                               com.google.protobuf.ByteString address)
      ```
    - #### createAccountCreateContract

      ```
      public static Contract.AccountCreateContract createAccountCreateContract(com.google.protobuf.ByteString owner,
                                                                               com.google.protobuf.ByteString address)
      ```
    - #### createSetAccountIdContract

      ```
      public static Contract.SetAccountIdContract createSetAccountIdContract(com.google.protobuf.ByteString accountId,
                                                                             com.google.protobuf.ByteString address)
      ```
    - #### createUpdateAssetContract

      ```
      public static Contract.UpdateAssetContract createUpdateAssetContract(com.google.protobuf.ByteString address,
                                                                           com.google.protobuf.ByteString description,
                                                                           com.google.protobuf.ByteString url,
                                                                           long newLimit,
                                                                           long newPublicLimit)
      ```
    - #### createUnfreezeAssetContract

      ```
      public static Contract.UnfreezeAssetContract createUnfreezeAssetContract(com.google.protobuf.ByteString address)
      ```
    - #### close

      ```
      public void close()
      ```
    - #### signTransaction

      ```
      public Chain.Transaction signTransaction(Response.TransactionExtention txnExt,
                                               KeyPair keyPair)
      ```

      Specified by:
      :   `signTransaction` in interface `Api`
    - #### signTransaction

      ```
      public Chain.Transaction signTransaction(Chain.Transaction txn,
                                               KeyPair keyPair)
      ```

      Specified by:
      :   `signTransaction` in interface `Api`
    - #### signTransaction

      ```
      public Chain.Transaction signTransaction(Response.TransactionExtention txnExt)
      ```

      Specified by:
      :   `signTransaction` in interface `Api`
    - #### signTransaction

      ```
      public Chain.Transaction signTransaction(Chain.Transaction txn)
      ```

      Specified by:
      :   `signTransaction` in interface `Api`
    - #### createTransactionExtention

      ```
      public Response.TransactionExtention createTransactionExtention(com.google.protobuf.Message request,
                                                                      Chain.Transaction.Contract.ContractType contractType)
                                                               throws IllegalException
      ```

      build Transaction Extention in local.

      Specified by:
      :   `createTransactionExtention` in interface `Api`

      Parameters:
      :   `contractType` - transaction type.
      :   `request` - transaction message object.

      Throws:
      :   `IllegalException`
    - #### estimateBandwidth

      ```
      public long estimateBandwidth(Chain.Transaction txn)
      ```

      Estimate the bandwidth consumption of the transaction.
      Please note that bandwidth estimations are based on signed transactions.

      Specified by:
      :   `estimateBandwidth` in interface `Api`

      Parameters:
      :   `txn` - the transaction to be estimated.
    - #### broadcastTransaction

      ```
      public java.lang.String broadcastTransaction(Chain.Transaction txn)
                                            throws java.lang.RuntimeException
      ```

      broadcast a transaction with the binding account.

      Specified by:
      :   `broadcastTransaction` in interface `Api`

      Parameters:
      :   `txn` - a signed transaction ready to be broadcasted

      Returns:
      :   a TransactionReturn object contains the broadcasting result

      Throws:
      :   `java.lang.RuntimeException` - if broadcastin fails
    - #### transfer

      ```
      public Response.TransactionExtention transfer(java.lang.String fromAddress,
                                                    java.lang.String toAddress,
                                                    long amount)
                                             throws IllegalException
      ```

      Transfer TRX. amount in SUN

      Specified by:
      :   `transfer` in interface `Api`

      Parameters:
      :   `fromAddress` - owner address
      :   `toAddress` - receive balance
      :   `amount` - transfer amount

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to transfer
    - #### transferTrc10

      ```
      public Response.TransactionExtention transferTrc10(java.lang.String fromAddress,
                                                         java.lang.String toAddress,
                                                         int tokenId,
                                                         long amount)
                                                  throws IllegalException
      ```

      Transfers TRC10 Asset

      Specified by:
      :   `transferTrc10` in interface `Api`

      Parameters:
      :   `fromAddress` - owner address
      :   `toAddress` - receive balance
      :   `tokenId` - asset name
      :   `amount` - transfer amount

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to transfer trc10
    - #### freezeBalance

      ```
      public Response.TransactionExtention freezeBalance(java.lang.String ownerAddress,
                                                         long frozenBalance,
                                                         int frozenDuration,
                                                         int resourceCode)
                                                  throws IllegalException
      ```

      Freeze balance to get energy or bandwidth, for 3 days

      Specified by:
      :   `freezeBalance` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `frozenBalance` - frozen balance
      :   `frozenDuration` - frozen duration
      :   `resourceCode` - Resource type, can be 0("BANDWIDTH") or 1("ENERGY")

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to freeze balance
    - #### freezeBalance

      ```
      public Response.TransactionExtention freezeBalance(java.lang.String ownerAddress,
                                                         long frozenBalance,
                                                         int frozenDuration,
                                                         int resourceCode,
                                                         java.lang.String receiveAddress)
                                                  throws IllegalException
      ```

      Freeze balance to get energy or bandwidth, for 3 days

      Specified by:
      :   `freezeBalance` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `frozenBalance` - frozen balance
      :   `frozenDuration` - frozen duration
      :   `resourceCode` - Resource type, can be 0("BANDWIDTH") or 1("ENERGY")
      :   `receiveAddress` - the address that will receive the resource, default hexString

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to freeze balance
    - #### freezeBalanceV2

      ```
      public Response.TransactionExtention freezeBalanceV2(java.lang.String ownerAddress,
                                                           long frozenBalance,
                                                           int resourceCode)
                                                    throws IllegalException
      ```

      Stake2.0 API
      Stake an amount of TRX to obtain bandwidth or energy, and obtain equivalent TRON Power(TP) according to the staked amount

      Specified by:
      :   `freezeBalanceV2` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `frozenBalance` - TRX stake amount, the unit is sun
      :   `resourceCode` - resource type, can be 0("BANDWIDTH") or 1("ENERGY")

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to freeze balance
    - #### unfreezeBalance

      ```
      public Response.TransactionExtention unfreezeBalance(java.lang.String ownerAddress,
                                                           int resourceCode)
                                                    throws IllegalException
      ```

      Unfreeze balance to get TRX back

      Specified by:
      :   `unfreezeBalance` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `resourceCode` - Resource type, can be 0("BANDWIDTH") or 1("ENERGY")

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to unfreeze balance
    - #### unfreezeBalance

      ```
      public Response.TransactionExtention unfreezeBalance(java.lang.String ownerAddress,
                                                           int resourceCode,
                                                           java.lang.String receiveAddress)
                                                    throws IllegalException
      ```

      Unfreeze balance to get TRX back

      Specified by:
      :   `unfreezeBalance` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `resourceCode` - Resource type, can be 0("BANDWIDTH") or 1("ENERGY")
      :   `receiveAddress` - the address that will lose the resource, default hexString

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to unfreeze balance
    - #### unfreezeBalanceV2

      ```
      public Response.TransactionExtention unfreezeBalanceV2(java.lang.String ownerAddress,
                                                             long unfreezeBalance,
                                                             int resourceCode)
                                                      throws IllegalException
      ```

      Stake2.0 API
      Unstake some TRX, release the corresponding amount of bandwidth or energy, and voting rights (TP)

      Specified by:
      :   `unfreezeBalanceV2` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `unfreezeBalance` - the amount of TRX to unstake, in sun
      :   `resourceCode` - Resource type, can be 0("BANDWIDTH") or 1("ENERGY")

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to unfreeze balance
    - #### cancelAllUnfreezeV2

      ```
      public Response.TransactionExtention cancelAllUnfreezeV2(java.lang.String ownerAddress)
                                                        throws IllegalException
      ```

      Stake2.0 API
      Cancel all the unstaking transactions in the waiting period

      Specified by:
      :   `cancelAllUnfreezeV2` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to delegate resource
    - #### delegateResource

      ```
      public Response.TransactionExtention delegateResource(java.lang.String ownerAddress,
                                                            long balance,
                                                            int resourceCode,
                                                            java.lang.String receiverAddress,
                                                            boolean lock)
                                                     throws IllegalException
      ```

      Stake2.0 API
      Delegate bandwidth or energy resources to other accounts

      Specified by:
      :   `delegateResource` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `balance` - Amount of TRX staked for resources to be delegated, unit is sun
      :   `resourceCode` - Resource type, can be 0("BANDWIDTH") or 1("ENERGY")
      :   `receiverAddress` - Resource receiver address
      :   `lock` - Whether it is locked, if it is set to true,
          the delegated resources cannot be undelegated within 3 days.
          When the lock time is not over, if the owner delegates the same type of resources using the lock to the same address,
          the lock time will be reset to 3 days

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to delegate resource
    - #### delegateResourceV2

      ```
      public Response.TransactionExtention delegateResourceV2(java.lang.String ownerAddress,
                                                              long balance,
                                                              int resourceCode,
                                                              java.lang.String receiverAddress,
                                                              boolean lock,
                                                              long lockPeriod)
                                                       throws IllegalException
      ```

      Stake2.0 API
      Delegate bandwidth or energy resources to other accounts

      Specified by:
      :   `delegateResourceV2` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `balance` - Amount of TRX staked for resources to be delegated, unit is sun
      :   `resourceCode` - Resource type, can be 0("BANDWIDTH") or 1("ENERGY")
      :   `receiverAddress` - Resource receiver address
      :   `lock` - Whether it is locked, if it is set to true,
          the delegated resources cannot be undelegated within 3 days.
          When the lock time is not over, if the owner delegates the same type of resources using the lock to the same address,
          the lock time will be reset to 3 days
      :   `lockPeriod` - The lockup period, unit is blocks, data type is int256,
          It indicates how many blocks the resource delegating is locked before it can be undelegated.

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to delegate resource
    - #### undelegateResource

      ```
      public Response.TransactionExtention undelegateResource(java.lang.String ownerAddress,
                                                              long balance,
                                                              int resourceCode,
                                                              java.lang.String receiverAddress)
                                                       throws IllegalException
      ```

      Stake2.0 API
      unDelegate resource

      Specified by:
      :   `undelegateResource` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `balance` - Amount of TRX staked for resources to be delegated, unit is sun
      :   `resourceCode` - Resource type, can be 0("BANDWIDTH") or 1("ENERGY")
      :   `receiverAddress` - Resource receiver address

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to undelegate resource
    - #### withdrawExpireUnfreeze

      ```
      public Response.TransactionExtention withdrawExpireUnfreeze(java.lang.String ownerAddress)
                                                           throws IllegalException
      ```

      Stake2.0 API
      withdraw unfrozen balance

      Specified by:
      :   `withdrawExpireUnfreeze` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to withdraw
    - #### getAvailableUnfreezeCount

      ```
      public long getAvailableUnfreezeCount(java.lang.String ownerAddress,
                                            NodeType... nodeType)
      ```

      Stake2.0 API
      query remaining times of executing unstake operation

      Specified by:
      :   `getAvailableUnfreezeCount` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   remaining times of executing unstake operation
    - #### getCanWithdrawUnfreezeAmount

      ```
      public long getCanWithdrawUnfreezeAmount(java.lang.String ownerAddress,
                                               NodeType... nodeType)
      ```

      Stake2.0 API
      query the withdrawable balance at the latest block timestamp

      Specified by:
      :   `getCanWithdrawUnfreezeAmount` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   withdrawable balance amount
    - #### getCanWithdrawUnfreezeAmount

      ```
      public long getCanWithdrawUnfreezeAmount(java.lang.String ownerAddress,
                                               long timestamp,
                                               NodeType... nodeType)
      ```

      Stake2.0 API
      query the withdrawable balance at the specified timestamp

      Specified by:
      :   `getCanWithdrawUnfreezeAmount` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `timestamp` - specified timestamp, milliseconds
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   withdrawable balance amount
    - #### getCanDelegatedMaxSize

      ```
      public long getCanDelegatedMaxSize(java.lang.String ownerAddress,
                                         int type,
                                         NodeType... nodeType)
      ```

      Stake2.0 API
      query the amount of delegatable resources share of the specified resource type for an address, unit is sun.

      Specified by:
      :   `getCanDelegatedMaxSize` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `type` - resource type, 0 is bandwidth, 1 is energy
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   the max amount of delegatable resources
    - #### getDelegatedResourceV2

      ```
      public Response.DelegatedResourceList getDelegatedResourceV2(java.lang.String fromAddress,
                                                                   java.lang.String toAddress,
                                                                   NodeType... nodeType)
      ```

      Stake2.0 API
      query the detail of resource share delegated from fromAddress to toAddress

      Specified by:
      :   `getDelegatedResourceV2` in interface `Api`

      Parameters:
      :   `fromAddress` - from address
      :   `toAddress` - to address
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   DelegatedResourceList
    - #### getDelegatedResourceAccountIndexV2

      ```
      public Response.DelegatedResourceAccountIndex getDelegatedResourceAccountIndexV2(java.lang.String address,
                                                                                       NodeType... nodeType)
                                                                                throws IllegalException
      ```

      Stake2.0 API
      query the delegated resource index of an account.

      Specified by:
      :   `getDelegatedResourceAccountIndexV2` in interface `Api`

      Parameters:
      :   `address` - owner address
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   DelegatedResourceAccountIndex

      Throws:
      :   `IllegalException` - if fail to get resource
    - #### voteWitness

      ```
      public Response.TransactionExtention voteWitness(java.lang.String ownerAddress,
                                                       java.util.HashMap<java.lang.String,java.lang.String> votes)
                                                throws IllegalException
      ```

      Vote for witnesses

      Specified by:
      :   `voteWitness` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `votes` - map of vote address -> vote count

      Returns:
      :   TransactionExtention
          IllegalNumException if fail to vote witness

      Throws:
      :   `IllegalException`
    - #### createAccount

      ```
      public Response.TransactionExtention createAccount(java.lang.String ownerAddress,
                                                         java.lang.String accountAddress)
                                                  throws IllegalException
      ```

      Create an account. Uses an already activated account to create a new account

      Specified by:
      :   `createAccount` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address, an activated account
      :   `accountAddress` - the address of the new account

      Returns:
      :   TransactionExtention
          IllegalNumException if fail to create account

      Throws:
      :   `IllegalException`
    - #### updateAccount

      ```
      public Response.TransactionExtention updateAccount(java.lang.String address,
                                                         java.lang.String accountName)
                                                  throws IllegalException
      ```

      Modify account name

      Specified by:
      :   `updateAccount` in interface `Api`

      Parameters:
      :   `address` - owner address
      :   `accountName` - the name of the account

      Returns:
      :   TransactionExtention
          IllegalNumException if fail to update account name

      Throws:
      :   `IllegalException`
    - #### getNowBlock

      ```
      public Chain.Block getNowBlock(NodeType... nodeType)
                              throws IllegalException
      ```

      Query the latest block information

      Specified by:
      :   `getNowBlock` in interface `Api`

      Parameters:
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   Block

      Throws:
      :   `IllegalException` - if fail to get now block
    - #### getNowBlock2

      ```
      public Response.BlockExtention getNowBlock2(NodeType... nodeType)
                                           throws IllegalException
      ```

      Query the latest block information

      Specified by:
      :   `getNowBlock2` in interface `Api`

      Parameters:
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   BlockExtention

      Throws:
      :   `IllegalException` - if fail to get now block
    - #### getBlockByNum

      ```
      public Response.BlockExtention getBlockByNum(long blockNum,
                                                   NodeType... nodeType)
                                            throws IllegalException
      ```

      Query block information by block height, it called getBlockByNum2 rpc

      Specified by:
      :   `getBlockByNum` in interface `Api`

      Parameters:
      :   `blockNum` - The block height
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   BlockExtention

      Throws:
      :   `IllegalException` - if fail to get block
    - #### getBlockByLatestNum

      ```
      public Response.BlockListExtention getBlockByLatestNum(long num)
                                                      throws IllegalException
      ```

      Get some latest blocks

      Specified by:
      :   `getBlockByLatestNum` in interface `Api`

      Parameters:
      :   `num` - Number of latest blocks

      Returns:
      :   BlockListExtention

      Throws:
      :   `IllegalException` - if the parameters are not correct
    - #### getBlockByLimitNext

      ```
      public Response.BlockListExtention getBlockByLimitNext(long startNum,
                                                             long endNum)
                                                      throws IllegalException
      ```

      Returns the list of Block Objects included in the 'Block Height' range specified

      Specified by:
      :   `getBlockByLimitNext` in interface `Api`

      Parameters:
      :   `startNum` - Number of start block height, including this block
      :   `endNum` - Number of end block height, excluding this block

      Returns:
      :   BlockListExtention

      Throws:
      :   `IllegalException` - if the blockList Not Found.
    - #### getNodeInfo

      ```
      public Response.NodeInfo getNodeInfo()
                                    throws IllegalException
      ```

      Get current API node info

      Specified by:
      :   `getNodeInfo` in interface `Api`

      Returns:
      :   NodeInfo

      Throws:
      :   `IllegalException` - if fail to get nodeInfo
    - #### listNodes

      ```
      public Response.NodeList listNodes()
                                  throws IllegalException
      ```

      List all nodes that current API node is connected to

      Specified by:
      :   `listNodes` in interface `Api`

      Returns:
      :   NodeList

      Throws:
      :   `IllegalException` - if fail to get node list
    - #### getTransactionInfoByBlockNum

      ```
      public Response.TransactionInfoList getTransactionInfoByBlockNum(long blockNum,
                                                                       NodeType... nodeType)
                                                                throws IllegalException
      ```

      Get transactionInfo from block number

      Specified by:
      :   `getTransactionInfoByBlockNum` in interface `Api`

      Parameters:
      :   `blockNum` - The block height
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   TransactionInfoList

      Throws:
      :   `IllegalException` - no transactions or the blockNum is incorrect
    - #### getTransactionInfoById

      ```
      public Response.TransactionInfo getTransactionInfoById(java.lang.String txID,
                                                             NodeType... nodeType)
                                                      throws IllegalException
      ```

      Query the transactionInfo by transaction id

      Specified by:
      :   `getTransactionInfoById` in interface `Api`

      Parameters:
      :   `txID` - Transaction hash, i.e. transaction id
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   TransactionInfo

      Throws:
      :   `IllegalException` - if the transactionInfo not found
    - #### getTransactionById

      ```
      public Chain.Transaction getTransactionById(java.lang.String txID,
                                                  NodeType... nodeType)
                                           throws IllegalException
      ```

      Query transaction information by transaction id

      Specified by:
      :   `getTransactionById` in interface `Api`

      Parameters:
      :   `txID` - Transaction hash, i.e. transaction id
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   Transaction

      Throws:
      :   `IllegalException` - if the transaction not found
    - #### getAccount

      ```
      public Response.Account getAccount(java.lang.String address,
                                         NodeType... nodeType)
      ```

      Get account info by address

      Specified by:
      :   `getAccount` in interface `Api`

      Parameters:
      :   `address` - address, default hexString
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   Account
    - #### getAccountResource

      ```
      public Response.AccountResourceMessage getAccountResource(java.lang.String address)
      ```

      Query the resource information of an account(bandwidth,energy,etc)

      Specified by:
      :   `getAccountResource` in interface `Api`

      Parameters:
      :   `address` - address, default hexString

      Returns:
      :   AccountResourceMessage
    - #### getAccountNet

      ```
      public Response.AccountNetMessage getAccountNet(java.lang.String address)
      ```

      Query bandwidth information

      Specified by:
      :   `getAccountNet` in interface `Api`

      Parameters:
      :   `address` - address, default hexString

      Returns:
      :   AccountResourceMessage
    - #### getAccountBalance

      ```
      public long getAccountBalance(java.lang.String address)
      ```

      Specified by:
      :   `getAccountBalance` in interface `Api`
    - #### getAccountById

      ```
      public Response.Account getAccountById(java.lang.String id,
                                             NodeType... nodeType)
      ```

      Specified by:
      :   `getAccountById` in interface `Api`
    - #### setAccountId

      ```
      public Chain.Transaction setAccountId(java.lang.String id,
                                            java.lang.String address)
                                     throws IllegalException
      ```

      Specified by:
      :   `setAccountId` in interface `Api`

      Throws:
      :   `IllegalException`
    - #### setAccountId2

      ```
      public Response.TransactionExtention setAccountId2(java.lang.String id,
                                                         java.lang.String address)
                                                  throws IllegalException
      ```

      Specified by:
      :   `setAccountId2` in interface `Api`

      Throws:
      :   `IllegalException`
    - #### getChainParameters

      ```
      public Response.ChainParameters getChainParameters()
                                                  throws IllegalException
      ```

      All parameters that the blockchain committee can set

      Specified by:
      :   `getChainParameters` in interface `Api`

      Returns:
      :   ChainParameters

      Throws:
      :   `IllegalException` - if fail to get chain parameters
    - #### getDelegatedResource

      ```
      public Response.DelegatedResourceList getDelegatedResource(java.lang.String fromAddress,
                                                                 java.lang.String toAddress,
                                                                 NodeType... nodeType)
      ```

      Returns all resources delegations from an account to another account. The fromAddress can be retrieved from the GetDelegatedResourceAccountIndex API

      Specified by:
      :   `getDelegatedResource` in interface `Api`

      Parameters:
      :   `fromAddress` - energy from address, default hexString
      :   `toAddress` - energy delegation information, default hexString
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   DelegatedResourceList
    - #### getDelegatedResourceAccountIndex

      ```
      public Response.DelegatedResourceAccountIndex getDelegatedResourceAccountIndex(java.lang.String address,
                                                                                     NodeType... nodeType)
      ```

      Query the energy delegation by an account. i.e. list all addresses that have delegated resources to an account

      Specified by:
      :   `getDelegatedResourceAccountIndex` in interface `Api`

      Parameters:
      :   `address` - address,, default hexString
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   DelegatedResourceAccountIndex
    - #### getAssetIssueList

      ```
      public Response.AssetIssueList getAssetIssueList(NodeType... nodeType)
      ```

      Query the list of all the TRC10 tokens

      Specified by:
      :   `getAssetIssueList` in interface `Api`

      Parameters:
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   AssetIssueList
    - #### getPaginatedAssetIssueList

      ```
      public Response.AssetIssueList getPaginatedAssetIssueList(long offset,
                                                                long limit,
                                                                NodeType... nodeType)
      ```

      Query the list of all the tokens by pagination.

      Specified by:
      :   `getPaginatedAssetIssueList` in interface `Api`

      Parameters:
      :   `offset` - the index of the start token
      :   `limit` - the amount of tokens per page
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   AssetIssueList, a list of Tokens that succeed the Token located at offset
    - #### getAssetIssueByAccount

      ```
      public Response.AssetIssueList getAssetIssueByAccount(java.lang.String address)
      ```

      Query the TRC10 token information issued by an account

      Specified by:
      :   `getAssetIssueByAccount` in interface `Api`

      Parameters:
      :   `address` - the Token Issuer account address

      Returns:
      :   AssetIssueList, a list of Tokens that succeed the Token located at offset
    - #### getAssetIssueById

      ```
      public Contract.AssetIssueContract getAssetIssueById(java.lang.String assetId,
                                                           NodeType... nodeType)
      ```

      Query a token by token id

      Specified by:
      :   `getAssetIssueById` in interface `Api`

      Parameters:
      :   `assetId` - the ID of the TRC10 token
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   AssetIssueContract, the token object, which contains the token name
    - #### getAssetIssueByName

      ```
      public Contract.AssetIssueContract getAssetIssueByName(java.lang.String name,
                                                             NodeType... nodeType)
      ```

      Query a token by token name

      Specified by:
      :   `getAssetIssueByName` in interface `Api`

      Parameters:
      :   `name` - the name of the TRC10 token
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   AssetIssueContract, the token object, which contains the token name
    - #### getAssetIssueListByName

      ```
      public Response.AssetIssueList getAssetIssueListByName(java.lang.String name,
                                                             NodeType... nodeType)
      ```

      Query the list of all the TRC10 tokens by token name

      Specified by:
      :   `getAssetIssueListByName` in interface `Api`

      Parameters:
      :   `name` - the name of the TRC10 token
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   AssetIssueList
    - #### participateAssetIssue

      ```
      public Response.TransactionExtention participateAssetIssue(java.lang.String toAddress,
                                                                 java.lang.String ownerAddress,
                                                                 java.lang.String assertName,
                                                                 long amount)
                                                          throws IllegalException
      ```

      Participate a token

      Specified by:
      :   `participateAssetIssue` in interface `Api`

      Parameters:
      :   `toAddress` - the issuer address of the token, default hexString
      :   `ownerAddress` - the participant address, default hexString
      :   `assertName` - token id, default hexString
      :   `amount` - participate token amount

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to participate AssetIssue
    - #### listProposals

      ```
      public Response.ProposalList listProposals()
      ```

      List all proposals

      Specified by:
      :   `listProposals` in interface `Api`

      Returns:
      :   ProposalList
    - #### getProposalById

      ```
      public Response.Proposal getProposalById(java.lang.String id)
      ```

      Query proposal based on ID

      Specified by:
      :   `getProposalById` in interface `Api`

      Parameters:
      :   `id` - proposal id

      Returns:
      :   Proposal, proposal details
    - #### listWitnesses

      ```
      public Response.WitnessList listWitnesses(NodeType... nodeType)
      ```

      List all witnesses that current API node is connected to

      Specified by:
      :   `listWitnesses` in interface `Api`

      Parameters:
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   WitnessList
    - #### getPaginatedNowWitnessList

      ```
      public Response.WitnessList getPaginatedNowWitnessList(long offset,
                                                             long limit,
                                                             NodeType... nodeType)
      ```

      Get a paginated list of real-time witnesses ordered by vote count
      Note: This method may throw an exception when FullNode is in the maintenance period.

      Specified by:
      :   `getPaginatedNowWitnessList` in interface `Api`

      Parameters:
      :   `offset` - the pagination offset, specifying the starting index of witnesses to return (0-based)
      :   `limit` - the number of witnesses to return
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, use full node default.
          If NodeType.SOLIDITY\_NODE, use solidity node.

      Returns:
      :   WitnessList
    - #### listExchanges

      ```
      public Response.ExchangeList listExchanges(NodeType... nodeType)
      ```

      List all exchange pairs

      Specified by:
      :   `listExchanges` in interface `Api`

      Parameters:
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   ExchangeList
    - #### getExchangeById

      ```
      public Response.Exchange getExchangeById(java.lang.String id,
                                               NodeType... nodeType)
                                        throws IllegalException
      ```

      Query exchange pair based on id

      Specified by:
      :   `getExchangeById` in interface `Api`

      Parameters:
      :   `id` - transaction pair id
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   Exchange

      Throws:
      :   `IllegalException` - if fail to get exchange pair
    - #### createAssetIssue

      ```
      public Response.TransactionExtention createAssetIssue(java.lang.String ownerAddress,
                                                            java.lang.String name,
                                                            java.lang.String abbr,
                                                            long totalSupply,
                                                            int trxNum,
                                                            int icoNum,
                                                            long startTime,
                                                            long endTime,
                                                            java.lang.String url,
                                                            long freeAssetNetLimit,
                                                            long publicFreeAssetNetLimit,
                                                            int precision,
                                                            java.util.HashMap<java.lang.String,java.lang.String> frozenSupply,
                                                            java.lang.String description)
                                                     throws IllegalException
      ```

      Issue a token

      Specified by:
      :   `createAssetIssue` in interface `Api`

      Parameters:
      :   `ownerAddress` - Owner address, default hexString
      :   `name` - Token name, default hexString
      :   `abbr` - Token name abbreviation, default hexString
      :   `totalSupply` - Token total supply
      :   `trxNum` - Define the price by the ratio of trx\_num/num
      :   `icoNum` - Define the price by the ratio of trx\_num/num
      :   `startTime` - ICO start time
      :   `endTime` - ICO end time
      :   `url` - Token official website url, default hexString
      :   `freeAssetNetLimit` - Token free asset net limit
      :   `publicFreeAssetNetLimit` - Token public free asset net limit
      :   `frozenSupply` - HashMap of frozenDay -> frozenAmount
      :   `description` - Token description, default hexString

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to create AssetIssue
    - #### createAssetIssue

      ```
      public Response.TransactionExtention createAssetIssue(java.lang.String ownerAddress,
                                                            java.lang.String name,
                                                            java.lang.String abbr,
                                                            long totalSupply,
                                                            int trxNum,
                                                            int icoNum,
                                                            long startTime,
                                                            long endTime,
                                                            java.lang.String url,
                                                            long freeAssetNetLimit,
                                                            long publicFreeAssetNetLimit,
                                                            int precision,
                                                            java.lang.String description)
                                                     throws IllegalException
      ```

      Issue a token

      Specified by:
      :   `createAssetIssue` in interface `Api`

      Parameters:
      :   `ownerAddress` - Owner address, default hexString
      :   `name` - Token name, default hexString
      :   `abbr` - Token name abbreviation, default hexString
      :   `totalSupply` - Token total supply
      :   `trxNum` - Define the price by the ratio of trx\_num/num
      :   `icoNum` - Define the price by the ratio of trx\_num/num
      :   `startTime` - ICO start time
      :   `endTime` - ICO end time
      :   `url` - Token official website url, default hexString
      :   `freeAssetNetLimit` - Token free asset net limit
      :   `publicFreeAssetNetLimit` - Token public free asset net limit
      :   `description` - Token description, default hexString

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to create AssetIssue
    - #### assetIssueContractBuilder

      ```
      public Contract.AssetIssueContract.Builder assetIssueContractBuilder(java.lang.String ownerAddress,
                                                                           java.lang.String name,
                                                                           java.lang.String abbr,
                                                                           long totalSupply,
                                                                           int trxNum,
                                                                           int icoNum,
                                                                           long startTime,
                                                                           long endTime,
                                                                           java.lang.String url,
                                                                           long freeAssetNetLimit,
                                                                           long publicFreeAssetNetLimit,
                                                                           int precision,
                                                                           java.lang.String description)
      ```

      Specified by:
      :   `assetIssueContractBuilder` in interface `Api`
    - #### updateAsset

      ```
      public Response.TransactionExtention updateAsset(java.lang.String ownerAddress,
                                                       java.lang.String description,
                                                       java.lang.String url,
                                                       long newLimit,
                                                       long newPublicLimit)
                                                throws IllegalException
      ```

      Update basic TRC10 token information

      Specified by:
      :   `updateAsset` in interface `Api`

      Parameters:
      :   `ownerAddress` - Owner address, default hexString
      :   `description` - The description of token, default hexString
      :   `url` - The token's website url, default hexString
      :   `newLimit` - Each token holder's free bandwidth
      :   `newPublicLimit` - The total free bandwidth of the token

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to update asset
    - #### unfreezeAsset

      ```
      public Response.TransactionExtention unfreezeAsset(java.lang.String ownerAddress)
                                                  throws IllegalException
      ```

      Unfreeze a token that has passed the minimum freeze duration

      Specified by:
      :   `unfreezeAsset` in interface `Api`

      Parameters:
      :   `ownerAddress` - Owner address, default hexString

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to unfreeze asset
    - #### accountPermissionUpdate

      ```
      public Response.TransactionExtention accountPermissionUpdate(Contract.AccountPermissionUpdateContract accountPermissionUpdateContract)
                                                            throws IllegalException
      ```

      Update account permissions for multiSign

      Specified by:
      :   `accountPermissionUpdate` in interface `Api`

      Parameters:
      :   `accountPermissionUpdateContract` - AccountPermissionUpdateContract

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to update account permission
    - #### accountPermissionUpdate

      ```
      public Response.TransactionExtention accountPermissionUpdate(java.lang.String ownerAddress,
                                                                   AccountPermissions accountPermissions)
                                                            throws IllegalException
      ```

      update account permissions with new owner/witness/active permissions

      Specified by:
      :   `accountPermissionUpdate` in interface `Api`

      Parameters:
      :   `ownerAddress` - Owner address
      :   `accountPermissions` - New AccountPermission (containing owner/witness/active permissions)

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if newOwnerPermission or newActivePermissions is null
    - #### getAccountPermissions

      ```
      public AccountPermissions getAccountPermissions(java.lang.String address,
                                                      NodeType... nodeType)
      ```

      Retrieves the permissions of a TRON account.

      It queries the account using [`getAccount(String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getAccount-java.lang.String-org.tron.trident.core.NodeType...-) and
      wraps the result into an [`AccountPermissions`](../../../../org/tron/trident/core/account/AccountPermissions.html "class in org.tron.trident.core.account") object.

      Specified by:
      :   `getAccountPermissions` in interface `Api`

      Parameters:
      :   `address` - account, in any allowed formats.
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, use full node default.
          If NodeType.SOLIDITY\_NODE, use solidity node.

      Returns:
      :   AccountPermissions, null if the account does not exist or inactive
    - #### getTransactionSignWeight

      ```
      public Response.TransactionSignWeight getTransactionSignWeight(Chain.Transaction trx)
      ```

      Query transaction sign weight

      Specified by:
      :   `getTransactionSignWeight` in interface `Api`

      Parameters:
      :   `trx` - transaction object

      Returns:
      :   TransactionSignWeight
    - #### getTransactionApprovedList

      ```
      public Response.TransactionApprovedList getTransactionApprovedList(Chain.Transaction trx)
      ```

      Query transaction approvedList

      Specified by:
      :   `getTransactionApprovedList` in interface `Api`

      Parameters:
      :   `trx` - transaction object

      Returns:
      :   TransactionApprovedList
    - #### getAccountSolidity

      ```
      @Deprecated
      public Response.Account getAccountSolidity(java.lang.String address)
      ```

      Deprecated. Since 0.10.0, scheduled for removal in future versions.
      use [`getAccount(String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getAccount-java.lang.String-org.tron.trident.core.NodeType...-) instead

      Get solid account info by address

      Specified by:
      :   `getAccountSolidity` in interface `Api`

      Parameters:
      :   `address` - address, default hexString

      Returns:
      :   Account
    - #### getTransactionInfoByBlockNumSolidity

      ```
      @Deprecated
      public Response.TransactionInfoList getTransactionInfoByBlockNumSolidity(long blockNum)
                                                                                    throws IllegalException
      ```

      Deprecated. Since 0.10.0, scheduled for removal in future versions.
      use [`getTransactionInfoByBlockNum(long, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getTransactionInfoByBlockNum-long-org.tron.trident.core.NodeType...-) instead

      Get transactionInfo from block number

      Specified by:
      :   `getTransactionInfoByBlockNumSolidity` in interface `Api`

      Parameters:
      :   `blockNum` - The block height

      Returns:
      :   TransactionInfoList

      Throws:
      :   `IllegalException` - no transactions or the blockNum is incorrect
    - #### getNowBlockSolidity

      ```
      @Deprecated
      public Response.BlockExtention getNowBlockSolidity()
                                                              throws IllegalException
      ```

      Deprecated. Since 0.10.0, scheduled for removal in future versions.
      use [`getNowBlock2(NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getNowBlock2-org.tron.trident.core.NodeType...-) instead

      Query the latest solid block information

      Specified by:
      :   `getNowBlockSolidity` in interface `Api`

      Returns:
      :   BlockExtention

      Throws:
      :   `IllegalException` - if fail to get now block
    - #### getTransactionByIdSolidity

      ```
      @Deprecated
      public Chain.Transaction getTransactionByIdSolidity(java.lang.String txID)
                                                               throws IllegalException
      ```

      Deprecated. Since 0.10.0, scheduled for removal in future versions.
      use [`getTransactionById(String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getTransactionById-java.lang.String-org.tron.trident.core.NodeType...-) instead

      Get transaction from a transaction id, must be in solid block

      Specified by:
      :   `getTransactionByIdSolidity` in interface `Api`

      Parameters:
      :   `txID` - Transaction hash, i.e. transaction id

      Returns:
      :   Transaction

      Throws:
      :   `IllegalException` - if the transaction not found
    - #### getRewardInfo

      ```
      public GrpcAPI.NumberMessage getRewardInfo(java.lang.String address,
                                                 NodeType... nodeType)
      ```

      Get the rewards that the voter has not received

      Specified by:
      :   `getRewardInfo` in interface `Api`

      Parameters:
      :   `address` - address, default hexString
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   NumberMessage
    - #### getRewardSolidity

      ```
      @Deprecated
      public GrpcAPI.NumberMessage getRewardSolidity(java.lang.String address)
      ```

      Deprecated. Since 0.10.0, scheduled for removal in future versions.
      use [`getRewardInfo(String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getRewardInfo-java.lang.String-org.tron.trident.core.NodeType...-) instead

      Get the rewards that the voter has not received

      Specified by:
      :   `getRewardSolidity` in interface `Api`

      Parameters:
      :   `address` - address, default hexString

      Returns:
      :   NumberMessage
    - #### updateBrokerage

      ```
      public Response.TransactionExtention updateBrokerage(java.lang.String address,
                                                           int brokerage)
                                                    throws IllegalException
      ```

      Specified by:
      :   `updateBrokerage` in interface `Api`

      Throws:
      :   `IllegalException`
    - #### getBrokerageInfo

      ```
      public long getBrokerageInfo(java.lang.String address,
                                   NodeType... nodeType)
      ```

      Query the ratio of brokerage of the witness.

      Specified by:
      :   `getBrokerageInfo` in interface `Api`

      Parameters:
      :   `address` - the address of the witness's account
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   the ratio of brokerage
    - #### getContract

      ```
      public Contract getContract(java.lang.String contractAddress)
      ```

      Obtain a `Contract` object via an address

      Specified by:
      :   `getContract` in interface `Api`

      Parameters:
      :   `contractAddress` - smart contract address

      Returns:
      :   the smart contract obtained from the address
    - #### getSmartContract

      ```
      public Common.SmartContract getSmartContract(java.lang.String contractAddress)
      ```

      Specified by:
      :   `getSmartContract` in interface `Api`
    - #### constantCall

      ```
      @Deprecated
      public Response.TransactionExtention constantCall(java.lang.String ownerAddress,
                                                                    java.lang.String contractAddress,
                                                                    Function function)
      ```

      Deprecated. Since 0.9.2, scheduled for removal in future versions.
      Use [`triggerConstantContract(String, String, Function, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-org.tron.trident.abi.datatypes.Function-org.tron.trident.core.NodeType...-) instead.

      make a constant call - no broadcasting, no need to broadcast

      Specified by:
      :   `constantCall` in interface `Api`

      Parameters:
      :   `ownerAddress` - the current caller.
      :   `contractAddress` - smart contract address.
      :   `function` - contract function.

      Returns:
      :   TransactionExtention.
    - #### constantCallV2

      ```
      @Deprecated
      public Response.TransactionExtention constantCallV2(java.lang.String ownerAddress,
                                                                      java.lang.String contractAddress,
                                                                      java.lang.String callData)
      ```

      Deprecated. Since 0.9.2, scheduled for removal in future versions.
      Use [`triggerConstantContract(String, String, String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-java.lang.String-org.tron.trident.core.NodeType...-) instead.

      make a constant call - no broadcasting, no need to broadcast

      Specified by:
      :   `constantCallV2` in interface `Api`

      Parameters:
      :   `ownerAddress` - the current caller.
      :   `contractAddress` - smart contract address.
      :   `callData` - The data passed along with a transaction that allows us to interact with smart contracts.

      Returns:
      :   TransactionExtention.
    - #### triggerConstantContract

      ```
      public Response.TransactionExtention triggerConstantContract(java.lang.String ownerAddress,
                                                                   java.lang.String contractAddress,
                                                                   Function function,
                                                                   NodeType... nodeType)
      ```

      Specified by:
      :   `triggerConstantContract` in interface `Api`

      See Also:
      :   [`triggerConstantContract(String, String, String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-java.lang.String-org.tron.trident.core.NodeType...-)
    - #### triggerConstantContract

      ```
      public Response.TransactionExtention triggerConstantContract(java.lang.String ownerAddress,
                                                                   java.lang.String contractAddress,
                                                                   java.lang.String callData,
                                                                   NodeType... nodeType)
      ```

      Specified by:
      :   `triggerConstantContract` in interface `Api`

      See Also:
      :   [`triggerConstantContract(String, String, String, long, long, String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-java.lang.String-long-long-java.lang.String-org.tron.trident.core.NodeType...-)
    - #### triggerConstantContract

      ```
      public Response.TransactionExtention triggerConstantContract(java.lang.String ownerAddress,
                                                                   java.lang.String contractAddress,
                                                                   java.lang.String callData,
                                                                   long callValue,
                                                                   long tokenValue,
                                                                   java.lang.String tokenId,
                                                                   NodeType... nodeType)
      ```

      make a constant call - no broadcasting, no need to broadcast

      Specified by:
      :   `triggerConstantContract` in interface `Api`

      Parameters:
      :   `ownerAddress` - the current caller.
      :   `contractAddress` - smart contract address.
      :   `callData` - The data passed along with a transaction that allows us to interact with smart
          contracts. It can be obtained by using [`FunctionEncoder.encode(org.tron.trident.abi.datatypes.Function)`](../../../../org/tron/trident/abi/FunctionEncoder.html#encode-org.tron.trident.abi.datatypes.Function-).
      :   `callValue` - call Value. If TRX not used, use 0.
      :   `tokenValue` - token Value, If token10 not used, use 0.
      :   `tokenId` - token10 ID, If token10 not used, use null.
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   TransactionExtention.
    - #### triggerCall

      ```
      @Deprecated
      public TransactionBuilder triggerCall(java.lang.String ownerAddress,
                                                        java.lang.String contractAddress,
                                                        Function function)
      ```

      Deprecated. Since 0.9.2, scheduled for removal in future versions.
      Use [`triggerConstantContract(String, String, Function, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-org.tron.trident.abi.datatypes.Function-org.tron.trident.core.NodeType...-) instead.

      make a constant call - no broadcasting, no need to broadcast

      Specified by:
      :   `triggerCall` in interface `Api`

      Parameters:
      :   `ownerAddress` - the current caller
      :   `contractAddress` - smart contract address
      :   `function` - contract function

      Returns:
      :   transaction builder. Users may set other fields, e.g. feeLimit
    - #### triggerCallV2

      ```
      @Deprecated
      public TransactionBuilder triggerCallV2(java.lang.String ownerAddress,
                                                          java.lang.String contractAddress,
                                                          java.lang.String callData)
      ```

      Deprecated. Since 0.9.2, scheduled for removal in future versions.
      Use [`triggerConstantContract(String, String, String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#triggerConstantContract-java.lang.String-java.lang.String-java.lang.String-org.tron.trident.core.NodeType...-) instead.

      make a constant call - no broadcasting, no need to broadcast

      Specified by:
      :   `triggerCallV2` in interface `Api`

      Parameters:
      :   `ownerAddress` - the current caller
      :   `contractAddress` - smart contract address
      :   `callData` - The data passed along with a transaction that allows us to interact with smart contracts.

      Returns:
      :   transaction builder. TransactionExtention detail.
    - #### triggerContract

      ```
      public Response.TransactionExtention triggerContract(java.lang.String ownerAddress,
                                                           java.lang.String contractAddress,
                                                           java.lang.String callData,
                                                           long callValue,
                                                           long tokenValue,
                                                           java.lang.String tokenId,
                                                           long feeLimit)
                                                    throws java.lang.Exception
      ```

      make a TriggerSmartContract, - no broadcasting. it can be broadcast later.

      Specified by:
      :   `triggerContract` in interface `Api`

      Parameters:
      :   `ownerAddress` - the current caller
      :   `contractAddress` - smart contract address
      :   `callData` - the encoded function call data
      :   `callValue` - the amount of sun send to contract. If not used, set 0
      :   `tokenValue` - the amount of tokenId. If not used, set 0
      :   `tokenId` - tokenId. If not used, set null
      :   `feeLimit` - fee unit:SUN

      Returns:
      :   TransactionExtention

      Throws:
      :   `java.lang.Exception` - if fail
    - #### getBlockBalance

      ```
      public Response.BlockBalanceTrace getBlockBalance(java.lang.String blockId,
                                                        long blockNum)
      ```

      GetBlockBalance
      Get all balance change operations in a block(Note: At present, the interface data can only be queried through the following official nodes
      47.241.20.47; 161.117.85.97; 161.117.224.116; 161.117.83.38)

      Specified by:
      :   `getBlockBalance` in interface `Api`

      Parameters:
      :   `blockId` - tx Id.eg:"000000000309c3c40be03c04615856fc6672b08af6d2cdbbf500a7cf9920fbdb"
      :   `blockNum` - block number

      Returns:
      :   BlockBalanceTrace
    - #### getBurnTRX

      ```
      public long getBurnTRX(NodeType... nodeType)
      ```

      GetBurnTRX
      Query the amount of TRX burned due to on-chain transaction fees since No. 54 Committee Proposal took effect

      Specified by:
      :   `getBurnTRX` in interface `Api`

      Parameters:
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   burn trx amount
    - #### createWitness

      ```
      public Response.TransactionExtention createWitness(java.lang.String ownerAddress,
                                                         java.lang.String url)
                                                  throws IllegalException
      ```

      CreateWitness
      Apply to become a witness.

      Specified by:
      :   `createWitness` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `url` - The website URL of the SR node

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to create witness
    - #### updateWitness

      ```
      public Response.TransactionExtention updateWitness(java.lang.String ownerAddress,
                                                         java.lang.String updateUrl)
                                                  throws IllegalException
      ```

      UpdateWitness
      Edit the URL of the witness's official website.

      Specified by:
      :   `updateWitness` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `updateUrl` - Updated URL

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to update witness
    - #### withdrawBalance

      ```
      public Response.TransactionExtention withdrawBalance(java.lang.String ownerAddress)
                                                    throws IllegalException
      ```

      WithdrawBalance
      Super Representative or user withdraw rewards, usable every 24 hours.
      Super representatives can withdraw the balance from the account allowance into the account balance,
      Users can claim the voting reward from the SRs and deposit into his account balance.

      Specified by:
      :   `withdrawBalance` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to withdraw balance
    - #### getNextMaintenanceTime

      ```
      public long getNextMaintenanceTime()
      ```

      GetNextMaintenanceTime
      Returns the timestamp of the next voting time in milliseconds.

      Specified by:
      :   `getNextMaintenanceTime` in interface `Api`

      Returns:
      :   get next maintenance time
    - #### proposalCreate

      ```
      public Response.TransactionExtention proposalCreate(java.lang.String ownerAddress,
                                                          java.util.Map<java.lang.Long,java.lang.Long> parameters)
                                                   throws IllegalException
      ```

      ProposalCreate
      Creates a proposal transaction.

      Specified by:
      :   `proposalCreate` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `parameters` - Parameters proposed to be modified and their values

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to proposal create
    - #### approveProposal

      ```
      public Response.TransactionExtention approveProposal(java.lang.String ownerAddress,
                                                           long proposalId,
                                                           boolean isAddApproval)
                                                    throws IllegalException
      ```

      ProposalApprove
      Approves proposed transaction.

      Specified by:
      :   `approveProposal` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `proposalId` - Proposal id
      :   `isAddApproval` - Whether to agree with the proposal

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to approve proposal
    - #### deleteProposal

      ```
      public Response.TransactionExtention deleteProposal(java.lang.String ownerAddress,
                                                          long proposalId)
                                                   throws IllegalException
      ```

      ProposalDelete
      Deletes Proposal Transaction.

      Specified by:
      :   `deleteProposal` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `proposalId` - Proposal id

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException` - if fail to delete proposal
    - #### getTransactionListFromPending

      ```
      public GrpcAPI.TransactionIdList getTransactionListFromPending()
      ```

      GetTransactionListFromPending
      Get transaction list information from pending pool

      Specified by:
      :   `getTransactionListFromPending` in interface `Api`

      Returns:
      :   transaction list information from pending pool
    - #### getPendingSize

      ```
      public long getPendingSize()
      ```

      GetPendingSize
      Get the size of the pending pool queue

      Specified by:
      :   `getPendingSize` in interface `Api`

      Returns:
      :   the size of the pending pool queue
    - #### getTransactionFromPending

      ```
      public Chain.Transaction getTransactionFromPending(java.lang.String txId)
                                                  throws IllegalException
      ```

      GetTransactionFromPending
      Get transaction details from the pending pool

      Specified by:
      :   `getTransactionFromPending` in interface `Api`

      Parameters:
      :   `txId` - Transaction ID

      Returns:
      :   Transaction

      Throws:
      :   `IllegalException` - if fail to get transaction from pending
    - #### getBlockById

      ```
      public Chain.Block getBlockById(java.lang.String blockID)
      ```

      GetBlockById
      Query block by ID(block hash).

      Specified by:
      :   `getBlockById` in interface `Api`

      Parameters:
      :   `blockID` - block hash.eg:"00000000000f424013e51b18e0782a32fa079ddafdb2f4c343468cf8896dc887"

      Returns:
      :   the size of the pending pool queue
    - #### estimateEnergy

      ```
      public Response.EstimateEnergyMessage estimateEnergy(java.lang.String ownerAddress,
                                                           java.lang.String contractAddress,
                                                           Function function,
                                                           NodeType... nodeType)
      ```

      Estimate the energy required for the successful execution of smart contract transactions
      This API is closed by default in tron node.
      To open this interface, the two configuration items vm.estimateEnergy and vm.supportConstant
      must be enabled in the node configuration file at the same time.

      Specified by:
      :   `estimateEnergy` in interface `Api`

      Parameters:
      :   `ownerAddress` - Owner address that triggers the contract. If visible=true, use base58check
          format, otherwise use hex format. For constant call you can use the all-zero address.
      :   `contractAddress` - Smart contract address.
      :   `function` - contract function
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   EstimateEnergyMessage. Estimated energy to run the contract
    - #### estimateEnergy

      ```
      public Response.EstimateEnergyMessage estimateEnergy(java.lang.String ownerAddress,
                                                           java.lang.String contractAddress,
                                                           java.lang.String callData,
                                                           long callValue,
                                                           long tokenValue,
                                                           java.lang.String tokenId,
                                                           NodeType... nodeType)
      ```

      Estimate the energy required for the successful execution of smart contract transactions
      This API is closed by default in tron node. To open this interface, the two configuration
      items vm.estimateEnergy and vm.supportConstant must be enabled in the node configuration file
      at the same time.

      Specified by:
      :   `estimateEnergy` in interface `Api`

      Parameters:
      :   `ownerAddress` - Owner address that triggers the contract. If visible=true, use base58check
          format, otherwise use hex format. For constant call you can use the all-zero address.
      :   `contractAddress` - Smart contract address.
      :   `callData` - The data passed along with a transaction that allows us to interact with smart contracts.
      :   `callValue` - call Value. If TRX not used, use 0.
      :   `tokenValue` - token Value, If token10 not used, use 0.
      :   `tokenId` - token10 ID, If token10 not used, use null.
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   EstimateEnergyMessage. Estimated energy to run the contract
    - #### estimateEnergyV2

      ```
      @Deprecated
      public Response.EstimateEnergyMessage estimateEnergyV2(java.lang.String ownerAddress,
                                                                         java.lang.String contractAddress,
                                                                         java.lang.String callData)
      ```

      Deprecated. Since 0.9.2, scheduled for removal in future versions.
      Use [`estimateEnergy(String, String, String, long, long, String, NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#estimateEnergy-java.lang.String-java.lang.String-java.lang.String-long-long-java.lang.String-org.tron.trident.core.NodeType...-) instead.

      Estimate the energy required for the successful execution of smart contract transactions
      This API is closed by default in tron node. To open this interface, the two configuration
      items vm.estimateEnergy and vm.supportConstant must be enabled in the node configuration file
      at the same time.

      Specified by:
      :   `estimateEnergyV2` in interface `Api`

      Parameters:
      :   `ownerAddress` - Owner address that triggers the contract. If visible=true, use base58check
          format, otherwise use hex format.
          For constant call you can use the all-zero address.
      :   `contractAddress` - Smart contract address.
      :   `callData` - The data passed along with a transaction that allows us to interact with smart contracts.

      Returns:
      :   EstimateEnergyMessage. Estimated energy to run the contract
    - #### getBandwidthPrices

      ```
      public Response.PricesResponseMessage getBandwidthPrices(NodeType... nodeType)
      ```

      GetBandwidthPrices
      Query historical bandwidth unit price.

      Specified by:
      :   `getBandwidthPrices` in interface `Api`

      Parameters:
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   prices string: All historical bandwidth unit price information.
          Each unit price change is separated by a comma.
          Before the colon is the millisecond timestamp,
          and after the colon is the bandwidth unit price in sun.
    - #### getEnergyPrices

      ```
      public Response.PricesResponseMessage getEnergyPrices(NodeType... nodeType)
      ```

      GetEnergyPrices
      Query historical energy unit price.

      Specified by:
      :   `getEnergyPrices` in interface `Api`

      Parameters:
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   prices string: All historical bandwidth unit price information.
          Each unit price change is separated by a comma.
          Before the colon is the millisecond timestamp,
          and after the colon is the bandwidth unit price in sun.
    - #### getMemoFee

      ```
      public Response.PricesResponseMessage getMemoFee()
      ```

      GetMemoFee
      Query historical memo fee.

      Specified by:
      :   `getMemoFee` in interface `Api`

      Returns:
      :   prices string: All historical bandwidth unit price information.
          Each unit price change is separated by a comma.
          Before the colon is the millisecond timestamp,
          and after the colon is the bandwidth unit price in sun.
    - #### getBandwidthPricesOnSolidity

      ```
      @Deprecated
      public Response.PricesResponseMessage getBandwidthPricesOnSolidity()
      ```

      Deprecated. Since 0.10.0, scheduled for removal in future versions.
      use [`getBandwidthPrices(NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getBandwidthPrices-org.tron.trident.core.NodeType...-) instead

      GetBandwidthPricesOnSolidity
      Query historical bandwidth unit price.

      Specified by:
      :   `getBandwidthPricesOnSolidity` in interface `Api`

      Returns:
      :   prices string: All historical bandwidth unit price information.
          Each unit price change is separated by a comma.
          Before the colon is the millisecond timestamp,
          and after the colon is the bandwidth unit price in sun.
    - #### getEnergyPricesOnSolidity

      ```
      @Deprecated
      public Response.PricesResponseMessage getEnergyPricesOnSolidity()
      ```

      Deprecated. Since 0.10.0, scheduled for removal in future versions.
      use [`getEnergyPrices(NodeType...)`](../../../../org/tron/trident/core/ApiWrapper.html#getEnergyPrices-org.tron.trident.core.NodeType...-) instead

      GetEnergyPricesOnSolidity
      Query historical energy unit price.

      Specified by:
      :   `getEnergyPricesOnSolidity` in interface `Api`

      Returns:
      :   prices string: All historical bandwidth unit price information.
          Each unit price change is separated by a comma.
          Before the colon is the millisecond timestamp,
          and after the colon is the bandwidth unit price in sun.
    - #### clearContractABI

      ```
      public Response.TransactionExtention clearContractABI(java.lang.String ownerAddress,
                                                            java.lang.String contractAddress)
                                                     throws IllegalException
      ```

      ClearABIContract

      Specified by:
      :   `clearContractABI` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `contractAddress` - contract address

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException`
    - #### getPaginatedExchangeList

      ```
      public Response.ExchangeList getPaginatedExchangeList(long offset,
                                                            long limit)
      ```

      get paginated exchange list

      Specified by:
      :   `getPaginatedExchangeList` in interface `Api`

      Parameters:
      :   `offset` - offset
      :   `limit` - limit

      Returns:
      :   exchange list
    - #### getPaginatedProposalList

      ```
      public Response.ProposalList getPaginatedProposalList(long offset,
                                                            long limit)
      ```

      get paginated proposal list

      Specified by:
      :   `getPaginatedProposalList` in interface `Api`

      Parameters:
      :   `offset` - offset
      :   `limit` - limit

      Returns:
      :   proposal list
    - #### getBlock

      ```
      public Response.BlockExtention getBlock(java.lang.String blockIDOrNum,
                                              boolean detail,
                                              NodeType... nodeType)
      ```

      get block of one specified block

      Specified by:
      :   `getBlock` in interface `Api`

      Parameters:
      :   `blockIDOrNum` - block Id or block num
      :   `detail` - if false, no transactions are contained.
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   BlockExtention
    - #### getBlock

      ```
      public Response.BlockExtention getBlock(boolean detail,
                                              NodeType... nodeType)
      ```

      get latest block extension

      Specified by:
      :   `getBlock` in interface `Api`

      Parameters:
      :   `detail` - specify whether to contains transaction in BlockExtention
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   BlockExtention
    - #### getBlockByIdOrNum

      ```
      public Chain.Block getBlockByIdOrNum(java.lang.String blockIDOrNum)
      ```

      GetBlockByIdOrNum

      Specified by:
      :   `getBlockByIdOrNum` in interface `Api`

      Parameters:
      :   `blockIDOrNum` - block Id with hex or block num with long

      Returns:
      :   Block
    - #### getContractInfo

      ```
      public Response.SmartContractDataWrapper getContractInfo(java.lang.String contractAddress)
      ```

      getContractInfo

      Specified by:
      :   `getContractInfo` in interface `Api`

      Parameters:
      :   `contractAddress` - contract address

      Returns:
      :   SmartContractDataWrapper
    - #### getMarketOrderByAccount

      ```
      public Response.MarketOrderList getMarketOrderByAccount(java.lang.String address,
                                                              NodeType... nodeType)
      ```

      getMarketOrderByAccount

      Specified by:
      :   `getMarketOrderByAccount` in interface `Api`

      Parameters:
      :   `address` - account address
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   MarketOrderList
    - #### getMarketOrderById

      ```
      public Response.MarketOrder getMarketOrderById(java.lang.String txn,
                                                     NodeType... nodeType)
      ```

      getMarketOrderById

      Specified by:
      :   `getMarketOrderById` in interface `Api`

      Parameters:
      :   `txn` - market transactionId
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   MarketOrder
    - #### getMarketOrderListByPair

      ```
      public Response.MarketOrderList getMarketOrderListByPair(java.lang.String sellTokenId,
                                                               java.lang.String buyTokenId,
                                                               NodeType... nodeType)
      ```

      getMarketOrderListByPair

      Specified by:
      :   `getMarketOrderListByPair` in interface `Api`

      Parameters:
      :   `sellTokenId` - market sell token id
      :   `buyTokenId` - market buy token id
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   MarketOrderList
    - #### getMarketPairList

      ```
      public Response.MarketOrderPairList getMarketPairList(NodeType... nodeType)
      ```

      getMarketPairList

      Specified by:
      :   `getMarketPairList` in interface `Api`

      Parameters:
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   MarketOrderPairList
    - #### getMarketPriceByPair

      ```
      public Response.MarketPriceList getMarketPriceByPair(java.lang.String sellTokenId,
                                                           java.lang.String buyTokenId,
                                                           NodeType... nodeType)
      ```

      getMarketPriceByPair

      Specified by:
      :   `getMarketPriceByPair` in interface `Api`

      Parameters:
      :   `sellTokenId` - market sell token id
      :   `buyTokenId` - market buy token id
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   MarketPriceList
    - #### exchangeCreate

      ```
      public Response.TransactionExtention exchangeCreate(java.lang.String ownerAddress,
                                                          java.lang.String firstToken,
                                                          long firstBalance,
                                                          java.lang.String secondToken,
                                                          long secondBalance)
                                                   throws IllegalException
      ```

      exchangeCreate

      Specified by:
      :   `exchangeCreate` in interface `Api`

      Parameters:
      :   `ownerAddress` - address
      :   `firstToken` - first token id. TRX is "\_", else token10 ID
      :   `firstBalance` - first token id balance
      :   `secondToken` - second token id. TRX is "\_", else token10 ID
      :   `secondBalance` - second token id balance

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException`
    - #### exchangeInject

      ```
      public Response.TransactionExtention exchangeInject(java.lang.String ownerAddress,
                                                          long exchangeId,
                                                          java.lang.String tokenId,
                                                          long amount)
                                                   throws IllegalException
      ```

      exchangeInject

      Specified by:
      :   `exchangeInject` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner
      :   `exchangeId` - exchange id
      :   `tokenId` - token id
      :   `amount` - inject the amount of tokenId to exchangeId

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException`
    - #### exchangeTransaction

      ```
      public Response.TransactionExtention exchangeTransaction(java.lang.String ownerAddress,
                                                               long exchangeId,
                                                               java.lang.String tokenId,
                                                               long amount,
                                                               long expected)
                                                        throws IllegalException
      ```

      create exchangeTransaction. alias is bancor transaction.

      Specified by:
      :   `exchangeTransaction` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner
      :   `exchangeId` - exchange id
      :   `tokenId` - sell token id
      :   `amount` - inject the amount of tokenId to exchangeId
      :   `expected` - amount of buyTokenId

      Returns:
      :   TransactionExtention

      Throws:
      :   `IllegalException`
    - #### exchangeWithdraw

      ```
      public Response.TransactionExtention exchangeWithdraw(java.lang.String ownerAddress,
                                                            long exchangeId,
                                                            java.lang.String tokenId,
                                                            long quant)
                                                     throws IllegalException
      ```

      create ExchangeWithdrawContract with parameters

      Specified by:
      :   `exchangeWithdraw` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `exchangeId` - exchangeId
      :   `tokenId` - tokenId
      :   `quant` - quant

      Returns:
      :   ExchangeWithdrawContract

      Throws:
      :   `IllegalException`
    - #### getTransactionCountByBlockNum

      ```
      public long getTransactionCountByBlockNum(long blockNum,
                                                NodeType... nodeType)
      ```

      getTransactionCountByBlockNum

      Specified by:
      :   `getTransactionCountByBlockNum` in interface `Api`

      Parameters:
      :   `blockNum` - block num
      :   `nodeType` - Optional parameter to specify which node to query.
          If not provided, uses full node default.
          If NodeType.SOLIDITY\_NODE, uses solidity node.

      Returns:
      :   the transaction count in block
    - #### marketCancelOrder

      ```
      public Response.TransactionExtention marketCancelOrder(java.lang.String ownerAddress,
                                                             java.lang.String orderId)
                                                      throws IllegalException
      ```

      crete MarketCancelOrderContract with parameters

      Specified by:
      :   `marketCancelOrder` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `orderId` - existing order Id

      Returns:
      :   MarketCancelOrderContract

      Throws:
      :   `IllegalException`
    - #### marketSellAsset

      ```
      public Response.TransactionExtention marketSellAsset(java.lang.String ownerAddress,
                                                           java.lang.String sellTokenId,
                                                           long sellTokenQuantity,
                                                           java.lang.String buyTokenId,
                                                           long buyTokenQuantity)
                                                    throws IllegalException
      ```

      create MarketSellAssetContract with parameters

      Specified by:
      :   `marketSellAsset` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `sellTokenId` - sell token Id, "\_" or all digit with 0~9
      :   `sellTokenQuantity` - sell token quantity
      :   `buyTokenId` - buy token Id, "\_" or all digit with 0~9
      :   `buyTokenQuantity` - buy token quantity

      Returns:
      :   MarketSellAssetContract

      Throws:
      :   `IllegalException`
    - #### updateEnergyLimit

      ```
      public Response.TransactionExtention updateEnergyLimit(java.lang.String ownerAddress,
                                                             java.lang.String contractAddress,
                                                             long originEnergyLimit)
                                                      throws IllegalException
      ```

      create UpdateEnergyLimitContract with parameters

      Specified by:
      :   `updateEnergyLimit` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `contractAddress` - contract address
      :   `originEnergyLimit` - origin energy limit, must gt 0

      Returns:
      :   UpdateEnergyLimitContract

      Throws:
      :   `IllegalException` - if originEnergyLimit is invalid
    - #### updateSetting

      ```
      public Response.TransactionExtention updateSetting(java.lang.String ownerAddress,
                                                         java.lang.String contractAddress,
                                                         long consumeUserResourcePercent)
                                                  throws IllegalException
      ```

      create UpdateSettingContract with parameters

      Specified by:
      :   `updateSetting` in interface `Api`

      Parameters:
      :   `ownerAddress` - owner address
      :   `contractAddress` - contract address
      :   `consumeUserResourcePercent` - consume user resource percent if user trigger this contract, must be [0,100]

      Returns:
      :   UpdateSettingContract

      Throws:
      :   `IllegalException` - if consumeUserResourcePercent is invalid
    - #### createSmartContract

      ```
      public Contract.CreateSmartContract createSmartContract(java.lang.String contractName,
                                                              java.lang.String address,
                                                              java.lang.String ABI,
                                                              java.lang.String code,
                                                              long callValue,
                                                              long consumeUserResourcePercent,
                                                              long originEnergyLimit,
                                                              long tokenValue,
                                                              java.lang.String tokenId)
                                                       throws java.lang.Exception
      ```

      Specified by:
      :   `createSmartContract` in interface `Api`

      Parameters:
      :   `contractName` - contractName
      :   `address` - ownerAddress
      :   `ABI` - abiString
      :   `code` - bytecode
      :   `callValue` - the amount of deposit TRX(unit sun), default is 0
      :   `consumeUserResourcePercent` - consumeUserResourcePercent,range 0-100
      :   `originEnergyLimit` - originEnergyLimit
      :   `tokenValue` - the amount of deposit token 10, default is 0
      :   `tokenId` - the ID of token 10

      Returns:
      :   CreateSmartContract

      Throws:
      :   `java.lang.Exception` - exception
    - #### createSmartContract

      ```
      public Contract.CreateSmartContract createSmartContract(java.lang.String contractName,
                                                              java.lang.String address,
                                                              java.lang.String ABI,
                                                              java.lang.String code,
                                                              long callValue,
                                                              long consumeUserResourcePercent,
                                                              long originEnergyLimit,
                                                              long tokenValue,
                                                              java.lang.String tokenId,
                                                              java.lang.String libraryAddressPair,
                                                              java.lang.String compilerVersion)
                                                       throws java.lang.Exception
      ```

      Specified by:
      :   `createSmartContract` in interface `Api`

      Parameters:
      :   `contractName` - contractName
      :   `address` - ownerAddress
      :   `ABI` - abiString
      :   `code` - bytecode
      :   `callValue` - the amount of deposit TRX(unit sun), default is 0
      :   `consumeUserResourcePercent` - consumeUserResourcePercent,range 0-100
      :   `originEnergyLimit` - originEnergyLimit
      :   `tokenValue` - the amount of deposit token 10, default is 0
      :   `tokenId` - the ID of token 10
      :   `libraryAddressPair` - walletCli compatible
      :   `compilerVersion` - walletCli compatible

      Returns:
      :   CreateSmartContract

      Throws:
      :   `java.lang.Exception` - exception
    - #### deployContract

      ```
      public Response.TransactionExtention deployContract(java.lang.String contractName,
                                                          java.lang.String abiStr,
                                                          java.lang.String bytecode,
                                                          java.util.List<Type<?>> constructorParams,
                                                          long feeLimit,
                                                          long consumeUserResourcePercent,
                                                          long originEnergyLimit,
                                                          long callValue,
                                                          java.lang.String tokenId,
                                                          long tokenValue)
                                                   throws java.lang.Exception
      ```

      Deploy a smart contract - no broadcasting

      Specified by:
      :   `deployContract` in interface `Api`

      Parameters:
      :   `contractName` - contract name
      :   `abiStr` - abi
      :   `bytecode` - bytecode
      :   `constructorParams` - constructorParams, no Params set null or empty list
      :   `feeLimit` - feeLimit
      :   `consumeUserResourcePercent` - consumeUserResourcePercent,range 0-100
      :   `originEnergyLimit` - originEnergyLimit
      :   `callValue` - TRX value
      :   `tokenValue` - token value of token10
      :   `tokenId` - token10 ID, no use set null or ""

      Returns:
      :   TransactionExtention

      Throws:
      :   `java.lang.Exception` - exception if fail