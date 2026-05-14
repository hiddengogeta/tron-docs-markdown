

org.tron.trident.proto

## Class Contract

* java.lang.Object
* + org.tron.trident.proto.Contract

* ---

    

  ```
  public final class Contract
  extends java.lang.Object
  ```

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.AccountCreateContract` Protobuf type `protocol.AccountCreateContract` |
    | `static interface` | `Contract.AccountCreateContractOrBuilder` |
    | `static class` | `Contract.AccountPermissionUpdateContract` Protobuf type `protocol.AccountPermissionUpdateContract` |
    | `static interface` | `Contract.AccountPermissionUpdateContractOrBuilder` |
    | `static class` | `Contract.AccountUpdateContract` Update account name. |
    | `static interface` | `Contract.AccountUpdateContractOrBuilder` |
    | `static class` | `Contract.AssetIssueContract` Protobuf type `protocol.AssetIssueContract` |
    | `static interface` | `Contract.AssetIssueContractOrBuilder` |
    | `static class` | `Contract.CancelAllUnfreezeV2Contract` Protobuf type `protocol.CancelAllUnfreezeV2Contract` |
    | `static interface` | `Contract.CancelAllUnfreezeV2ContractOrBuilder` |
    | `static class` | `Contract.ClearABIContract` Protobuf type `protocol.ClearABIContract` |
    | `static interface` | `Contract.ClearABIContractOrBuilder` |
    | `static class` | `Contract.ContractState` Protobuf type `protocol.ContractState` |
    | `static interface` | `Contract.ContractStateOrBuilder` |
    | `static class` | `Contract.CreateSmartContract` Protobuf type `protocol.CreateSmartContract` |
    | `static interface` | `Contract.CreateSmartContractOrBuilder` |
    | `static class` | `Contract.DelegateResourceContract` Protobuf type `protocol.DelegateResourceContract` |
    | `static interface` | `Contract.DelegateResourceContractOrBuilder` |
    | `static class` | `Contract.ExchangeCreateContract` Protobuf type `protocol.ExchangeCreateContract` |
    | `static interface` | `Contract.ExchangeCreateContractOrBuilder` |
    | `static class` | `Contract.ExchangeInjectContract` Protobuf type `protocol.ExchangeInjectContract` |
    | `static interface` | `Contract.ExchangeInjectContractOrBuilder` |
    | `static class` | `Contract.ExchangeTransactionContract` Protobuf type `protocol.ExchangeTransactionContract` |
    | `static interface` | `Contract.ExchangeTransactionContractOrBuilder` |
    | `static class` | `Contract.ExchangeWithdrawContract` Protobuf type `protocol.ExchangeWithdrawContract` |
    | `static interface` | `Contract.ExchangeWithdrawContractOrBuilder` |
    | `static class` | `Contract.FreezeBalanceContract` Protobuf type `protocol.FreezeBalanceContract` |
    | `static interface` | `Contract.FreezeBalanceContractOrBuilder` |
    | `static class` | `Contract.FreezeBalanceV2Contract` stake 2.0 |
    | `static interface` | `Contract.FreezeBalanceV2ContractOrBuilder` |
    | `static class` | `Contract.MarketCancelOrderContract` Protobuf type `protocol.MarketCancelOrderContract` |
    | `static interface` | `Contract.MarketCancelOrderContractOrBuilder` |
    | `static class` | `Contract.MarketSellAssetContract` Protobuf type `protocol.MarketSellAssetContract` |
    | `static interface` | `Contract.MarketSellAssetContractOrBuilder` |
    | `static class` | `Contract.ParticipateAssetIssueContract` Protobuf type `protocol.ParticipateAssetIssueContract` |
    | `static interface` | `Contract.ParticipateAssetIssueContractOrBuilder` |
    | `static class` | `Contract.ProposalApproveContract` Protobuf type `protocol.ProposalApproveContract` |
    | `static interface` | `Contract.ProposalApproveContractOrBuilder` |
    | `static class` | `Contract.ProposalCreateContract` Protobuf type `protocol.ProposalCreateContract` |
    | `static interface` | `Contract.ProposalCreateContractOrBuilder` |
    | `static class` | `Contract.ProposalDeleteContract` Protobuf type `protocol.ProposalDeleteContract` |
    | `static interface` | `Contract.ProposalDeleteContractOrBuilder` |
    | `static class` | `Contract.SetAccountIdContract` Set account id if the account has no id. |
    | `static interface` | `Contract.SetAccountIdContractOrBuilder` |
    | `static class` | `Contract.TransferAssetContract` Protobuf type `protocol.TransferAssetContract` |
    | `static interface` | `Contract.TransferAssetContractOrBuilder` |
    | `static class` | `Contract.TransferContract` Protobuf type `protocol.TransferContract` |
    | `static interface` | `Contract.TransferContractOrBuilder` |
    | `static class` | `Contract.TriggerSmartContract` Protobuf type `protocol.TriggerSmartContract` |
    | `static interface` | `Contract.TriggerSmartContractOrBuilder` |
    | `static class` | `Contract.UnDelegateResourceContract` Protobuf type `protocol.UnDelegateResourceContract` |
    | `static interface` | `Contract.UnDelegateResourceContractOrBuilder` |
    | `static class` | `Contract.UnfreezeAssetContract` Protobuf type `protocol.UnfreezeAssetContract` |
    | `static interface` | `Contract.UnfreezeAssetContractOrBuilder` |
    | `static class` | `Contract.UnfreezeBalanceContract` Protobuf type `protocol.UnfreezeBalanceContract` |
    | `static interface` | `Contract.UnfreezeBalanceContractOrBuilder` |
    | `static class` | `Contract.UnfreezeBalanceV2Contract` Protobuf type `protocol.UnfreezeBalanceV2Contract` |
    | `static interface` | `Contract.UnfreezeBalanceV2ContractOrBuilder` |
    | `static class` | `Contract.UpdateAssetContract` Protobuf type `protocol.UpdateAssetContract` |
    | `static interface` | `Contract.UpdateAssetContractOrBuilder` |
    | `static class` | `Contract.UpdateBrokerageContract` Protobuf type `protocol.UpdateBrokerageContract` |
    | `static interface` | `Contract.UpdateBrokerageContractOrBuilder` |
    | `static class` | `Contract.UpdateEnergyLimitContract` Protobuf type `protocol.UpdateEnergyLimitContract` |
    | `static interface` | `Contract.UpdateEnergyLimitContractOrBuilder` |
    | `static class` | `Contract.UpdateSettingContract` Protobuf type `protocol.UpdateSettingContract` |
    | `static interface` | `Contract.UpdateSettingContractOrBuilder` |
    | `static class` | `Contract.VoteAssetContract` Protobuf type `protocol.VoteAssetContract` |
    | `static interface` | `Contract.VoteAssetContractOrBuilder` |
    | `static class` | `Contract.VoteWitnessContract` Protobuf type `protocol.VoteWitnessContract` |
    | `static interface` | `Contract.VoteWitnessContractOrBuilder` |
    | `static class` | `Contract.WithdrawBalanceContract` Protobuf type `protocol.WithdrawBalanceContract` |
    | `static interface` | `Contract.WithdrawBalanceContractOrBuilder` |
    | `static class` | `Contract.WithdrawExpireUnfreezeContract` Protobuf type `protocol.WithdrawExpireUnfreezeContract` |
    | `static interface` | `Contract.WithdrawExpireUnfreezeContractOrBuilder` |
    | `static class` | `Contract.WitnessCreateContract` Protobuf type `protocol.WitnessCreateContract` |
    | `static interface` | `Contract.WitnessCreateContractOrBuilder` |
    | `static class` | `Contract.WitnessUpdateContract` Protobuf type `protocol.WitnessUpdateContract` |
    | `static interface` | `Contract.WitnessUpdateContractOrBuilder` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static com.google.protobuf.Descriptors.FileDescriptor` | `getDescriptor()` |
    | `static void` | `registerAllExtensions(com.google.protobuf.ExtensionRegistry registry)` |
    | `static void` | `registerAllExtensions(com.google.protobuf.ExtensionRegistryLite registry)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### registerAllExtensions

      ```
      public static void registerAllExtensions(com.google.protobuf.ExtensionRegistryLite registry)
      ```
    - #### registerAllExtensions

      ```
      public static void registerAllExtensions(com.google.protobuf.ExtensionRegistry registry)
      ```
    - #### getDescriptor

      ```
      public static com.google.protobuf.Descriptors.FileDescriptor getDescriptor()
      ```