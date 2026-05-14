

org.tron.trident.api

## Class WalletGrpc.WalletBlockingStub

* java.lang.Object
* + io.grpc.stub.AbstractStub<S>
  + - io.grpc.stub.AbstractBlockingStub<[WalletGrpc.WalletBlockingStub](../../../../org/tron/trident/api/WalletGrpc.WalletBlockingStub.html "class in org.tron.trident.api")>
    - * org.tron.trident.api.WalletGrpc.WalletBlockingStub

* Enclosing class:
  :   [WalletGrpc](../../../../org/tron/trident/api/WalletGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class WalletGrpc.WalletBlockingStub
  extends io.grpc.stub.AbstractBlockingStub<WalletGrpc.WalletBlockingStub>
  ```

  A stub to allow clients to do synchronous rpc calls to service Wallet.

* + ### Nested Class Summary

    - ### Nested classes/interfaces inherited from class io.grpc.stub.AbstractStub

      `io.grpc.stub.AbstractStub.StubFactory<T extends io.grpc.stub.AbstractStub<T>>`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionExtention` | `addSign(Response.TransactionSign request)` |
    | `Response.TransactionReturn` | `broadcastTransaction(Chain.Transaction request)` Transactions: |
    | `protected WalletGrpc.WalletBlockingStub` | `build(io.grpc.Channel channel, io.grpc.CallOptions callOptions)` |
    | `GrpcAPI.BytesMessage` | `createAddress(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.ShieldedTRC20Parameters` | `createShieldedContractParameters(GrpcAPI.PrivateShieldedTRC20Parameters request)` |
    | `GrpcAPI.ShieldedTRC20Parameters` | `createShieldedContractParametersWithoutAsk(GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk request)` |
    | `Response.TransactionExtention` | `createWitness2(Contract.WitnessCreateContract request)` voting&SRs |
    | `Response.TransactionExtention` | `deployContract(Contract.CreateSmartContract request)` rpc CreateCommonTransaction(Transaction) returns (TransactionExtention) {} rpc CreateAccount(AccountCreateContract) returns (Transaction) {} rpc CreateAccount2(AccountCreateContract) returns (TransactionExtention) {} rpc UpdateAccount(AccountUpdateContract) returns (Transaction) {} rpc UpdateAccount2(AccountUpdateContract) returns (TransactionExtention) {} rpc SetAccountId(SetAccountIdContract) returns (Transaction) {} rpc AccountPermissionUpdate(AccountPermissionUpdateContract) returns (TransactionExtention) {} rpc CreateTransaction(TransferContract) returns (Transaction) {} rpc CreateTransaction2(TransferContract) returns (TransactionExtention) {} rpc CreateAssetIssue(AssetIssueContract) returns (Transaction) {} rpc CreateAssetIssue2(AssetIssueContract) returns (TransactionExtention) {} rpc UpdateAsset(UpdateAssetContract) returns (Transaction) {} rpc UpdateAsset2(UpdateAssetContract) returns (TransactionExtention) {} rpc TransferAsset(TransferAssetContract) returns (Transaction) {} rpc TransferAsset2(TransferAssetContract) returns (TransactionExtention) {} rpc ParticipateAssetIssue(ParticipateAssetIssueContract) returns (Transaction) {} rpc ParticipateAssetIssue2(ParticipateAssetIssueContract) returns (TransactionExtention) {} rpc UnfreezeAsset(UnfreezeAssetContract) returns (Transaction) {} rpc UnfreezeAsset2(UnfreezeAssetContract) returns (TransactionExtention) {} rpc CreateWitness(WitnessCreateContract) returns (Transaction) {} rpc CreateWitness2(WitnessCreateContract) returns (TransactionExtention) {} rpc UpdateWitness(WitnessUpdateContract) returns (Transaction) {} rpc UpdateWitness2(WitnessUpdateContract) returns (TransactionExtention) {} rpc UpdateBrokerage(UpdateBrokerageContract) returns (TransactionExtention) {} rpc VoteWitnessAccount(VoteWitnessContract) returns (Transaction) {} rpc VoteWitnessAccount2(VoteWitnessContract) returns (TransactionExtention) {} rpc FreezeBalance(FreezeBalanceContract) returns (Transaction) {} rpc FreezeBalance2(FreezeBalanceContract) returns (TransactionExtention) {} rpc UnfreezeBalance(UnfreezeBalanceContract) returns (Transaction) {} rpc UnfreezeBalance2(UnfreezeBalanceContract) returns (TransactionExtention) {} rpc WithdrawBalance(WithdrawBalanceContract) returns (Transaction) {} rpc WithdrawBalance2(WithdrawBalanceContract) returns (TransactionExtention) {} rpc ProposalCreate(ProposalCreateContract) returns (TransactionExtention) {} rpc ProposalApprove(ProposalApproveContract) returns (TransactionExtention) {} rpc ProposalDelete(ProposalDeleteContract) returns (TransactionExtention) {} |
    | `Response.EasyTransferResponse` | `easyTransfer(GrpcAPI.EasyTransferMessage request)` |
    | `Response.EasyTransferResponse` | `easyTransferAsset(GrpcAPI.EasyTransferAssetMessage request)` |
    | `Response.EasyTransferResponse` | `easyTransferAssetByPrivate(GrpcAPI.EasyTransferAssetByPrivateMessage request)` |
    | `Response.EasyTransferResponse` | `easyTransferByPrivate(GrpcAPI.EasyTransferByPrivateMessage request)` |
    | `Response.EstimateEnergyMessage` | `estimateEnergy(Contract.TriggerSmartContract request)` |
    | `Response.AddressPrKeyPairMessage` | `generateAddress(GrpcAPI.EmptyMessage request)` |
    | `Response.Account` | `getAccount(GrpcAPI.AccountAddressMessage request)` FLAW: Although the parameters' type is changed, it is still bad API design. |
    | `Response.Account` | `getAccountById(GrpcAPI.AccountIdMessage request)` |
    | `Response.AccountNetMessage` | `getAccountNet(GrpcAPI.AccountAddressMessage request)` |
    | `Response.AccountResourceMessage` | `getAccountResource(GrpcAPI.AccountAddressMessage request)` |
    | `GrpcAPI.BytesMessage` | `getAkFromAsk(GrpcAPI.BytesMessage request)` |
    | `Response.AssetIssueList` | `getAssetIssueByAccount(GrpcAPI.AccountAddressMessage request)` |
    | `Contract.AssetIssueContract` | `getAssetIssueById(GrpcAPI.BytesMessage request)` |
    | `Contract.AssetIssueContract` | `getAssetIssueByName(GrpcAPI.BytesMessage request)` |
    | `Response.AssetIssueList` | `getAssetIssueList(GrpcAPI.EmptyMessage request)` |
    | `Response.AssetIssueList` | `getAssetIssueListByName(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage` | `getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request)` |
    | `Response.PricesResponseMessage` | `getBandwidthPrices(GrpcAPI.EmptyMessage request)` query resource price |
    | `Response.BlockExtention` | `getBlock(GrpcAPI.BlockReq request)` |
    | `Response.BlockBalanceTrace` | `getBlockBalanceTrace(Response.BlockIdentifier request)` |
    | `Chain.Block` | `getBlockById(GrpcAPI.BytesMessage request)` NOTE: `GetBlockById2` is missing. |
    | `Response.BlockList` | `getBlockByLatestNum(GrpcAPI.NumberMessage request)` |
    | `Response.BlockListExtention` | `getBlockByLatestNum2(GrpcAPI.NumberMessage request)` |
    | `Response.BlockList` | `getBlockByLimitNext(GrpcAPI.BlockLimit request)` |
    | `Response.BlockListExtention` | `getBlockByLimitNext2(GrpcAPI.BlockLimit request)` |
    | `Chain.Block` | `getBlockByNum(GrpcAPI.NumberMessage request)` deprecated |
    | `Response.BlockExtention` | `getBlockByNum2(GrpcAPI.NumberMessage request)` Use this function instead of GetBlockByNum. |
    | `GrpcAPI.NumberMessage` | `getBrokerageInfo(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.NumberMessage` | `getBurnTrx(GrpcAPI.EmptyMessage request)` query the network |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage` | `getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage` | `getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request)` |
    | `Response.ChainParameters` | `getChainParameters(GrpcAPI.EmptyMessage request)` |
    | `Common.SmartContract` | `getContract(GrpcAPI.BytesMessage request)` |
    | `Response.SmartContractDataWrapper` | `getContractInfo(GrpcAPI.BytesMessage request)` FLAW: Abusing of `info`. |
    | `Response.DelegatedResourceList` | `getDelegatedResource(Response.DelegatedResourceMessage request)` |
    | `Response.DelegatedResourceAccountIndex` | `getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request)` |
    | `Response.DelegatedResourceAccountIndex` | `getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request)` |
    | `Response.DelegatedResourceList` | `getDelegatedResourceV2(Response.DelegatedResourceMessage request)` |
    | `GrpcAPI.DiversifierMessage` | `getDiversifier(GrpcAPI.EmptyMessage request)` |
    | `Response.PricesResponseMessage` | `getEnergyPrices(GrpcAPI.EmptyMessage request)` |
    | `Response.Exchange` | `getExchangeById(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage` | `getExpandedSpendingKey(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.IncomingViewingKeyMessage` | `getIncomingViewingKey(GrpcAPI.ViewingKeyMessage request)` |
    | `Response.MarketOrderList` | `getMarketOrderByAccount(GrpcAPI.BytesMessage request)` Market API: |
    | `Response.MarketOrder` | `getMarketOrderById(GrpcAPI.BytesMessage request)` |
    | `Response.MarketOrderList` | `getMarketOrderListByPair(Response.MarketOrderPair request)` |
    | `Response.MarketOrderPairList` | `getMarketPairList(GrpcAPI.EmptyMessage request)` |
    | `Response.MarketPriceList` | `getMarketPriceByPair(Response.MarketOrderPair request)` |
    | `Response.PricesResponseMessage` | `getMemoFee(GrpcAPI.EmptyMessage request)` |
    | `GrpcAPI.ShieldedAddressInfo` | `getNewShieldedAddress(GrpcAPI.EmptyMessage request)` |
    | `GrpcAPI.NumberMessage` | `getNextMaintenanceTime(GrpcAPI.EmptyMessage request)` |
    | `GrpcAPI.BytesMessage` | `getNkFromNsk(GrpcAPI.BytesMessage request)` |
    | `Response.NodeInfo` | `getNodeInfo(GrpcAPI.EmptyMessage request)` The real APIs: |
    | `Chain.Block` | `getNowBlock(GrpcAPI.EmptyMessage request)` |
    | `Response.BlockExtention` | `getNowBlock2(GrpcAPI.EmptyMessage request)` |
    | `Response.AssetIssueList` | `getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request)` |
    | `Response.ExchangeList` | `getPaginatedExchangeList(GrpcAPI.PaginatedMessage request)` |
    | `Response.WitnessList` | `getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request)` |
    | `Response.ProposalList` | `getPaginatedProposalList(GrpcAPI.PaginatedMessage request)` |
    | `GrpcAPI.NumberMessage` | `getPendingSize(GrpcAPI.EmptyMessage request)` |
    | `Response.Proposal` | `getProposalById(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.BytesMessage` | `getRcm(GrpcAPI.EmptyMessage request)` |
    | `GrpcAPI.NumberMessage` | `getRewardInfo(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.BytesMessage` | `getSpendingKey(GrpcAPI.EmptyMessage request)` FLAW: Unsafe shielded junk(should be implemented offline). |
    | `Response.TransactionApprovedList` | `getTransactionApprovedList(Chain.Transaction request)` |
    | `Chain.Transaction` | `getTransactionById(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.NumberMessage` | `getTransactionCountByBlockNum(GrpcAPI.NumberMessage request)` |
    | `Chain.Transaction` | `getTransactionFromPending(GrpcAPI.BytesMessage request)` |
    | `Response.TransactionInfoList` | `getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request)` |
    | `Response.TransactionInfo` | `getTransactionInfoById(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.TransactionIdList` | `getTransactionListFromPending(GrpcAPI.EmptyMessage request)` pending pool |
    | `Chain.Transaction` | `getTransactionSign(Response.TransactionSign request)` FLAW: Unsafe junk. |
    | `Response.TransactionExtention` | `getTransactionSign2(Response.TransactionSign request)` |
    | `Response.TransactionSignWeight` | `getTransactionSignWeight(Chain.Transaction request)` |
    | `GrpcAPI.BytesMessage` | `getTriggerInputForShieldedTRC20Contract(GrpcAPI.ShieldedTRC20TriggerContractParameters request)` |
    | `GrpcAPI.PaymentAddressMessage` | `getZenPaymentAddress(GrpcAPI.IncomingViewingKeyDiversifierMessage request)` |
    | `Response.NullifierResult` | `isShieldedTRC20ContractNoteSpent(GrpcAPI.NfTRC20Parameters request)` |
    | `Response.ExchangeList` | `listExchanges(GrpcAPI.EmptyMessage request)` |
    | `Response.NodeList` | `listNodes(GrpcAPI.EmptyMessage request)` |
    | `Response.ProposalList` | `listProposals(GrpcAPI.EmptyMessage request)` |
    | `Response.WitnessList` | `listWitnesses(GrpcAPI.EmptyMessage request)` |
    | `Response.DecryptNotesTRC20` | `scanShieldedTRC20NotesByIvk(GrpcAPI.IvkDecryptTRC20Parameters request)` Shielded helpers: |
    | `Response.DecryptNotesTRC20` | `scanShieldedTRC20NotesByOvk(GrpcAPI.OvkDecryptTRC20Parameters request)` |
    | `GrpcAPI.NumberMessage` | `totalTransaction(GrpcAPI.EmptyMessage request)` java-tron return default 0 |
    | `Response.TransactionExtention` | `triggerConstantContract(Contract.TriggerSmartContract request)` |
    | `Response.TransactionExtention` | `triggerContract(Contract.TriggerSmartContract request)` rpc UpdateSetting(UpdateSettingContract) returns (TransactionExtention) {} // consume\_user\_resource\_percent rpc UpdateEnergyLimit(UpdateEnergyLimitContract) returns (TransactionExtention) {} // origin\_energy\_limit rpc ClearContractABI(ClearABIContract) returns (TransactionExtention) {} |
    | `Response.TransactionExtention` | `withdrawBalance2(Contract.WithdrawBalanceContract request)` |

    - ### Methods inherited from class io.grpc.stub.AbstractBlockingStub

      `newStub, newStub`
    - ### Methods inherited from class io.grpc.stub.AbstractStub

      `getCallOptions, getChannel, withCallCredentials, withChannel, withCompression, withDeadline, withDeadlineAfter, withDeadlineAfter, withExecutor, withInterceptors, withMaxInboundMessageSize, withMaxOutboundMessageSize, withOnReadyThreshold, withOption, withWaitForReady`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### build

      ```
      protected WalletGrpc.WalletBlockingStub build(io.grpc.Channel channel,
                                                    io.grpc.CallOptions callOptions)
      ```

      Specified by:
      :   `build` in class `io.grpc.stub.AbstractStub<WalletGrpc.WalletBlockingStub>`
    - #### broadcastTransaction

      ```
      public Response.TransactionReturn broadcastTransaction(Chain.Transaction request)
      ```

      ```
       Transactions:
      ```
    - #### deployContract

      ```
      public Response.TransactionExtention deployContract(Contract.CreateSmartContract request)
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
      public Response.TransactionExtention triggerContract(Contract.TriggerSmartContract request)
      ```

      ```
        rpc UpdateSetting(UpdateSettingContract) returns (TransactionExtention) {}          // consume_user_resource_percent
        rpc UpdateEnergyLimit(UpdateEnergyLimitContract) returns (TransactionExtention) {}  // origin_energy_limit
        rpc ClearContractABI(ClearABIContract) returns (TransactionExtention) {}
      ```
    - #### triggerConstantContract

      ```
      public Response.TransactionExtention triggerConstantContract(Contract.TriggerSmartContract request)
      ```
    - #### estimateEnergy

      ```
      public Response.EstimateEnergyMessage estimateEnergy(Contract.TriggerSmartContract request)
      ```
    - #### getNodeInfo

      ```
      public Response.NodeInfo getNodeInfo(GrpcAPI.EmptyMessage request)
      ```

      ```
       The real APIs:
      ```
    - #### listNodes

      ```
      public Response.NodeList listNodes(GrpcAPI.EmptyMessage request)
      ```
    - #### getChainParameters

      ```
      public Response.ChainParameters getChainParameters(GrpcAPI.EmptyMessage request)
      ```
    - #### totalTransaction

      ```
      public GrpcAPI.NumberMessage totalTransaction(GrpcAPI.EmptyMessage request)
      ```

      ```
       java-tron return default 0
      ```
    - #### getNextMaintenanceTime

      ```
      public GrpcAPI.NumberMessage getNextMaintenanceTime(GrpcAPI.EmptyMessage request)
      ```
    - #### getTransactionSignWeight

      ```
      public Response.TransactionSignWeight getTransactionSignWeight(Chain.Transaction request)
      ```
    - #### getTransactionApprovedList

      ```
      public Response.TransactionApprovedList getTransactionApprovedList(Chain.Transaction request)
      ```
    - #### getAccount

      ```
      public Response.Account getAccount(GrpcAPI.AccountAddressMessage request)
      ```

      ```
       FLAW: Although the parameters' type is changed, it is still bad API design.
      ```
    - #### getAccountById

      ```
      public Response.Account getAccountById(GrpcAPI.AccountIdMessage request)
      ```
    - #### getAccountNet

      ```
      public Response.AccountNetMessage getAccountNet(GrpcAPI.AccountAddressMessage request)
      ```
    - #### getAccountResource

      ```
      public Response.AccountResourceMessage getAccountResource(GrpcAPI.AccountAddressMessage request)
      ```
    - #### getAssetIssueByAccount

      ```
      public Response.AssetIssueList getAssetIssueByAccount(GrpcAPI.AccountAddressMessage request)
      ```
    - #### getAssetIssueByName

      ```
      public Contract.AssetIssueContract getAssetIssueByName(GrpcAPI.BytesMessage request)
      ```
    - #### getAssetIssueListByName

      ```
      public Response.AssetIssueList getAssetIssueListByName(GrpcAPI.BytesMessage request)
      ```
    - #### getAssetIssueById

      ```
      public Contract.AssetIssueContract getAssetIssueById(GrpcAPI.BytesMessage request)
      ```
    - #### getAssetIssueList

      ```
      public Response.AssetIssueList getAssetIssueList(GrpcAPI.EmptyMessage request)
      ```
    - #### getPaginatedAssetIssueList

      ```
      public Response.AssetIssueList getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request)
      ```
    - #### getBlock

      ```
      public Response.BlockExtention getBlock(GrpcAPI.BlockReq request)
      ```
    - #### getNowBlock

      ```
      public Chain.Block getNowBlock(GrpcAPI.EmptyMessage request)
      ```
    - #### getNowBlock2

      ```
      public Response.BlockExtention getNowBlock2(GrpcAPI.EmptyMessage request)
      ```
    - #### getBlockByNum

      ```
      public Chain.Block getBlockByNum(GrpcAPI.NumberMessage request)
      ```

      ```
      deprecated
      ```
    - #### getBlockByNum2

      ```
      public Response.BlockExtention getBlockByNum2(GrpcAPI.NumberMessage request)
      ```

      ```
      Use this function instead of GetBlockByNum.
      ```
    - #### getBlockById

      ```
      public Chain.Block getBlockById(GrpcAPI.BytesMessage request)
      ```

      ```
       NOTE: `GetBlockById2` is missing. The closest is `GetBlockByLatestNum2`.
      ```
    - #### getBlockByLimitNext

      ```
      public Response.BlockList getBlockByLimitNext(GrpcAPI.BlockLimit request)
      ```
    - #### getBlockByLimitNext2

      ```
      public Response.BlockListExtention getBlockByLimitNext2(GrpcAPI.BlockLimit request)
      ```
    - #### getBlockByLatestNum

      ```
      public Response.BlockList getBlockByLatestNum(GrpcAPI.NumberMessage request)
      ```
    - #### getBlockByLatestNum2

      ```
      public Response.BlockListExtention getBlockByLatestNum2(GrpcAPI.NumberMessage request)
      ```
    - #### getTransactionCountByBlockNum

      ```
      public GrpcAPI.NumberMessage getTransactionCountByBlockNum(GrpcAPI.NumberMessage request)
      ```
    - #### getTransactionById

      ```
      public Chain.Transaction getTransactionById(GrpcAPI.BytesMessage request)
      ```
    - #### getTransactionInfoById

      ```
      public Response.TransactionInfo getTransactionInfoById(GrpcAPI.BytesMessage request)
      ```
    - #### getTransactionInfoByBlockNum

      ```
      public Response.TransactionInfoList getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request)
      ```
    - #### getContract

      ```
      public Common.SmartContract getContract(GrpcAPI.BytesMessage request)
      ```
    - #### getContractInfo

      ```
      public Response.SmartContractDataWrapper getContractInfo(GrpcAPI.BytesMessage request)
      ```

      ```
       FLAW: Abusing of `info`. Should be a `GetContractCode`.
      ```
    - #### listWitnesses

      ```
      public Response.WitnessList listWitnesses(GrpcAPI.EmptyMessage request)
      ```
    - #### getPaginatedNowWitnessList

      ```
      public Response.WitnessList getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request)
      ```
    - #### getBrokerageInfo

      ```
      public GrpcAPI.NumberMessage getBrokerageInfo(GrpcAPI.BytesMessage request)
      ```
    - #### getRewardInfo

      ```
      public GrpcAPI.NumberMessage getRewardInfo(GrpcAPI.BytesMessage request)
      ```
    - #### getDelegatedResource

      ```
      public Response.DelegatedResourceList getDelegatedResource(Response.DelegatedResourceMessage request)
      ```
    - #### getDelegatedResourceAccountIndex

      ```
      public Response.DelegatedResourceAccountIndex getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request)
      ```
    - #### listProposals

      ```
      public Response.ProposalList listProposals(GrpcAPI.EmptyMessage request)
      ```
    - #### getProposalById

      ```
      public Response.Proposal getProposalById(GrpcAPI.BytesMessage request)
      ```
    - #### getPaginatedProposalList

      ```
      public Response.ProposalList getPaginatedProposalList(GrpcAPI.PaginatedMessage request)
      ```
    - #### listExchanges

      ```
      public Response.ExchangeList listExchanges(GrpcAPI.EmptyMessage request)
      ```
    - #### getExchangeById

      ```
      public Response.Exchange getExchangeById(GrpcAPI.BytesMessage request)
      ```
    - #### getPaginatedExchangeList

      ```
      public Response.ExchangeList getPaginatedExchangeList(GrpcAPI.PaginatedMessage request)
      ```
    - #### scanShieldedTRC20NotesByIvk

      ```
      public Response.DecryptNotesTRC20 scanShieldedTRC20NotesByIvk(GrpcAPI.IvkDecryptTRC20Parameters request)
      ```

      ```
       Shielded helpers:
      ```
    - #### scanShieldedTRC20NotesByOvk

      ```
      public Response.DecryptNotesTRC20 scanShieldedTRC20NotesByOvk(GrpcAPI.OvkDecryptTRC20Parameters request)
      ```
    - #### isShieldedTRC20ContractNoteSpent

      ```
      public Response.NullifierResult isShieldedTRC20ContractNoteSpent(GrpcAPI.NfTRC20Parameters request)
      ```
    - #### getMarketOrderByAccount

      ```
      public Response.MarketOrderList getMarketOrderByAccount(GrpcAPI.BytesMessage request)
      ```

      ```
       Market API:
      ```
    - #### getMarketOrderById

      ```
      public Response.MarketOrder getMarketOrderById(GrpcAPI.BytesMessage request)
      ```
    - #### getMarketPriceByPair

      ```
      public Response.MarketPriceList getMarketPriceByPair(Response.MarketOrderPair request)
      ```
    - #### getMarketOrderListByPair

      ```
      public Response.MarketOrderList getMarketOrderListByPair(Response.MarketOrderPair request)
      ```
    - #### getMarketPairList

      ```
      public Response.MarketOrderPairList getMarketPairList(GrpcAPI.EmptyMessage request)
      ```
    - #### getTransactionSign

      ```
      public Chain.Transaction getTransactionSign(Response.TransactionSign request)
      ```

      ```
       FLAW: Unsafe junk.
      ```
    - #### getTransactionSign2

      ```
      public Response.TransactionExtention getTransactionSign2(Response.TransactionSign request)
      ```
    - #### easyTransferAsset

      ```
      public Response.EasyTransferResponse easyTransferAsset(GrpcAPI.EasyTransferAssetMessage request)
      ```
    - #### easyTransferAssetByPrivate

      ```
      public Response.EasyTransferResponse easyTransferAssetByPrivate(GrpcAPI.EasyTransferAssetByPrivateMessage request)
      ```
    - #### easyTransfer

      ```
      public Response.EasyTransferResponse easyTransfer(GrpcAPI.EasyTransferMessage request)
      ```
    - #### easyTransferByPrivate

      ```
      public Response.EasyTransferResponse easyTransferByPrivate(GrpcAPI.EasyTransferByPrivateMessage request)
      ```
    - #### createAddress

      ```
      public GrpcAPI.BytesMessage createAddress(GrpcAPI.BytesMessage request)
      ```
    - #### generateAddress

      ```
      public Response.AddressPrKeyPairMessage generateAddress(GrpcAPI.EmptyMessage request)
      ```
    - #### addSign

      ```
      public Response.TransactionExtention addSign(Response.TransactionSign request)
      ```
    - #### getSpendingKey

      ```
      public GrpcAPI.BytesMessage getSpendingKey(GrpcAPI.EmptyMessage request)
      ```

      ```
       FLAW: Unsafe shielded junk(should be implemented offline).
      ```
    - #### getExpandedSpendingKey

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage getExpandedSpendingKey(GrpcAPI.BytesMessage request)
      ```
    - #### getAkFromAsk

      ```
      public GrpcAPI.BytesMessage getAkFromAsk(GrpcAPI.BytesMessage request)
      ```
    - #### getNkFromNsk

      ```
      public GrpcAPI.BytesMessage getNkFromNsk(GrpcAPI.BytesMessage request)
      ```
    - #### getIncomingViewingKey

      ```
      public GrpcAPI.IncomingViewingKeyMessage getIncomingViewingKey(GrpcAPI.ViewingKeyMessage request)
      ```
    - #### getDiversifier

      ```
      public GrpcAPI.DiversifierMessage getDiversifier(GrpcAPI.EmptyMessage request)
      ```
    - #### getZenPaymentAddress

      ```
      public GrpcAPI.PaymentAddressMessage getZenPaymentAddress(GrpcAPI.IncomingViewingKeyDiversifierMessage request)
      ```
    - #### getNewShieldedAddress

      ```
      public GrpcAPI.ShieldedAddressInfo getNewShieldedAddress(GrpcAPI.EmptyMessage request)
      ```
    - #### getRcm

      ```
      public GrpcAPI.BytesMessage getRcm(GrpcAPI.EmptyMessage request)
      ```
    - #### createShieldedContractParameters

      ```
      public GrpcAPI.ShieldedTRC20Parameters createShieldedContractParameters(GrpcAPI.PrivateShieldedTRC20Parameters request)
      ```
    - #### createShieldedContractParametersWithoutAsk

      ```
      public GrpcAPI.ShieldedTRC20Parameters createShieldedContractParametersWithoutAsk(GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk request)
      ```
    - #### getTriggerInputForShieldedTRC20Contract

      ```
      public GrpcAPI.BytesMessage getTriggerInputForShieldedTRC20Contract(GrpcAPI.ShieldedTRC20TriggerContractParameters request)
      ```
    - #### getAvailableUnfreezeCount

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request)
      ```
    - #### getCanWithdrawUnfreezeAmount

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request)
      ```
    - #### getCanDelegatedMaxSize

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request)
      ```
    - #### getDelegatedResourceV2

      ```
      public Response.DelegatedResourceList getDelegatedResourceV2(Response.DelegatedResourceMessage request)
      ```
    - #### getDelegatedResourceAccountIndexV2

      ```
      public Response.DelegatedResourceAccountIndex getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request)
      ```
    - #### getBurnTrx

      ```
      public GrpcAPI.NumberMessage getBurnTrx(GrpcAPI.EmptyMessage request)
      ```

      ```
      query the network
      ```
    - #### getBlockBalanceTrace

      ```
      public Response.BlockBalanceTrace getBlockBalanceTrace(Response.BlockIdentifier request)
      ```
    - #### createWitness2

      ```
      public Response.TransactionExtention createWitness2(Contract.WitnessCreateContract request)
      ```

      ```
      voting&SRs
      ```
    - #### withdrawBalance2

      ```
      public Response.TransactionExtention withdrawBalance2(Contract.WithdrawBalanceContract request)
      ```
    - #### getTransactionListFromPending

      ```
      public GrpcAPI.TransactionIdList getTransactionListFromPending(GrpcAPI.EmptyMessage request)
      ```

      ```
      pending pool
      ```
    - #### getTransactionFromPending

      ```
      public Chain.Transaction getTransactionFromPending(GrpcAPI.BytesMessage request)
      ```
    - #### getPendingSize

      ```
      public GrpcAPI.NumberMessage getPendingSize(GrpcAPI.EmptyMessage request)
      ```
    - #### getBandwidthPrices

      ```
      public Response.PricesResponseMessage getBandwidthPrices(GrpcAPI.EmptyMessage request)
      ```

      ```
      query resource price
      ```
    - #### getEnergyPrices

      ```
      public Response.PricesResponseMessage getEnergyPrices(GrpcAPI.EmptyMessage request)
      ```
    - #### getMemoFee

      ```
      public Response.PricesResponseMessage getMemoFee(GrpcAPI.EmptyMessage request)
      ```