

org.tron.trident.api

## Class WalletGrpc.WalletStub

* java.lang.Object
* + io.grpc.stub.AbstractStub<S>
  + - io.grpc.stub.AbstractAsyncStub<[WalletGrpc.WalletStub](../../../../org/tron/trident/api/WalletGrpc.WalletStub.html "class in org.tron.trident.api")>
    - * org.tron.trident.api.WalletGrpc.WalletStub

* Enclosing class:
  :   [WalletGrpc](../../../../org/tron/trident/api/WalletGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class WalletGrpc.WalletStub
  extends io.grpc.stub.AbstractAsyncStub<WalletGrpc.WalletStub>
  ```

  A stub to allow clients to do asynchronous rpc calls to service Wallet.

* + ### Nested Class Summary

    - ### Nested classes/interfaces inherited from class io.grpc.stub.AbstractStub

      `io.grpc.stub.AbstractStub.StubFactory<T extends io.grpc.stub.AbstractStub<T>>`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `void` | `addSign(Response.TransactionSign request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |
    | `void` | `broadcastTransaction(Chain.Transaction request, io.grpc.stub.StreamObserver<Response.TransactionReturn> responseObserver)` Transactions: |
    | `protected WalletGrpc.WalletStub` | `build(io.grpc.Channel channel, io.grpc.CallOptions callOptions)` |
    | `void` | `createAddress(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `void` | `createShieldedContractParameters(GrpcAPI.PrivateShieldedTRC20Parameters request, io.grpc.stub.StreamObserver<GrpcAPI.ShieldedTRC20Parameters> responseObserver)` |
    | `void` | `createShieldedContractParametersWithoutAsk(GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk request, io.grpc.stub.StreamObserver<GrpcAPI.ShieldedTRC20Parameters> responseObserver)` |
    | `void` | `createWitness2(Contract.WitnessCreateContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` voting&SRs |
    | `void` | `deployContract(Contract.CreateSmartContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` rpc CreateCommonTransaction(Transaction) returns (TransactionExtention) {} rpc CreateAccount(AccountCreateContract) returns (Transaction) {} rpc CreateAccount2(AccountCreateContract) returns (TransactionExtention) {} rpc UpdateAccount(AccountUpdateContract) returns (Transaction) {} rpc UpdateAccount2(AccountUpdateContract) returns (TransactionExtention) {} rpc SetAccountId(SetAccountIdContract) returns (Transaction) {} rpc AccountPermissionUpdate(AccountPermissionUpdateContract) returns (TransactionExtention) {} rpc CreateTransaction(TransferContract) returns (Transaction) {} rpc CreateTransaction2(TransferContract) returns (TransactionExtention) {} rpc CreateAssetIssue(AssetIssueContract) returns (Transaction) {} rpc CreateAssetIssue2(AssetIssueContract) returns (TransactionExtention) {} rpc UpdateAsset(UpdateAssetContract) returns (Transaction) {} rpc UpdateAsset2(UpdateAssetContract) returns (TransactionExtention) {} rpc TransferAsset(TransferAssetContract) returns (Transaction) {} rpc TransferAsset2(TransferAssetContract) returns (TransactionExtention) {} rpc ParticipateAssetIssue(ParticipateAssetIssueContract) returns (Transaction) {} rpc ParticipateAssetIssue2(ParticipateAssetIssueContract) returns (TransactionExtention) {} rpc UnfreezeAsset(UnfreezeAssetContract) returns (Transaction) {} rpc UnfreezeAsset2(UnfreezeAssetContract) returns (TransactionExtention) {} rpc CreateWitness(WitnessCreateContract) returns (Transaction) {} rpc CreateWitness2(WitnessCreateContract) returns (TransactionExtention) {} rpc UpdateWitness(WitnessUpdateContract) returns (Transaction) {} rpc UpdateWitness2(WitnessUpdateContract) returns (TransactionExtention) {} rpc UpdateBrokerage(UpdateBrokerageContract) returns (TransactionExtention) {} rpc VoteWitnessAccount(VoteWitnessContract) returns (Transaction) {} rpc VoteWitnessAccount2(VoteWitnessContract) returns (TransactionExtention) {} rpc FreezeBalance(FreezeBalanceContract) returns (Transaction) {} rpc FreezeBalance2(FreezeBalanceContract) returns (TransactionExtention) {} rpc UnfreezeBalance(UnfreezeBalanceContract) returns (Transaction) {} rpc UnfreezeBalance2(UnfreezeBalanceContract) returns (TransactionExtention) {} rpc WithdrawBalance(WithdrawBalanceContract) returns (Transaction) {} rpc WithdrawBalance2(WithdrawBalanceContract) returns (TransactionExtention) {} rpc ProposalCreate(ProposalCreateContract) returns (TransactionExtention) {} rpc ProposalApprove(ProposalApproveContract) returns (TransactionExtention) {} rpc ProposalDelete(ProposalDeleteContract) returns (TransactionExtention) {} |
    | `void` | `easyTransfer(GrpcAPI.EasyTransferMessage request, io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)` |
    | `void` | `easyTransferAsset(GrpcAPI.EasyTransferAssetMessage request, io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)` |
    | `void` | `easyTransferAssetByPrivate(GrpcAPI.EasyTransferAssetByPrivateMessage request, io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)` |
    | `void` | `easyTransferByPrivate(GrpcAPI.EasyTransferByPrivateMessage request, io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)` |
    | `void` | `estimateEnergy(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.EstimateEnergyMessage> responseObserver)` |
    | `void` | `generateAddress(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.AddressPrKeyPairMessage> responseObserver)` |
    | `void` | `getAccount(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.Account> responseObserver)` FLAW: Although the parameters' type is changed, it is still bad API design. |
    | `void` | `getAccountById(GrpcAPI.AccountIdMessage request, io.grpc.stub.StreamObserver<Response.Account> responseObserver)` |
    | `void` | `getAccountNet(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.AccountNetMessage> responseObserver)` |
    | `void` | `getAccountResource(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.AccountResourceMessage> responseObserver)` |
    | `void` | `getAkFromAsk(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `void` | `getAssetIssueByAccount(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `void` | `getAssetIssueById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)` |
    | `void` | `getAssetIssueByName(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)` |
    | `void` | `getAssetIssueList(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `void` | `getAssetIssueListByName(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `void` | `getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.GetAvailableUnfreezeCountResponseMessage> responseObserver)` |
    | `void` | `getBandwidthPrices(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` query resource price |
    | `void` | `getBlock(GrpcAPI.BlockReq request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `void` | `getBlockBalanceTrace(Response.BlockIdentifier request, io.grpc.stub.StreamObserver<Response.BlockBalanceTrace> responseObserver)` |
    | `void` | `getBlockById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` NOTE: `GetBlockById2` is missing. |
    | `void` | `getBlockByLatestNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.BlockList> responseObserver)` |
    | `void` | `getBlockByLatestNum2(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.BlockListExtention> responseObserver)` |
    | `void` | `getBlockByLimitNext(GrpcAPI.BlockLimit request, io.grpc.stub.StreamObserver<Response.BlockList> responseObserver)` |
    | `void` | `getBlockByLimitNext2(GrpcAPI.BlockLimit request, io.grpc.stub.StreamObserver<Response.BlockListExtention> responseObserver)` |
    | `void` | `getBlockByNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` deprecated |
    | `void` | `getBlockByNum2(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` Use this function instead of GetBlockByNum. |
    | `void` | `getBrokerageInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `void` | `getBurnTrx(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` query the network |
    | `void` | `getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.CanDelegatedMaxSizeResponseMessage> responseObserver)` |
    | `void` | `getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage> responseObserver)` |
    | `void` | `getChainParameters(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.ChainParameters> responseObserver)` |
    | `void` | `getContract(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Common.SmartContract> responseObserver)` |
    | `void` | `getContractInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.SmartContractDataWrapper> responseObserver)` FLAW: Abusing of `info`. |
    | `void` | `getDelegatedResource(Response.DelegatedResourceMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)` |
    | `void` | `getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)` |
    | `void` | `getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)` |
    | `void` | `getDelegatedResourceV2(Response.DelegatedResourceMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)` |
    | `void` | `getDiversifier(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.DiversifierMessage> responseObserver)` |
    | `void` | `getEnergyPrices(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` |
    | `void` | `getExchangeById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.Exchange> responseObserver)` |
    | `void` | `getExpandedSpendingKey(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.ExpandedSpendingKeyMessage> responseObserver)` |
    | `void` | `getIncomingViewingKey(GrpcAPI.ViewingKeyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.IncomingViewingKeyMessage> responseObserver)` |
    | `void` | `getMarketOrderByAccount(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)` Market API: |
    | `void` | `getMarketOrderById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.MarketOrder> responseObserver)` |
    | `void` | `getMarketOrderListByPair(Response.MarketOrderPair request, io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)` |
    | `void` | `getMarketPairList(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.MarketOrderPairList> responseObserver)` |
    | `void` | `getMarketPriceByPair(Response.MarketOrderPair request, io.grpc.stub.StreamObserver<Response.MarketPriceList> responseObserver)` |
    | `void` | `getMemoFee(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` |
    | `void` | `getNewShieldedAddress(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.ShieldedAddressInfo> responseObserver)` |
    | `void` | `getNextMaintenanceTime(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `void` | `getNkFromNsk(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `void` | `getNodeInfo(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.NodeInfo> responseObserver)` The real APIs: |
    | `void` | `getNowBlock(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` |
    | `void` | `getNowBlock2(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `void` | `getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `void` | `getPaginatedExchangeList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)` |
    | `void` | `getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)` |
    | `void` | `getPaginatedProposalList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.ProposalList> responseObserver)` |
    | `void` | `getPendingSize(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `void` | `getProposalById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.Proposal> responseObserver)` |
    | `void` | `getRcm(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `void` | `getRewardInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `void` | `getSpendingKey(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` FLAW: Unsafe shielded junk(should be implemented offline). |
    | `void` | `getTransactionApprovedList(Chain.Transaction request, io.grpc.stub.StreamObserver<Response.TransactionApprovedList> responseObserver)` |
    | `void` | `getTransactionById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)` |
    | `void` | `getTransactionCountByBlockNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `void` | `getTransactionFromPending(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)` |
    | `void` | `getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.TransactionInfoList> responseObserver)` |
    | `void` | `getTransactionInfoById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.TransactionInfo> responseObserver)` |
    | `void` | `getTransactionListFromPending(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.TransactionIdList> responseObserver)` pending pool |
    | `void` | `getTransactionSign(Response.TransactionSign request, io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)` FLAW: Unsafe junk. |
    | `void` | `getTransactionSign2(Response.TransactionSign request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |
    | `void` | `getTransactionSignWeight(Chain.Transaction request, io.grpc.stub.StreamObserver<Response.TransactionSignWeight> responseObserver)` |
    | `void` | `getTriggerInputForShieldedTRC20Contract(GrpcAPI.ShieldedTRC20TriggerContractParameters request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `void` | `getZenPaymentAddress(GrpcAPI.IncomingViewingKeyDiversifierMessage request, io.grpc.stub.StreamObserver<GrpcAPI.PaymentAddressMessage> responseObserver)` |
    | `void` | `isShieldedTRC20ContractNoteSpent(GrpcAPI.NfTRC20Parameters request, io.grpc.stub.StreamObserver<Response.NullifierResult> responseObserver)` |
    | `void` | `listExchanges(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)` |
    | `void` | `listNodes(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.NodeList> responseObserver)` |
    | `void` | `listProposals(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.ProposalList> responseObserver)` |
    | `void` | `listWitnesses(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)` |
    | `void` | `scanShieldedTRC20NotesByIvk(GrpcAPI.IvkDecryptTRC20Parameters request, io.grpc.stub.StreamObserver<Response.DecryptNotesTRC20> responseObserver)` Shielded helpers: |
    | `void` | `scanShieldedTRC20NotesByOvk(GrpcAPI.OvkDecryptTRC20Parameters request, io.grpc.stub.StreamObserver<Response.DecryptNotesTRC20> responseObserver)` |
    | `void` | `totalTransaction(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` java-tron return default 0 |
    | `void` | `triggerConstantContract(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |
    | `void` | `triggerContract(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` rpc UpdateSetting(UpdateSettingContract) returns (TransactionExtention) {} // consume\_user\_resource\_percent rpc UpdateEnergyLimit(UpdateEnergyLimitContract) returns (TransactionExtention) {} // origin\_energy\_limit rpc ClearContractABI(ClearABIContract) returns (TransactionExtention) {} |
    | `void` | `withdrawBalance2(Contract.WithdrawBalanceContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |

    - ### Methods inherited from class io.grpc.stub.AbstractAsyncStub

      `newStub, newStub`
    - ### Methods inherited from class io.grpc.stub.AbstractStub

      `getCallOptions, getChannel, withCallCredentials, withChannel, withCompression, withDeadline, withDeadlineAfter, withDeadlineAfter, withExecutor, withInterceptors, withMaxInboundMessageSize, withMaxOutboundMessageSize, withOnReadyThreshold, withOption, withWaitForReady`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### build

      ```
      protected WalletGrpc.WalletStub build(io.grpc.Channel channel,
                                            io.grpc.CallOptions callOptions)
      ```

      Specified by:
      :   `build` in class `io.grpc.stub.AbstractStub<WalletGrpc.WalletStub>`
    - #### broadcastTransaction

      ```
      public void broadcastTransaction(Chain.Transaction request,
                                       io.grpc.stub.StreamObserver<Response.TransactionReturn> responseObserver)
      ```

      ```
       Transactions:
      ```
    - #### deployContract

      ```
      public void deployContract(Contract.CreateSmartContract request,
                                 io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
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
      public void triggerContract(Contract.TriggerSmartContract request,
                                  io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```

      ```
        rpc UpdateSetting(UpdateSettingContract) returns (TransactionExtention) {}          // consume_user_resource_percent
        rpc UpdateEnergyLimit(UpdateEnergyLimitContract) returns (TransactionExtention) {}  // origin_energy_limit
        rpc ClearContractABI(ClearABIContract) returns (TransactionExtention) {}
      ```
    - #### triggerConstantContract

      ```
      public void triggerConstantContract(Contract.TriggerSmartContract request,
                                          io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```
    - #### estimateEnergy

      ```
      public void estimateEnergy(Contract.TriggerSmartContract request,
                                 io.grpc.stub.StreamObserver<Response.EstimateEnergyMessage> responseObserver)
      ```
    - #### getNodeInfo

      ```
      public void getNodeInfo(GrpcAPI.EmptyMessage request,
                              io.grpc.stub.StreamObserver<Response.NodeInfo> responseObserver)
      ```

      ```
       The real APIs:
      ```
    - #### listNodes

      ```
      public void listNodes(GrpcAPI.EmptyMessage request,
                            io.grpc.stub.StreamObserver<Response.NodeList> responseObserver)
      ```
    - #### getChainParameters

      ```
      public void getChainParameters(GrpcAPI.EmptyMessage request,
                                     io.grpc.stub.StreamObserver<Response.ChainParameters> responseObserver)
      ```
    - #### totalTransaction

      ```
      public void totalTransaction(GrpcAPI.EmptyMessage request,
                                   io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```

      ```
       java-tron return default 0
      ```
    - #### getNextMaintenanceTime

      ```
      public void getNextMaintenanceTime(GrpcAPI.EmptyMessage request,
                                         io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getTransactionSignWeight

      ```
      public void getTransactionSignWeight(Chain.Transaction request,
                                           io.grpc.stub.StreamObserver<Response.TransactionSignWeight> responseObserver)
      ```
    - #### getTransactionApprovedList

      ```
      public void getTransactionApprovedList(Chain.Transaction request,
                                             io.grpc.stub.StreamObserver<Response.TransactionApprovedList> responseObserver)
      ```
    - #### getAccount

      ```
      public void getAccount(GrpcAPI.AccountAddressMessage request,
                             io.grpc.stub.StreamObserver<Response.Account> responseObserver)
      ```

      ```
       FLAW: Although the parameters' type is changed, it is still bad API design.
      ```
    - #### getAccountById

      ```
      public void getAccountById(GrpcAPI.AccountIdMessage request,
                                 io.grpc.stub.StreamObserver<Response.Account> responseObserver)
      ```
    - #### getAccountNet

      ```
      public void getAccountNet(GrpcAPI.AccountAddressMessage request,
                                io.grpc.stub.StreamObserver<Response.AccountNetMessage> responseObserver)
      ```
    - #### getAccountResource

      ```
      public void getAccountResource(GrpcAPI.AccountAddressMessage request,
                                     io.grpc.stub.StreamObserver<Response.AccountResourceMessage> responseObserver)
      ```
    - #### getAssetIssueByAccount

      ```
      public void getAssetIssueByAccount(GrpcAPI.AccountAddressMessage request,
                                         io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)
      ```
    - #### getAssetIssueByName

      ```
      public void getAssetIssueByName(GrpcAPI.BytesMessage request,
                                      io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)
      ```
    - #### getAssetIssueListByName

      ```
      public void getAssetIssueListByName(GrpcAPI.BytesMessage request,
                                          io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)
      ```
    - #### getAssetIssueById

      ```
      public void getAssetIssueById(GrpcAPI.BytesMessage request,
                                    io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)
      ```
    - #### getAssetIssueList

      ```
      public void getAssetIssueList(GrpcAPI.EmptyMessage request,
                                    io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)
      ```
    - #### getPaginatedAssetIssueList

      ```
      public void getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request,
                                             io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)
      ```
    - #### getBlock

      ```
      public void getBlock(GrpcAPI.BlockReq request,
                           io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)
      ```
    - #### getNowBlock

      ```
      public void getNowBlock(GrpcAPI.EmptyMessage request,
                              io.grpc.stub.StreamObserver<Chain.Block> responseObserver)
      ```
    - #### getNowBlock2

      ```
      public void getNowBlock2(GrpcAPI.EmptyMessage request,
                               io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)
      ```
    - #### getBlockByNum

      ```
      public void getBlockByNum(GrpcAPI.NumberMessage request,
                                io.grpc.stub.StreamObserver<Chain.Block> responseObserver)
      ```

      ```
      deprecated
      ```
    - #### getBlockByNum2

      ```
      public void getBlockByNum2(GrpcAPI.NumberMessage request,
                                 io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)
      ```

      ```
      Use this function instead of GetBlockByNum.
      ```
    - #### getBlockById

      ```
      public void getBlockById(GrpcAPI.BytesMessage request,
                               io.grpc.stub.StreamObserver<Chain.Block> responseObserver)
      ```

      ```
       NOTE: `GetBlockById2` is missing. The closest is `GetBlockByLatestNum2`.
      ```
    - #### getBlockByLimitNext

      ```
      public void getBlockByLimitNext(GrpcAPI.BlockLimit request,
                                      io.grpc.stub.StreamObserver<Response.BlockList> responseObserver)
      ```
    - #### getBlockByLimitNext2

      ```
      public void getBlockByLimitNext2(GrpcAPI.BlockLimit request,
                                       io.grpc.stub.StreamObserver<Response.BlockListExtention> responseObserver)
      ```
    - #### getBlockByLatestNum

      ```
      public void getBlockByLatestNum(GrpcAPI.NumberMessage request,
                                      io.grpc.stub.StreamObserver<Response.BlockList> responseObserver)
      ```
    - #### getBlockByLatestNum2

      ```
      public void getBlockByLatestNum2(GrpcAPI.NumberMessage request,
                                       io.grpc.stub.StreamObserver<Response.BlockListExtention> responseObserver)
      ```
    - #### getTransactionCountByBlockNum

      ```
      public void getTransactionCountByBlockNum(GrpcAPI.NumberMessage request,
                                                io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getTransactionById

      ```
      public void getTransactionById(GrpcAPI.BytesMessage request,
                                     io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)
      ```
    - #### getTransactionInfoById

      ```
      public void getTransactionInfoById(GrpcAPI.BytesMessage request,
                                         io.grpc.stub.StreamObserver<Response.TransactionInfo> responseObserver)
      ```
    - #### getTransactionInfoByBlockNum

      ```
      public void getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request,
                                               io.grpc.stub.StreamObserver<Response.TransactionInfoList> responseObserver)
      ```
    - #### getContract

      ```
      public void getContract(GrpcAPI.BytesMessage request,
                              io.grpc.stub.StreamObserver<Common.SmartContract> responseObserver)
      ```
    - #### getContractInfo

      ```
      public void getContractInfo(GrpcAPI.BytesMessage request,
                                  io.grpc.stub.StreamObserver<Response.SmartContractDataWrapper> responseObserver)
      ```

      ```
       FLAW: Abusing of `info`. Should be a `GetContractCode`.
      ```
    - #### listWitnesses

      ```
      public void listWitnesses(GrpcAPI.EmptyMessage request,
                                io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)
      ```
    - #### getPaginatedNowWitnessList

      ```
      public void getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request,
                                             io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)
      ```
    - #### getBrokerageInfo

      ```
      public void getBrokerageInfo(GrpcAPI.BytesMessage request,
                                   io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getRewardInfo

      ```
      public void getRewardInfo(GrpcAPI.BytesMessage request,
                                io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getDelegatedResource

      ```
      public void getDelegatedResource(Response.DelegatedResourceMessage request,
                                       io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)
      ```
    - #### getDelegatedResourceAccountIndex

      ```
      public void getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request,
                                                   io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)
      ```
    - #### listProposals

      ```
      public void listProposals(GrpcAPI.EmptyMessage request,
                                io.grpc.stub.StreamObserver<Response.ProposalList> responseObserver)
      ```
    - #### getProposalById

      ```
      public void getProposalById(GrpcAPI.BytesMessage request,
                                  io.grpc.stub.StreamObserver<Response.Proposal> responseObserver)
      ```
    - #### getPaginatedProposalList

      ```
      public void getPaginatedProposalList(GrpcAPI.PaginatedMessage request,
                                           io.grpc.stub.StreamObserver<Response.ProposalList> responseObserver)
      ```
    - #### listExchanges

      ```
      public void listExchanges(GrpcAPI.EmptyMessage request,
                                io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)
      ```
    - #### getExchangeById

      ```
      public void getExchangeById(GrpcAPI.BytesMessage request,
                                  io.grpc.stub.StreamObserver<Response.Exchange> responseObserver)
      ```
    - #### getPaginatedExchangeList

      ```
      public void getPaginatedExchangeList(GrpcAPI.PaginatedMessage request,
                                           io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)
      ```
    - #### scanShieldedTRC20NotesByIvk

      ```
      public void scanShieldedTRC20NotesByIvk(GrpcAPI.IvkDecryptTRC20Parameters request,
                                              io.grpc.stub.StreamObserver<Response.DecryptNotesTRC20> responseObserver)
      ```

      ```
       Shielded helpers:
      ```
    - #### scanShieldedTRC20NotesByOvk

      ```
      public void scanShieldedTRC20NotesByOvk(GrpcAPI.OvkDecryptTRC20Parameters request,
                                              io.grpc.stub.StreamObserver<Response.DecryptNotesTRC20> responseObserver)
      ```
    - #### isShieldedTRC20ContractNoteSpent

      ```
      public void isShieldedTRC20ContractNoteSpent(GrpcAPI.NfTRC20Parameters request,
                                                   io.grpc.stub.StreamObserver<Response.NullifierResult> responseObserver)
      ```
    - #### getMarketOrderByAccount

      ```
      public void getMarketOrderByAccount(GrpcAPI.BytesMessage request,
                                          io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)
      ```

      ```
       Market API:
      ```
    - #### getMarketOrderById

      ```
      public void getMarketOrderById(GrpcAPI.BytesMessage request,
                                     io.grpc.stub.StreamObserver<Response.MarketOrder> responseObserver)
      ```
    - #### getMarketPriceByPair

      ```
      public void getMarketPriceByPair(Response.MarketOrderPair request,
                                       io.grpc.stub.StreamObserver<Response.MarketPriceList> responseObserver)
      ```
    - #### getMarketOrderListByPair

      ```
      public void getMarketOrderListByPair(Response.MarketOrderPair request,
                                           io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)
      ```
    - #### getMarketPairList

      ```
      public void getMarketPairList(GrpcAPI.EmptyMessage request,
                                    io.grpc.stub.StreamObserver<Response.MarketOrderPairList> responseObserver)
      ```
    - #### getTransactionSign

      ```
      public void getTransactionSign(Response.TransactionSign request,
                                     io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)
      ```

      ```
       FLAW: Unsafe junk.
      ```
    - #### getTransactionSign2

      ```
      public void getTransactionSign2(Response.TransactionSign request,
                                      io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```
    - #### easyTransferAsset

      ```
      public void easyTransferAsset(GrpcAPI.EasyTransferAssetMessage request,
                                    io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)
      ```
    - #### easyTransferAssetByPrivate

      ```
      public void easyTransferAssetByPrivate(GrpcAPI.EasyTransferAssetByPrivateMessage request,
                                             io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)
      ```
    - #### easyTransfer

      ```
      public void easyTransfer(GrpcAPI.EasyTransferMessage request,
                               io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)
      ```
    - #### easyTransferByPrivate

      ```
      public void easyTransferByPrivate(GrpcAPI.EasyTransferByPrivateMessage request,
                                        io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)
      ```
    - #### createAddress

      ```
      public void createAddress(GrpcAPI.BytesMessage request,
                                io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### generateAddress

      ```
      public void generateAddress(GrpcAPI.EmptyMessage request,
                                  io.grpc.stub.StreamObserver<Response.AddressPrKeyPairMessage> responseObserver)
      ```
    - #### addSign

      ```
      public void addSign(Response.TransactionSign request,
                          io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```
    - #### getSpendingKey

      ```
      public void getSpendingKey(GrpcAPI.EmptyMessage request,
                                 io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```

      ```
       FLAW: Unsafe shielded junk(should be implemented offline).
      ```
    - #### getExpandedSpendingKey

      ```
      public void getExpandedSpendingKey(GrpcAPI.BytesMessage request,
                                         io.grpc.stub.StreamObserver<GrpcAPI.ExpandedSpendingKeyMessage> responseObserver)
      ```
    - #### getAkFromAsk

      ```
      public void getAkFromAsk(GrpcAPI.BytesMessage request,
                               io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### getNkFromNsk

      ```
      public void getNkFromNsk(GrpcAPI.BytesMessage request,
                               io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### getIncomingViewingKey

      ```
      public void getIncomingViewingKey(GrpcAPI.ViewingKeyMessage request,
                                        io.grpc.stub.StreamObserver<GrpcAPI.IncomingViewingKeyMessage> responseObserver)
      ```
    - #### getDiversifier

      ```
      public void getDiversifier(GrpcAPI.EmptyMessage request,
                                 io.grpc.stub.StreamObserver<GrpcAPI.DiversifierMessage> responseObserver)
      ```
    - #### getZenPaymentAddress

      ```
      public void getZenPaymentAddress(GrpcAPI.IncomingViewingKeyDiversifierMessage request,
                                       io.grpc.stub.StreamObserver<GrpcAPI.PaymentAddressMessage> responseObserver)
      ```
    - #### getNewShieldedAddress

      ```
      public void getNewShieldedAddress(GrpcAPI.EmptyMessage request,
                                        io.grpc.stub.StreamObserver<GrpcAPI.ShieldedAddressInfo> responseObserver)
      ```
    - #### getRcm

      ```
      public void getRcm(GrpcAPI.EmptyMessage request,
                         io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### createShieldedContractParameters

      ```
      public void createShieldedContractParameters(GrpcAPI.PrivateShieldedTRC20Parameters request,
                                                   io.grpc.stub.StreamObserver<GrpcAPI.ShieldedTRC20Parameters> responseObserver)
      ```
    - #### createShieldedContractParametersWithoutAsk

      ```
      public void createShieldedContractParametersWithoutAsk(GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk request,
                                                             io.grpc.stub.StreamObserver<GrpcAPI.ShieldedTRC20Parameters> responseObserver)
      ```
    - #### getTriggerInputForShieldedTRC20Contract

      ```
      public void getTriggerInputForShieldedTRC20Contract(GrpcAPI.ShieldedTRC20TriggerContractParameters request,
                                                          io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### getAvailableUnfreezeCount

      ```
      public void getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request,
                                            io.grpc.stub.StreamObserver<GrpcAPI.GetAvailableUnfreezeCountResponseMessage> responseObserver)
      ```
    - #### getCanWithdrawUnfreezeAmount

      ```
      public void getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request,
                                               io.grpc.stub.StreamObserver<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage> responseObserver)
      ```
    - #### getCanDelegatedMaxSize

      ```
      public void getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request,
                                         io.grpc.stub.StreamObserver<GrpcAPI.CanDelegatedMaxSizeResponseMessage> responseObserver)
      ```
    - #### getDelegatedResourceV2

      ```
      public void getDelegatedResourceV2(Response.DelegatedResourceMessage request,
                                         io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)
      ```
    - #### getDelegatedResourceAccountIndexV2

      ```
      public void getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request,
                                                     io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)
      ```
    - #### getBurnTrx

      ```
      public void getBurnTrx(GrpcAPI.EmptyMessage request,
                             io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```

      ```
      query the network
      ```
    - #### getBlockBalanceTrace

      ```
      public void getBlockBalanceTrace(Response.BlockIdentifier request,
                                       io.grpc.stub.StreamObserver<Response.BlockBalanceTrace> responseObserver)
      ```
    - #### createWitness2

      ```
      public void createWitness2(Contract.WitnessCreateContract request,
                                 io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```

      ```
      voting&SRs
      ```
    - #### withdrawBalance2

      ```
      public void withdrawBalance2(Contract.WithdrawBalanceContract request,
                                   io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```
    - #### getTransactionListFromPending

      ```
      public void getTransactionListFromPending(GrpcAPI.EmptyMessage request,
                                                io.grpc.stub.StreamObserver<GrpcAPI.TransactionIdList> responseObserver)
      ```

      ```
      pending pool
      ```
    - #### getTransactionFromPending

      ```
      public void getTransactionFromPending(GrpcAPI.BytesMessage request,
                                            io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)
      ```
    - #### getPendingSize

      ```
      public void getPendingSize(GrpcAPI.EmptyMessage request,
                                 io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getBandwidthPrices

      ```
      public void getBandwidthPrices(GrpcAPI.EmptyMessage request,
                                     io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)
      ```

      ```
      query resource price
      ```
    - #### getEnergyPrices

      ```
      public void getEnergyPrices(GrpcAPI.EmptyMessage request,
                                  io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)
      ```
    - #### getMemoFee

      ```
      public void getMemoFee(GrpcAPI.EmptyMessage request,
                             io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)
      ```