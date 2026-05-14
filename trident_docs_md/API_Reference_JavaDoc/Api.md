

org.tron.trident.core

## Interface Api

* All Known Implementing Classes:
  :   [ApiWrapper](../../../../org/tron/trident/core/ApiWrapper.html "class in org.tron.trident.core")

  ---

    

  ```
  public interface Api
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionExtention` | `accountPermissionUpdate(Contract.AccountPermissionUpdateContract contract)` |
    | `Response.TransactionExtention` | `accountPermissionUpdate(java.lang.String ownerAddress, AccountPermissions accountPermissions)` |
    | `Response.TransactionExtention` | `approveProposal(java.lang.String ownerAddress, long proposalId, boolean isAddApproval)` |
    | `Contract.AssetIssueContract.Builder` | `assetIssueContractBuilder(java.lang.String ownerAddress, java.lang.String name, java.lang.String abbr, long totalSupply, int trxNum, int icoNum, long startTime, long endTime, java.lang.String url, long freeAssetNetLimit, long publicFreeAssetNetLimit, int precision, java.lang.String description)` |
    | `java.lang.String` | `broadcastTransaction(Chain.Transaction txn)` |
    | `Response.TransactionExtention` | `cancelAllUnfreezeV2(java.lang.String ownerAddress)` |
    | `Response.TransactionExtention` | `clearContractABI(java.lang.String ownerAddress, java.lang.String contractAddress)` |
    | `Response.TransactionExtention` | `constantCall(java.lang.String ownerAddress, java.lang.String contractAddress, Function function)` Deprecated. |
    | `Response.TransactionExtention` | `constantCallV2(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData)` Deprecated. |
    | `Response.TransactionExtention` | `createAccount(java.lang.String ownerAddress, java.lang.String accountAddress)` |
    | `Response.TransactionExtention` | `createAssetIssue(java.lang.String ownerAddress, java.lang.String name, java.lang.String abbr, long totalSupply, int trxNum, int icoNum, long startTime, long endTime, java.lang.String url, long freeAssetNetLimit, long publicFreeAssetNetLimit, int precision, java.util.HashMap<java.lang.String,java.lang.String> frozenSupply, java.lang.String description)` |
    | `Response.TransactionExtention` | `createAssetIssue(java.lang.String ownerAddress, java.lang.String name, java.lang.String abbr, long totalSupply, int trxNum, int icoNum, long startTime, long endTime, java.lang.String url, long freeAssetNetLimit, long publicFreeAssetNetLimit, int precision, java.lang.String description)` |
    | `Contract.CreateSmartContract` | `createSmartContract(java.lang.String contractName, java.lang.String address, java.lang.String ABI, java.lang.String code, long callValue, long consumeUserResourcePercent, long originEnergyLimit, long tokenValue, java.lang.String tokenId)` |
    | `Contract.CreateSmartContract` | `createSmartContract(java.lang.String contractName, java.lang.String address, java.lang.String ABI, java.lang.String code, long callValue, long consumeUserResourcePercent, long originEnergyLimit, long tokenValue, java.lang.String tokenId, java.lang.String libraryAddressPair, java.lang.String compilerVersion)` |
    | `Response.TransactionExtention` | `createTransactionExtention(com.google.protobuf.Message request, Chain.Transaction.Contract.ContractType contractType)` |
    | `Response.TransactionExtention` | `createWitness(java.lang.String ownerAddress, java.lang.String url)` |
    | `Response.TransactionExtention` | `delegateResource(java.lang.String ownerAddress, long balance, int resourceCode, java.lang.String receiverAddress, boolean lock)` |
    | `Response.TransactionExtention` | `delegateResourceV2(java.lang.String ownerAddress, long balance, int resourceCode, java.lang.String receiverAddress, boolean lock, long lockPeriod)` |
    | `Response.TransactionExtention` | `deleteProposal(java.lang.String ownerAddress, long proposalId)` |
    | `Response.TransactionExtention` | `deployContract(java.lang.String contractName, java.lang.String abiStr, java.lang.String bytecode, java.util.List<Type<?>> constructorParams, long feeLimit, long consumeUserResourcePercent, long originEnergyLimit, long callValue, java.lang.String tokenId, long tokenValue)` |
    | `long` | `estimateBandwidth(Chain.Transaction txn)` |
    | `Response.EstimateEnergyMessage` | `estimateEnergy(java.lang.String ownerAddress, java.lang.String contractAddress, Function function, NodeType... nodeType)` |
    | `Response.EstimateEnergyMessage` | `estimateEnergy(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData, long callValue, long tokenValue, java.lang.String tokenId, NodeType... nodeType)` |
    | `Response.EstimateEnergyMessage` | `estimateEnergyV2(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData)` Deprecated. |
    | `Response.TransactionExtention` | `exchangeCreate(java.lang.String ownerAddress, java.lang.String firstToken, long firstBalance, java.lang.String secondToken, long secondBalance)` |
    | `Response.TransactionExtention` | `exchangeInject(java.lang.String ownerAddress, long exchangeId, java.lang.String tokenId, long amount)` |
    | `Response.TransactionExtention` | `exchangeTransaction(java.lang.String ownerAddress, long exchangeId, java.lang.String tokenId, long amount, long expected)` |
    | `Response.TransactionExtention` | `exchangeWithdraw(java.lang.String ownerAddress, long exchangeId, java.lang.String tokenId, long quant)` |
    | `Response.TransactionExtention` | `freezeBalance(java.lang.String ownerAddress, long frozenBalance, int frozenDuration, int resourceCode)` |
    | `Response.TransactionExtention` | `freezeBalance(java.lang.String ownerAddress, long frozenBalance, int frozenDuration, int resourceCode, java.lang.String receiveAddress)` |
    | `Response.TransactionExtention` | `freezeBalanceV2(java.lang.String ownerAddress, long frozenBalance, int resourceCode)` |
    | `Response.Account` | `getAccount(java.lang.String address, NodeType... nodeType)` |
    | `long` | `getAccountBalance(java.lang.String address)` |
    | `Response.Account` | `getAccountById(java.lang.String id, NodeType... nodeType)` |
    | `Response.AccountNetMessage` | `getAccountNet(java.lang.String address)` |
    | `AccountPermissions` | `getAccountPermissions(java.lang.String address, NodeType... nodeType)` |
    | `Response.AccountResourceMessage` | `getAccountResource(java.lang.String address)` |
    | `Response.Account` | `getAccountSolidity(java.lang.String address)` Deprecated. |
    | `Response.AssetIssueList` | `getAssetIssueByAccount(java.lang.String address)` |
    | `Contract.AssetIssueContract` | `getAssetIssueById(java.lang.String assetId, NodeType... nodeType)` |
    | `Contract.AssetIssueContract` | `getAssetIssueByName(java.lang.String name, NodeType... nodeType)` |
    | `Response.AssetIssueList` | `getAssetIssueList(NodeType... nodeType)` |
    | `Response.AssetIssueList` | `getAssetIssueListByName(java.lang.String name, NodeType... nodeType)` |
    | `long` | `getAvailableUnfreezeCount(java.lang.String ownerAddress, NodeType... nodeType)` |
    | `Response.PricesResponseMessage` | `getBandwidthPrices(NodeType... nodeType)` |
    | `Response.PricesResponseMessage` | `getBandwidthPricesOnSolidity()` Deprecated. |
    | `Response.BlockExtention` | `getBlock(boolean detail, NodeType... nodeType)` |
    | `Response.BlockExtention` | `getBlock(java.lang.String blockIDOrNum, boolean detail, NodeType... nodeType)` |
    | `Response.BlockBalanceTrace` | `getBlockBalance(java.lang.String blockId, long blockNum)` |
    | `Chain.Block` | `getBlockById(java.lang.String blockID)` |
    | `Chain.Block` | `getBlockByIdOrNum(java.lang.String blockIDOrNum)` |
    | `Response.BlockListExtention` | `getBlockByLatestNum(long num)` |
    | `Response.BlockListExtention` | `getBlockByLimitNext(long startNum, long endNum)` |
    | `Response.BlockExtention` | `getBlockByNum(long blockNum, NodeType... nodeType)` |
    | `long` | `getBrokerageInfo(java.lang.String address, NodeType... nodeType)` |
    | `long` | `getBurnTRX(NodeType... nodeType)` |
    | `long` | `getCanDelegatedMaxSize(java.lang.String ownerAddress, int type, NodeType... nodeType)` |
    | `long` | `getCanWithdrawUnfreezeAmount(java.lang.String ownerAddress, long timestamp, NodeType... nodeType)` |
    | `long` | `getCanWithdrawUnfreezeAmount(java.lang.String ownerAddress, NodeType... nodeType)` |
    | `Response.ChainParameters` | `getChainParameters()` |
    | `Contract` | `getContract(java.lang.String contractAddress)` |
    | `Response.SmartContractDataWrapper` | `getContractInfo(java.lang.String contractAddr)` |
    | `Response.DelegatedResourceList` | `getDelegatedResource(java.lang.String fromAddress, java.lang.String toAddress, NodeType... nodeType)` |
    | `Response.DelegatedResourceAccountIndex` | `getDelegatedResourceAccountIndex(java.lang.String address, NodeType... nodeType)` |
    | `Response.DelegatedResourceAccountIndex` | `getDelegatedResourceAccountIndexV2(java.lang.String address, NodeType... nodeType)` |
    | `Response.DelegatedResourceList` | `getDelegatedResourceV2(java.lang.String fromAddress, java.lang.String toAddress, NodeType... nodeType)` |
    | `Response.PricesResponseMessage` | `getEnergyPrices(NodeType... nodeType)` |
    | `Response.PricesResponseMessage` | `getEnergyPricesOnSolidity()` Deprecated. |
    | `Response.Exchange` | `getExchangeById(java.lang.String id, NodeType... nodeType)` |
    | `Response.MarketOrderList` | `getMarketOrderByAccount(java.lang.String account, NodeType... nodeType)` |
    | `Response.MarketOrder` | `getMarketOrderById(java.lang.String txn, NodeType... nodeType)` |
    | `Response.MarketOrderList` | `getMarketOrderListByPair(java.lang.String sellTokenId, java.lang.String buyTokenId, NodeType... nodeType)` |
    | `Response.MarketOrderPairList` | `getMarketPairList(NodeType... nodeType)` |
    | `Response.MarketPriceList` | `getMarketPriceByPair(java.lang.String sellTokenId, java.lang.String buyTokenId, NodeType... nodeType)` |
    | `Response.PricesResponseMessage` | `getMemoFee()` |
    | `long` | `getNextMaintenanceTime()` |
    | `Response.NodeInfo` | `getNodeInfo()` |
    | `Chain.Block` | `getNowBlock(NodeType... nodeType)` |
    | `Response.BlockExtention` | `getNowBlock2(NodeType... nodeType)` |
    | `Response.BlockExtention` | `getNowBlockSolidity()` Deprecated. |
    | `Response.AssetIssueList` | `getPaginatedAssetIssueList(long offset, long limit, NodeType... nodeType)` |
    | `Response.ExchangeList` | `getPaginatedExchangeList(long offset, long limit)` |
    | `Response.WitnessList` | `getPaginatedNowWitnessList(long offset, long limit, NodeType... nodeType)` |
    | `Response.ProposalList` | `getPaginatedProposalList(long offset, long limit)` |
    | `long` | `getPendingSize()` |
    | `Response.Proposal` | `getProposalById(java.lang.String id)` |
    | `GrpcAPI.NumberMessage` | `getRewardInfo(java.lang.String address, NodeType... nodeType)` |
    | `GrpcAPI.NumberMessage` | `getRewardSolidity(java.lang.String address)` Deprecated. |
    | `Common.SmartContract` | `getSmartContract(java.lang.String contractAddress)` |
    | `Response.TransactionApprovedList` | `getTransactionApprovedList(Chain.Transaction trx)` |
    | `Chain.Transaction` | `getTransactionById(java.lang.String txID, NodeType... nodeType)` |
    | `Chain.Transaction` | `getTransactionByIdSolidity(java.lang.String txID)` Deprecated. |
    | `long` | `getTransactionCountByBlockNum(long blockNum, NodeType... nodeType)` |
    | `Chain.Transaction` | `getTransactionFromPending(java.lang.String txId)` |
    | `Response.TransactionInfoList` | `getTransactionInfoByBlockNum(long blockNum, NodeType... nodeType)` |
    | `Response.TransactionInfoList` | `getTransactionInfoByBlockNumSolidity(long blockNum)` Deprecated. |
    | `Response.TransactionInfo` | `getTransactionInfoById(java.lang.String txID, NodeType... nodeType)` |
    | `GrpcAPI.TransactionIdList` | `getTransactionListFromPending()` |
    | `Response.TransactionSignWeight` | `getTransactionSignWeight(Chain.Transaction trx)` |
    | `Response.ExchangeList` | `listExchanges(NodeType... nodeType)` |
    | `Response.NodeList` | `listNodes()` |
    | `Response.ProposalList` | `listProposals()` |
    | `Response.WitnessList` | `listWitnesses(NodeType... nodeType)` |
    | `Response.TransactionExtention` | `marketCancelOrder(java.lang.String ownerAddress, java.lang.String orderId)` |
    | `Response.TransactionExtention` | `marketSellAsset(java.lang.String ownerAddress, java.lang.String sellTokenId, long sellTokenQuantity, java.lang.String buyTokenId, long buyTokenQuantity)` |
    | `Response.TransactionExtention` | `participateAssetIssue(java.lang.String toAddress, java.lang.String ownerAddress, java.lang.String assertName, long amount)` |
    | `Response.TransactionExtention` | `proposalCreate(java.lang.String ownerAddress, java.util.Map<java.lang.Long,java.lang.Long> parameters)` |
    | `Chain.Transaction` | `setAccountId(java.lang.String id, java.lang.String address)` |
    | `Response.TransactionExtention` | `setAccountId2(java.lang.String id, java.lang.String address)` |
    | `Chain.Transaction` | `signTransaction(Chain.Transaction txn)` |
    | `Chain.Transaction` | `signTransaction(Chain.Transaction txn, KeyPair keyPair)` |
    | `Chain.Transaction` | `signTransaction(Response.TransactionExtention txnExt)` |
    | `Chain.Transaction` | `signTransaction(Response.TransactionExtention txnExt, KeyPair keyPair)` |
    | `Response.TransactionExtention` | `transfer(java.lang.String fromAddress, java.lang.String toAddress, long amount)` |
    | `Response.TransactionExtention` | `transferTrc10(java.lang.String fromAddress, java.lang.String toAddress, int tokenId, long amount)` |
    | `TransactionBuilder` | `triggerCall(java.lang.String ownerAddress, java.lang.String contractAddress, Function function)` Deprecated. |
    | `TransactionBuilder` | `triggerCallV2(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData)` Deprecated. |
    | `Response.TransactionExtention` | `triggerConstantContract(java.lang.String ownerAddress, java.lang.String contractAddress, Function function, NodeType... nodeType)` |
    | `Response.TransactionExtention` | `triggerConstantContract(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData, long callValue, long tokenValue, java.lang.String tokenId, NodeType... nodeType)` |
    | `Response.TransactionExtention` | `triggerConstantContract(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData, NodeType... nodeType)` |
    | `Response.TransactionExtention` | `triggerContract(java.lang.String ownerAddress, java.lang.String contractAddress, java.lang.String callData, long callValue, long tokenValue, java.lang.String tokenId, long feeLimit)` |
    | `Response.TransactionExtention` | `undelegateResource(java.lang.String ownerAddress, long balance, int resourceCode, java.lang.String receiverAddress)` |
    | `Response.TransactionExtention` | `unfreezeAsset(java.lang.String ownerAddress)` |
    | `Response.TransactionExtention` | `unfreezeBalance(java.lang.String ownerAddress, int resourceCode)` |
    | `Response.TransactionExtention` | `unfreezeBalance(java.lang.String ownerAddress, int resourceCode, java.lang.String receiveAddress)` |
    | `Response.TransactionExtention` | `unfreezeBalanceV2(java.lang.String ownerAddress, long unfreezeBalance, int resourceCode)` |
    | `Response.TransactionExtention` | `updateAccount(java.lang.String address, java.lang.String accountName)` |
    | `Response.TransactionExtention` | `updateAsset(java.lang.String ownerAddress, java.lang.String description, java.lang.String url, long newLimit, long newPublicLimit)` |
    | `Response.TransactionExtention` | `updateBrokerage(java.lang.String address, int brokerage)` |
    | `Response.TransactionExtention` | `updateEnergyLimit(java.lang.String ownerAddress, java.lang.String contractAddress, long originEnergyLimit)` |
    | `Response.TransactionExtention` | `updateSetting(java.lang.String ownerAddress, java.lang.String contractAddress, long consumeUserResourcePercent)` |
    | `Response.TransactionExtention` | `updateWitness(java.lang.String ownerAddress, java.lang.String updateUrl)` |
    | `Response.TransactionExtention` | `voteWitness(java.lang.String ownerAddress, java.util.HashMap<java.lang.String,java.lang.String> votes)` |
    | `Response.TransactionExtention` | `withdrawBalance(java.lang.String ownerAddress)` |
    | `Response.TransactionExtention` | `withdrawExpireUnfreeze(java.lang.String ownerAddress)` |

