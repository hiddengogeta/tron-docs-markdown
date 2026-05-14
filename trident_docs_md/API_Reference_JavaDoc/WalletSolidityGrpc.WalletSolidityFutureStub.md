

org.tron.trident.api

## Class WalletSolidityGrpc.WalletSolidityFutureStub

* java.lang.Object
* + io.grpc.stub.AbstractStub<S>
  + - io.grpc.stub.AbstractFutureStub<[WalletSolidityGrpc.WalletSolidityFutureStub](../../../../org/tron/trident/api/WalletSolidityGrpc.WalletSolidityFutureStub.html "class in org.tron.trident.api")>
    - * org.tron.trident.api.WalletSolidityGrpc.WalletSolidityFutureStub

* Enclosing class:
  :   [WalletSolidityGrpc](../../../../org/tron/trident/api/WalletSolidityGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class WalletSolidityGrpc.WalletSolidityFutureStub
  extends io.grpc.stub.AbstractFutureStub<WalletSolidityGrpc.WalletSolidityFutureStub>
  ```

  A stub to allow clients to do ListenableFuture-style rpc calls to service WalletSolidity.

  ```
   NOTE: All other solidified APIs are useless.
  ```

* + ### Nested Class Summary

    - ### Nested classes/interfaces inherited from class io.grpc.stub.AbstractStub

      `io.grpc.stub.AbstractStub.StubFactory<T extends io.grpc.stub.AbstractStub<T>>`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `protected WalletSolidityGrpc.WalletSolidityFutureStub` | `build(io.grpc.Channel channel, io.grpc.CallOptions callOptions)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.EstimateEnergyMessage>` | `estimateEnergy(Contract.TriggerSmartContract request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.Account>` | `getAccount(GrpcAPI.AccountAddressMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.Account>` | `getAccountById(GrpcAPI.AccountIdMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Contract.AssetIssueContract>` | `getAssetIssueById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Contract.AssetIssueContract>` | `getAssetIssueByName(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList>` | `getAssetIssueList(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList>` | `getAssetIssueListByName(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.GetAvailableUnfreezeCountResponseMessage>` | `getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.PricesResponseMessage>` | `getBandwidthPrices(GrpcAPI.EmptyMessage request)` query resource price |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention>` | `getBlock(GrpcAPI.BlockReq request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Chain.Block>` | `getBlockByNum(GrpcAPI.NumberMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention>` | `getBlockByNum2(GrpcAPI.NumberMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getBrokerageInfo(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getBurnTrx(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.CanDelegatedMaxSizeResponseMessage>` | `getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage>` | `getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceList>` | `getDelegatedResource(Response.DelegatedResourceMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceAccountIndex>` | `getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceAccountIndex>` | `getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceList>` | `getDelegatedResourceV2(Response.DelegatedResourceMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.PricesResponseMessage>` | `getEnergyPrices(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.Exchange>` | `getExchangeById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderList>` | `getMarketOrderByAccount(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketOrder>` | `getMarketOrderById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderList>` | `getMarketOrderListByPair(Response.MarketOrderPair request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderPairList>` | `getMarketPairList(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.MarketPriceList>` | `getMarketPriceByPair(Response.MarketOrderPair request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Chain.Block>` | `getNowBlock(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention>` | `getNowBlock2(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList>` | `getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.WitnessList>` | `getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getRewardInfo(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Chain.Transaction>` | `getTransactionById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage>` | `getTransactionCountByBlockNum(GrpcAPI.NumberMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionInfoList>` | `getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionInfo>` | `getTransactionInfoById(GrpcAPI.BytesMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.ExchangeList>` | `listExchanges(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.WitnessList>` | `listWitnesses(GrpcAPI.EmptyMessage request)` |
    | `com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention>` | `triggerConstantContract(Contract.TriggerSmartContract request)` |

    - ### Methods inherited from class io.grpc.stub.AbstractFutureStub

      `newStub, newStub`
    - ### Methods inherited from class io.grpc.stub.AbstractStub

      `getCallOptions, getChannel, withCallCredentials, withChannel, withCompression, withDeadline, withDeadlineAfter, withDeadlineAfter, withExecutor, withInterceptors, withMaxInboundMessageSize, withMaxOutboundMessageSize, withOnReadyThreshold, withOption, withWaitForReady`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### build

      ```
      protected WalletSolidityGrpc.WalletSolidityFutureStub build(io.grpc.Channel channel,
                                                                  io.grpc.CallOptions callOptions)
      ```

      Specified by:
      :   `build` in class `io.grpc.stub.AbstractStub<WalletSolidityGrpc.WalletSolidityFutureStub>`
    - #### getAccount

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.Account> getAccount(GrpcAPI.AccountAddressMessage request)
      ```
    - #### getAccountById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.Account> getAccountById(GrpcAPI.AccountIdMessage request)
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
    - #### getBlockByNum2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.BlockExtention> getBlockByNum2(GrpcAPI.NumberMessage request)
      ```
    - #### getTransactionById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Chain.Transaction> getTransactionById(GrpcAPI.BytesMessage request)
      ```
    - #### getTransactionInfoByBlockNum

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionInfoList> getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request)
      ```
    - #### getTransactionInfoById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionInfo> getTransactionInfoById(GrpcAPI.BytesMessage request)
      ```
    - #### getTransactionCountByBlockNum

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getTransactionCountByBlockNum(GrpcAPI.NumberMessage request)
      ```
    - #### estimateEnergy

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.EstimateEnergyMessage> estimateEnergy(Contract.TriggerSmartContract request)
      ```
    - #### triggerConstantContract

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.TransactionExtention> triggerConstantContract(Contract.TriggerSmartContract request)
      ```
    - #### getBrokerageInfo

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getBrokerageInfo(GrpcAPI.BytesMessage request)
      ```
    - #### getRewardInfo

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getRewardInfo(GrpcAPI.BytesMessage request)
      ```
    - #### getAssetIssueList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList> getAssetIssueList(GrpcAPI.EmptyMessage request)
      ```
    - #### getPaginatedAssetIssueList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.AssetIssueList> getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request)
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
    - #### getBurnTrx

      ```
      public com.google.common.util.concurrent.ListenableFuture<GrpcAPI.NumberMessage> getBurnTrx(GrpcAPI.EmptyMessage request)
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
    - #### listWitnesses

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.WitnessList> listWitnesses(GrpcAPI.EmptyMessage request)
      ```
    - #### getExchangeById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.Exchange> getExchangeById(GrpcAPI.BytesMessage request)
      ```
    - #### listExchanges

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.ExchangeList> listExchanges(GrpcAPI.EmptyMessage request)
      ```
    - #### getPaginatedNowWitnessList

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.WitnessList> getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request)
      ```
    - #### getMarketOrderById

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.MarketOrder> getMarketOrderById(GrpcAPI.BytesMessage request)
      ```
    - #### getMarketOrderByAccount

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.MarketOrderList> getMarketOrderByAccount(GrpcAPI.BytesMessage request)
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
    - #### getDelegatedResource

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceList> getDelegatedResource(Response.DelegatedResourceMessage request)
      ```
    - #### getDelegatedResourceV2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceList> getDelegatedResourceV2(Response.DelegatedResourceMessage request)
      ```
    - #### getDelegatedResourceAccountIndex

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceAccountIndex> getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request)
      ```
    - #### getDelegatedResourceAccountIndexV2

      ```
      public com.google.common.util.concurrent.ListenableFuture<Response.DelegatedResourceAccountIndex> getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request)
      ```