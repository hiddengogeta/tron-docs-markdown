

org.tron.trident.api

## Class WalletGrpc.WalletFutureStub

* java.lang.Object
* + io.grpc.stub.AbstractStub<S>
  + - io.grpc.stub.AbstractFutureStub<[WalletGrpc.WalletFutureStub](../../../../org/tron/trident/api/WalletGrpc.WalletFutureStub.html "class in org.tron.trident.api")>
    - * org.tron.trident.api.WalletGrpc.WalletFutureStub

* Enclosing class:
  :   [WalletGrpc](../../../../org/tron/trident/api/WalletGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class WalletGrpc.WalletFutureStub
  extends io.grpc.stub.AbstractFutureStub<WalletGrpc.WalletFutureStub>
  ```

  A stub to allow clients to do ListenableFuture-style rpc calls to service Wallet.

* + ### Nested Class Summary

    - ### Nested classes/interfaces inherited from class io.grpc.stub.AbstractStub

      `io.grpc.stub.AbstractStub.StubFactory<T extends io.grpc.stub.AbstractStub<T>>`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention>` | `addSign(Response.TransactionSign request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionReturn>` | `broadcastTransaction(Chain.Transaction request)` Transactions: |
    | `protected WalletGrpc.WalletFutureStub` | `build(io.grpc.Channel channel, io.grpc.CallOptions callOptions)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage>` | `createAddress(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.ShieldedTRC20Parameters>` | `createShieldedContractParameters(GrpcAPI.PrivateShieldedTRC20Parameters request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.ShieldedTRC20Parameters>` | `createShieldedContractParametersWithoutAsk(GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention>` | `createWitness2(Contract.WitnessCreateContract request)` voting&SRs |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention>` | `deployContract(Contract.CreateSmartContract request)` rpc CreateCommonTransaction(Transaction) returns (TransactionExtention) {} rpc CreateAccount(AccountCreateContract) returns (Transaction) {} rpc CreateAccount2(AccountCreateContract) returns (TransactionExtention) {} rpc UpdateAccount(AccountUpdateContract) returns (Transaction) {} rpc UpdateAccount2(AccountUpdateContract) returns (TransactionExtention) {} rpc SetAccountId(SetAccountIdContract) returns (Transaction) {} rpc AccountPermissionUpdate(AccountPermissionUpdateContract) returns (TransactionExtention) {} rpc CreateTransaction(TransferContract) returns (Transaction) {} rpc CreateTransaction2(TransferContract) returns (TransactionExtention) {} rpc CreateAssetIssue(AssetIssueContract) returns (Transaction) {} rpc CreateAssetIssue2(AssetIssueContract) returns (TransactionExtention) {} rpc UpdateAsset(UpdateAssetContract) returns (Transaction) {} rpc UpdateAsset2(UpdateAssetContract) returns (TransactionExtention) {} rpc TransferAsset(TransferAssetContract) returns (Transaction) {} rpc TransferAsset2(TransferAssetContract) returns (TransactionExtention) {} rpc ParticipateAssetIssue(ParticipateAssetIssueContract) returns (Transaction) {} rpc ParticipateAssetIssue2(ParticipateAssetIssueContract) returns (TransactionExtention) {} rpc UnfreezeAsset(UnfreezeAssetContract) returns (Transaction) {} rpc UnfreezeAsset2(UnfreezeAssetContract) returns (TransactionExtention) {} rpc CreateWitness(WitnessCreateContract) returns (Transaction) {} rpc CreateWitness2(WitnessCreateContract) returns (TransactionExtention) {} rpc UpdateWitness(WitnessUpdateContract) returns (Transaction) {} rpc UpdateWitness2(WitnessUpdateContract) returns (TransactionExtention) {} rpc UpdateBrokerage(UpdateBrokerageContract) returns (TransactionExtention) {} rpc VoteWitnessAccount(VoteWitnessContract) returns (Transaction) {} rpc VoteWitnessAccount2(VoteWitnessContract) returns (TransactionExtention) {} rpc FreezeBalance(FreezeBalanceContract) returns (Transaction) {} rpc FreezeBalance2(FreezeBalanceContract) returns (TransactionExtention) {} rpc UnfreezeBalance(UnfreezeBalanceContract) returns (Transaction) {} rpc UnfreezeBalance2(UnfreezeBalanceContract) returns (TransactionExtention) {} rpc WithdrawBalance(WithdrawBalanceContract) returns (Transaction) {} rpc WithdrawBalance2(WithdrawBalanceContract) returns (TransactionExtention) {} rpc ProposalCreate(ProposalCreateContract) returns (TransactionExtention) {} rpc ProposalApprove(ProposalApproveContract) returns (TransactionExtention) {} rpc ProposalDelete(ProposalDeleteContract) returns (TransactionExtention) {} |
    | `com.google.common.util.concurrent.ListenableFuture<Response.EasyTransferResponse>` | `easyTransfer(GrpcAPI.EasyTransferMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.EasyTransferResponse>` | `easyTransferAsset(GrpcAPI.EasyTransferAssetMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.EasyTransferResponse>` | `easyTransferAssetByPrivate(GrpcAPI.EasyTransferAssetByPrivateMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.EasyTransferResponse>` | `easyTransferByPrivate(GrpcAPI.EasyTransferByPrivateMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.EstimateEnergyMessage>` | `estimateEnergy(Contract.TriggerSmartContract request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AddressPrKeyPairMessage>` | `generateAddress(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.Account>` | `getAccount(GrpcAPI.AccountAddressMessage request)` FLAW: Although the parameters' type is changed, it is still bad API design. |
    | `com.google.common.util.concurrent.ListenableFuture<Response.Account>` | `getAccountById(GrpcAPI.AccountIdMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AccountNetMessage>` | `getAccountNet(GrpcAPI.AccountAddressMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AccountResourceMessage>` | `getAccountResource(GrpcAPI.AccountAddressMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage>` | `getAkFromAsk(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList>` | `getAssetIssueByAccount(GrpcAPI.AccountAddressMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Contract.AssetIssueContract>` | `getAssetIssueById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Contract.AssetIssueContract>` | `getAssetIssueByName(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList>` | `getAssetIssueList(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList>` | `getAssetIssueListByName(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.GetAvailableUnfreezeCountResponseMessage>` | `getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.PricesResponseMessage>` | `getBandwidthPrices(GrpcAPI.EmptyMessage request)` query resource price |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention>` | `getBlock(GrpcAPI.BlockReq request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockBalanceTrace>` | `getBlockBalanceTrace(Response.BlockIdentifier request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Chain.Block>` | `getBlockById(GrpcAPI.BytesMessage request)` NOTE: `GetBlockById2` is missing. |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockList>` | `getBlockByLatestNum(GrpcAPI.NumberMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockListExtention>` | `getBlockByLatestNum2(GrpcAPI.NumberMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockList>` | `getBlockByLimitNext(GrpcAPI.BlockLimit request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockListExtention>` | `getBlockByLimitNext2(GrpcAPI.BlockLimit request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Chain.Block>` | `getBlockByNum(GrpcAPI.NumberMessage request)` deprecated |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention>` | `getBlockByNum2(GrpcAPI.NumberMessage request)` Use this function instead of GetBlockByNum. |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getBrokerageInfo(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getBurnTrx(GrpcAPI.EmptyMessage request)` query the network |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.CanDelegatedMaxSizeResponseMessage>` | `getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage>` | `getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.ChainParameters>` | `getChainParameters(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Common.SmartContract>` | `getContract(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.SmartContractDataWrapper>` | `getContractInfo(GrpcAPI.BytesMessage request)` FLAW: Abusing of `info`. |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceList>` | `getDelegatedResource(Response.DelegatedResourceMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceAccountIndex>` | `getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceAccountIndex>` | `getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceList>` | `getDelegatedResourceV2(Response.DelegatedResourceMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.DiversifierMessage>` | `getDiversifier(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.PricesResponseMessage>` | `getEnergyPrices(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.Exchange>` | `getExchangeById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.ExpandedSpendingKeyMessage>` | `getExpandedSpendingKey(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.IncomingViewingKeyMessage>` | `getIncomingViewingKey(GrpcAPI.ViewingKeyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderList>` | `getMarketOrderByAccount(GrpcAPI.BytesMessage request)` Market API: |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketOrder>` | `getMarketOrderById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderList>` | `getMarketOrderListByPair(Response.MarketOrderPair request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderPairList>` | `getMarketPairList(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketPriceList>` | `getMarketPriceByPair(Response.MarketOrderPair request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.PricesResponseMessage>` | `getMemoFee(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.ShieldedAddressInfo>` | `getNewShieldedAddress(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getNextMaintenanceTime(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage>` | `getNkFromNsk(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.NodeInfo>` | `getNodeInfo(GrpcAPI.EmptyMessage request)` The real APIs: |
    | `com.google.common.util.concurrent.ListenableFuture<Chain.Block>` | `getNowBlock(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention>` | `getNowBlock2(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList>` | `getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.ExchangeList>` | `getPaginatedExchangeList(GrpcAPI.PaginatedMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.WitnessList>` | `getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.ProposalList>` | `getPaginatedProposalList(GrpcAPI.PaginatedMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getPendingSize(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.Proposal>` | `getProposalById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage>` | `getRcm(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getRewardInfo(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage>` | `getSpendingKey(GrpcAPI.EmptyMessage request)` FLAW: Unsafe shielded junk(should be implemented offline). |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionApprovedList>` | `getTransactionApprovedList(Chain.Transaction request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Chain.Transaction>` | `getTransactionById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getTransactionCountByBlockNum(GrpcAPI.NumberMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Chain.Transaction>` | `getTransactionFromPending(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionInfoList>` | `getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionInfo>` | `getTransactionInfoById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.TransactionIdList>` | `getTransactionListFromPending(GrpcAPI.EmptyMessage request)` pending pool |
    | `com.google.common.util.concurrent.ListenableFuture<Chain.Transaction>` | `getTransactionSign(Response.TransactionSign request)` FLAW: Unsafe junk. |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention>` | `getTransactionSign2(Response.TransactionSign request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionSignWeight>` | `getTransactionSignWeight(Chain.Transaction request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage>` | `getTriggerInputForShieldedTRC20Contract(GrpcAPI.ShieldedTRC20TriggerContractParameters request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.PaymentAddressMessage>` | `getZenPaymentAddress(GrpcAPI.IncomingViewingKeyDiversifierMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.NullifierResult>` | `isShieldedTRC20ContractNoteSpent(GrpcAPI.NfTRC20Parameters request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.ExchangeList>` | `listExchanges(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.NodeList>` | `listNodes(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.ProposalList>` | `listProposals(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.WitnessList>` | `listWitnesses(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DecryptNotesTRC20>` | `scanShieldedTRC20NotesByIvk(GrpcAPI.IvkDecryptTRC20Parameters request)` Shielded helpers: |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DecryptNotesTRC20>` | `scanShieldedTRC20NotesByOvk(GrpcAPI.OvkDecryptTRC20Parameters request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `totalTransaction(GrpcAPI.EmptyMessage request)` java-tron return default 0 |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention>` | `triggerConstantContract(Contract.TriggerSmartContract request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention>` | `triggerContract(Contract.TriggerSmartContract request)` rpc UpdateSetting(UpdateSettingContract) returns (TransactionExtention) {} // consume\_user\_resource\_percent rpc UpdateEnergyLimit(UpdateEnergyLimitContract) returns (TransactionExtention) {} // origin\_energy\_limit rpc ClearContractABI(ClearABIContract) returns (TransactionExtention) {} |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention>` | `withdrawBalance2(Contract.WithdrawBalanceContract request)` |

    - ### Methods inherited from class io.grpc.stub.AbstractFutureStub

      `newStub, newStub`
    - ### Methods inherited from class io.grpc.stub.AbstractStub

      `getCallOptions, getChannel, withCallCredentials, withChannel, withCompression, withDeadline, withDeadlineAfter, withDeadlineAfter, withExecutor, withInterceptors, withMaxInboundMessageSize, withMaxOutboundMessageSize, withOnReadyThreshold, withOption, withWaitForReady`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### build

      ```
      protected WalletGrpc.WalletFutureStub build(io.grpc.Channel channel,
                                                  io.grpc.CallOptions callOptions)
      ```

      Specified by:
      :   `build` in class `io.grpc.stub.AbstractStub<WalletGrpc.WalletFutureStub>`
    - #### broadcastTransaction

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionReturn> broadcastTransaction(Chain.Transaction request)
      ```

      ```
       Transactions:
      ```
    - #### deployContract

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention> deployContract(Contract.CreateSmartContract request)
      ```

      ```
        rpc CreateCommonTransaction(Transaction) returns (TransactionExtention) {}
        rpc CreateAccount(AccountCreateContract) returns (Transaction) {}
        rpc CreateAccount2(AccountCreateContract) returns (TransactionExtention) {}
        rpc UpdateAccount(AccountUpdateContract) returns (Transaction) {}
        rpc UpdateAccount2(AccountUpdateContract) returns (TransactionExtention) {}
        rpc SetAccountId(SetAccountIdContract) returns (Transaction) {}
        rpc AccountPermissionUpdate(AccountPermissionUpdateContract) returns (TransactionExtention) {}
        rpc CreateTransaction(TransferContract) returns (Transaction) {}
        rpc CreateTransaction2(TransferContract) returns (TransactionExtention) {}
        rpc CreateAssetIssue(AssetIssueContract) returns (Transaction) {}
        rpc CreateAssetIssue2(AssetIssueContract) returns (TransactionExtention) {}
        rpc UpdateAsset(UpdateAssetContract) returns (Transaction) {}
        rpc UpdateAsset2(UpdateAssetContract) returns (TransactionExtention) {}
        rpc TransferAsset(TransferAssetContract) returns (Transaction) {}
        rpc TransferAsset2(TransferAssetContract) returns (TransactionExtention) {}
        rpc ParticipateAssetIssue(ParticipateAssetIssueContract) returns (Transaction) {}
        rpc ParticipateAssetIssue2(ParticipateAssetIssueContract) returns (TransactionExtention) {}
        rpc UnfreezeAsset(UnfreezeAssetContract) returns (Transaction) {}
        rpc UnfreezeAsset2(UnfreezeAssetContract) returns (TransactionExtention) {}
        rpc CreateWitness(WitnessCreateContract) returns (Transaction) {}
        rpc CreateWitness2(WitnessCreateContract) returns (TransactionExtention) {}
        rpc UpdateWitness(WitnessUpdateContract) returns (Transaction) {}
        rpc UpdateWitness2(WitnessUpdateContract) returns (TransactionExtention) {}
        rpc UpdateBrokerage(UpdateBrokerageContract) returns (TransactionExtention) {}
        rpc VoteWitnessAccount(VoteWitnessContract) returns (Transaction) {}
        rpc VoteWitnessAccount2(VoteWitnessContract) returns (TransactionExtention) {}
        rpc FreezeBalance(FreezeBalanceContract) returns (Transaction) {}
        rpc FreezeBalance2(FreezeBalanceContract) returns (TransactionExtention) {}
        rpc UnfreezeBalance(UnfreezeBalanceContract) returns (Transaction) {}
        rpc UnfreezeBalance2(UnfreezeBalanceContract) returns (TransactionExtention) {}
        rpc WithdrawBalance(WithdrawBalanceContract) returns (Transaction) {}
        rpc WithdrawBalance2(WithdrawBalanceContract) returns (TransactionExtention) {}
        rpc ProposalCreate(ProposalCreateContract) returns (TransactionExtention) {}
        rpc ProposalApprove(ProposalApproveContract) returns (TransactionExtention) {}
        rpc ProposalDelete(ProposalDeleteContract) returns (TransactionExtention) {}
      ```
    - #### triggerContract

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention> triggerContract(Contract.TriggerSmartContract request)
      ```

      ```
        rpc UpdateSetting(UpdateSettingContract) returns (TransactionExtention) {}          // consume_user_resource_percent
        rpc UpdateEnergyLimit(UpdateEnergyLimitContract) returns (TransactionExtention) {}  // origin_energy_limit
        rpc ClearContractABI(ClearABIContract) returns (TransactionExtention) {}
      ```
    - #### triggerConstantContract

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention> triggerConstantContract(Contract.TriggerSmartContract request)
      ```
    - #### estimateEnergy

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.EstimateEnergyMessage> estimateEnergy(Contract.TriggerSmartContract request)
      ```
    - #### getNodeInfo

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.NodeInfo> getNodeInfo(GrpcAPI.EmptyMessage request)
      ```

      ```
       The real APIs:
      ```
    - #### listNodes

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.NodeList> listNodes(GrpcAPI.EmptyMessage request)
      ```
    - #### getChainParameters

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.ChainParameters> getChainParameters(GrpcAPI.EmptyMessage request)
      ```
    - #### totalTransaction

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> totalTransaction(GrpcAPI.EmptyMessage request)
      ```

      ```
       java-tron return default 0
      ```
    - #### getNextMaintenanceTime

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getNextMaintenanceTime(GrpcAPI.EmptyMessage request)
      ```
    - #### getTransactionSignWeight

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionSignWeight> getTransactionSignWeight(Chain.Transaction request)
      ```
    - #### getTransactionApprovedList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionApprovedList> getTransactionApprovedList(Chain.Transaction request)
      ```
    - #### getAccount

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.Account> getAccount(GrpcAPI.AccountAddressMessage request)
      ```

      ```
       FLAW: Although the parameters' type is changed, it is still bad API design.
      ```
    - #### getAccountById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.Account> getAccountById(GrpcAPI.AccountIdMessage request)
      ```
    - #### getAccountNet

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.AccountNetMessage> getAccountNet(GrpcAPI.AccountAddressMessage request)
      ```
    - #### getAccountResource

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.AccountResourceMessage> getAccountResource(GrpcAPI.AccountAddressMessage request)
      ```
    - #### getAssetIssueByAccount

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList> getAssetIssueByAccount(GrpcAPI.AccountAddressMessage request)
      ```
    - #### getAssetIssueByName

      ```
      public com.google.common.util.concurrent.ListenableFuture<Contract.AssetIssueContract> getAssetIssueByName(GrpcAPI.BytesMessage request)
      ```
    - #### getAssetIssueListByName

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList> getAssetIssueListByName(GrpcAPI.BytesMessage request)
      ```
    - #### getAssetIssueById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Contract.AssetIssueContract> getAssetIssueById(GrpcAPI.BytesMessage request)
      ```
    - #### getAssetIssueList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList> getAssetIssueList(GrpcAPI.EmptyMessage request)
      ```
    - #### getPaginatedAssetIssueList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList> getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request)
      ```
    - #### getBlock

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention> getBlock(GrpcAPI.BlockReq request)
      ```
    - #### getNowBlock

      ```
      public com.google.common.util.concurrent.ListenableFuture<Chain.Block> getNowBlock(GrpcAPI.EmptyMessage request)
      ```
    - #### getNowBlock2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention> getNowBlock2(GrpcAPI.EmptyMessage request)
      ```
    - #### getBlockByNum

      ```
      public com.google.common.util.concurrent.ListenableFuture<Chain.Block> getBlockByNum(GrpcAPI.NumberMessage request)
      ```

      ```
      deprecated
      ```
    - #### getBlockByNum2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention> getBlockByNum2(GrpcAPI.NumberMessage request)
      ```

      ```
      Use this function instead of GetBlockByNum.
      ```
    - #### getBlockById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Chain.Block> getBlockById(GrpcAPI.BytesMessage request)
      ```

      ```
       NOTE: `GetBlockById2` is missing. The closest is `GetBlockByLatestNum2`.
      ```
    - #### getBlockByLimitNext

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.BlockList> getBlockByLimitNext(GrpcAPI.BlockLimit request)
      ```
    - #### getBlockByLimitNext2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.BlockListExtention> getBlockByLimitNext2(GrpcAPI.BlockLimit request)
      ```
    - #### getBlockByLatestNum

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.BlockList> getBlockByLatestNum(GrpcAPI.NumberMessage request)
      ```
    - #### getBlockByLatestNum2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.BlockListExtention> getBlockByLatestNum2(GrpcAPI.NumberMessage request)
      ```
    - #### getTransactionCountByBlockNum

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getTransactionCountByBlockNum(GrpcAPI.NumberMessage request)
      ```
    - #### getTransactionById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Chain.Transaction> getTransactionById(GrpcAPI.BytesMessage request)
      ```
    - #### getTransactionInfoById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionInfo> getTransactionInfoById(GrpcAPI.BytesMessage request)
      ```
    - #### getTransactionInfoByBlockNum

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionInfoList> getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request)
      ```
    - #### getContract

      ```
      public com.google.common.util.concurrent.ListenableFuture<Common.SmartContract> getContract(GrpcAPI.BytesMessage request)
      ```
    - #### getContractInfo

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.SmartContractDataWrapper> getContractInfo(GrpcAPI.BytesMessage request)
      ```

      ```
       FLAW: Abusing of `info`. Should be a `GetContractCode`.
      ```
    - #### listWitnesses

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.WitnessList> listWitnesses(GrpcAPI.EmptyMessage request)
      ```
    - #### getPaginatedNowWitnessList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.WitnessList> getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request)
      ```
    - #### getBrokerageInfo

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getBrokerageInfo(GrpcAPI.BytesMessage request)
      ```
    - #### getRewardInfo

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getRewardInfo(GrpcAPI.BytesMessage request)
      ```
    - #### getDelegatedResource

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceList> getDelegatedResource(Response.DelegatedResourceMessage request)
      ```
    - #### getDelegatedResourceAccountIndex

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceAccountIndex> getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request)
      ```
    - #### listProposals

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.ProposalList> listProposals(GrpcAPI.EmptyMessage request)
      ```
    - #### getProposalById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.Proposal> getProposalById(GrpcAPI.BytesMessage request)
      ```
    - #### getPaginatedProposalList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.ProposalList> getPaginatedProposalList(GrpcAPI.PaginatedMessage request)
      ```
    - #### listExchanges

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.ExchangeList> listExchanges(GrpcAPI.EmptyMessage request)
      ```
    - #### getExchangeById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.Exchange> getExchangeById(GrpcAPI.BytesMessage request)
      ```
    - #### getPaginatedExchangeList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.ExchangeList> getPaginatedExchangeList(GrpcAPI.PaginatedMessage request)
      ```
    - #### scanShieldedTRC20NotesByIvk

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DecryptNotesTRC20> scanShieldedTRC20NotesByIvk(GrpcAPI.IvkDecryptTRC20Parameters request)
      ```

      ```
       Shielded helpers:
      ```
    - #### scanShieldedTRC20NotesByOvk

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DecryptNotesTRC20> scanShieldedTRC20NotesByOvk(GrpcAPI.OvkDecryptTRC20Parameters request)
      ```
    - #### isShieldedTRC20ContractNoteSpent

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.NullifierResult> isShieldedTRC20ContractNoteSpent(GrpcAPI.NfTRC20Parameters request)
      ```
    - #### getMarketOrderByAccount

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderList> getMarketOrderByAccount(GrpcAPI.BytesMessage request)
      ```

      ```
       Market API:
      ```
    - #### getMarketOrderById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.MarketOrder> getMarketOrderById(GrpcAPI.BytesMessage request)
      ```
    - #### getMarketPriceByPair

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.MarketPriceList> getMarketPriceByPair(Response.MarketOrderPair request)
      ```
    - #### getMarketOrderListByPair

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderList> getMarketOrderListByPair(Response.MarketOrderPair request)
      ```
    - #### getMarketPairList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderPairList> getMarketPairList(GrpcAPI.EmptyMessage request)
      ```
    - #### getTransactionSign

      ```
      public com.google.common.util.concurrent.ListenableFuture<Chain.Transaction> getTransactionSign(Response.TransactionSign request)
      ```

      ```
       FLAW: Unsafe junk.
      ```
    - #### getTransactionSign2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention> getTransactionSign2(Response.TransactionSign request)
      ```
    - #### easyTransferAsset

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.EasyTransferResponse> easyTransferAsset(GrpcAPI.EasyTransferAssetMessage request)
      ```
    - #### easyTransferAssetByPrivate

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.EasyTransferResponse> easyTransferAssetByPrivate(GrpcAPI.EasyTransferAssetByPrivateMessage request)
      ```
    - #### easyTransfer

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.EasyTransferResponse> easyTransfer(GrpcAPI.EasyTransferMessage request)
      ```
    - #### easyTransferByPrivate

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.EasyTransferResponse> easyTransferByPrivate(GrpcAPI.EasyTransferByPrivateMessage request)
      ```
    - #### createAddress

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage> createAddress(GrpcAPI.BytesMessage request)
      ```
    - #### generateAddress

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.AddressPrKeyPairMessage> generateAddress(GrpcAPI.EmptyMessage request)
      ```
    - #### addSign

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention> addSign(Response.TransactionSign request)
      ```
    - #### getSpendingKey

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage> getSpendingKey(GrpcAPI.EmptyMessage request)
      ```

      ```
       FLAW: Unsafe shielded junk(should be implemented offline).
      ```
    - #### getExpandedSpendingKey

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.ExpandedSpendingKeyMessage> getExpandedSpendingKey(GrpcAPI.BytesMessage request)
      ```
    - #### getAkFromAsk

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage> getAkFromAsk(GrpcAPI.BytesMessage request)
      ```
    - #### getNkFromNsk

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage> getNkFromNsk(GrpcAPI.BytesMessage request)
      ```
    - #### getIncomingViewingKey

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.IncomingViewingKeyMessage> getIncomingViewingKey(GrpcAPI.ViewingKeyMessage request)
      ```
    - #### getDiversifier

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.DiversifierMessage> getDiversifier(GrpcAPI.EmptyMessage request)
      ```
    - #### getZenPaymentAddress

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.PaymentAddressMessage> getZenPaymentAddress(GrpcAPI.IncomingViewingKeyDiversifierMessage request)
      ```
    - #### getNewShieldedAddress

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.ShieldedAddressInfo> getNewShieldedAddress(GrpcAPI.EmptyMessage request)
      ```
    - #### getRcm

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage> getRcm(GrpcAPI.EmptyMessage request)
      ```
    - #### createShieldedContractParameters

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.ShieldedTRC20Parameters> createShieldedContractParameters(GrpcAPI.PrivateShieldedTRC20Parameters request)
      ```
    - #### createShieldedContractParametersWithoutAsk

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.ShieldedTRC20Parameters> createShieldedContractParametersWithoutAsk(GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk request)
      ```
    - #### getTriggerInputForShieldedTRC20Contract

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.BytesMessage> getTriggerInputForShieldedTRC20Contract(GrpcAPI.ShieldedTRC20TriggerContractParameters request)
      ```
    - #### getAvailableUnfreezeCount

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.GetAvailableUnfreezeCountResponseMessage> getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request)
      ```
    - #### getCanWithdrawUnfreezeAmount

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage> getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request)
      ```
    - #### getCanDelegatedMaxSize

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.CanDelegatedMaxSizeResponseMessage> getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request)
      ```
    - #### getDelegatedResourceV2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceList> getDelegatedResourceV2(Response.DelegatedResourceMessage request)
      ```
    - #### getDelegatedResourceAccountIndexV2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceAccountIndex> getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request)
      ```
    - #### getBurnTrx

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getBurnTrx(GrpcAPI.EmptyMessage request)
      ```

      ```
      query the network
      ```
    - #### getBlockBalanceTrace

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.BlockBalanceTrace> getBlockBalanceTrace(Response.BlockIdentifier request)
      ```
    - #### createWitness2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention> createWitness2(Contract.WitnessCreateContract request)
      ```

      ```
      voting&SRs
      ```
    - #### withdrawBalance2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention> withdrawBalance2(Contract.WithdrawBalanceContract request)
      ```
    - #### getTransactionListFromPending

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.TransactionIdList> getTransactionListFromPending(GrpcAPI.EmptyMessage request)
      ```

      ```
      pending pool
      ```
    - #### getTransactionFromPending

      ```
      public com.google.common.util.concurrent.ListenableFuture<Chain.Transaction> getTransactionFromPending(GrpcAPI.BytesMessage request)
      ```
    - #### getPendingSize

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getPendingSize(GrpcAPI.EmptyMessage request)
      ```
    - #### getBandwidthPrices

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.PricesResponseMessage> getBandwidthPrices(GrpcAPI.EmptyMessage request)
      ```

      ```
      query resource price
      ```
    - #### getEnergyPrices

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.PricesResponseMessage> getEnergyPrices(GrpcAPI.EmptyMessage request)
      ```
    - #### getMemoFee

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.PricesResponseMessage> getMemoFee(GrpcAPI.EmptyMessage request)
      ```