* + ### Method Detail

    - #### signTransaction

      ```
      Chain.Transaction signTransaction(Response.TransactionExtention txnExt,
                                        KeyPair keyPair)
      ```
    - #### signTransaction

      ```
      Chain.Transaction signTransaction(Chain.Transaction txn,
                                        KeyPair keyPair)
      ```
    - #### signTransaction

      ```
      Chain.Transaction signTransaction(Response.TransactionExtention txnExt)
      ```
    - #### signTransaction

      ```
      Chain.Transaction signTransaction(Chain.Transaction txn)
      ```
    - #### createTransactionExtention

      ```
      Response.TransactionExtention createTransactionExtention(com.google.protobuf.Message request,
                                                               Chain.Transaction.Contract.ContractType contractType)
                                                        throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### estimateBandwidth

      ```
      long estimateBandwidth(Chain.Transaction txn)
      ```
    - #### broadcastTransaction

      ```
      java.lang.String broadcastTransaction(Chain.Transaction txn)
                                     throws java.lang.RuntimeException
      ```

      Throws:
      :   `java.lang.RuntimeException`
    - #### transfer

      ```
      Response.TransactionExtention transfer(java.lang.String fromAddress,
                                             java.lang.String toAddress,
                                             long amount)
                                      throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### transferTrc10

      ```
      Response.TransactionExtention transferTrc10(java.lang.String fromAddress,
                                                  java.lang.String toAddress,
                                                  int tokenId,
                                                  long amount)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### freezeBalance

      ```
      Response.TransactionExtention freezeBalance(java.lang.String ownerAddress,
                                                  long frozenBalance,
                                                  int frozenDuration,
                                                  int resourceCode)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### freezeBalance

      ```
      Response.TransactionExtention freezeBalance(java.lang.String ownerAddress,
                                                  long frozenBalance,
                                                  int frozenDuration,
                                                  int resourceCode,
                                                  java.lang.String receiveAddress)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### freezeBalanceV2

      ```
      Response.TransactionExtention freezeBalanceV2(java.lang.String ownerAddress,
                                                    long frozenBalance,
                                                    int resourceCode)
                                             throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### unfreezeBalance

      ```
      Response.TransactionExtention unfreezeBalance(java.lang.String ownerAddress,
                                                    int resourceCode)
                                             throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### unfreezeBalance

      ```
      Response.TransactionExtention unfreezeBalance(java.lang.String ownerAddress,
                                                    int resourceCode,
                                                    java.lang.String receiveAddress)
                                             throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### unfreezeBalanceV2

      ```
      Response.TransactionExtention unfreezeBalanceV2(java.lang.String ownerAddress,
                                                      long unfreezeBalance,
                                                      int resourceCode)
                                               throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### cancelAllUnfreezeV2

      ```
      Response.TransactionExtention cancelAllUnfreezeV2(java.lang.String ownerAddress)
                                                 throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### delegateResource

      ```
      Response.TransactionExtention delegateResource(java.lang.String ownerAddress,
                                                     long balance,
                                                     int resourceCode,
                                                     java.lang.String receiverAddress,
                                                     boolean lock)
                                              throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### delegateResourceV2

      ```
      Response.TransactionExtention delegateResourceV2(java.lang.String ownerAddress,
                                                       long balance,
                                                       int resourceCode,
                                                       java.lang.String receiverAddress,
                                                       boolean lock,
                                                       long lockPeriod)
                                                throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### undelegateResource

      ```
      Response.TransactionExtention undelegateResource(java.lang.String ownerAddress,
                                                       long balance,
                                                       int resourceCode,
                                                       java.lang.String receiverAddress)
                                                throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### withdrawExpireUnfreeze

      ```
      Response.TransactionExtention withdrawExpireUnfreeze(java.lang.String ownerAddress)
                                                    throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getAvailableUnfreezeCount

      ```
      long getAvailableUnfreezeCount(java.lang.String ownerAddress,
                                     NodeType... nodeType)
      ```
    - #### getCanWithdrawUnfreezeAmount

      ```
      long getCanWithdrawUnfreezeAmount(java.lang.String ownerAddress,
                                        NodeType... nodeType)
      ```
    - #### getCanWithdrawUnfreezeAmount

      ```
      long getCanWithdrawUnfreezeAmount(java.lang.String ownerAddress,
                                        long timestamp,
                                        NodeType... nodeType)
      ```
    - #### getCanDelegatedMaxSize

      ```
      long getCanDelegatedMaxSize(java.lang.String ownerAddress,
                                  int type,
                                  NodeType... nodeType)
      ```
    - #### getDelegatedResourceV2

      ```
      Response.DelegatedResourceList getDelegatedResourceV2(java.lang.String fromAddress,
                                                            java.lang.String toAddress,
                                                            NodeType... nodeType)
      ```
    - #### getDelegatedResourceAccountIndexV2

      ```
      Response.DelegatedResourceAccountIndex getDelegatedResourceAccountIndexV2(java.lang.String address,
                                                                                NodeType... nodeType)
                                                                         throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### voteWitness

      ```
      Response.TransactionExtention voteWitness(java.lang.String ownerAddress,
                                                java.util.HashMap<java.lang.String,java.lang.String> votes)
                                         throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### createAccount

      ```
      Response.TransactionExtention createAccount(java.lang.String ownerAddress,
                                                  java.lang.String accountAddress)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### updateAccount

      ```
      Response.TransactionExtention updateAccount(java.lang.String address,
                                                  java.lang.String accountName)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getNowBlock

      ```
      Chain.Block getNowBlock(NodeType... nodeType)
                       throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getNowBlock2

      ```
      Response.BlockExtention getNowBlock2(NodeType... nodeType)
                                    throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getBlockByNum

      ```
      Response.BlockExtention getBlockByNum(long blockNum,
                                            NodeType... nodeType)
                                     throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getBlockByLatestNum

      ```
      Response.BlockListExtention getBlockByLatestNum(long num)
                                               throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getBlockByLimitNext

      ```
      Response.BlockListExtention getBlockByLimitNext(long startNum,
                                                      long endNum)
                                               throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getNodeInfo

      ```
      Response.NodeInfo getNodeInfo()
                             throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### listNodes

      ```
      Response.NodeList listNodes()
                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getTransactionInfoByBlockNum

      ```
      Response.TransactionInfoList getTransactionInfoByBlockNum(long blockNum,
                                                                NodeType... nodeType)
                                                         throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getTransactionInfoById

      ```
      Response.TransactionInfo getTransactionInfoById(java.lang.String txID,
                                                      NodeType... nodeType)
                                               throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getTransactionById

      ```
      Chain.Transaction getTransactionById(java.lang.String txID,
                                           NodeType... nodeType)
                                    throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getAccount

      ```
      Response.Account getAccount(java.lang.String address,
                                  NodeType... nodeType)
      ```
    - #### getAccountResource

      ```
      Response.AccountResourceMessage getAccountResource(java.lang.String address)
      ```
    - #### getAccountNet

      ```
      Response.AccountNetMessage getAccountNet(java.lang.String address)
      ```
    - #### getAccountBalance

      ```
      long getAccountBalance(java.lang.String address)
      ```
    - #### getAccountById

      ```
      Response.Account getAccountById(java.lang.String id,
                                      NodeType... nodeType)
      ```
    - #### setAccountId

      ```
      Chain.Transaction setAccountId(java.lang.String id,
                                     java.lang.String address)
                              throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### setAccountId2

      ```
      Response.TransactionExtention setAccountId2(java.lang.String id,
                                                  java.lang.String address)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getChainParameters

      ```
      Response.ChainParameters getChainParameters()
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getDelegatedResource

      ```
      Response.DelegatedResourceList getDelegatedResource(java.lang.String fromAddress,
                                                          java.lang.String toAddress,
                                                          NodeType... nodeType)
      ```
    - #### getDelegatedResourceAccountIndex

      ```
      Response.DelegatedResourceAccountIndex getDelegatedResourceAccountIndex(java.lang.String address,
                                                                              NodeType... nodeType)
      ```
    - #### getAssetIssueList

      ```
      Response.AssetIssueList getAssetIssueList(NodeType... nodeType)
      ```
    - #### getPaginatedAssetIssueList

      ```
      Response.AssetIssueList getPaginatedAssetIssueList(long offset,
                                                         long limit,
                                                         NodeType... nodeType)
      ```
    - #### getAssetIssueByAccount

      ```
      Response.AssetIssueList getAssetIssueByAccount(java.lang.String address)
      ```
    - #### getAssetIssueById

      ```
      Contract.AssetIssueContract getAssetIssueById(java.lang.String assetId,
                                                    NodeType... nodeType)
      ```
    - #### getAssetIssueByName

      ```
      Contract.AssetIssueContract getAssetIssueByName(java.lang.String name,
                                                      NodeType... nodeType)
      ```
    - #### getAssetIssueListByName

      ```
      Response.AssetIssueList getAssetIssueListByName(java.lang.String name,
                                                      NodeType... nodeType)
      ```
    - #### participateAssetIssue

      ```
      Response.TransactionExtention participateAssetIssue(java.lang.String toAddress,
                                                          java.lang.String ownerAddress,
                                                          java.lang.String assertName,
                                                          long amount)
                                                   throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### listProposals

      ```
      Response.ProposalList listProposals()
      ```
    - #### getProposalById

      ```
      Response.Proposal getProposalById(java.lang.String id)
      ```
    - #### listWitnesses

      ```
      Response.WitnessList listWitnesses(NodeType... nodeType)
      ```
    - #### getPaginatedNowWitnessList

      ```
      Response.WitnessList getPaginatedNowWitnessList(long offset,
                                                      long limit,
                                                      NodeType... nodeType)
      ```
    - #### listExchanges

      ```
      Response.ExchangeList listExchanges(NodeType... nodeType)
      ```
    - #### getExchangeById

      ```
      Response.Exchange getExchangeById(java.lang.String id,
                                        NodeType... nodeType)
                                 throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### createAssetIssue

      ```
      Response.TransactionExtention createAssetIssue(java.lang.String ownerAddress,
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

      Throws:
      :   `IllegalException`
    - #### createAssetIssue

      ```
      Response.TransactionExtention createAssetIssue(java.lang.String ownerAddress,
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

      Throws:
      :   `IllegalException`
    - #### assetIssueContractBuilder

      ```
      Contract.AssetIssueContract.Builder assetIssueContractBuilder(java.lang.String ownerAddress,
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
    - #### updateAsset

      ```
      Response.TransactionExtention updateAsset(java.lang.String ownerAddress,
                                                java.lang.String description,
                                                java.lang.String url,
                                                long newLimit,
                                                long newPublicLimit)
                                         throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### unfreezeAsset

      ```
      Response.TransactionExtention unfreezeAsset(java.lang.String ownerAddress)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### accountPermissionUpdate

      ```
      Response.TransactionExtention accountPermissionUpdate(Contract.AccountPermissionUpdateContract contract)
                                                     throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### accountPermissionUpdate

      ```
      Response.TransactionExtention accountPermissionUpdate(java.lang.String ownerAddress,
                                                            AccountPermissions accountPermissions)
                                                     throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getAccountPermissions

      ```
      AccountPermissions getAccountPermissions(java.lang.String address,
                                               NodeType... nodeType)
                                        throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getTransactionSignWeight

      ```
      Response.TransactionSignWeight getTransactionSignWeight(Chain.Transaction trx)
      ```
    - #### getTransactionApprovedList

      ```
      Response.TransactionApprovedList getTransactionApprovedList(Chain.Transaction trx)
      ```
    - #### getAccountSolidity

      ```
      @Deprecated
      Response.Account getAccountSolidity(java.lang.String address)
      ```

      Deprecated.
    - #### getTransactionInfoByBlockNumSolidity

      ```
      @Deprecated
      Response.TransactionInfoList getTransactionInfoByBlockNumSolidity(long blockNum)
                                                                             throws IllegalException
      ```

      Deprecated.

      Throws:
      :   `IllegalException`
    - #### getNowBlockSolidity

      ```
      @Deprecated
      Response.BlockExtention getNowBlockSolidity()
                                                       throws IllegalException
      ```

      Deprecated.

      Throws:
      :   `IllegalException`
    - #### getTransactionByIdSolidity

      ```
      @Deprecated
      Chain.Transaction getTransactionByIdSolidity(java.lang.String txID)
                                                        throws IllegalException
      ```

      Deprecated.

      Throws:
      :   `IllegalException`
    - #### getRewardSolidity

      ```
      @Deprecated
      GrpcAPI.NumberMessage getRewardSolidity(java.lang.String address)
      ```

      Deprecated.
    - #### getRewardInfo

      ```
      GrpcAPI.NumberMessage getRewardInfo(java.lang.String address,
                                          NodeType... nodeType)
      ```
    - #### updateBrokerage

      ```
      Response.TransactionExtention updateBrokerage(java.lang.String address,
                                                    int brokerage)
                                             throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getBrokerageInfo

      ```
      long getBrokerageInfo(java.lang.String address,
                            NodeType... nodeType)
      ```
    - #### getContract

      ```
      Contract getContract(java.lang.String contractAddress)
      ```
    - #### getSmartContract

      ```
      Common.SmartContract getSmartContract(java.lang.String contractAddress)
      ```
    - #### constantCall

      ```
      @Deprecated
      Response.TransactionExtention constantCall(java.lang.String ownerAddress,
                                                             java.lang.String contractAddress,
                                                             Function function)
      ```

      Deprecated.
    - #### triggerCall

      ```
      @Deprecated
      TransactionBuilder triggerCall(java.lang.String ownerAddress,
                                                 java.lang.String contractAddress,
                                                 Function function)
      ```

      Deprecated.
    - #### triggerContract

      ```
      Response.TransactionExtention triggerContract(java.lang.String ownerAddress,
                                                    java.lang.String contractAddress,
                                                    java.lang.String callData,
                                                    long callValue,
                                                    long tokenValue,
                                                    java.lang.String tokenId,
                                                    long feeLimit)
                                             throws java.lang.Exception
      ```

      Throws:
      :   `java.lang.Exception`
    - #### getBlockBalance

      ```
      Response.BlockBalanceTrace getBlockBalance(java.lang.String blockId,
                                                 long blockNum)
      ```
    - #### getBurnTRX

      ```
      long getBurnTRX(NodeType... nodeType)
      ```
    - #### createWitness

      ```
      Response.TransactionExtention createWitness(java.lang.String ownerAddress,
                                                  java.lang.String url)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### updateWitness

      ```
      Response.TransactionExtention updateWitness(java.lang.String ownerAddress,
                                                  java.lang.String updateUrl)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### withdrawBalance

      ```
      Response.TransactionExtention withdrawBalance(java.lang.String ownerAddress)
                                             throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getNextMaintenanceTime

      ```
      long getNextMaintenanceTime()
      ```
    - #### proposalCreate

      ```
      Response.TransactionExtention proposalCreate(java.lang.String ownerAddress,
                                                   java.util.Map<java.lang.Long,java.lang.Long> parameters)
                                            throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### approveProposal

      ```
      Response.TransactionExtention approveProposal(java.lang.String ownerAddress,
                                                    long proposalId,
                                                    boolean isAddApproval)
                                             throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### deleteProposal

      ```
      Response.TransactionExtention deleteProposal(java.lang.String ownerAddress,
                                                   long proposalId)
                                            throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getTransactionListFromPending

      ```
      GrpcAPI.TransactionIdList getTransactionListFromPending()
      ```
    - #### getPendingSize

      ```
      long getPendingSize()
      ```
    - #### getTransactionFromPending

      ```
      Chain.Transaction getTransactionFromPending(java.lang.String txId)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getBlockById

      ```
      Chain.Block getBlockById(java.lang.String blockID)
      ```
    - #### estimateEnergy

      ```
      Response.EstimateEnergyMessage estimateEnergy(java.lang.String ownerAddress,
                                                    java.lang.String contractAddress,
                                                    Function function,
                                                    NodeType... nodeType)
      ```
    - #### estimateEnergy

      ```
      Response.EstimateEnergyMessage estimateEnergy(java.lang.String ownerAddress,
                                                    java.lang.String contractAddress,
                                                    java.lang.String callData,
                                                    long callValue,
                                                    long tokenValue,
                                                    java.lang.String tokenId,
                                                    NodeType... nodeType)
      ```
    - #### estimateEnergyV2

      ```
      @Deprecated
      Response.EstimateEnergyMessage estimateEnergyV2(java.lang.String ownerAddress,
                                                                  java.lang.String contractAddress,
                                                                  java.lang.String callData)
      ```

      Deprecated.
    - #### triggerCallV2

      ```
      @Deprecated
      TransactionBuilder triggerCallV2(java.lang.String ownerAddress,
                                                   java.lang.String contractAddress,
                                                   java.lang.String callData)
      ```

      Deprecated.
    - #### constantCallV2

      ```
      @Deprecated
      Response.TransactionExtention constantCallV2(java.lang.String ownerAddress,
                                                               java.lang.String contractAddress,
                                                               java.lang.String callData)
      ```

      Deprecated.
    - #### triggerConstantContract

      ```
      Response.TransactionExtention triggerConstantContract(java.lang.String ownerAddress,
                                                            java.lang.String contractAddress,
                                                            Function function,
                                                            NodeType... nodeType)
      ```
    - #### triggerConstantContract

      ```
      Response.TransactionExtention triggerConstantContract(java.lang.String ownerAddress,
                                                            java.lang.String contractAddress,
                                                            java.lang.String callData,
                                                            NodeType... nodeType)
      ```
    - #### triggerConstantContract

      ```
      Response.TransactionExtention triggerConstantContract(java.lang.String ownerAddress,
                                                            java.lang.String contractAddress,
                                                            java.lang.String callData,
                                                            long callValue,
                                                            long tokenValue,
                                                            java.lang.String tokenId,
                                                            NodeType... nodeType)
      ```
    - #### getBandwidthPrices

      ```
      Response.PricesResponseMessage getBandwidthPrices(NodeType... nodeType)
      ```
    - #### getEnergyPrices

      ```
      Response.PricesResponseMessage getEnergyPrices(NodeType... nodeType)
      ```
    - #### getMemoFee

      ```
      Response.PricesResponseMessage getMemoFee()
      ```
    - #### getBandwidthPricesOnSolidity

      ```
      @Deprecated
      Response.PricesResponseMessage getBandwidthPricesOnSolidity()
      ```

      Deprecated.
    - #### getEnergyPricesOnSolidity

      ```
      @Deprecated
      Response.PricesResponseMessage getEnergyPricesOnSolidity()
      ```

      Deprecated.
    - #### clearContractABI

      ```
      Response.TransactionExtention clearContractABI(java.lang.String ownerAddress,
                                                     java.lang.String contractAddress)
                                              throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getPaginatedExchangeList

      ```
      Response.ExchangeList getPaginatedExchangeList(long offset,
                                                     long limit)
      ```
    - #### getPaginatedProposalList

      ```
      Response.ProposalList getPaginatedProposalList(long offset,
                                                     long limit)
      ```
    - #### getBlock

      ```
      Response.BlockExtention getBlock(java.lang.String blockIDOrNum,
                                       boolean detail,
                                       NodeType... nodeType)
      ```
    - #### getBlock

      ```
      Response.BlockExtention getBlock(boolean detail,
                                       NodeType... nodeType)
      ```
    - #### getBlockByIdOrNum

      ```
      Chain.Block getBlockByIdOrNum(java.lang.String blockIDOrNum)
      ```
    - #### getContractInfo

      ```
      Response.SmartContractDataWrapper getContractInfo(java.lang.String contractAddr)
      ```
    - #### getMarketOrderByAccount

      ```
      Response.MarketOrderList getMarketOrderByAccount(java.lang.String account,
                                                       NodeType... nodeType)
      ```
    - #### getMarketOrderById

      ```
      Response.MarketOrder getMarketOrderById(java.lang.String txn,
                                              NodeType... nodeType)
      ```
    - #### getMarketOrderListByPair

      ```
      Response.MarketOrderList getMarketOrderListByPair(java.lang.String sellTokenId,
                                                        java.lang.String buyTokenId,
                                                        NodeType... nodeType)
      ```
    - #### getMarketPairList

      ```
      Response.MarketOrderPairList getMarketPairList(NodeType... nodeType)
      ```
    - #### getMarketPriceByPair

      ```
      Response.MarketPriceList getMarketPriceByPair(java.lang.String sellTokenId,
                                                    java.lang.String buyTokenId,
                                                    NodeType... nodeType)
      ```
    - #### exchangeCreate

      ```
      Response.TransactionExtention exchangeCreate(java.lang.String ownerAddress,
                                                   java.lang.String firstToken,
                                                   long firstBalance,
                                                   java.lang.String secondToken,
                                                   long secondBalance)
                                            throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### exchangeInject

      ```
      Response.TransactionExtention exchangeInject(java.lang.String ownerAddress,
                                                   long exchangeId,
                                                   java.lang.String tokenId,
                                                   long amount)
                                            throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### exchangeTransaction

      ```
      Response.TransactionExtention exchangeTransaction(java.lang.String ownerAddress,
                                                        long exchangeId,
                                                        java.lang.String tokenId,
                                                        long amount,
                                                        long expected)
                                                 throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### exchangeWithdraw

      ```
      Response.TransactionExtention exchangeWithdraw(java.lang.String ownerAddress,
                                                     long exchangeId,
                                                     java.lang.String tokenId,
                                                     long quant)
                                              throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### getTransactionCountByBlockNum

      ```
      long getTransactionCountByBlockNum(long blockNum,
                                         NodeType... nodeType)
      ```
    - #### marketCancelOrder

      ```
      Response.TransactionExtention marketCancelOrder(java.lang.String ownerAddress,
                                                      java.lang.String orderId)
                                               throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### marketSellAsset

      ```
      Response.TransactionExtention marketSellAsset(java.lang.String ownerAddress,
                                                    java.lang.String sellTokenId,
                                                    long sellTokenQuantity,
                                                    java.lang.String buyTokenId,
                                                    long buyTokenQuantity)
                                             throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### updateEnergyLimit

      ```
      Response.TransactionExtention updateEnergyLimit(java.lang.String ownerAddress,
                                                      java.lang.String contractAddress,
                                                      long originEnergyLimit)
                                               throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### updateSetting

      ```
      Response.TransactionExtention updateSetting(java.lang.String ownerAddress,
                                                  java.lang.String contractAddress,
                                                  long consumeUserResourcePercent)
                                           throws IllegalException
      ```

      Throws:
      :   `IllegalException`
    - #### createSmartContract

      ```
      Contract.CreateSmartContract createSmartContract(java.lang.String contractName,
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

      Throws:
      :   `java.lang.Exception`
    - #### createSmartContract

      ```
      Contract.CreateSmartContract createSmartContract(java.lang.String contractName,
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

      Throws:
      :   `java.lang.Exception`
    - #### deployContract

      ```
      Response.TransactionExtention deployContract(java.lang.String contractName,
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

      Throws:
      :   `java.lang.Exception`