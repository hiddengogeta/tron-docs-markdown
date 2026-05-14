

org.tron.trident.proto

## Enum Chain.Transaction.Contract.ContractType

* java.lang.Object
* + java.lang.Enum<[Chain.Transaction.Contract.ContractType](../../../../org/tron/trident/proto/Chain.Transaction.Contract.ContractType.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Chain.Transaction.Contract.ContractType

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Chain.Transaction.Contract.ContractType](../../../../org/tron/trident/proto/Chain.Transaction.Contract.ContractType.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Chain.Transaction.Contract](../../../../org/tron/trident/proto/Chain.Transaction.Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Chain.Transaction.Contract.ContractType
  extends java.lang.Enum<Chain.Transaction.Contract.ContractType>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.Transaction.Contract.ContractType`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `AccountCreateContract` `AccountCreateContract = 0;` |
    | `AccountPermissionUpdateContract` `AccountPermissionUpdateContract = 46;` |
    | `AccountUpdateContract` `AccountUpdateContract = 10;` |
    | `AssetIssueContract` `AssetIssueContract = 6;` |
    | `CancelAllUnfreezeV2Contract` `CancelAllUnfreezeV2Contract = 59;` |
    | `ClearABIContract` `ClearABIContract = 48;` |
    | `CreateSmartContract` `CreateSmartContract = 30;` |
    | `CustomContract` `CustomContract = 20;` |
    | `DelegateResourceContract` `DelegateResourceContract = 57;` |
    | `ExchangeCreateContract` `ExchangeCreateContract = 41;` |
    | `ExchangeInjectContract` `ExchangeInjectContract = 42;` |
    | `ExchangeTransactionContract` `ExchangeTransactionContract = 44;` |
    | `ExchangeWithdrawContract` `ExchangeWithdrawContract = 43;` |
    | `FreezeBalanceContract` `FreezeBalanceContract = 11;` |
    | `FreezeBalanceV2Contract` `FreezeBalanceV2Contract = 54;` |
    | `GetContract` `GetContract = 32;` |
    | `MarketCancelOrderContract` `MarketCancelOrderContract = 53;` |
    | `MarketSellAssetContract` `MarketSellAssetContract = 52;` |
    | `ParticipateAssetIssueContract` `ParticipateAssetIssueContract = 9;` |
    | `ProposalApproveContract` `ProposalApproveContract = 17;` |
    | `ProposalCreateContract` `ProposalCreateContract = 16;` |
    | `ProposalDeleteContract` `ProposalDeleteContract = 18;` |
    | `SetAccountIdContract` `SetAccountIdContract = 19;` |
    | `ShieldedTransferContract` `ShieldedTransferContract = 51;` |
    | `TransferAssetContract` `TransferAssetContract = 2;` |
    | `TransferContract` `TransferContract = 1;` |
    | `TriggerSmartContract` `TriggerSmartContract = 31;` |
    | `UnDelegateResourceContract` `UnDelegateResourceContract = 58;` |
    | `UnfreezeAssetContract` `UnfreezeAssetContract = 14;` |
    | `UnfreezeBalanceContract` `UnfreezeBalanceContract = 12;` |
    | `UnfreezeBalanceV2Contract` `UnfreezeBalanceV2Contract = 55;` |
    | `UNRECOGNIZED` |
    | `UpdateAssetContract` `UpdateAssetContract = 15;` |
    | `UpdateBrokerageContract` `UpdateBrokerageContract = 49;` |
    | `UpdateEnergyLimitContract` `UpdateEnergyLimitContract = 45;` |
    | `UpdateSettingContract` `UpdateSettingContract = 33;` |
    | `VoteAssetContract` `VoteAssetContract = 3;` |
    | `VoteWitnessContract` `VoteWitnessContract = 4;` |
    | `WithdrawBalanceContract` `WithdrawBalanceContract = 13;` |
    | `WithdrawExpireUnfreezeContract` `WithdrawExpireUnfreezeContract = 56;` |
    | `WitnessCreateContract` `WitnessCreateContract = 5;` |
    | `WitnessUpdateContract` `WitnessUpdateContract = 8;` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `AccountCreateContract_VALUE` `AccountCreateContract = 0;` |
    | `static int` | `AccountPermissionUpdateContract_VALUE` `AccountPermissionUpdateContract = 46;` |
    | `static int` | `AccountUpdateContract_VALUE` `AccountUpdateContract = 10;` |
    | `static int` | `AssetIssueContract_VALUE` `AssetIssueContract = 6;` |
    | `static int` | `CancelAllUnfreezeV2Contract_VALUE` `CancelAllUnfreezeV2Contract = 59;` |
    | `static int` | `ClearABIContract_VALUE` `ClearABIContract = 48;` |
    | `static int` | `CreateSmartContract_VALUE` `CreateSmartContract = 30;` |
    | `static int` | `CustomContract_VALUE` `CustomContract = 20;` |
    | `static int` | `DelegateResourceContract_VALUE` `DelegateResourceContract = 57;` |
    | `static int` | `ExchangeCreateContract_VALUE` `ExchangeCreateContract = 41;` |
    | `static int` | `ExchangeInjectContract_VALUE` `ExchangeInjectContract = 42;` |
    | `static int` | `ExchangeTransactionContract_VALUE` `ExchangeTransactionContract = 44;` |
    | `static int` | `ExchangeWithdrawContract_VALUE` `ExchangeWithdrawContract = 43;` |
    | `static int` | `FreezeBalanceContract_VALUE` `FreezeBalanceContract = 11;` |
    | `static int` | `FreezeBalanceV2Contract_VALUE` `FreezeBalanceV2Contract = 54;` |
    | `static int` | `GetContract_VALUE` `GetContract = 32;` |
    | `static int` | `MarketCancelOrderContract_VALUE` `MarketCancelOrderContract = 53;` |
    | `static int` | `MarketSellAssetContract_VALUE` `MarketSellAssetContract = 52;` |
    | `static int` | `ParticipateAssetIssueContract_VALUE` `ParticipateAssetIssueContract = 9;` |
    | `static int` | `ProposalApproveContract_VALUE` `ProposalApproveContract = 17;` |
    | `static int` | `ProposalCreateContract_VALUE` `ProposalCreateContract = 16;` |
    | `static int` | `ProposalDeleteContract_VALUE` `ProposalDeleteContract = 18;` |
    | `static int` | `SetAccountIdContract_VALUE` `SetAccountIdContract = 19;` |
    | `static int` | `ShieldedTransferContract_VALUE` `ShieldedTransferContract = 51;` |
    | `static int` | `TransferAssetContract_VALUE` `TransferAssetContract = 2;` |
    | `static int` | `TransferContract_VALUE` `TransferContract = 1;` |
    | `static int` | `TriggerSmartContract_VALUE` `TriggerSmartContract = 31;` |
    | `static int` | `UnDelegateResourceContract_VALUE` `UnDelegateResourceContract = 58;` |
    | `static int` | `UnfreezeAssetContract_VALUE` `UnfreezeAssetContract = 14;` |
    | `static int` | `UnfreezeBalanceContract_VALUE` `UnfreezeBalanceContract = 12;` |
    | `static int` | `UnfreezeBalanceV2Contract_VALUE` `UnfreezeBalanceV2Contract = 55;` |
    | `static int` | `UpdateAssetContract_VALUE` `UpdateAssetContract = 15;` |
    | `static int` | `UpdateBrokerageContract_VALUE` `UpdateBrokerageContract = 49;` |
    | `static int` | `UpdateEnergyLimitContract_VALUE` `UpdateEnergyLimitContract = 45;` |
    | `static int` | `UpdateSettingContract_VALUE` `UpdateSettingContract = 33;` |
    | `static int` | `VoteAssetContract_VALUE` `VoteAssetContract = 3;` |
    | `static int` | `VoteWitnessContract_VALUE` `VoteWitnessContract = 4;` |
    | `static int` | `WithdrawBalanceContract_VALUE` `WithdrawBalanceContract = 13;` |
    | `static int` | `WithdrawExpireUnfreezeContract_VALUE` `WithdrawExpireUnfreezeContract = 56;` |
    | `static int` | `WitnessCreateContract_VALUE` `WitnessCreateContract = 5;` |
    | `static int` | `WitnessUpdateContract_VALUE` `WitnessUpdateContract = 8;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Chain.Transaction.Contract.ContractType` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Chain.Transaction.Contract.ContractType>` | `internalGetValueMap()` |
    | `static Chain.Transaction.Contract.ContractType` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Chain.Transaction.Contract.ContractType` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Chain.Transaction.Contract.ContractType.html#forNumber-int-) instead. |
    | `static Chain.Transaction.Contract.ContractType` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Chain.Transaction.Contract.ContractType[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### AccountCreateContract

      ```
      public static final Chain.Transaction.Contract.ContractType AccountCreateContract
      ```

      `AccountCreateContract = 0;`
    - #### TransferContract

      ```
      public static final Chain.Transaction.Contract.ContractType TransferContract
      ```

      `TransferContract = 1;`
    - #### TransferAssetContract

      ```
      public static final Chain.Transaction.Contract.ContractType TransferAssetContract
      ```

      `TransferAssetContract = 2;`
    - #### VoteAssetContract

      ```
      public static final Chain.Transaction.Contract.ContractType VoteAssetContract
      ```

      `VoteAssetContract = 3;`
    - #### VoteWitnessContract

      ```
      public static final Chain.Transaction.Contract.ContractType VoteWitnessContract
      ```

      `VoteWitnessContract = 4;`
    - #### WitnessCreateContract

      ```
      public static final Chain.Transaction.Contract.ContractType WitnessCreateContract
      ```

      `WitnessCreateContract = 5;`
    - #### AssetIssueContract

      ```
      public static final Chain.Transaction.Contract.ContractType AssetIssueContract
      ```

      `AssetIssueContract = 6;`
    - #### WitnessUpdateContract

      ```
      public static final Chain.Transaction.Contract.ContractType WitnessUpdateContract
      ```

      `WitnessUpdateContract = 8;`
    - #### ParticipateAssetIssueContract

      ```
      public static final Chain.Transaction.Contract.ContractType ParticipateAssetIssueContract
      ```

      `ParticipateAssetIssueContract = 9;`
    - #### AccountUpdateContract

      ```
      public static final Chain.Transaction.Contract.ContractType AccountUpdateContract
      ```

      `AccountUpdateContract = 10;`
    - #### FreezeBalanceContract

      ```
      public static final Chain.Transaction.Contract.ContractType FreezeBalanceContract
      ```

      `FreezeBalanceContract = 11;`
    - #### UnfreezeBalanceContract

      ```
      public static final Chain.Transaction.Contract.ContractType UnfreezeBalanceContract
      ```

      `UnfreezeBalanceContract = 12;`
    - #### WithdrawBalanceContract

      ```
      public static final Chain.Transaction.Contract.ContractType WithdrawBalanceContract
      ```

      `WithdrawBalanceContract = 13;`
    - #### UnfreezeAssetContract

      ```
      public static final Chain.Transaction.Contract.ContractType UnfreezeAssetContract
      ```

      `UnfreezeAssetContract = 14;`
    - #### UpdateAssetContract

      ```
      public static final Chain.Transaction.Contract.ContractType UpdateAssetContract
      ```

      `UpdateAssetContract = 15;`
    - #### ProposalCreateContract

      ```
      public static final Chain.Transaction.Contract.ContractType ProposalCreateContract
      ```

      `ProposalCreateContract = 16;`
    - #### ProposalApproveContract

      ```
      public static final Chain.Transaction.Contract.ContractType ProposalApproveContract
      ```

      `ProposalApproveContract = 17;`
    - #### ProposalDeleteContract

      ```
      public static final Chain.Transaction.Contract.ContractType ProposalDeleteContract
      ```

      `ProposalDeleteContract = 18;`
    - #### SetAccountIdContract

      ```
      public static final Chain.Transaction.Contract.ContractType SetAccountIdContract
      ```

      `SetAccountIdContract = 19;`
    - #### CustomContract

      ```
      public static final Chain.Transaction.Contract.ContractType CustomContract
      ```

      `CustomContract = 20;`
    - #### CreateSmartContract

      ```
      public static final Chain.Transaction.Contract.ContractType CreateSmartContract
      ```

      `CreateSmartContract = 30;`
    - #### TriggerSmartContract

      ```
      public static final Chain.Transaction.Contract.ContractType TriggerSmartContract
      ```

      `TriggerSmartContract = 31;`
    - #### GetContract

      ```
      public static final Chain.Transaction.Contract.ContractType GetContract
      ```

      `GetContract = 32;`
    - #### UpdateSettingContract

      ```
      public static final Chain.Transaction.Contract.ContractType UpdateSettingContract
      ```

      `UpdateSettingContract = 33;`
    - #### ExchangeCreateContract

      ```
      public static final Chain.Transaction.Contract.ContractType ExchangeCreateContract
      ```

      `ExchangeCreateContract = 41;`
    - #### ExchangeInjectContract

      ```
      public static final Chain.Transaction.Contract.ContractType ExchangeInjectContract
      ```

      `ExchangeInjectContract = 42;`
    - #### ExchangeWithdrawContract

      ```
      public static final Chain.Transaction.Contract.ContractType ExchangeWithdrawContract
      ```

      `ExchangeWithdrawContract = 43;`
    - #### ExchangeTransactionContract

      ```
      public static final Chain.Transaction.Contract.ContractType ExchangeTransactionContract
      ```

      `ExchangeTransactionContract = 44;`
    - #### UpdateEnergyLimitContract

      ```
      public static final Chain.Transaction.Contract.ContractType UpdateEnergyLimitContract
      ```

      `UpdateEnergyLimitContract = 45;`
    - #### AccountPermissionUpdateContract

      ```
      public static final Chain.Transaction.Contract.ContractType AccountPermissionUpdateContract
      ```

      `AccountPermissionUpdateContract = 46;`
    - #### ClearABIContract

      ```
      public static final Chain.Transaction.Contract.ContractType ClearABIContract
      ```

      `ClearABIContract = 48;`
    - #### UpdateBrokerageContract

      ```
      public static final Chain.Transaction.Contract.ContractType UpdateBrokerageContract
      ```

      `UpdateBrokerageContract = 49;`
    - #### ShieldedTransferContract

      ```
      public static final Chain.Transaction.Contract.ContractType ShieldedTransferContract
      ```

      `ShieldedTransferContract = 51;`
    - #### MarketSellAssetContract

      ```
      public static final Chain.Transaction.Contract.ContractType MarketSellAssetContract
      ```

      `MarketSellAssetContract = 52;`
    - #### MarketCancelOrderContract

      ```
      public static final Chain.Transaction.Contract.ContractType MarketCancelOrderContract
      ```

      `MarketCancelOrderContract = 53;`
    - #### FreezeBalanceV2Contract

      ```
      public static final Chain.Transaction.Contract.ContractType FreezeBalanceV2Contract
      ```

      `FreezeBalanceV2Contract = 54;`
    - #### UnfreezeBalanceV2Contract

      ```
      public static final Chain.Transaction.Contract.ContractType UnfreezeBalanceV2Contract
      ```

      `UnfreezeBalanceV2Contract = 55;`
    - #### WithdrawExpireUnfreezeContract

      ```
      public static final Chain.Transaction.Contract.ContractType WithdrawExpireUnfreezeContract
      ```

      `WithdrawExpireUnfreezeContract = 56;`
    - #### DelegateResourceContract

      ```
      public static final Chain.Transaction.Contract.ContractType DelegateResourceContract
      ```

      `DelegateResourceContract = 57;`
    - #### UnDelegateResourceContract

      ```
      public static final Chain.Transaction.Contract.ContractType UnDelegateResourceContract
      ```

      `UnDelegateResourceContract = 58;`
    - #### CancelAllUnfreezeV2Contract

      ```
      public static final Chain.Transaction.Contract.ContractType CancelAllUnfreezeV2Contract
      ```

      `CancelAllUnfreezeV2Contract = 59;`
    - #### UNRECOGNIZED

      ```
      public static final Chain.Transaction.Contract.ContractType UNRECOGNIZED
      ```
  + ### Field Detail

    - #### AccountCreateContract\_VALUE

      ```
      public static final int AccountCreateContract_VALUE
      ```

      `AccountCreateContract = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.AccountCreateContract_VALUE)
    - #### TransferContract\_VALUE

      ```
      public static final int TransferContract_VALUE
      ```

      `TransferContract = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.TransferContract_VALUE)
    - #### TransferAssetContract\_VALUE

      ```
      public static final int TransferAssetContract_VALUE
      ```

      `TransferAssetContract = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.TransferAssetContract_VALUE)
    - #### VoteAssetContract\_VALUE

      ```
      public static final int VoteAssetContract_VALUE
      ```

      `VoteAssetContract = 3;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.VoteAssetContract_VALUE)
    - #### VoteWitnessContract\_VALUE

      ```
      public static final int VoteWitnessContract_VALUE
      ```

      `VoteWitnessContract = 4;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.VoteWitnessContract_VALUE)
    - #### WitnessCreateContract\_VALUE

      ```
      public static final int WitnessCreateContract_VALUE
      ```

      `WitnessCreateContract = 5;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.WitnessCreateContract_VALUE)
    - #### AssetIssueContract\_VALUE

      ```
      public static final int AssetIssueContract_VALUE
      ```

      `AssetIssueContract = 6;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.AssetIssueContract_VALUE)
    - #### WitnessUpdateContract\_VALUE

      ```
      public static final int WitnessUpdateContract_VALUE
      ```

      `WitnessUpdateContract = 8;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.WitnessUpdateContract_VALUE)
    - #### ParticipateAssetIssueContract\_VALUE

      ```
      public static final int ParticipateAssetIssueContract_VALUE
      ```

      `ParticipateAssetIssueContract = 9;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ParticipateAssetIssueContract_VALUE)
    - #### AccountUpdateContract\_VALUE

      ```
      public static final int AccountUpdateContract_VALUE
      ```

      `AccountUpdateContract = 10;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.AccountUpdateContract_VALUE)
    - #### FreezeBalanceContract\_VALUE

      ```
      public static final int FreezeBalanceContract_VALUE
      ```

      `FreezeBalanceContract = 11;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.FreezeBalanceContract_VALUE)
    - #### UnfreezeBalanceContract\_VALUE

      ```
      public static final int UnfreezeBalanceContract_VALUE
      ```

      `UnfreezeBalanceContract = 12;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.UnfreezeBalanceContract_VALUE)
    - #### WithdrawBalanceContract\_VALUE

      ```
      public static final int WithdrawBalanceContract_VALUE
      ```

      `WithdrawBalanceContract = 13;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.WithdrawBalanceContract_VALUE)
    - #### UnfreezeAssetContract\_VALUE

      ```
      public static final int UnfreezeAssetContract_VALUE
      ```

      `UnfreezeAssetContract = 14;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.UnfreezeAssetContract_VALUE)
    - #### UpdateAssetContract\_VALUE

      ```
      public static final int UpdateAssetContract_VALUE
      ```

      `UpdateAssetContract = 15;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.UpdateAssetContract_VALUE)
    - #### ProposalCreateContract\_VALUE

      ```
      public static final int ProposalCreateContract_VALUE
      ```

      `ProposalCreateContract = 16;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ProposalCreateContract_VALUE)
    - #### ProposalApproveContract\_VALUE

      ```
      public static final int ProposalApproveContract_VALUE
      ```

      `ProposalApproveContract = 17;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ProposalApproveContract_VALUE)
    - #### ProposalDeleteContract\_VALUE

      ```
      public static final int ProposalDeleteContract_VALUE
      ```

      `ProposalDeleteContract = 18;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ProposalDeleteContract_VALUE)
    - #### SetAccountIdContract\_VALUE

      ```
      public static final int SetAccountIdContract_VALUE
      ```

      `SetAccountIdContract = 19;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.SetAccountIdContract_VALUE)
    - #### CustomContract\_VALUE

      ```
      public static final int CustomContract_VALUE
      ```

      `CustomContract = 20;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.CustomContract_VALUE)
    - #### CreateSmartContract\_VALUE

      ```
      public static final int CreateSmartContract_VALUE
      ```

      `CreateSmartContract = 30;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.CreateSmartContract_VALUE)
    - #### TriggerSmartContract\_VALUE

      ```
      public static final int TriggerSmartContract_VALUE
      ```

      `TriggerSmartContract = 31;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.TriggerSmartContract_VALUE)
    - #### GetContract\_VALUE

      ```
      public static final int GetContract_VALUE
      ```

      `GetContract = 32;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.GetContract_VALUE)
    - #### UpdateSettingContract\_VALUE

      ```
      public static final int UpdateSettingContract_VALUE
      ```

      `UpdateSettingContract = 33;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.UpdateSettingContract_VALUE)
    - #### ExchangeCreateContract\_VALUE

      ```
      public static final int ExchangeCreateContract_VALUE
      ```

      `ExchangeCreateContract = 41;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ExchangeCreateContract_VALUE)
    - #### ExchangeInjectContract\_VALUE

      ```
      public static final int ExchangeInjectContract_VALUE
      ```

      `ExchangeInjectContract = 42;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ExchangeInjectContract_VALUE)
    - #### ExchangeWithdrawContract\_VALUE

      ```
      public static final int ExchangeWithdrawContract_VALUE
      ```

      `ExchangeWithdrawContract = 43;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ExchangeWithdrawContract_VALUE)
    - #### ExchangeTransactionContract\_VALUE

      ```
      public static final int ExchangeTransactionContract_VALUE
      ```

      `ExchangeTransactionContract = 44;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ExchangeTransactionContract_VALUE)
    - #### UpdateEnergyLimitContract\_VALUE

      ```
      public static final int UpdateEnergyLimitContract_VALUE
      ```

      `UpdateEnergyLimitContract = 45;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.UpdateEnergyLimitContract_VALUE)
    - #### AccountPermissionUpdateContract\_VALUE

      ```
      public static final int AccountPermissionUpdateContract_VALUE
      ```

      `AccountPermissionUpdateContract = 46;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.AccountPermissionUpdateContract_VALUE)
    - #### ClearABIContract\_VALUE

      ```
      public static final int ClearABIContract_VALUE
      ```

      `ClearABIContract = 48;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ClearABIContract_VALUE)
    - #### UpdateBrokerageContract\_VALUE

      ```
      public static final int UpdateBrokerageContract_VALUE
      ```

      `UpdateBrokerageContract = 49;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.UpdateBrokerageContract_VALUE)
    - #### ShieldedTransferContract\_VALUE

      ```
      public static final int ShieldedTransferContract_VALUE
      ```

      `ShieldedTransferContract = 51;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.ShieldedTransferContract_VALUE)
    - #### MarketSellAssetContract\_VALUE

      ```
      public static final int MarketSellAssetContract_VALUE
      ```

      `MarketSellAssetContract = 52;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.MarketSellAssetContract_VALUE)
    - #### MarketCancelOrderContract\_VALUE

      ```
      public static final int MarketCancelOrderContract_VALUE
      ```

      `MarketCancelOrderContract = 53;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.MarketCancelOrderContract_VALUE)
    - #### FreezeBalanceV2Contract\_VALUE

      ```
      public static final int FreezeBalanceV2Contract_VALUE
      ```

      `FreezeBalanceV2Contract = 54;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.FreezeBalanceV2Contract_VALUE)
    - #### UnfreezeBalanceV2Contract\_VALUE

      ```
      public static final int UnfreezeBalanceV2Contract_VALUE
      ```

      `UnfreezeBalanceV2Contract = 55;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.UnfreezeBalanceV2Contract_VALUE)
    - #### WithdrawExpireUnfreezeContract\_VALUE

      ```
      public static final int WithdrawExpireUnfreezeContract_VALUE
      ```

      `WithdrawExpireUnfreezeContract = 56;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.WithdrawExpireUnfreezeContract_VALUE)
    - #### DelegateResourceContract\_VALUE

      ```
      public static final int DelegateResourceContract_VALUE
      ```

      `DelegateResourceContract = 57;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.DelegateResourceContract_VALUE)
    - #### UnDelegateResourceContract\_VALUE

      ```
      public static final int UnDelegateResourceContract_VALUE
      ```

      `UnDelegateResourceContract = 58;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.UnDelegateResourceContract_VALUE)
    - #### CancelAllUnfreezeV2Contract\_VALUE

      ```
      public static final int CancelAllUnfreezeV2Contract_VALUE
      ```

      `CancelAllUnfreezeV2Contract = 59;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.ContractType.CancelAllUnfreezeV2Contract_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Chain.Transaction.Contract.ContractType[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Chain.Transaction.Contract.ContractType c : Chain.Transaction.Contract.ContractType.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Chain.Transaction.Contract.ContractType valueOf(java.lang.String name)
      ```

      Returns the enum constant of this type with the specified name.
      The string must match *exactly* an identifier used to declare an
      enum constant in this type. (Extraneous whitespace characters are
      not permitted.)

      Parameters:
      :   `name` - the name of the enum constant to be returned.

      Returns:
      :   the enum constant with the specified name

      Throws:
      :   `java.lang.IllegalArgumentException` - if this enum type has no constant with the specified name
      :   `java.lang.NullPointerException` - if the argument is null
    - #### getNumber

      ```
      public final int getNumber()
      ```

      Specified by:
      :   `getNumber` in interface `com.google.protobuf.Internal.EnumLite`

      Specified by:
      :   `getNumber` in interface `com.google.protobuf.ProtocolMessageEnum`
    - #### valueOf

      ```
      @Deprecated
      public static Chain.Transaction.Contract.ContractType valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Chain.Transaction.Contract.ContractType.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Chain.Transaction.Contract.ContractType forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Chain.Transaction.Contract.ContractType> internalGetValueMap()
      ```
    - #### getValueDescriptor

      ```
      public final com.google.protobuf.Descriptors.EnumValueDescriptor getValueDescriptor()
      ```

      Specified by:
      :   `getValueDescriptor` in interface `com.google.protobuf.ProtocolMessageEnum`
    - #### getDescriptorForType

      ```
      public final com.google.protobuf.Descriptors.EnumDescriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.ProtocolMessageEnum`
    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.EnumDescriptor getDescriptor()
      ```
    - #### valueOf

      ```
      public static Chain.Transaction.Contract.ContractType valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```