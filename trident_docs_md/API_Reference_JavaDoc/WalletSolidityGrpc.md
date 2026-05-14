

org.tron.trident.api

## Class WalletSolidityGrpc

* java.lang.Object
* + org.tron.trident.api.WalletSolidityGrpc

* ---

    

  ```
  @Generated(value="by gRPC proto compiler (version 1.60.0)",
             comments="Source: api/api.proto")
  public final class WalletSolidityGrpc
  extends java.lang.Object
  ```

  ```
   NOTE: All other solidified APIs are useless.
  ```

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static interface` | `WalletSolidityGrpc.AsyncService` NOTE: All other solidified APIs are useless. |
    | `static class` | `WalletSolidityGrpc.WalletSolidityBlockingStub` A stub to allow clients to do synchronous rpc calls to service WalletSolidity. |
    | `static class` | `WalletSolidityGrpc.WalletSolidityFutureStub` A stub to allow clients to do ListenableFuture-style rpc calls to service WalletSolidity. |
    | `static class` | `WalletSolidityGrpc.WalletSolidityImplBase` Base class for the server implementation of the service WalletSolidity. |
    | `static class` | `WalletSolidityGrpc.WalletSolidityStub` A stub to allow clients to do asynchronous rpc calls to service WalletSolidity. |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static java.lang.String` | `SERVICE_NAME` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static io.grpc.ServerServiceDefinition` | `bindService(WalletSolidityGrpc.AsyncService service)` |
    | `static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.EstimateEnergyMessage>` | `getEstimateEnergyMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.AccountIdMessage,Response.Account>` | `getGetAccountByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.Account>` | `getGetAccountMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Contract.AssetIssueContract>` | `getGetAssetIssueByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Contract.AssetIssueContract>` | `getGetAssetIssueByNameMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.AssetIssueList>` | `getGetAssetIssueListByNameMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.AssetIssueList>` | `getGetAssetIssueListMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.GetAvailableUnfreezeCountRequestMessage,GrpcAPI.GetAvailableUnfreezeCountResponseMessage>` | `getGetAvailableUnfreezeCountMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage>` | `getGetBandwidthPricesMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.BlockExtention>` | `getGetBlockByNum2Method()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Chain.Block>` | `getGetBlockByNumMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BlockReq,Response.BlockExtention>` | `getGetBlockMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.NumberMessage>` | `getGetBrokerageInfoMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage>` | `getGetBurnTrxMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.CanDelegatedMaxSizeRequestMessage,GrpcAPI.CanDelegatedMaxSizeResponseMessage>` | `getGetCanDelegatedMaxSizeMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage,GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage>` | `getGetCanWithdrawUnfreezeAmountMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.DelegatedResourceAccountIndex>` | `getGetDelegatedResourceAccountIndexMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.DelegatedResourceAccountIndex>` | `getGetDelegatedResourceAccountIndexV2Method()` |
    | `static io.grpc.MethodDescriptor<Response.DelegatedResourceMessage,Response.DelegatedResourceList>` | `getGetDelegatedResourceMethod()` |
    | `static io.grpc.MethodDescriptor<Response.DelegatedResourceMessage,Response.DelegatedResourceList>` | `getGetDelegatedResourceV2Method()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage>` | `getGetEnergyPricesMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.Exchange>` | `getGetExchangeByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.MarketOrderList>` | `getGetMarketOrderByAccountMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.MarketOrder>` | `getGetMarketOrderByIdMethod()` |
    | `static io.grpc.MethodDescriptor<Response.MarketOrderPair,Response.MarketOrderList>` | `getGetMarketOrderListByPairMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.MarketOrderPairList>` | `getGetMarketPairListMethod()` |
    | `static io.grpc.MethodDescriptor<Response.MarketOrderPair,Response.MarketPriceList>` | `getGetMarketPriceByPairMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.BlockExtention>` | `getGetNowBlock2Method()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Chain.Block>` | `getGetNowBlockMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.AssetIssueList>` | `getGetPaginatedAssetIssueListMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.WitnessList>` | `getGetPaginatedNowWitnessListMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.NumberMessage>` | `getGetRewardInfoMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Chain.Transaction>` | `getGetTransactionByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,GrpcAPI.NumberMessage>` | `getGetTransactionCountByBlockNumMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.TransactionInfoList>` | `getGetTransactionInfoByBlockNumMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.TransactionInfo>` | `getGetTransactionInfoByIdMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.ExchangeList>` | `getListExchangesMethod()` |
    | `static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.WitnessList>` | `getListWitnessesMethod()` |
    | `static io.grpc.ServiceDescriptor` | `getServiceDescriptor()` |
    | `static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.TransactionExtention>` | `getTriggerConstantContractMethod()` |
    | `static WalletSolidityGrpc.WalletSolidityBlockingStub` | `newBlockingStub(io.grpc.Channel channel)` Creates a new blocking-style stub that supports unary and streaming output calls on the service |
    | `static WalletSolidityGrpc.WalletSolidityFutureStub` | `newFutureStub(io.grpc.Channel channel)` Creates a new ListenableFuture-style stub that supports unary calls on the service |
    | `static WalletSolidityGrpc.WalletSolidityStub` | `newStub(io.grpc.Channel channel)` Creates a new async stub that supports all call types for the service |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### SERVICE\_NAME

      ```
      public static final java.lang.String SERVICE_NAME
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.WalletSolidityGrpc.SERVICE_NAME)
  + ### Method Detail

    - #### getGetAccountMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.AccountAddressMessage,Response.Account> getGetAccountMethod()
      ```
    - #### getGetAccountByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.AccountIdMessage,Response.Account> getGetAccountByIdMethod()
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
    - #### getGetTransactionByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Chain.Transaction> getGetTransactionByIdMethod()
      ```
    - #### getGetTransactionInfoByBlockNumMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,Response.TransactionInfoList> getGetTransactionInfoByBlockNumMethod()
      ```
    - #### getGetTransactionInfoByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.TransactionInfo> getGetTransactionInfoByIdMethod()
      ```
    - #### getGetTransactionCountByBlockNumMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.NumberMessage,GrpcAPI.NumberMessage> getGetTransactionCountByBlockNumMethod()
      ```
    - #### getEstimateEnergyMethod

      ```
      public static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.EstimateEnergyMessage> getEstimateEnergyMethod()
      ```
    - #### getTriggerConstantContractMethod

      ```
      public static io.grpc.MethodDescriptor<Contract.TriggerSmartContract,Response.TransactionExtention> getTriggerConstantContractMethod()
      ```
    - #### getGetBrokerageInfoMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.NumberMessage> getGetBrokerageInfoMethod()
      ```
    - #### getGetRewardInfoMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,GrpcAPI.NumberMessage> getGetRewardInfoMethod()
      ```
    - #### getGetAssetIssueListMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.AssetIssueList> getGetAssetIssueListMethod()
      ```
    - #### getGetPaginatedAssetIssueListMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.AssetIssueList> getGetPaginatedAssetIssueListMethod()
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
    - #### getGetBurnTrxMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,GrpcAPI.NumberMessage> getGetBurnTrxMethod()
      ```
    - #### getGetBandwidthPricesMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage> getGetBandwidthPricesMethod()
      ```
    - #### getGetEnergyPricesMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.PricesResponseMessage> getGetEnergyPricesMethod()
      ```
    - #### getListWitnessesMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.WitnessList> getListWitnessesMethod()
      ```
    - #### getGetExchangeByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.Exchange> getGetExchangeByIdMethod()
      ```
    - #### getListExchangesMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.EmptyMessage,Response.ExchangeList> getListExchangesMethod()
      ```
    - #### getGetPaginatedNowWitnessListMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.PaginatedMessage,Response.WitnessList> getGetPaginatedNowWitnessListMethod()
      ```
    - #### getGetMarketOrderByIdMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.MarketOrder> getGetMarketOrderByIdMethod()
      ```
    - #### getGetMarketOrderByAccountMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.MarketOrderList> getGetMarketOrderByAccountMethod()
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
    - #### getGetDelegatedResourceMethod

      ```
      public static io.grpc.MethodDescriptor<Response.DelegatedResourceMessage,Response.DelegatedResourceList> getGetDelegatedResourceMethod()
      ```
    - #### getGetDelegatedResourceV2Method

      ```
      public static io.grpc.MethodDescriptor<Response.DelegatedResourceMessage,Response.DelegatedResourceList> getGetDelegatedResourceV2Method()
      ```
    - #### getGetDelegatedResourceAccountIndexMethod

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.DelegatedResourceAccountIndex> getGetDelegatedResourceAccountIndexMethod()
      ```
    - #### getGetDelegatedResourceAccountIndexV2Method

      ```
      public static io.grpc.MethodDescriptor<GrpcAPI.BytesMessage,Response.DelegatedResourceAccountIndex> getGetDelegatedResourceAccountIndexV2Method()
      ```
    - #### newStub

      ```
      public static WalletSolidityGrpc.WalletSolidityStub newStub(io.grpc.Channel channel)
      ```

      Creates a new async stub that supports all call types for the service
    - #### newBlockingStub

      ```
      public static WalletSolidityGrpc.WalletSolidityBlockingStub newBlockingStub(io.grpc.Channel channel)
      ```

      Creates a new blocking-style stub that supports unary and streaming output calls on the service
    - #### newFutureStub

      ```
      public static WalletSolidityGrpc.WalletSolidityFutureStub newFutureStub(io.grpc.Channel channel)
      ```

      Creates a new ListenableFuture-style stub that supports unary calls on the service
    - #### bindService

      ```
      public static final io.grpc.ServerServiceDefinition bindService(WalletSolidityGrpc.AsyncService service)
      ```
    - #### getServiceDescriptor

      ```
      public static io.grpc.ServiceDescriptor getServiceDescriptor()
      ```