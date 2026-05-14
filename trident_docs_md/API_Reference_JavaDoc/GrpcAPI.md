

org.tron.trident.api

## Class GrpcAPI

* java.lang.Object
* + org.tron.trident.api.GrpcAPI

* ---

    

  ```
  public final class GrpcAPI
  extends java.lang.Object
  ```

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.AccountAddressMessage` NOTE: This is used to replace the design flaw of GetAccount. |
    | `static interface` | `GrpcAPI.AccountAddressMessageOrBuilder` |
    | `static class` | `GrpcAPI.AccountIdMessage` Protobuf type `protocol.AccountIdMessage` |
    | `static interface` | `GrpcAPI.AccountIdMessageOrBuilder` |
    | `static class` | `GrpcAPI.BlockLimit` Protobuf type `protocol.BlockLimit` |
    | `static interface` | `GrpcAPI.BlockLimitOrBuilder` |
    | `static class` | `GrpcAPI.BlockReq` Protobuf type `protocol.BlockReq` |
    | `static interface` | `GrpcAPI.BlockReqOrBuilder` |
    | `static class` | `GrpcAPI.BytesMessage` Protobuf type `protocol.BytesMessage` |
    | `static interface` | `GrpcAPI.BytesMessageOrBuilder` |
    | `static class` | `GrpcAPI.CanDelegatedMaxSizeRequestMessage` Protobuf type `protocol.CanDelegatedMaxSizeRequestMessage` |
    | `static interface` | `GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder` |
    | `static class` | `GrpcAPI.CanDelegatedMaxSizeResponseMessage` Protobuf type `protocol.CanDelegatedMaxSizeResponseMessage` |
    | `static interface` | `GrpcAPI.CanDelegatedMaxSizeResponseMessageOrBuilder` |
    | `static class` | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage` Stake 2.0 |
    | `static interface` | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessageOrBuilder` |
    | `static class` | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage` Protobuf type `protocol.CanWithdrawUnfreezeAmountResponseMessage` |
    | `static interface` | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessageOrBuilder` |
    | `static class` | `GrpcAPI.DiversifierMessage` Protobuf type `protocol.DiversifierMessage` |
    | `static interface` | `GrpcAPI.DiversifierMessageOrBuilder` |
    | `static class` | `GrpcAPI.EasyTransferAssetByPrivateMessage` Protobuf type `protocol.EasyTransferAssetByPrivateMessage` |
    | `static interface` | `GrpcAPI.EasyTransferAssetByPrivateMessageOrBuilder` |
    | `static class` | `GrpcAPI.EasyTransferAssetMessage` Protobuf type `protocol.EasyTransferAssetMessage` |
    | `static interface` | `GrpcAPI.EasyTransferAssetMessageOrBuilder` |
    | `static class` | `GrpcAPI.EasyTransferByPrivateMessage` Protobuf type `protocol.EasyTransferByPrivateMessage` |
    | `static interface` | `GrpcAPI.EasyTransferByPrivateMessageOrBuilder` |
    | `static class` | `GrpcAPI.EasyTransferMessage` Protobuf type `protocol.EasyTransferMessage` |
    | `static interface` | `GrpcAPI.EasyTransferMessageOrBuilder` |
    | `static class` | `GrpcAPI.EmptyMessage` Protobuf type `protocol.EmptyMessage` |
    | `static interface` | `GrpcAPI.EmptyMessageOrBuilder` |
    | `static class` | `GrpcAPI.ExpandedSpendingKeyMessage` Protobuf type `protocol.ExpandedSpendingKeyMessage` |
    | `static interface` | `GrpcAPI.ExpandedSpendingKeyMessageOrBuilder` |
    | `static class` | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage` Protobuf type `protocol.GetAvailableUnfreezeCountRequestMessage` |
    | `static interface` | `GrpcAPI.GetAvailableUnfreezeCountRequestMessageOrBuilder` |
    | `static class` | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage` Protobuf type `protocol.GetAvailableUnfreezeCountResponseMessage` |
    | `static interface` | `GrpcAPI.GetAvailableUnfreezeCountResponseMessageOrBuilder` |
    | `static class` | `GrpcAPI.IncomingViewingKeyDiversifierMessage` What's the fucking API design |
    | `static interface` | `GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder` |
    | `static class` | `GrpcAPI.IncomingViewingKeyMessage` Protobuf type `protocol.IncomingViewingKeyMessage` |
    | `static interface` | `GrpcAPI.IncomingViewingKeyMessageOrBuilder` |
    | `static class` | `GrpcAPI.IvkDecryptTRC20Parameters` Protobuf type `protocol.IvkDecryptTRC20Parameters` |
    | `static interface` | `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder` |
    | `static class` | `GrpcAPI.NfTRC20Parameters` Protobuf type `protocol.NfTRC20Parameters` |
    | `static interface` | `GrpcAPI.NfTRC20ParametersOrBuilder` |
    | `static class` | `GrpcAPI.NumberMessage` Protobuf type `protocol.NumberMessage` |
    | `static interface` | `GrpcAPI.NumberMessageOrBuilder` |
    | `static class` | `GrpcAPI.OvkDecryptTRC20Parameters` Protobuf type `protocol.OvkDecryptTRC20Parameters` |
    | `static interface` | `GrpcAPI.OvkDecryptTRC20ParametersOrBuilder` |
    | `static class` | `GrpcAPI.PaginatedMessage` FLAW: Paginated APIs are usless. |
    | `static interface` | `GrpcAPI.PaginatedMessageOrBuilder` |
    | `static class` | `GrpcAPI.PaymentAddressMessage` Protobuf type `protocol.PaymentAddressMessage` |
    | `static interface` | `GrpcAPI.PaymentAddressMessageOrBuilder` |
    | `static class` | `GrpcAPI.PrivateShieldedTRC20Parameters` Protobuf type `protocol.PrivateShieldedTRC20Parameters` |
    | `static interface` | `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder` |
    | `static class` | `GrpcAPI.PrivateShieldedTRC20ParametersWithoutAsk` Protobuf type `protocol.PrivateShieldedTRC20ParametersWithoutAsk` |
    | `static interface` | `GrpcAPI.PrivateShieldedTRC20ParametersWithoutAskOrBuilder` |
    | `static class` | `GrpcAPI.ReceiveDescription` Protobuf type `protocol.ReceiveDescription` |
    | `static interface` | `GrpcAPI.ReceiveDescriptionOrBuilder` |
    | `static class` | `GrpcAPI.ReceiveNote` Protobuf type `protocol.ReceiveNote` |
    | `static interface` | `GrpcAPI.ReceiveNoteOrBuilder` |
    | `static class` | `GrpcAPI.ShieldedAddressInfo` Protobuf type `protocol.ShieldedAddressInfo` |
    | `static interface` | `GrpcAPI.ShieldedAddressInfoOrBuilder` |
    | `static class` | `GrpcAPI.ShieldedTRC20Parameters` Protobuf type `protocol.ShieldedTRC20Parameters` |
    | `static interface` | `GrpcAPI.ShieldedTRC20ParametersOrBuilder` |
    | `static class` | `GrpcAPI.ShieldedTRC20TriggerContractParameters` Protobuf type `protocol.ShieldedTRC20TriggerContractParameters` |
    | `static interface` | `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder` |
    | `static class` | `GrpcAPI.SpendDescription` Protobuf type `protocol.SpendDescription` |
    | `static interface` | `GrpcAPI.SpendDescriptionOrBuilder` |
    | `static class` | `GrpcAPI.SpendNoteTRC20` Protobuf type `protocol.SpendNoteTRC20` |
    | `static interface` | `GrpcAPI.SpendNoteTRC20OrBuilder` |
    | `static class` | `GrpcAPI.TransactionIdList` Protobuf type `protocol.TransactionIdList` |
    | `static interface` | `GrpcAPI.TransactionIdListOrBuilder` |
    | `static class` | `GrpcAPI.ViewingKeyMessage` - Shielded TRC20 |
    | `static interface` | `GrpcAPI.ViewingKeyMessageOrBuilder` |
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