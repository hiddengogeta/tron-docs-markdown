

org.tron.trident.proto

## Class Response

* java.lang.Object
* + org.tron.trident.proto.Response

* ---

    

  ```
  public final class Response
  extends java.lang.Object
  ```

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.Account` Account |
    | `static class` | `Response.AccountNetMessage` deprecated |
    | `static interface` | `Response.AccountNetMessageOrBuilder` |
    | `static interface` | `Response.AccountOrBuilder` |
    | `static class` | `Response.AccountResourceMessage` Protobuf type `protocol.AccountResourceMessage` |
    | `static interface` | `Response.AccountResourceMessageOrBuilder` |
    | `static class` | `Response.AddressPrKeyPairMessage` Protobuf type `protocol.AddressPrKeyPairMessage` |
    | `static interface` | `Response.AddressPrKeyPairMessageOrBuilder` |
    | `static class` | `Response.AssetIssueList` Protobuf type `protocol.AssetIssueList` |
    | `static interface` | `Response.AssetIssueListOrBuilder` |
    | `static class` | `Response.BlockBalanceTrace` Protobuf type `protocol.BlockBalanceTrace` |
    | `static interface` | `Response.BlockBalanceTraceOrBuilder` |
    | `static class` | `Response.BlockExtention` Protobuf type `protocol.BlockExtention` |
    | `static interface` | `Response.BlockExtentionOrBuilder` |
    | `static class` | `Response.BlockIdentifier` Protobuf type `protocol.BlockIdentifier` |
    | `static interface` | `Response.BlockIdentifierOrBuilder` |
    | `static class` | `Response.BlockList` Protobuf type `protocol.BlockList` |
    | `static class` | `Response.BlockListExtention` Protobuf type `protocol.BlockListExtention` |
    | `static interface` | `Response.BlockListExtentionOrBuilder` |
    | `static interface` | `Response.BlockListOrBuilder` |
    | `static class` | `Response.ChainParameters` Protobuf type `protocol.ChainParameters` |
    | `static interface` | `Response.ChainParametersOrBuilder` |
    | `static class` | `Response.DecryptNotesTRC20` Protobuf type `protocol.DecryptNotesTRC20` |
    | `static interface` | `Response.DecryptNotesTRC20OrBuilder` |
    | `static class` | `Response.DelegatedResource` Protobuf type `protocol.DelegatedResource` |
    | `static class` | `Response.DelegatedResourceAccountIndex` Protobuf type `protocol.DelegatedResourceAccountIndex` |
    | `static interface` | `Response.DelegatedResourceAccountIndexOrBuilder` |
    | `static class` | `Response.DelegatedResourceList` Protobuf type `protocol.DelegatedResourceList` |
    | `static interface` | `Response.DelegatedResourceListOrBuilder` |
    | `static class` | `Response.DelegatedResourceMessage` Protobuf type `protocol.DelegatedResourceMessage` |
    | `static interface` | `Response.DelegatedResourceMessageOrBuilder` |
    | `static interface` | `Response.DelegatedResourceOrBuilder` |
    | `static class` | `Response.EasyTransferResponse` Protobuf type `protocol.EasyTransferResponse` |
    | `static interface` | `Response.EasyTransferResponseOrBuilder` |
    | `static class` | `Response.EstimateEnergyMessage` Protobuf type `protocol.EstimateEnergyMessage` |
    | `static interface` | `Response.EstimateEnergyMessageOrBuilder` |
    | `static class` | `Response.Exchange` Protobuf type `protocol.Exchange` |
    | `static class` | `Response.ExchangeList` Protobuf type `protocol.ExchangeList` |
    | `static interface` | `Response.ExchangeListOrBuilder` |
    | `static interface` | `Response.ExchangeOrBuilder` |
    | `static class` | `Response.InternalTransaction` Protobuf type `protocol.InternalTransaction` |
    | `static interface` | `Response.InternalTransactionOrBuilder` |
    | `static class` | `Response.MarketOrder` Protobuf type `protocol.MarketOrder` |
    | `static class` | `Response.MarketOrderList` Protobuf type `protocol.MarketOrderList` |
    | `static interface` | `Response.MarketOrderListOrBuilder` |
    | `static interface` | `Response.MarketOrderOrBuilder` |
    | `static class` | `Response.MarketOrderPair` Protobuf type `protocol.MarketOrderPair` |
    | `static class` | `Response.MarketOrderPairList` Protobuf type `protocol.MarketOrderPairList` |
    | `static interface` | `Response.MarketOrderPairListOrBuilder` |
    | `static interface` | `Response.MarketOrderPairOrBuilder` |
    | `static class` | `Response.MarketPrice` Protobuf type `protocol.MarketPrice` |
    | `static class` | `Response.MarketPriceList` Protobuf type `protocol.MarketPriceList` |
    | `static interface` | `Response.MarketPriceListOrBuilder` |
    | `static interface` | `Response.MarketPriceOrBuilder` |
    | `static class` | `Response.NodeInfo` Protobuf type `protocol.NodeInfo` |
    | `static interface` | `Response.NodeInfoOrBuilder` |
    | `static class` | `Response.NodeList` Gossip node list |
    | `static interface` | `Response.NodeListOrBuilder` |
    | `static class` | `Response.NullifierResult` Protobuf type `protocol.NullifierResult` |
    | `static interface` | `Response.NullifierResultOrBuilder` |
    | `static class` | `Response.PricesResponseMessage` Protobuf type `protocol.PricesResponseMessage` |
    | `static interface` | `Response.PricesResponseMessageOrBuilder` |
    | `static class` | `Response.Proposal` Protobuf type `protocol.Proposal` |
    | `static class` | `Response.ProposalList` Protobuf type `protocol.ProposalList` |
    | `static interface` | `Response.ProposalListOrBuilder` |
    | `static interface` | `Response.ProposalOrBuilder` |
    | `static class` | `Response.ResourceReceipt` Protobuf type `protocol.ResourceReceipt` |
    | `static interface` | `Response.ResourceReceiptOrBuilder` |
    | `static class` | `Response.SmartContractDataWrapper` Protobuf type `protocol.SmartContractDataWrapper` |
    | `static interface` | `Response.SmartContractDataWrapperOrBuilder` |
    | `static class` | `Response.TransactionApprovedList` Protobuf type `protocol.TransactionApprovedList` |
    | `static interface` | `Response.TransactionApprovedListOrBuilder` |
    | `static class` | `Response.TransactionBalanceTrace` Protobuf type `protocol.TransactionBalanceTrace` |
    | `static interface` | `Response.TransactionBalanceTraceOrBuilder` |
    | `static class` | `Response.TransactionExtention` Protobuf type `protocol.TransactionExtention` |
    | `static interface` | `Response.TransactionExtentionOrBuilder` |
    | `static class` | `Response.TransactionInfo` Protobuf type `protocol.TransactionInfo` |
    | `static class` | `Response.TransactionInfoList` Protobuf type `protocol.TransactionInfoList` |
    | `static interface` | `Response.TransactionInfoListOrBuilder` |
    | `static interface` | `Response.TransactionInfoOrBuilder` |
    | `static class` | `Response.TransactionList` Protobuf type `protocol.TransactionList` |
    | `static interface` | `Response.TransactionListOrBuilder` |
    | `static class` | `Response.TransactionReturn` Protobuf type `protocol.TransactionReturn` |
    | `static interface` | `Response.TransactionReturnOrBuilder` |
    | `static class` | `Response.TransactionSign` Protobuf type `protocol.TransactionSign` |
    | `static interface` | `Response.TransactionSignOrBuilder` |
    | `static class` | `Response.TransactionSignWeight` Protobuf type `protocol.TransactionSignWeight` |
    | `static interface` | `Response.TransactionSignWeightOrBuilder` |
    | `static class` | `Response.Witness` Witness |
    | `static class` | `Response.WitnessList` Protobuf type `protocol.WitnessList` |
    | `static interface` | `Response.WitnessListOrBuilder` |
    | `static interface` | `Response.WitnessOrBuilder` |
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