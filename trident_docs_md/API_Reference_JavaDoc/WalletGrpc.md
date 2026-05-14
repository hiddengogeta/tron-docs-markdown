

org.tron.trident.api

## Class WalletGrpc

* java.lang.Object
* + org.tron.trident.api.WalletGrpc

* ---

    

  ```
  @Generated(value="by gRPC proto compiler (version 1.60.0)",
             comments="Source: api/api.proto")
  public final class WalletGrpc
  extends java.lang.Object
  ```

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static interface` | `WalletGrpc.AsyncService` |
    | `static class` | `WalletGrpc.WalletBlockingStub` A stub to allow clients to do synchronous rpc calls to service Wallet. |
    | `static class` | `WalletGrpc.WalletFutureStub` A stub to allow clients to do ListenableFuture-style rpc calls to service Wallet. |
    | `static class` | `WalletGrpc.WalletImplBase` Base class for the server implementation of the service Wallet. |
    | `static class` | `WalletGrpc.WalletStub` A stub to allow clients to do asynchronous rpc calls to service Wallet. |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static java.lang.String` | `SERVICE_NAME` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static io.grpc.ServerServiceDefinition` | `bindService(WalletGrpc.AsyncService service)` |
    | `static io.grpc.MethodDescriptor<Response.TransactionSign,Response.TransactionExtention>` | `getAddSignMethod()` |
    | `static io.grpc.MethodDescriptor<Chain.Transaction,Response.TransactionReturn>` | `getBroadcastTransactionMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.BytesMessage>` | `getCreateAddressMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.PrivateShieldedTRC20Parameters,GrpcAPI.ShieldedTRC20Parameters>` | `getCreateShieldedContractParametersMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk,GrpcAPI.ShieldedTRC20Parameters>` | `getCreateShieldedContractParametersWithoutAskMethod()` |
    | `static io.grpc.MethodDescriptor<Contract.WitnessCreateContract,Response.TransactionExtention>` | `getCreateWitness2Method()` |
    | `static io.grpc.MethodDescriptor<Contract.CreateSmartContract,Response.TransactionExtention>` | `getDeployContractMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EasyTransferAssetByPrivateMessage,Response.EasyTransferResponse>` | `getEasyTransferAssetByPrivateMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EasyTransferAssetMessage,Response.EasyTransferResponse>` | `getEasyTransferAssetMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EasyTransferByPrivateMessage,Response.EasyTransferResponse>` | `getEasyTransferByPrivateMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EasyTransferMessage,Response.EasyTransferResponse>` | `getEasyTransferMethod()` |
    | `static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.EstimateEnergyMessage>` | `getEstimateEnergyMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.AddressPrKeyPairMessage>` | `getGenerateAddressMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.AccountIdMessage,Response.Account>` | `getGetAccountByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.Account>` | `getGetAccountMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.AccountNetMessage>` | `getGetAccountNetMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.AccountResourceMessage>` | `getGetAccountResourceMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.BytesMessage>` | `getGetAkFromAskMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.AssetIssueList>` | `getGetAssetIssueByAccountMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Contract.AssetIssueContract>` | `getGetAssetIssueByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Contract.AssetIssueContract>` | `getGetAssetIssueByNameMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.AssetIssueList>` | `getGetAssetIssueListByNameMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.AssetIssueList>` | `getGetAssetIssueListMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.GetAvailableUnfreezeCountRequestMessage,GrpcAPI.GetAvailableUnfreezeCountResponseMessage>` | `getGetAvailableUnfreezeCountMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage>` | `getGetBandwidthPricesMethod()` |
    | `static io.grpc.MethodDescriptor<Response.BlockIdentifier,Response.BlockBalanceTrace>` | `getGetBlockBalanceTraceMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Chain.Block>` | `getGetBlockByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.BlockListExtention>` | `getGetBlockByLatestNum2Method()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.BlockList>` | `getGetBlockByLatestNumMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BlockLimit,Response.BlockListExtention>` | `getGetBlockByLimitNext2Method()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BlockLimit,Response.BlockList>` | `getGetBlockByLimitNextMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.BlockExtention>` | `getGetBlockByNum2Method()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Chain.Block>` | `getGetBlockByNumMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BlockReq,Response.BlockExtention>` | `getGetBlockMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.NumberMessage>` | `getGetBrokerageInfoMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage>` | `getGetBurnTrxMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.CanDelegatedMaxSizeRequestMessage,GrpcAPI.CanDelegatedMaxSizeResponseMessage>` | `getGetCanDelegatedMaxSizeMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage,GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage>` | `getGetCanWithdrawUnfreezeAmountMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.ChainParameters>` | `getGetChainParametersMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.SmartContractDataWrapper>` | `getGetContractInfoMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Common.SmartContract>` | `getGetContractMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.DelegatedResourceAccountIndex>` | `getGetDelegatedResourceAccountIndexMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.DelegatedResourceAccountIndex>` | `getGetDelegatedResourceAccountIndexV2Method()` |
    | `static io.grpc.MethodDescriptor<Response.DelegatedResourceMessage,Response.DelegatedResourceList>` | `getGetDelegatedResourceMethod()` |
    | `static io.grpc.MethodDescriptor<Response.DelegatedResourceMessage,Response.DelegatedResourceList>` | `getGetDelegatedResourceV2Method()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.DiversifierMessage>` | `getGetDiversifierMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage>` | `getGetEnergyPricesMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.Exchange>` | `getGetExchangeByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.ExpandedSpendingKeyMessage>` | `getGetExpandedSpendingKeyMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.ViewingKeyMessage,GrpcAPI.IncomingViewingKeyMessage>` | `getGetIncomingViewingKeyMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.MarketOrderList>` | `getGetMarketOrderByAccountMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.MarketOrder>` | `getGetMarketOrderByIdMethod()` |
    | `static io.grpc.MethodDescriptor<Response.MarketOrderPair,Response.MarketOrderList>` | `getGetMarketOrderListByPairMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.MarketOrderPairList>` | `getGetMarketPairListMethod()` |
    | `static io.grpc.MethodDescriptor<Response.MarketOrderPair,Response.MarketPriceList>` | `getGetMarketPriceByPairMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage>` | `getGetMemoFeeMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.ShieldedAddressInfo>` | `getGetNewShieldedAddressMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage>` | `getGetNextMaintenanceTimeMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.BytesMessage>` | `getGetNkFromNskMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.NodeInfo>` | `getGetNodeInfoMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.BlockExtention>` | `getGetNowBlock2Method()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Chain.Block>` | `getGetNowBlockMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.AssetIssueList>` | `getGetPaginatedAssetIssueListMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.ExchangeList>` | `getGetPaginatedExchangeListMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.WitnessList>` | `getGetPaginatedNowWitnessListMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.ProposalList>` | `getGetPaginatedProposalListMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage>` | `getGetPendingSizeMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.Proposal>` | `getGetProposalByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.BytesMessage>` | `getGetRcmMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.NumberMessage>` | `getGetRewardInfoMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.BytesMessage>` | `getGetSpendingKeyMethod()` |
    | `static io.grpc.MethodDescriptor<Chain.Transaction,Response.TransactionApprovedList>` | `getGetTransactionApprovedListMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Chain.Transaction>` | `getGetTransactionByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,GrpcAPI.NumberMessage>` | `getGetTransactionCountByBlockNumMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Chain.Transaction>` | `getGetTransactionFromPendingMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.TransactionInfoList>` | `getGetTransactionInfoByBlockNumMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.TransactionInfo>` | `getGetTransactionInfoByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.TransactionIdList>` | `getGetTransactionListFromPendingMethod()` |
    | `static io.grpc.MethodDescriptor<Response.TransactionSign,Response.TransactionExtention>` | `getGetTransactionSign2Method()` |
    | `static io.grpc.MethodDescriptor<Response.TransactionSign,Chain.Transaction>` | `getGetTransactionSignMethod()` |
    | `static io.grpc.MethodDescriptor<Chain.Transaction,Response.TransactionSignWeight>` | `getGetTransactionSignWeightMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.ShieldedTRC20TriggerContractParameters,GrpcAPI.BytesMessage>` | `getGetTriggerInputForShieldedTRC20ContractMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.IncomingViewingKeyDiversifierMessage,GrpcAPI.PaymentAddressMessage>` | `getGetZenPaymentAddressMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NfTRC20Parameters,Response.NullifierResult>` | `getIsShieldedTRC20ContractNoteSpentMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.ExchangeList>` | `getListExchangesMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.NodeList>` | `getListNodesMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.ProposalList>` | `getListProposalsMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.WitnessList>` | `getListWitnessesMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.IvkDecryptTRC20Parameters,Response.DecryptNotesTRC20>` | `getScanShieldedTRC20NotesByIvkMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.OvkDecryptTRC20Parameters,Response.DecryptNotesTRC20>` | `getScanShieldedTRC20NotesByOvkMethod()` |
    | `static io.grpc.ServiceDescriptor` | `getServiceDescriptor()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage>` | `getTotalTransactionMethod()` |
    | `static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.TransactionExtention>` | `getTriggerConstantContractMethod()` |
    | `static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.TransactionExtention>` | `getTriggerContractMethod()` |
    | `static io.grpc.MethodDescriptor<Contract.WithdrawBalanceContract,Response.TransactionExtention>` | `getWithdrawBalance2Method()` |
    | `static WalletGrpc.WalletBlockingStub` | `newBlockingStub(io.grpc.Channel channel)` Creates a new blocking-style stub that supports unary and streaming output calls on the service |
    | `static WalletGrpc.WalletFutureStub` | `newFutureStub(io.grpc.Channel channel)` Creates a new ListenableFuture-style stub that supports unary calls on the service |
    | `static WalletGrpc.WalletStub` | `newStub(io.grpc.Channel channel)` Creates a new async stub that supports all call types for the service |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### SERVICE\_NAME

      ```
      public static final java.lang.String SERVICE_NAME
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.WalletGrpc.SERVICE_NAME)
  + ### Method Detail

    - #### getBroadcastTransactionMethod

      ```
      public static io.grpc.MethodDescriptor<Chain.Transaction,Response.TransactionReturn> getBroadcastTransactionMethod()
      ```
    - #### getDeployContractMethod

      ```
      public static io.grpc.MethodDescriptor<Contract.CreateSmartContract,Response.TransactionExtention> getDeployContractMethod()
      ```
    - #### getTriggerContractMethod

      ```
      public static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.TransactionExtention> getTriggerContractMethod()
      ```
    - #### getTriggerConstantContractMethod

      ```
      public static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.TransactionExtention> getTriggerConstantContractMethod()
      ```
    - #### getEstimateEnergyMethod

      ```
      public static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.EstimateEnergyMessage> getEstimateEnergyMethod()
      ```
    - #### getGetNodeInfoMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.NodeInfo> getGetNodeInfoMethod()
      ```
    - #### getListNodesMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.NodeList> getListNodesMethod()
      ```
    - #### getGetChainParametersMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.ChainParameters> getGetChainParametersMethod()
      ```
    - #### getTotalTransactionMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage> getTotalTransactionMethod()
      ```
    - #### getGetNextMaintenanceTimeMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage> getGetNextMaintenanceTimeMethod()
      ```
    - #### getGetTransactionSignWeightMethod

      ```
      public static io.grpc.MethodDescriptor<Chain.Transaction,Response.TransactionSignWeight> getGetTransactionSignWeightMethod()
      ```
    - #### getGetTransactionApprovedListMethod

      ```
      public static io.grpc.MethodDescriptor<Chain.Transaction,Response.TransactionApprovedList> getGetTransactionApprovedListMethod()
      ```
    - #### getGetAccountMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.Account> getGetAccountMethod()
      ```
    - #### getGetAccountByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.AccountIdMessage,Response.Account> getGetAccountByIdMethod()
      ```
    - #### getGetAccountNetMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.AccountNetMessage> getGetAccountNetMethod()
      ```
    - #### getGetAccountResourceMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.AccountResourceMessage> getGetAccountResourceMethod()
      ```
    - #### getGetAssetIssueByAccountMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.AssetIssueList> getGetAssetIssueByAccountMethod()
      ```
    - #### getGetAssetIssueByNameMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Contract.AssetIssueContract> getGetAssetIssueByNameMethod()
      ```
    - #### getGetAssetIssueListByNameMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.AssetIssueList> getGetAssetIssueListByNameMethod()
      ```
    - #### getGetAssetIssueByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Contract.AssetIssueContract> getGetAssetIssueByIdMethod()
      ```
    - #### getGetAssetIssueListMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.AssetIssueList> getGetAssetIssueListMethod()
      ```
    - #### getGetPaginatedAssetIssueListMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.AssetIssueList> getGetPaginatedAssetIssueListMethod()
      ```
    - #### getGetBlockMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BlockReq,Response.BlockExtention> getGetBlockMethod()
      ```
    - #### getGetNowBlockMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Chain.Block> getGetNowBlockMethod()
      ```
    - #### getGetNowBlock2Method

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.BlockExtention> getGetNowBlock2Method()
      ```
    - #### getGetBlockByNumMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Chain.Block> getGetBlockByNumMethod()
      ```
    - #### getGetBlockByNum2Method

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.BlockExtention> getGetBlockByNum2Method()
      ```
    - #### getGetBlockByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Chain.Block> getGetBlockByIdMethod()
      ```
    - #### getGetBlockByLimitNextMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BlockLimit,Response.BlockList> getGetBlockByLimitNextMethod()
      ```
    - #### getGetBlockByLimitNext2Method

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BlockLimit,Response.BlockListExtention> getGetBlockByLimitNext2Method()
      ```
    - #### getGetBlockByLatestNumMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.BlockList> getGetBlockByLatestNumMethod()
      ```
    - #### getGetBlockByLatestNum2Method

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.BlockListExtention> getGetBlockByLatestNum2Method()
      ```
    - #### getGetTransactionCountByBlockNumMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,GrpcAPI.NumberMessage> getGetTransactionCountByBlockNumMethod()
      ```
    - #### getGetTransactionByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Chain.Transaction> getGetTransactionByIdMethod()
      ```
    - #### getGetTransactionInfoByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.TransactionInfo> getGetTransactionInfoByIdMethod()
      ```
    - #### getGetTransactionInfoByBlockNumMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.TransactionInfoList> getGetTransactionInfoByBlockNumMethod()
      ```
    - #### getGetContractMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Common.SmartContract> getGetContractMethod()
      ```
    - #### getGetContractInfoMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.SmartContractDataWrapper> getGetContractInfoMethod()
      ```
    - #### getListWitnessesMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.WitnessList> getListWitnessesMethod()
      ```
    - #### getGetPaginatedNowWitnessListMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.WitnessList> getGetPaginatedNowWitnessListMethod()
      ```
    - #### getGetBrokerageInfoMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.NumberMessage> getGetBrokerageInfoMethod()
      ```
    - #### getGetRewardInfoMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.NumberMessage> getGetRewardInfoMethod()
      ```
    - #### getGetDelegatedResourceMethod

      ```
      public static io.grpc.MethodDescriptor<Response.DelegatedResourceMessage,Response.DelegatedResourceList> getGetDelegatedResourceMethod()
      ```
    - #### getGetDelegatedResourceAccountIndexMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.DelegatedResourceAccountIndex> getGetDelegatedResourceAccountIndexMethod()
      ```
    - #### getListProposalsMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.ProposalList> getListProposalsMethod()
      ```
    - #### getGetProposalByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.Proposal> getGetProposalByIdMethod()
      ```
    - #### getGetPaginatedProposalListMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.ProposalList> getGetPaginatedProposalListMethod()
      ```
    - #### getListExchangesMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.ExchangeList> getListExchangesMethod()
      ```
    - #### getGetExchangeByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.Exchange> getGetExchangeByIdMethod()
      ```
    - #### getGetPaginatedExchangeListMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.ExchangeList> getGetPaginatedExchangeListMethod()
      ```
    - #### getScanShieldedTRC20NotesByIvkMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.IvkDecryptTRC20Parameters,Response.DecryptNotesTRC20> getScanShieldedTRC20NotesByIvkMethod()
      ```
    - #### getScanShieldedTRC20NotesByOvkMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.OvkDecryptTRC20Parameters,Response.DecryptNotesTRC20> getScanShieldedTRC20NotesByOvkMethod()
      ```
    - #### getIsShieldedTRC20ContractNoteSpentMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.NfTRC20Parameters,Response.NullifierResult> getIsShieldedTRC20ContractNoteSpentMethod()
      ```
    - #### getGetMarketOrderByAccountMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.MarketOrderList> getGetMarketOrderByAccountMethod()
      ```
    - #### getGetMarketOrderByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.MarketOrder> getGetMarketOrderByIdMethod()
      ```
    - #### getGetMarketPriceByPairMethod

      ```
      public static io.grpc.MethodDescriptor<Response.MarketOrderPair,Response.MarketPriceList> getGetMarketPriceByPairMethod()
      ```
    - #### getGetMarketOrderListByPairMethod

      ```
      public static io.grpc.MethodDescriptor<Response.MarketOrderPair,Response.MarketOrderList> getGetMarketOrderListByPairMethod()
      ```
    - #### getGetMarketPairListMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.MarketOrderPairList> getGetMarketPairListMethod()
      ```
    - #### getGetTransactionSignMethod

      ```
      public static io.grpc.MethodDescriptor<Response.TransactionSign,Chain.Transaction> getGetTransactionSignMethod()
      ```
    - #### getGetTransactionSign2Method

      ```
      public static io.grpc.MethodDescriptor<Response.TransactionSign,Response.TransactionExtention> getGetTransactionSign2Method()
      ```
    - #### getEasyTransferAssetMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EasyTransferAssetMessage,Response.EasyTransferResponse> getEasyTransferAssetMethod()
      ```
    - #### getEasyTransferAssetByPrivateMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EasyTransferAssetByPrivateMessage,Response.EasyTransferResponse> getEasyTransferAssetByPrivateMethod()
      ```
    - #### getEasyTransferMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EasyTransferMessage,Response.EasyTransferResponse> getEasyTransferMethod()
      ```
    - #### getEasyTransferByPrivateMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EasyTransferByPrivateMessage,Response.EasyTransferResponse> getEasyTransferByPrivateMethod()
      ```
    - #### getCreateAddressMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.BytesMessage> getCreateAddressMethod()
      ```
    - #### getGenerateAddressMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.AddressPrKeyPairMessage> getGenerateAddressMethod()
      ```
    - #### getAddSignMethod

      ```
      public static io.grpc.MethodDescriptor<Response.TransactionSign,Response.TransactionExtention> getAddSignMethod()
      ```
    - #### getGetSpendingKeyMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.BytesMessage> getGetSpendingKeyMethod()
      ```
    - #### getGetExpandedSpendingKeyMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.ExpandedSpendingKeyMessage> getGetExpandedSpendingKeyMethod()
      ```
    - #### getGetAkFromAskMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.BytesMessage> getGetAkFromAskMethod()
      ```
    - #### getGetNkFromNskMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.BytesMessage> getGetNkFromNskMethod()
      ```
    - #### getGetIncomingViewingKeyMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.ViewingKeyMessage,GrpcAPI.IncomingViewingKeyMessage> getGetIncomingViewingKeyMethod()
      ```
    - #### getGetDiversifierMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.DiversifierMessage> getGetDiversifierMethod()
      ```
    - #### getGetZenPaymentAddressMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.IncomingViewingKeyDiversifierMessage,GrpcAPI.PaymentAddressMessage> getGetZenPaymentAddressMethod()
      ```
    - #### getGetNewShieldedAddressMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.ShieldedAddressInfo> getGetNewShieldedAddressMethod()
      ```
    - #### getGetRcmMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.BytesMessage> getGetRcmMethod()
      ```
    - #### getCreateShieldedContractParametersMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.PrivateShieldedTRC20Parameters,GrpcAPI.ShieldedTRC20Parameters> getCreateShieldedContractParametersMethod()
      ```
    - #### getCreateShieldedContractParametersWithoutAskMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk,GrpcAPI.ShieldedTRC20Parameters> getCreateShieldedContractParametersWithoutAskMethod()
      ```
    - #### getGetTriggerInputForShieldedTRC20ContractMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.ShieldedTRC20TriggerContractParameters,GrpcAPI.BytesMessage> getGetTriggerInputForShieldedTRC20ContractMethod()
      ```
    - #### getGetAvailableUnfreezeCountMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.GetAvailableUnfreezeCountRequestMessage,GrpcAPI.GetAvailableUnfreezeCountResponseMessage> getGetAvailableUnfreezeCountMethod()
      ```
    - #### getGetCanWithdrawUnfreezeAmountMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage,GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage> getGetCanWithdrawUnfreezeAmountMethod()
      ```
    - #### getGetCanDelegatedMaxSizeMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.CanDelegatedMaxSizeRequestMessage,GrpcAPI.CanDelegatedMaxSizeResponseMessage> getGetCanDelegatedMaxSizeMethod()
      ```
    - #### getGetDelegatedResourceV2Method

      ```
      public static io.grpc.MethodDescriptor<Response.DelegatedResourceMessage,Response.DelegatedResourceList> getGetDelegatedResourceV2Method()
      ```
    - #### getGetDelegatedResourceAccountIndexV2Method

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.DelegatedResourceAccountIndex> getGetDelegatedResourceAccountIndexV2Method()
      ```
    - #### getGetBurnTrxMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage> getGetBurnTrxMethod()
      ```
    - #### getGetBlockBalanceTraceMethod

      ```
      public static io.grpc.MethodDescriptor<Response.BlockIdentifier,Response.BlockBalanceTrace> getGetBlockBalanceTraceMethod()
      ```
    - #### getCreateWitness2Method

      ```
      public static io.grpc.MethodDescriptor<Contract.WitnessCreateContract,Response.TransactionExtention> getCreateWitness2Method()
      ```
    - #### getWithdrawBalance2Method

      ```
      public static io.grpc.MethodDescriptor<Contract.WithdrawBalanceContract,Response.TransactionExtention> getWithdrawBalance2Method()
      ```
    - #### getGetTransactionListFromPendingMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.TransactionIdList> getGetTransactionListFromPendingMethod()
      ```
    - #### getGetTransactionFromPendingMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Chain.Transaction> getGetTransactionFromPendingMethod()
      ```
    - #### getGetPendingSizeMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage> getGetPendingSizeMethod()
      ```
    - #### getGetBandwidthPricesMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage> getGetBandwidthPricesMethod()
      ```
    - #### getGetEnergyPricesMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage> getGetEnergyPricesMethod()
      ```
    - #### getGetMemoFeeMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage> getGetMemoFeeMethod()
      ```
    - #### newStub

      ```
      public static WalletGrpc.WalletStub newStub(io.grpc.Channel channel)
      ```

      Creates a new async stub that supports all call types for the service
    - #### newBlockingStub

      ```
      public static WalletGrpc.WalletBlockingStub newBlockingStub(io.grpc.Channel channel)
      ```

      Creates a new blocking-style stub that supports unary and streaming output calls on the service
    - #### newFutureStub

      ```
      public static WalletGrpc.WalletFutureStub newFutureStub(io.grpc.Channel channel)
      ```

      Creates a new ListenableFuture-style stub that supports unary calls on the service
    - #### bindService

      ```
      public static final io.grpc.ServerServiceDefinition bindService(WalletGrpc.AsyncService service)
      ```
    - #### getServiceDescriptor

      ```
      public static io.grpc.ServiceDescriptor getServiceDescriptor()
      ```