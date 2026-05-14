

org.tron.trident.api

## Interface WalletGrpc.AsyncService

* All Known Implementing Classes:
  :   [WalletGrpc.WalletImplBase](../../../../org/tron/trident/api/WalletGrpc.WalletImplBase.html "class in org.tron.trident.api")

  Enclosing class:
  :   [WalletGrpc](../../../../org/tron/trident/api/WalletGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface WalletGrpc.AsyncService
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);)

    | Modifier and Type | Method and Description |
    | `default void` | `addSign(Response.TransactionSign request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |
    | `default void` | `broadcastTransaction(Chain.Transaction request, io.grpc.stub.StreamObserver<Response.TransactionReturn> responseObserver)` Transactions: |
    | `default void` | `createAddress(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `default void` | `createShieldedContractParameters(GrpcAPI.PrivateShieldedTRC20Parameters request, io.grpc.stub.StreamObserver<GrpcAPI.ShieldedTRC20Parameters> responseObserver)` |
    | `default void` | `createShieldedContractParametersWithoutAsk(GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk request, io.grpc.stub.StreamObserver<GrpcAPI.ShieldedTRC20Parameters> responseObserver)` |
    | `default void` | `createWitness2(Contract.WitnessCreateContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` voting&SRs |
    | `default void` | `deployContract(Contract.CreateSmartContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` rpc CreateCommonTransaction(Transaction) returns (TransactionExtention) {} rpc CreateAccount(AccountCreateContract) returns (Transaction) {} rpc CreateAccount2(AccountCreateContract) returns (TransactionExtention) {} rpc UpdateAccount(AccountUpdateContract) returns (Transaction) {} rpc UpdateAccount2(AccountUpdateContract) returns (TransactionExtention) {} rpc SetAccountId(SetAccountIdContract) returns (Transaction) {} rpc AccountPermissionUpdate(AccountPermissionUpdateContract) returns (TransactionExtention) {} rpc CreateTransaction(TransferContract) returns (Transaction) {} rpc CreateTransaction2(TransferContract) returns (TransactionExtention) {} rpc CreateAssetIssue(AssetIssueContract) returns (Transaction) {} rpc CreateAssetIssue2(AssetIssueContract) returns (TransactionExtention) {} rpc UpdateAsset(UpdateAssetContract) returns (Transaction) {} rpc UpdateAsset2(UpdateAssetContract) returns (TransactionExtention) {} rpc TransferAsset(TransferAssetContract) returns (Transaction) {} rpc TransferAsset2(TransferAssetContract) returns (TransactionExtention) {} rpc ParticipateAssetIssue(ParticipateAssetIssueContract) returns (Transaction) {} rpc ParticipateAssetIssue2(ParticipateAssetIssueContract) returns (TransactionExtention) {} rpc UnfreezeAsset(UnfreezeAssetContract) returns (Transaction) {} rpc UnfreezeAsset2(UnfreezeAssetContract) returns (TransactionExtention) {} rpc CreateWitness(WitnessCreateContract) returns (Transaction) {} rpc CreateWitness2(WitnessCreateContract) returns (TransactionExtention) {} rpc UpdateWitness(WitnessUpdateContract) returns (Transaction) {} rpc UpdateWitness2(WitnessUpdateContract) returns (TransactionExtention) {} rpc UpdateBrokerage(UpdateBrokerageContract) returns (TransactionExtention) {} rpc VoteWitnessAccount(VoteWitnessContract) returns (Transaction) {} rpc VoteWitnessAccount2(VoteWitnessContract) returns (TransactionExtention) {} rpc FreezeBalance(FreezeBalanceContract) returns (Transaction) {} rpc FreezeBalance2(FreezeBalanceContract) returns (TransactionExtention) {} rpc UnfreezeBalance(UnfreezeBalanceContract) returns (Transaction) {} rpc UnfreezeBalance2(UnfreezeBalanceContract) returns (TransactionExtention) {} rpc WithdrawBalance(WithdrawBalanceContract) returns (Transaction) {} rpc WithdrawBalance2(WithdrawBalanceContract) returns (TransactionExtention) {} rpc ProposalCreate(ProposalCreateContract) returns (TransactionExtention) {} rpc ProposalApprove(ProposalApproveContract) returns (TransactionExtention) {} rpc ProposalDelete(ProposalDeleteContract) returns (TransactionExtention) {} |
    | `default void` | `easyTransfer(GrpcAPI.EasyTransferMessage request, io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)` |
    | `default void` | `easyTransferAsset(GrpcAPI.EasyTransferAssetMessage request, io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)` |
    | `default void` | `easyTransferAssetByPrivate(GrpcAPI.EasyTransferAssetByPrivateMessage request, io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)` |
    | `default void` | `easyTransferByPrivate(GrpcAPI.EasyTransferByPrivateMessage request, io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)` |
    | `default void` | `estimateEnergy(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.EstimateEnergyMessage> responseObserver)` |
    | `default void` | `generateAddress(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.AddressPrKeyPairMessage> responseObserver)` |
    | `default void` | `getAccount(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.Account> responseObserver)` FLAW: Although the parameters' type is changed, it is still bad API design. |
    | `default void` | `getAccountById(GrpcAPI.AccountIdMessage request, io.grpc.stub.StreamObserver<Response.Account> responseObserver)` |
    | `default void` | `getAccountNet(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.AccountNetMessage> responseObserver)` |
    | `default void` | `getAccountResource(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.AccountResourceMessage> responseObserver)` |
    | `default void` | `getAkFromAsk(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `default void` | `getAssetIssueByAccount(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `default void` | `getAssetIssueById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)` |
    | `default void` | `getAssetIssueByName(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)` |
    | `default void` | `getAssetIssueList(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `default void` | `getAssetIssueListByName(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `default void` | `getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.GetAvailableUnfreezeCountResponseMessage> responseObserver)` |
    | `default void` | `getBandwidthPrices(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` query resource price |
    | `default void` | `getBlock(GrpcAPI.BlockReq request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `default void` | `getBlockBalanceTrace(Response.BlockIdentifier request, io.grpc.stub.StreamObserver<Response.BlockBalanceTrace> responseObserver)` |
    | `default void` | `getBlockById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` NOTE: `GetBlockById2` is missing. |
    | `default void` | `getBlockByLatestNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.BlockList> responseObserver)` |
    | `default void` | `getBlockByLatestNum2(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.BlockListExtention> responseObserver)` |
    | `default void` | `getBlockByLimitNext(GrpcAPI.BlockLimit request, io.grpc.stub.StreamObserver<Response.BlockList> responseObserver)` |
    | `default void` | `getBlockByLimitNext2(GrpcAPI.BlockLimit request, io.grpc.stub.StreamObserver<Response.BlockListExtention> responseObserver)` |
    | `default void` | `getBlockByNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` deprecated |
    | `default void` | `getBlockByNum2(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` Use this function instead of GetBlockByNum. |
    | `default void` | `getBrokerageInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `default void` | `getBurnTrx(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` query the network |
    | `default void` | `getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.CanDelegatedMaxSizeResponseMessage> responseObserver)` |
    | `default void` | `getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage> responseObserver)` |
    | `default void` | `getChainParameters(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.ChainParameters> responseObserver)` |
    | `default void` | `getContract(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Common.SmartContract> responseObserver)` |
    | `default void` | `getContractInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.SmartContractDataWrapper> responseObserver)` FLAW: Abusing of `info`. |
    | `default void` | `getDelegatedResource(Response.DelegatedResourceMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)` |
    | `default void` | `getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)` |
    | `default void` | `getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)` |
    | `default void` | `getDelegatedResourceV2(Response.DelegatedResourceMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)` |
    | `default void` | `getDiversifier(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.DiversifierMessage> responseObserver)` |
    | `default void` | `getEnergyPrices(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` |
    | `default void` | `getExchangeById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.Exchange> responseObserver)` |
    | `default void` | `getExpandedSpendingKey(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.ExpandedSpendingKeyMessage> responseObserver)` |
    | `default void` | `getIncomingViewingKey(GrpcAPI.ViewingKeyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.IncomingViewingKeyMessage> responseObserver)` |
    | `default void` | `getMarketOrderByAccount(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)` Market API: |
    | `default void` | `getMarketOrderById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.MarketOrder> responseObserver)` |
    | `default void` | `getMarketOrderListByPair(Response.MarketOrderPair request, io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)` |
    | `default void` | `getMarketPairList(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.MarketOrderPairList> responseObserver)` |
    | `default void` | `getMarketPriceByPair(Response.MarketOrderPair request, io.grpc.stub.StreamObserver<Response.MarketPriceList> responseObserver)` |
    | `default void` | `getMemoFee(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` |
    | `default void` | `getNewShieldedAddress(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.ShieldedAddressInfo> responseObserver)` |
    | `default void` | `getNextMaintenanceTime(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `default void` | `getNkFromNsk(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `default void` | `getNodeInfo(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.NodeInfo> responseObserver)` The real APIs: |
    | `default void` | `getNowBlock(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` |
    | `default void` | `getNowBlock2(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `default void` | `getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `default void` | `getPaginatedExchangeList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)` |
    | `default void` | `getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)` |
    | `default void` | `getPaginatedProposalList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.ProposalList> responseObserver)` |
    | `default void` | `getPendingSize(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `default void` | `getProposalById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.Proposal> responseObserver)` |
    | `default void` | `getRcm(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `default void` | `getRewardInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `default void` | `getSpendingKey(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` FLAW: Unsafe shielded junk(should be implemented offline). |
    | `default void` | `getTransactionApprovedList(Chain.Transaction request, io.grpc.stub.StreamObserver<Response.TransactionApprovedList> responseObserver)` |
    | `default void` | `getTransactionById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)` |
    | `default void` | `getTransactionCountByBlockNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `default void` | `getTransactionFromPending(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)` |
    | `default void` | `getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.TransactionInfoList> responseObserver)` |
    | `default void` | `getTransactionInfoById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.TransactionInfo> responseObserver)` |
    | `default void` | `getTransactionListFromPending(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.TransactionIdList> responseObserver)` pending pool |
    | `default void` | `getTransactionSign(Response.TransactionSign request, io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)` FLAW: Unsafe junk. |
    | `default void` | `getTransactionSign2(Response.TransactionSign request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |
    | `default void` | `getTransactionSignWeight(Chain.Transaction request, io.grpc.stub.StreamObserver<Response.TransactionSignWeight> responseObserver)` |
    | `default void` | `getTriggerInputForShieldedTRC20Contract(GrpcAPI.ShieldedTRC20TriggerContractParameters request, io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)` |
    | `default void` | `getZenPaymentAddress(GrpcAPI.IncomingViewingKeyDiversifierMessage request, io.grpc.stub.StreamObserver<GrpcAPI.PaymentAddressMessage> responseObserver)` |
    | `default void` | `isShieldedTRC20ContractNoteSpent(GrpcAPI.NfTRC20Parameters request, io.grpc.stub.StreamObserver<Response.NullifierResult> responseObserver)` |
    | `default void` | `listExchanges(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)` |
    | `default void` | `listNodes(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.NodeList> responseObserver)` |
    | `default void` | `listProposals(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.ProposalList> responseObserver)` |
    | `default void` | `listWitnesses(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)` |
    | `default void` | `scanShieldedTRC20NotesByIvk(GrpcAPI.IvkDecryptTRC20Parameters request, io.grpc.stub.StreamObserver<Response.DecryptNotesTRC20> responseObserver)` Shielded helpers: |
    | `default void` | `scanShieldedTRC20NotesByOvk(GrpcAPI.OvkDecryptTRC20Parameters request, io.grpc.stub.StreamObserver<Response.DecryptNotesTRC20> responseObserver)` |
    | `default void` | `totalTransaction(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` java-tron return default 0 |
    | `default void` | `triggerConstantContract(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |
    | `default void` | `triggerContract(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` rpc UpdateSetting(UpdateSettingContract) returns (TransactionExtention) {} // consume\_user\_resource\_percent rpc UpdateEnergyLimit(UpdateEnergyLimitContract) returns (TransactionExtention) {} // origin\_energy\_limit rpc ClearContractABI(ClearABIContract) returns (TransactionExtention) {} |
    | `default void` | `withdrawBalance2(Contract.WithdrawBalanceContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |

* + ### Method Detail

    - #### broadcastTransaction

      ```
      default void broadcastTransaction(Chain.Transaction request,
                                        io.grpc.stub.StreamObserver<Response.TransactionReturn> responseObserver)
      ```

      ```
       Transactions:
      ```
    - #### deployContract

      ```
      default void deployContract(Contract.CreateSmartContract request,
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
      default void triggerContract(Contract.TriggerSmartContract request,
                                   io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```

      ```
        rpc UpdateSetting(UpdateSettingContract) returns (TransactionExtention) {}          // consume_user_resource_percent
        rpc UpdateEnergyLimit(UpdateEnergyLimitContract) returns (TransactionExtention) {}  // origin_energy_limit
        rpc ClearContractABI(ClearABIContract) returns (TransactionExtention) {}
      ```
    - #### triggerConstantContract

      ```
      default void triggerConstantContract(Contract.TriggerSmartContract request,
                                           io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```
    - #### estimateEnergy

      ```
      default void estimateEnergy(Contract.TriggerSmartContract request,
                                  io.grpc.stub.StreamObserver<Response.EstimateEnergyMessage> responseObserver)
      ```
    - #### getNodeInfo

      ```
      default void getNodeInfo(GrpcAPI.EmptyMessage request,
                               io.grpc.stub.StreamObserver<Response.NodeInfo> responseObserver)
      ```

      ```
       The real APIs:
      ```
    - #### listNodes

      ```
      default void listNodes(GrpcAPI.EmptyMessage request,
                             io.grpc.stub.StreamObserver<Response.NodeList> responseObserver)
      ```
    - #### getChainParameters

      ```
      default void getChainParameters(GrpcAPI.EmptyMessage request,
                                      io.grpc.stub.StreamObserver<Response.ChainParameters> responseObserver)
      ```
    - #### totalTransaction

      ```
      default void totalTransaction(GrpcAPI.EmptyMessage request,
                                    io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```

      ```
       java-tron return default 0
      ```
    - #### getNextMaintenanceTime

      ```
      default void getNextMaintenanceTime(GrpcAPI.EmptyMessage request,
                                          io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getTransactionSignWeight

      ```
      default void getTransactionSignWeight(Chain.Transaction request,
                                            io.grpc.stub.StreamObserver<Response.TransactionSignWeight> responseObserver)
      ```
    - #### getTransactionApprovedList

      ```
      default void getTransactionApprovedList(Chain.Transaction request,
                                              io.grpc.stub.StreamObserver<Response.TransactionApprovedList> responseObserver)
      ```
    - #### getAccount

      ```
      default void getAccount(GrpcAPI.AccountAddressMessage request,
                              io.grpc.stub.StreamObserver<Response.Account> responseObserver)
      ```

      ```
       FLAW: Although the parameters' type is changed, it is still bad API design.
      ```
    - #### getAccountById

      ```
      default void getAccountById(GrpcAPI.AccountIdMessage request,
                                  io.grpc.stub.StreamObserver<Response.Account> responseObserver)
      ```
    - #### getAccountNet

      ```
      default void getAccountNet(GrpcAPI.AccountAddressMessage request,
                                 io.grpc.stub.StreamObserver<Response.AccountNetMessage> responseObserver)
      ```
    - #### getAccountResource

      ```
      default void getAccountResource(GrpcAPI.AccountAddressMessage request,
                                      io.grpc.stub.StreamObserver<Response.AccountResourceMessage> responseObserver)
      ```
    - #### getAssetIssueByAccount

      ```
      default void getAssetIssueByAccount(GrpcAPI.AccountAddressMessage request,
                                          io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)
      ```
    - #### getAssetIssueByName

      ```
      default void getAssetIssueByName(GrpcAPI.BytesMessage request,
                                       io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)
      ```
    - #### getAssetIssueListByName

      ```
      default void getAssetIssueListByName(GrpcAPI.BytesMessage request,
                                           io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)
      ```
    - #### getAssetIssueById

      ```
      default void getAssetIssueById(GrpcAPI.BytesMessage request,
                                     io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)
      ```
    - #### getAssetIssueList

      ```
      default void getAssetIssueList(GrpcAPI.EmptyMessage request,
                                     io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)
      ```
    - #### getPaginatedAssetIssueList

      ```
      default void getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request,
                                              io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)
      ```
    - #### getBlock

      ```
      default void getBlock(GrpcAPI.BlockReq request,
                            io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)
      ```
    - #### getNowBlock

      ```
      default void getNowBlock(GrpcAPI.EmptyMessage request,
                               io.grpc.stub.StreamObserver<Chain.Block> responseObserver)
      ```
    - #### getNowBlock2

      ```
      default void getNowBlock2(GrpcAPI.EmptyMessage request,
                                io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)
      ```
    - #### getBlockByNum

      ```
      default void getBlockByNum(GrpcAPI.NumberMessage request,
                                 io.grpc.stub.StreamObserver<Chain.Block> responseObserver)
      ```

      ```
      deprecated
      ```
    - #### getBlockByNum2

      ```
      default void getBlockByNum2(GrpcAPI.NumberMessage request,
                                  io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)
      ```

      ```
      Use this function instead of GetBlockByNum.
      ```
    - #### getBlockById

      ```
      default void getBlockById(GrpcAPI.BytesMessage request,
                                io.grpc.stub.StreamObserver<Chain.Block> responseObserver)
      ```

      ```
       NOTE: `GetBlockById2` is missing. The closest is `GetBlockByLatestNum2`.
      ```
    - #### getBlockByLimitNext

      ```
      default void getBlockByLimitNext(GrpcAPI.BlockLimit request,
                                       io.grpc.stub.StreamObserver<Response.BlockList> responseObserver)
      ```
    - #### getBlockByLimitNext2

      ```
      default void getBlockByLimitNext2(GrpcAPI.BlockLimit request,
                                        io.grpc.stub.StreamObserver<Response.BlockListExtention> responseObserver)
      ```
    - #### getBlockByLatestNum

      ```
      default void getBlockByLatestNum(GrpcAPI.NumberMessage request,
                                       io.grpc.stub.StreamObserver<Response.BlockList> responseObserver)
      ```
    - #### getBlockByLatestNum2

      ```
      default void getBlockByLatestNum2(GrpcAPI.NumberMessage request,
                                        io.grpc.stub.StreamObserver<Response.BlockListExtention> responseObserver)
      ```
    - #### getTransactionCountByBlockNum

      ```
      default void getTransactionCountByBlockNum(GrpcAPI.NumberMessage request,
                                                 io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getTransactionById

      ```
      default void getTransactionById(GrpcAPI.BytesMessage request,
                                      io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)
      ```
    - #### getTransactionInfoById

      ```
      default void getTransactionInfoById(GrpcAPI.BytesMessage request,
                                          io.grpc.stub.StreamObserver<Response.TransactionInfo> responseObserver)
      ```
    - #### getTransactionInfoByBlockNum

      ```
      default void getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request,
                                                io.grpc.stub.StreamObserver<Response.TransactionInfoList> responseObserver)
      ```
    - #### getContract

      ```
      default void getContract(GrpcAPI.BytesMessage request,
                               io.grpc.stub.StreamObserver<Common.SmartContract> responseObserver)
      ```
    - #### getContractInfo

      ```
      default void getContractInfo(GrpcAPI.BytesMessage request,
                                   io.grpc.stub.StreamObserver<Response.SmartContractDataWrapper> responseObserver)
      ```

      ```
       FLAW: Abusing of `info`. Should be a `GetContractCode`.
      ```
    - #### listWitnesses

      ```
      default void listWitnesses(GrpcAPI.EmptyMessage request,
                                 io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)
      ```
    - #### getPaginatedNowWitnessList

      ```
      default void getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request,
                                              io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)
      ```
    - #### getBrokerageInfo

      ```
      default void getBrokerageInfo(GrpcAPI.BytesMessage request,
                                    io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getRewardInfo

      ```
      default void getRewardInfo(GrpcAPI.BytesMessage request,
                                 io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getDelegatedResource

      ```
      default void getDelegatedResource(Response.DelegatedResourceMessage request,
                                        io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)
      ```
    - #### getDelegatedResourceAccountIndex

      ```
      default void getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request,
                                                    io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)
      ```
    - #### listProposals

      ```
      default void listProposals(GrpcAPI.EmptyMessage request,
                                 io.grpc.stub.StreamObserver<Response.ProposalList> responseObserver)
      ```
    - #### getProposalById

      ```
      default void getProposalById(GrpcAPI.BytesMessage request,
                                   io.grpc.stub.StreamObserver<Response.Proposal> responseObserver)
      ```
    - #### getPaginatedProposalList

      ```
      default void getPaginatedProposalList(GrpcAPI.PaginatedMessage request,
                                            io.grpc.stub.StreamObserver<Response.ProposalList> responseObserver)
      ```
    - #### listExchanges

      ```
      default void listExchanges(GrpcAPI.EmptyMessage request,
                                 io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)
      ```
    - #### getExchangeById

      ```
      default void getExchangeById(GrpcAPI.BytesMessage request,
                                   io.grpc.stub.StreamObserver<Response.Exchange> responseObserver)
      ```
    - #### getPaginatedExchangeList

      ```
      default void getPaginatedExchangeList(GrpcAPI.PaginatedMessage request,
                                            io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)
      ```
    - #### scanShieldedTRC20NotesByIvk

      ```
      default void scanShieldedTRC20NotesByIvk(GrpcAPI.IvkDecryptTRC20Parameters request,
                                               io.grpc.stub.StreamObserver<Response.DecryptNotesTRC20> responseObserver)
      ```

      ```
       Shielded helpers:
      ```
    - #### scanShieldedTRC20NotesByOvk

      ```
      default void scanShieldedTRC20NotesByOvk(GrpcAPI.OvkDecryptTRC20Parameters request,
                                               io.grpc.stub.StreamObserver<Response.DecryptNotesTRC20> responseObserver)
      ```
    - #### isShieldedTRC20ContractNoteSpent

      ```
      default void isShieldedTRC20ContractNoteSpent(GrpcAPI.NfTRC20Parameters request,
                                                    io.grpc.stub.StreamObserver<Response.NullifierResult> responseObserver)
      ```
    - #### getMarketOrderByAccount

      ```
      default void getMarketOrderByAccount(GrpcAPI.BytesMessage request,
                                           io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)
      ```

      ```
       Market API:
      ```
    - #### getMarketOrderById

      ```
      default void getMarketOrderById(GrpcAPI.BytesMessage request,
                                      io.grpc.stub.StreamObserver<Response.MarketOrder> responseObserver)
      ```
    - #### getMarketPriceByPair

      ```
      default void getMarketPriceByPair(Response.MarketOrderPair request,
                                        io.grpc.stub.StreamObserver<Response.MarketPriceList> responseObserver)
      ```
    - #### getMarketOrderListByPair

      ```
      default void getMarketOrderListByPair(Response.MarketOrderPair request,
                                            io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)
      ```
    - #### getMarketPairList

      ```
      default void getMarketPairList(GrpcAPI.EmptyMessage request,
                                     io.grpc.stub.StreamObserver<Response.MarketOrderPairList> responseObserver)
      ```
    - #### getTransactionSign

      ```
      default void getTransactionSign(Response.TransactionSign request,
                                      io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)
      ```

      ```
       FLAW: Unsafe junk.
      ```
    - #### getTransactionSign2

      ```
      default void getTransactionSign2(Response.TransactionSign request,
                                       io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```
    - #### easyTransferAsset

      ```
      default void easyTransferAsset(GrpcAPI.EasyTransferAssetMessage request,
                                     io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)
      ```
    - #### easyTransferAssetByPrivate

      ```
      default void easyTransferAssetByPrivate(GrpcAPI.EasyTransferAssetByPrivateMessage request,
                                              io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)
      ```
    - #### easyTransfer

      ```
      default void easyTransfer(GrpcAPI.EasyTransferMessage request,
                                io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)
      ```
    - #### easyTransferByPrivate

      ```
      default void easyTransferByPrivate(GrpcAPI.EasyTransferByPrivateMessage request,
                                         io.grpc.stub.StreamObserver<Response.EasyTransferResponse> responseObserver)
      ```
    - #### createAddress

      ```
      default void createAddress(GrpcAPI.BytesMessage request,
                                 io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### generateAddress

      ```
      default void generateAddress(GrpcAPI.EmptyMessage request,
                                   io.grpc.stub.StreamObserver<Response.AddressPrKeyPairMessage> responseObserver)
      ```
    - #### addSign

      ```
      default void addSign(Response.TransactionSign request,
                           io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```
    - #### getSpendingKey

      ```
      default void getSpendingKey(GrpcAPI.EmptyMessage request,
                                  io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```

      ```
       FLAW: Unsafe shielded junk(should be implemented offline).
      ```
    - #### getExpandedSpendingKey

      ```
      default void getExpandedSpendingKey(GrpcAPI.BytesMessage request,
                                          io.grpc.stub.StreamObserver<GrpcAPI.ExpandedSpendingKeyMessage> responseObserver)
      ```
    - #### getAkFromAsk

      ```
      default void getAkFromAsk(GrpcAPI.BytesMessage request,
                                io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### getNkFromNsk

      ```
      default void getNkFromNsk(GrpcAPI.BytesMessage request,
                                io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### getIncomingViewingKey

      ```
      default void getIncomingViewingKey(GrpcAPI.ViewingKeyMessage request,
                                         io.grpc.stub.StreamObserver<GrpcAPI.IncomingViewingKeyMessage> responseObserver)
      ```
    - #### getDiversifier

      ```
      default void getDiversifier(GrpcAPI.EmptyMessage request,
                                  io.grpc.stub.StreamObserver<GrpcAPI.DiversifierMessage> responseObserver)
      ```
    - #### getZenPaymentAddress

      ```
      default void getZenPaymentAddress(GrpcAPI.IncomingViewingKeyDiversifierMessage request,
                                        io.grpc.stub.StreamObserver<GrpcAPI.PaymentAddressMessage> responseObserver)
      ```
    - #### getNewShieldedAddress

      ```
      default void getNewShieldedAddress(GrpcAPI.EmptyMessage request,
                                         io.grpc.stub.StreamObserver<GrpcAPI.ShieldedAddressInfo> responseObserver)
      ```
    - #### getRcm

      ```
      default void getRcm(GrpcAPI.EmptyMessage request,
                          io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### createShieldedContractParameters

      ```
      default void createShieldedContractParameters(GrpcAPI.PrivateShieldedTRC20Parameters request,
                                                    io.grpc.stub.StreamObserver<GrpcAPI.ShieldedTRC20Parameters> responseObserver)
      ```
    - #### createShieldedContractParametersWithoutAsk

      ```
      default void createShieldedContractParametersWithoutAsk(GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk request,
                                                              io.grpc.stub.StreamObserver<GrpcAPI.ShieldedTRC20Parameters> responseObserver)
      ```
    - #### getTriggerInputForShieldedTRC20Contract

      ```
      default void getTriggerInputForShieldedTRC20Contract(GrpcAPI.ShieldedTRC20TriggerContractParameters request,
                                                           io.grpc.stub.StreamObserver<GrpcAPI.BytesMessage> responseObserver)
      ```
    - #### getAvailableUnfreezeCount

      ```
      default void getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request,
                                             io.grpc.stub.StreamObserver<GrpcAPI.GetAvailableUnfreezeCountResponseMessage> responseObserver)
      ```
    - #### getCanWithdrawUnfreezeAmount

      ```
      default void getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request,
                                                io.grpc.stub.StreamObserver<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage> responseObserver)
      ```
    - #### getCanDelegatedMaxSize

      ```
      default void getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request,
                                          io.grpc.stub.StreamObserver<GrpcAPI.CanDelegatedMaxSizeResponseMessage> responseObserver)
      ```
    - #### getDelegatedResourceV2

      ```
      default void getDelegatedResourceV2(Response.DelegatedResourceMessage request,
                                          io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)
      ```
    - #### getDelegatedResourceAccountIndexV2

      ```
      default void getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request,
                                                      io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)
      ```
    - #### getBurnTrx

      ```
      default void getBurnTrx(GrpcAPI.EmptyMessage request,
                              io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```

      ```
      query the network
      ```
    - #### getBlockBalanceTrace

      ```
      default void getBlockBalanceTrace(Response.BlockIdentifier request,
                                        io.grpc.stub.StreamObserver<Response.BlockBalanceTrace> responseObserver)
      ```
    - #### createWitness2

      ```
      default void createWitness2(Contract.WitnessCreateContract request,
                                  io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```

      ```
      voting&SRs
      ```
    - #### withdrawBalance2

      ```
      default void withdrawBalance2(Contract.WithdrawBalanceContract request,
                                    io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
      ```
    - #### getTransactionListFromPending

      ```
      default void getTransactionListFromPending(GrpcAPI.EmptyMessage request,
                                                 io.grpc.stub.StreamObserver<GrpcAPI.TransactionIdList> responseObserver)
      ```

      ```
      pending pool
      ```
    - #### getTransactionFromPending

      ```
      default void getTransactionFromPending(GrpcAPI.BytesMessage request,
                                             io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)
      ```
    - #### getPendingSize

      ```
      default void getPendingSize(GrpcAPI.EmptyMessage request,
                                  io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### getBandwidthPrices

      ```
      default void getBandwidthPrices(GrpcAPI.EmptyMessage request,
                                      io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)
      ```

      ```
      query resource price
      ```
    - #### getEnergyPrices

      ```
      default void getEnergyPrices(GrpcAPI.EmptyMessage request,
                                   io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)
      ```
    - #### getMemoFee

      ```
      default void getMemoFee(GrpcAPI.EmptyMessage request,
                              io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)
      ```