

org.tron.trident.api

## Class WalletSolidityGrpc.WalletSolidityStub

* java.lang.Object
* + io.grpc.stub.AbstractStub<S>
  + - io.grpc.stub.AbstractAsyncStub<[WalletSolidityGrpc.WalletSolidityStub](../../../../org/tron/trident/api/WalletSolidityGrpc.WalletSolidityStub.html "class in org.tron.trident.api")>
    - * org.tron.trident.api.WalletSolidityGrpc.WalletSolidityStub

* Enclosing class:
  :   [WalletSolidityGrpc](../../../../org/tron/trident/api/WalletSolidityGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class WalletSolidityGrpc.WalletSolidityStub
  extends io.grpc.stub.AbstractAsyncStub<WalletSolidityGrpc.WalletSolidityStub>
  ```

  A stub to allow clients to do asynchronous rpc calls to service WalletSolidity.

  ```
   NOTE: All other solidified APIs are useless.
  ```

* + ### Nested Class Summary

    - ### Nested classes/interfaces inherited from class io.grpc.stub.AbstractStub

      `io.grpc.stub.AbstractStub.StubFactory<T extends io.grpc.stub.AbstractStub<T>>`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `protected WalletSolidityGrpc.WalletSolidityStub` | `build(io.grpc.Channel channel, io.grpc.CallOptions callOptions)` |
    | `void` | `estimateEnergy(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.EstimateEnergyMessage> responseObserver)` |
    | `void` | `getAccount(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.Account> responseObserver)` |
    | `void` | `getAccountById(GrpcAPI.AccountIdMessage request, io.grpc.stub.StreamObserver<Response.Account> responseObserver)` |
    | `void` | `getAssetIssueById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)` |
    | `void` | `getAssetIssueByName(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)` |
    | `void` | `getAssetIssueList(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `void` | `getAssetIssueListByName(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `void` | `getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.GetAvailableUnfreezeCountResponseMessage> responseObserver)` |
    | `void` | `getBandwidthPrices(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` query resource price |
    | `void` | `getBlock(GrpcAPI.BlockReq request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `void` | `getBlockByNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` |
    | `void` | `getBlockByNum2(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `void` | `getBrokerageInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `void` | `getBurnTrx(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `void` | `getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.CanDelegatedMaxSizeResponseMessage> responseObserver)` |
    | `void` | `getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage> responseObserver)` |
    | `void` | `getDelegatedResource(Response.DelegatedResourceMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)` |
    | `void` | `getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)` |
    | `void` | `getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)` |
    | `void` | `getDelegatedResourceV2(Response.DelegatedResourceMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)` |
    | `void` | `getEnergyPrices(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` |
    | `void` | `getExchangeById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.Exchange> responseObserver)` |
    | `void` | `getMarketOrderByAccount(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)` |
    | `void` | `getMarketOrderById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.MarketOrder> responseObserver)` |
    | `void` | `getMarketOrderListByPair(Response.MarketOrderPair request, io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)` |
    | `void` | `getMarketPairList(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.MarketOrderPairList> responseObserver)` |
    | `void` | `getMarketPriceByPair(Response.MarketOrderPair request, io.grpc.stub.StreamObserver<Response.MarketPriceList> responseObserver)` |
    | `void` | `getNowBlock(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` |
    | `void` | `getNowBlock2(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `void` | `getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `void` | `getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)` |
    | `void` | `getRewardInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `void` | `getTransactionById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)` |
    | `void` | `getTransactionCountByBlockNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `void` | `getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.TransactionInfoList> responseObserver)` |
    | `void` | `getTransactionInfoById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.TransactionInfo> responseObserver)` |
    | `void` | `listExchanges(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)` |
    | `void` | `listWitnesses(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)` |
    | `void` | `triggerConstantContract(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |

    - ### Methods inherited from class io.grpc.stub.AbstractAsyncStub

      `newStub, newStub`
    - ### Methods inherited from class io.grpc.stub.AbstractStub

      `getCallOptions, getChannel, withCallCredentials, withChannel, withCompression, withDeadline, withDeadlineAfter, withDeadlineAfter, withExecutor, withInterceptors, withMaxInboundMessageSize, withMaxOutboundMessageSize, withOnReadyThreshold, withOption, withWaitForReady`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### build

      ```
      protected WalletSolidityGrpc.WalletSolidityStub build(io.grpc.Channel channel,
                                                            io.grpc.CallOptions callOptions)
      ```

      Specified by:
      :   `build` in class `io.grpc.stub.AbstractStub<WalletSolidityGrpc.WalletSolidityStub>`
    - #### getAccount

      ```
      public void getAccount(GrpcAPI.AccountAddressMessage request,
                             io.grpc.stub.StreamObserver<Response.Account> responseObserver)
      ```
    - #### getAccountById

      ```
      public void getAccountById(GrpcAPI.AccountIdMessage request,
                                 io.grpc.stub.StreamObserver<Response.Account> responseObserver)
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
    - #### getBlockByNum2

      ```
      public void getBlockByNum2(GrpcAPI.NumberMessage request,
                                 io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)
      ```
    - #### getTransactionById

      ```
      public void getTransactionById(GrpcAPI.BytesMessage request,
                                     io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)
      ```
    - #### getTransactionInfoByBlockNum

      ```
      public void getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request,
                                               io.grpc.stub.StreamObserver<Response.TransactionInfoList> responseObserver)
      ```
    - #### getTransactionInfoById

      ```
      public void getTransactionInfoById(GrpcAPI.BytesMessage request,
                                         io.grpc.stub.StreamObserver<Response.TransactionInfo> responseObserver)
      ```
    - #### getTransactionCountByBlockNum

      ```
      public void getTransactionCountByBlockNum(GrpcAPI.NumberMessage request,
                                                io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### estimateEnergy

      ```
      public void estimateEnergy(Contract.TriggerSmartContract request,
                                 io.grpc.stub.StreamObserver<Response.EstimateEnergyMessage> responseObserver)
      ```
    - #### triggerConstantContract

      ```
      public void triggerConstantContract(Contract.TriggerSmartContract request,
                                          io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
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
    - #### getBurnTrx

      ```
      public void getBurnTrx(GrpcAPI.EmptyMessage request,
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
    - #### listWitnesses

      ```
      public void listWitnesses(GrpcAPI.EmptyMessage request,
                                io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)
      ```
    - #### getExchangeById

      ```
      public void getExchangeById(GrpcAPI.BytesMessage request,
                                  io.grpc.stub.StreamObserver<Response.Exchange> responseObserver)
      ```
    - #### listExchanges

      ```
      public void listExchanges(GrpcAPI.EmptyMessage request,
                                io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)
      ```
    - #### getPaginatedNowWitnessList

      ```
      public void getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request,
                                             io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)
      ```
    - #### getMarketOrderById

      ```
      public void getMarketOrderById(GrpcAPI.BytesMessage request,
                                     io.grpc.stub.StreamObserver<Response.MarketOrder> responseObserver)
      ```
    - #### getMarketOrderByAccount

      ```
      public void getMarketOrderByAccount(GrpcAPI.BytesMessage request,
                                          io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)
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
    - #### getDelegatedResource

      ```
      public void getDelegatedResource(Response.DelegatedResourceMessage request,
                                       io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)
      ```
    - #### getDelegatedResourceV2

      ```
      public void getDelegatedResourceV2(Response.DelegatedResourceMessage request,
                                         io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)
      ```
    - #### getDelegatedResourceAccountIndex

      ```
      public void getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request,
                                                   io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)
      ```
    - #### getDelegatedResourceAccountIndexV2

      ```
      public void getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request,
                                                     io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)
      ```