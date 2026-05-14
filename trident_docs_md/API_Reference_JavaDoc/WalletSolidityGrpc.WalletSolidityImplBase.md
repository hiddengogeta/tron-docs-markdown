

org.tron.trident.api

## Class WalletSolidityGrpc.WalletSolidityImplBase

* java.lang.Object
* + org.tron.trident.api.WalletSolidityGrpc.WalletSolidityImplBase

* All Implemented Interfaces:
  :   io.grpc.BindableService, [WalletSolidityGrpc.AsyncService](../../../../org/tron/trident/api/WalletSolidityGrpc.AsyncService.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [WalletSolidityGrpc](../../../../org/tron/trident/api/WalletSolidityGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public abstract static class WalletSolidityGrpc.WalletSolidityImplBase
  extends java.lang.Object
  implements io.grpc.BindableService, WalletSolidityGrpc.AsyncService
  ```

  Base class for the server implementation of the service WalletSolidity.

  ```
   NOTE: All other solidified APIs are useless.
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `WalletSolidityImplBase()` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `io.grpc.ServerServiceDefinition` | `bindService()` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.api.[WalletSolidityGrpc.AsyncService](../../../../org/tron/trident/api/WalletSolidityGrpc.AsyncService.html "interface in org.tron.trident.api")

      `estimateEnergy, getAccount, getAccountById, getAssetIssueById, getAssetIssueByName, getAssetIssueList, getAssetIssueListByName, getAvailableUnfreezeCount, getBandwidthPrices, getBlock, getBlockByNum, getBlockByNum2, getBrokerageInfo, getBurnTrx, getCanDelegatedMaxSize, getCanWithdrawUnfreezeAmount, getDelegatedResource, getDelegatedResourceAccountIndex, getDelegatedResourceAccountIndexV2, getDelegatedResourceV2, getEnergyPrices, getExchangeById, getMarketOrderByAccount, getMarketOrderById, getMarketOrderListByPair, getMarketPairList, getMarketPriceByPair, getNowBlock, getNowBlock2, getPaginatedAssetIssueList, getPaginatedNowWitnessList, getRewardInfo, getTransactionById, getTransactionCountByBlockNum, getTransactionInfoByBlockNum, getTransactionInfoById, listExchanges, listWitnesses, triggerConstantContract`

* + ### Constructor Detail

    - #### WalletSolidityImplBase

      ```
      public WalletSolidityImplBase()
      ```
  + ### Method Detail

    - #### bindService

      ```
      public final io.grpc.ServerServiceDefinition bindService()
      ```

      Specified by:
      :   `bindService` in interface `io.grpc.BindableService`