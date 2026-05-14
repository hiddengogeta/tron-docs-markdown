

org.tron.trident.api

## Interface WalletSolidityGrpc.AsyncService

* All Known Implementing Classes:
  :   [WalletSolidityGrpc.WalletSolidityImplBase](../../../../org/tron/trident/api/WalletSolidityGrpc.WalletSolidityImplBase.html "class in org.tron.trident.api")

  Enclosing class:
  :   [WalletSolidityGrpc](../../../../org/tron/trident/api/WalletSolidityGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface WalletSolidityGrpc.AsyncService
  ```

  ```
   NOTE: All other solidified APIs are useless.
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);)

    | Modifier and Type | Method and Description |
    | `default void` | `estimateEnergy(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.EstimateEnergyMessage> responseObserver)` |
    | `default void` | `getAccount(GrpcAPI.AccountAddressMessage request, io.grpc.stub.StreamObserver<Response.Account> responseObserver)` |
    | `default void` | `getAccountById(GrpcAPI.AccountIdMessage request, io.grpc.stub.StreamObserver<Response.Account> responseObserver)` |
    | `default void` | `getAssetIssueById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)` |
    | `default void` | `getAssetIssueByName(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Contract.AssetIssueContract> responseObserver)` |
    | `default void` | `getAssetIssueList(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `default void` | `getAssetIssueListByName(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `default void` | `getAvailableUnfreezeCount(GrpcAPI.GetAvailableUnfreezeCountRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.GetAvailableUnfreezeCountResponseMessage> responseObserver)` |
    | `default void` | `getBandwidthPrices(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` query resource price |
    | `default void` | `getBlock(GrpcAPI.BlockReq request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `default void` | `getBlockByNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` |
    | `default void` | `getBlockByNum2(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `default void` | `getBrokerageInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `default void` | `getBurnTrx(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `default void` | `getCanDelegatedMaxSize(GrpcAPI.CanDelegatedMaxSizeRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.CanDelegatedMaxSizeResponseMessage> responseObserver)` |
    | `default void` | `getCanWithdrawUnfreezeAmount(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage request, io.grpc.stub.StreamObserver<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage> responseObserver)` |
    | `default void` | `getDelegatedResource(Response.DelegatedResourceMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)` |
    | `default void` | `getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)` |
    | `default void` | `getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)` |
    | `default void` | `getDelegatedResourceV2(Response.DelegatedResourceMessage request, io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)` |
    | `default void` | `getEnergyPrices(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.PricesResponseMessage> responseObserver)` |
    | `default void` | `getExchangeById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.Exchange> responseObserver)` |
    | `default void` | `getMarketOrderByAccount(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)` |
    | `default void` | `getMarketOrderById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.MarketOrder> responseObserver)` |
    | `default void` | `getMarketOrderListByPair(Response.MarketOrderPair request, io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)` |
    | `default void` | `getMarketPairList(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.MarketOrderPairList> responseObserver)` |
    | `default void` | `getMarketPriceByPair(Response.MarketOrderPair request, io.grpc.stub.StreamObserver<Response.MarketPriceList> responseObserver)` |
    | `default void` | `getNowBlock(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Chain.Block> responseObserver)` |
    | `default void` | `getNowBlock2(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)` |
    | `default void` | `getPaginatedAssetIssueList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.AssetIssueList> responseObserver)` |
    | `default void` | `getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request, io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)` |
    | `default void` | `getRewardInfo(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `default void` | `getTransactionById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)` |
    | `default void` | `getTransactionCountByBlockNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)` |
    | `default void` | `getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request, io.grpc.stub.StreamObserver<Response.TransactionInfoList> responseObserver)` |
    | `default void` | `getTransactionInfoById(GrpcAPI.BytesMessage request, io.grpc.stub.StreamObserver<Response.TransactionInfo> responseObserver)` |
    | `default void` | `listExchanges(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)` |
    | `default void` | `listWitnesses(GrpcAPI.EmptyMessage request, io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)` |
    | `default void` | `triggerConstantContract(Contract.TriggerSmartContract request, io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)` |

* + ### Method Detail

    - #### getAccount

      ```
      default void getAccount(GrpcAPI.AccountAddressMessage request,
                              io.grpc.stub.StreamObserver<Response.Account> responseObserver)
      ```
    - #### getAccountById

      ```
      default void getAccountById(GrpcAPI.AccountIdMessage request,
                                  io.grpc.stub.StreamObserver<Response.Account> responseObserver)
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
    - #### getBlockByNum2

      ```
      default void getBlockByNum2(GrpcAPI.NumberMessage request,
                                  io.grpc.stub.StreamObserver<Response.BlockExtention> responseObserver)
      ```
    - #### getTransactionById

      ```
      default void getTransactionById(GrpcAPI.BytesMessage request,
                                      io.grpc.stub.StreamObserver<Chain.Transaction> responseObserver)
      ```
    - #### getTransactionInfoByBlockNum

      ```
      default void getTransactionInfoByBlockNum(GrpcAPI.NumberMessage request,
                                                io.grpc.stub.StreamObserver<Response.TransactionInfoList> responseObserver)
      ```
    - #### getTransactionInfoById

      ```
      default void getTransactionInfoById(GrpcAPI.BytesMessage request,
                                          io.grpc.stub.StreamObserver<Response.TransactionInfo> responseObserver)
      ```
    - #### getTransactionCountByBlockNum

      ```
      default void getTransactionCountByBlockNum(GrpcAPI.NumberMessage request,
                                                 io.grpc.stub.StreamObserver<GrpcAPI.NumberMessage> responseObserver)
      ```
    - #### estimateEnergy

      ```
      default void estimateEnergy(Contract.TriggerSmartContract request,
                                  io.grpc.stub.StreamObserver<Response.EstimateEnergyMessage> responseObserver)
      ```
    - #### triggerConstantContract

      ```
      default void triggerConstantContract(Contract.TriggerSmartContract request,
                                           io.grpc.stub.StreamObserver<Response.TransactionExtention> responseObserver)
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
    - #### getBurnTrx

      ```
      default void getBurnTrx(GrpcAPI.EmptyMessage request,
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
    - #### listWitnesses

      ```
      default void listWitnesses(GrpcAPI.EmptyMessage request,
                                 io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)
      ```
    - #### getExchangeById

      ```
      default void getExchangeById(GrpcAPI.BytesMessage request,
                                   io.grpc.stub.StreamObserver<Response.Exchange> responseObserver)
      ```
    - #### listExchanges

      ```
      default void listExchanges(GrpcAPI.EmptyMessage request,
                                 io.grpc.stub.StreamObserver<Response.ExchangeList> responseObserver)
      ```
    - #### getPaginatedNowWitnessList

      ```
      default void getPaginatedNowWitnessList(GrpcAPI.PaginatedMessage request,
                                              io.grpc.stub.StreamObserver<Response.WitnessList> responseObserver)
      ```
    - #### getMarketOrderById

      ```
      default void getMarketOrderById(GrpcAPI.BytesMessage request,
                                      io.grpc.stub.StreamObserver<Response.MarketOrder> responseObserver)
      ```
    - #### getMarketOrderByAccount

      ```
      default void getMarketOrderByAccount(GrpcAPI.BytesMessage request,
                                           io.grpc.stub.StreamObserver<Response.MarketOrderList> responseObserver)
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
    - #### getDelegatedResource

      ```
      default void getDelegatedResource(Response.DelegatedResourceMessage request,
                                        io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)
      ```
    - #### getDelegatedResourceV2

      ```
      default void getDelegatedResourceV2(Response.DelegatedResourceMessage request,
                                          io.grpc.stub.StreamObserver<Response.DelegatedResourceList> responseObserver)
      ```
    - #### getDelegatedResourceAccountIndex

      ```
      default void getDelegatedResourceAccountIndex(GrpcAPI.BytesMessage request,
                                                    io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)
      ```
    - #### getDelegatedResourceAccountIndexV2

      ```
      default void getDelegatedResourceAccountIndexV2(GrpcAPI.BytesMessage request,
                                                      io.grpc.stub.StreamObserver<Response.DelegatedResourceAccountIndex> responseObserver)
      ```