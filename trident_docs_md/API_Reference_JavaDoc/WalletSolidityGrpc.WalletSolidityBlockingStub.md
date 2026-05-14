

org.tron.trident.api

## Class WalletSolidityGrpc.WalletSolidityBlockingStub

* java.lang.Object
* + io.grpc.stub.AbstractStub<S>
  + - io.grpc.stub.AbstractBlockingStub<[WalletSolidityGrpc.WalletSolidityBlockingStub](../../../../org/tron/trident/api/WalletSolidityGrpc.WalletSolidityBlockingStub.html "class in org.tron.trident.api")>
    - * org.tron.trident.api.WalletSolidityGrpc.WalletSolidityBlockingStub

* Enclosing class:
  :   [WalletSolidityGrpc](../../../../org/tron/trident/api/WalletSolidityGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class WalletSolidityGrpc.WalletSolidityBlockingStub
  extends io.grpc.stub.AbstractBlockingStub<WalletSolidityGrpc.WalletSolidityBlockingStub>
  ```

  A stub to allow clients to do synchronous rpc calls to service WalletSolidity.

  ```
   NOTE: All other solidified APIs are useless.
  ```

* + ### Nested Class Summary

    - ### Nested classes/interfaces inherited from class io.grpc.stub.AbstractStub

      `io.grpc.stub.AbstractStub.StubFactory<T extends io.grpc.stub.AbstractStub<T>>`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `protected WalletSolidityGrpc.WalletSolidityBlockingStub` | `build(io.grpc.Channel channel, io.grpc.CallOptions callOptions)` |
    | `Response.EstimateEnergyMessage` | `estimateEnergy(Contract.TriggerSmartContract request)` |
    | `Response.Account` | `getAccount(GrpcAPI.AccountAddressMessage request)` |
    | `Response.Account` | `getAccountById(GrpcAPI.AccountIdMessage request)` |
    | `Contract.AssetIssueContract` | `getAssetIssueById(GrpcAPI.BytesMessage request)` |
    | `Contract.AssetIssueContract` | `getAssetIssueByName(GrpcAPI.BytesMessage request)` |
    | `Response.AssetIssueList` | `getAssetIssueList(GrpcAPI.EmptyMessage request)` |
    | `Response.AssetIssueList` | `getAssetIssueListByName(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage` | `getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request)` |
    | `Response.PricesResponseMessage` | `getBandwidthPrices(GrpcAPI.EmptyMessage request)` query resource price |
    | `Response.BlockExtention` | `getBlock(GrpcAPI.BlockReq request)` |
    | `Chain.Block` | `getBlockByNum(GrpcAPI.NumberMessage request)` |
    | `Response.BlockExtention` | `getBlockByNum2(GrpcAPI.NumberMessage request)` |
    | `GrpcAPI.NumberMessage` | `getBrokerageInfo(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.NumberMessage` | `getBurnTrx(GrpcAPI.EmptyMessage request)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage` | `getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage` | `getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request)` |
    | `Response.DelegatedResourceList` | `getDelegatedResource(Response.DelegatedResourceMessage request)` |
    | `Response.DelegatedResourceAccountIndex` | `getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request)` |
    | `Response.DelegatedResourceAccountIndex` | `getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request)` |
    | `Response.DelegatedResourceList` | `getDelegatedResourceV2(Response.DelegatedResourceMessage request)` |
    | `Response.PricesResponseMessage` | `getEnergyPrices(GrpcAPI.EmptyMessage request)` |
    | `Response.Exchange` | `getExchangeById(GrpcAPI.BytesMessage request)` |
    | `Response.MarketOrderList` | `getMarketOrderByAccount(GrpcAPI.BytesMessage request)` |
    | `Response.MarketOrder` | `getMarketOrderById(GrpcAPI.BytesMessage request)` |
    | `Response.MarketOrderList` | `getMarketOrderListByPair(Response.MarketOrderPair request)` |
    | `Response.MarketOrderPairList` | `getMarketPairList(GrpcAPI.EmptyMessage request)` |
    | `Response.MarketPriceList` | `getMarketPriceByPair(Response.MarketOrderPair request)` |
    | `Chain.Block` | `getNowBlock(GrpcAPI.EmptyMessage request)` |
    | `Response.BlockExtention` | `getNowBlock2(GrpcAPI.EmptyMessage request)` |
    | `Response.AssetIssueList` | `getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request)` |
    | `Response.WitnessList` | `getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request)` |
    | `GrpcAPI.NumberMessage` | `getRewardInfo(GrpcAPI.BytesMessage request)` |
    | `Chain.Transaction` | `getTransactionById(GrpcAPI.BytesMessage request)` |
    | `GrpcAPI.NumberMessage` | `getTransactionCountByBlockNum(GrpcAPI.NumberMessage request)` |
    | `Response.TransactionInfoList` | `getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request)` |
    | `Response.TransactionInfo` | `getTransactionInfoById(GrpcAPI.BytesMessage request)` |
    | `Response.ExchangeList` | `listExchanges(GrpcAPI.EmptyMessage request)` |
    | `Response.WitnessList` | `listWitnesses(GrpcAPI.EmptyMessage request)` |
    | `Response.TransactionExtention` | `triggerConstantContract(Contract.TriggerSmartContract request)` |

    - ### Methods inherited from class io.grpc.stub.AbstractBlockingStub

      `newStub, newStub`
    - ### Methods inherited from class io.grpc.stub.AbstractStub

      `getCallOptions, getChannel, withCallCredentials, withChannel, withCompression, withDeadline, withDeadlineAfter, withDeadlineAfter, withExecutor, withInterceptors, withMaxInboundMessageSize, withMaxOutboundMessageSize, withOnReadyThreshold, withOption, withWaitForReady`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### build

      ```
      protected WalletSolidityGrpc.WalletSolidityBlockingStub build(io.grpc.Channel channel,
                                                                    io.grpc.CallOptions callOptions)
      ```

      Specified by:
      :   `build` in class `io.grpc.stub.AbstractStub<WalletSolidityGrpc.WalletSolidityBlockingStub>`
    - #### getAccount

      ```
      public Response.Account getAccount(GrpcAPI.AccountAddressMessage request)
      ```
    - #### getAccountById

      ```
      public Response.Account getAccountById(GrpcAPI.AccountIdMessage request)
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
    - #### getBlockByNum2

      ```
      public Response.BlockExtention getBlockByNum2(GrpcAPI.NumberMessage request)
      ```
    - #### getTransactionById

      ```
      public Chain.Transaction getTransactionById(GrpcAPI.BytesMessage request)
      ```
    - #### getTransactionInfoByBlockNum

      ```
      public Response.TransactionInfoList getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request)
      ```
    - #### getTransactionInfoById

      ```
      public Response.TransactionInfo getTransactionInfoById(GrpcAPI.BytesMessage request)
      ```
    - #### getTransactionCountByBlockNum

      ```
      public GrpcAPI.NumberMessage getTransactionCountByBlockNum(GrpcAPI.NumberMessage request)
      ```
    - #### estimateEnergy

      ```
      public Response.EstimateEnergyMessage estimateEnergy(Contract.TriggerSmartContract request)
      ```
    - #### triggerConstantContract

      ```
      public Response.TransactionExtention triggerConstantContract(Contract.TriggerSmartContract request)
      ```
    - #### getBrokerageInfo

      ```
      public GrpcAPI.NumberMessage getBrokerageInfo(GrpcAPI.BytesMessage request)
      ```
    - #### getRewardInfo

      ```
      public GrpcAPI.NumberMessage getRewardInfo(GrpcAPI.BytesMessage request)
      ```
    - #### getAssetIssueList

      ```
      public Response.AssetIssueList getAssetIssueList(GrpcAPI.EmptyMessage request)
      ```
    - #### getPaginatedAssetIssueList

      ```
      public Response.AssetIssueList getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request)
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
    - #### getBurnTrx

      ```
      public GrpcAPI.NumberMessage getBurnTrx(GrpcAPI.EmptyMessage request)
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
    - #### listWitnesses

      ```
      public Response.WitnessList listWitnesses(GrpcAPI.EmptyMessage request)
      ```
    - #### getExchangeById

      ```
      public Response.Exchange getExchangeById(GrpcAPI.BytesMessage request)
      ```
    - #### listExchanges

      ```
      public Response.ExchangeList listExchanges(GrpcAPI.EmptyMessage request)
      ```
    - #### getPaginatedNowWitnessList

      ```
      public Response.WitnessList getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request)
      ```
    - #### getMarketOrderById

      ```
      public Response.MarketOrder getMarketOrderById(GrpcAPI.BytesMessage request)
      ```
    - #### getMarketOrderByAccount

      ```
      public Response.MarketOrderList getMarketOrderByAccount(GrpcAPI.BytesMessage request)
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
    - #### getDelegatedResource

      ```
      public Response.DelegatedResourceList getDelegatedResource(Response.DelegatedResourceMessage request)
      ```
    - #### getDelegatedResourceV2

      ```
      public Response.DelegatedResourceList getDelegatedResourceV2(Response.DelegatedResourceMessage request)
      ```
    - #### getDelegatedResourceAccountIndex

      ```
      public Response.DelegatedResourceAccountIndex getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request)
      ```
    - #### getDelegatedResourceAccountIndexV2

      ```
      public Response.DelegatedResourceAccountIndex getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request)
      ```