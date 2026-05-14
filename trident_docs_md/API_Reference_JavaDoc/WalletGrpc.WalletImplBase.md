

org.tron.trident.api

## Class WalletGrpc.WalletImplBase

* java.lang.Object
* + org.tron.trident.api.WalletGrpc.WalletImplBase

* All Implemented Interfaces:
  :   io.grpc.BindableService, [WalletGrpc.AsyncService](../../../../org/tron/trident/api/WalletGrpc.AsyncService.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [WalletGrpc](../../../../org/tron/trident/api/WalletGrpc.html "class in org.tron.trident.api")

  ---

    

  ```
  public abstract static class WalletGrpc.WalletImplBase
  extends java.lang.Object
  implements io.grpc.BindableService, WalletGrpc.AsyncService
  ```

  Base class for the server implementation of the service Wallet.

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `WalletImplBase()` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `io.grpc.ServerServiceDefinition` | `bindService()` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.api.[WalletGrpc.AsyncService](../../../../org/tron/trident/api/WalletGrpc.AsyncService.html "interface in org.tron.trident.api")

      `addSign, broadcastTransaction, createAddress, createShieldedContractParameters, createShieldedContractParametersWithoutAsk, createWitness2, deployContract, easyTransfer, easyTransferAsset, easyTransferAssetByPrivate, easyTransferByPrivate, estimateEnergy, generateAddress, getAccount, getAccountById, getAccountNet, getAccountResource, getAkFromAsk, getAssetIssueByAccount, getAssetIssueById, getAssetIssueByName, getAssetIssueList, getAssetIssueListByName, getAvailableUnfreezeCount, getBandwidthPrices, getBlock, getBlockBalanceTrace, getBlockById, getBlockByLatestNum, getBlockByLatestNum2, getBlockByLimitNext, getBlockByLimitNext2, getBlockByNum, getBlockByNum2, getBrokerageInfo, getBurnTrx, getCanDelegatedMaxSize, getCanWithdrawUnfreezeAmount, getChainParameters, getContract, getContractInfo, getDelegatedResource, getDelegatedResourceAccountIndex, getDelegatedResourceAccountIndexV2, getDelegatedResourceV2, getDiversifier, getEnergyPrices, getExchangeById, getExpandedSpendingKey, getIncomingViewingKey, getMarketOrderByAccount, getMarketOrderById, getMarketOrderListByPair, getMarketPairList, getMarketPriceByPair, getMemoFee, getNewShieldedAddress, getNextMaintenanceTime, getNkFromNsk, getNodeInfo, getNowBlock, getNowBlock2, getPaginatedAssetIssueList, getPaginatedExchangeList, getPaginatedNowWitnessList, getPaginatedProposalList, getPendingSize, getProposalById, getRcm, getRewardInfo, getSpendingKey, getTransactionApprovedList, getTransactionById, getTransactionCountByBlockNum, getTransactionFromPending, getTransactionInfoByBlockNum, getTransactionInfoById, getTransactionListFromPending, getTransactionSign, getTransactionSign2, getTransactionSignWeight, getTriggerInputForShieldedTRC20Contract, getZenPaymentAddress, isShieldedTRC20ContractNoteSpent, listExchanges, listNodes, listProposals, listWitnesses, scanShieldedTRC20NotesByIvk, scanShieldedTRC20NotesByOvk, totalTransaction, triggerConstantContract, triggerContract, withdrawBalance2`

* + ### Constructor Detail

    - #### WalletImplBase

      ```
      public WalletImplBase()
      ```
  + ### Method Detail

    - #### bindService

      ```
      public final io.grpc.ServerServiceDefinition bindService()
      ```

      Specified by:
      :   `bindService` in interface `io.grpc.BindableService`