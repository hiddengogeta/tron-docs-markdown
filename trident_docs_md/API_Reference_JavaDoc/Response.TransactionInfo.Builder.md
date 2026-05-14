

org.tron.trident.proto

## Class Response.TransactionInfo.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionInfo.Builder](../../../../org/tron/trident/proto/Response.TransactionInfo.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionInfo.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionInfoOrBuilder](../../../../org/tron/trident/proto/Response.TransactionInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionInfo](../../../../org/tron/trident/proto/Response.TransactionInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionInfo.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>
  implements Response.TransactionInfoOrBuilder
  ```

  Protobuf type `protocol.TransactionInfo`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionInfo.Builder` | `addAllContractResult(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` `repeated bytes contractResult = 5;` |
    | `Response.TransactionInfo.Builder` | `addAllInternalTransactions(java.lang.Iterable<? extends Response.InternalTransaction> values)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Builder` | `addAllLog(java.lang.Iterable<? extends Response.TransactionInfo.Log> values)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Builder` | `addAllOrderDetails(java.lang.Iterable<? extends Common.MarketOrderDetail> values)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Response.TransactionInfo.Builder` | `addContractResult(com.google.protobuf.ByteString value)` `repeated bytes contractResult = 5;` |
    | `Response.TransactionInfo.Builder` | `addInternalTransactions(int index, Response.InternalTransaction.Builder builderForValue)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Builder` | `addInternalTransactions(int index, Response.InternalTransaction value)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Builder` | `addInternalTransactions(Response.InternalTransaction.Builder builderForValue)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Builder` | `addInternalTransactions(Response.InternalTransaction value)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.InternalTransaction.Builder` | `addInternalTransactionsBuilder()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.InternalTransaction.Builder` | `addInternalTransactionsBuilder(int index)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Builder` | `addLog(int index, Response.TransactionInfo.Log.Builder builderForValue)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Builder` | `addLog(int index, Response.TransactionInfo.Log value)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Builder` | `addLog(Response.TransactionInfo.Log.Builder builderForValue)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Builder` | `addLog(Response.TransactionInfo.Log value)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Log.Builder` | `addLogBuilder()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Log.Builder` | `addLogBuilder(int index)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Builder` | `addOrderDetails(Common.MarketOrderDetail.Builder builderForValue)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Response.TransactionInfo.Builder` | `addOrderDetails(Common.MarketOrderDetail value)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Response.TransactionInfo.Builder` | `addOrderDetails(int index, Common.MarketOrderDetail.Builder builderForValue)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Response.TransactionInfo.Builder` | `addOrderDetails(int index, Common.MarketOrderDetail value)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetail.Builder` | `addOrderDetailsBuilder()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetail.Builder` | `addOrderDetailsBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Response.TransactionInfo.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionInfo` | `build()` |
    | `Response.TransactionInfo` | `buildPartial()` |
    | `Response.TransactionInfo.Builder` | `clear()` |
    | `Response.TransactionInfo.Builder` | `clearAssetIssueID()` `string assetIssueID = 14;` |
    | `Response.TransactionInfo.Builder` | `clearBlockNumber()` `int64 blockNumber = 3;` |
    | `Response.TransactionInfo.Builder` | `clearBlockTimeStamp()` `int64 blockTimeStamp = 4;` |
    | `Response.TransactionInfo.Builder` | `clearCancelUnfreezeV2Amount()` |
    | `Response.TransactionInfo.Builder` | `clearContractAddress()` `bytes contract_address = 6;` |
    | `Response.TransactionInfo.Builder` | `clearContractResult()` `repeated bytes contractResult = 5;` |
    | `Response.TransactionInfo.Builder` | `clearExchangeId()` `int64 exchange_id = 21;` |
    | `Response.TransactionInfo.Builder` | `clearExchangeInjectAnotherAmount()` `int64 exchange_inject_another_amount = 19;` |
    | `Response.TransactionInfo.Builder` | `clearExchangeReceivedAmount()` `int64 exchange_received_amount = 18;` |
    | `Response.TransactionInfo.Builder` | `clearExchangeWithdrawAnotherAmount()` `int64 exchange_withdraw_another_amount = 20;` |
    | `Response.TransactionInfo.Builder` | `clearFee()` `int64 fee = 2;` |
    | `Response.TransactionInfo.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionInfo.Builder` | `clearId()` `bytes id = 1;` |
    | `Response.TransactionInfo.Builder` | `clearInternalTransactions()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Builder` | `clearLog()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionInfo.Builder` | `clearOrderDetails()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Response.TransactionInfo.Builder` | `clearOrderId()` `bytes orderId = 25;` |
    | `Response.TransactionInfo.Builder` | `clearPackingFee()` `int64 packingFee = 27;` |
    | `Response.TransactionInfo.Builder` | `clearReceipt()` `.protocol.ResourceReceipt receipt = 7;` |
    | `Response.TransactionInfo.Builder` | `clearResMessage()` `bytes resMessage = 10;` |
    | `Response.TransactionInfo.Builder` | `clearResult()` `.protocol.TransactionInfo.code result = 9;` |
    | `Response.TransactionInfo.Builder` | `clearShieldedTransactionFee()` `int64 shielded_transaction_fee = 22;` |
    | `Response.TransactionInfo.Builder` | `clearUnfreezeAmount()` `int64 unfreeze_amount = 16;` |
    | `Response.TransactionInfo.Builder` | `clearWithdrawAmount()` `int64 withdraw_amount = 15;` |
    | `Response.TransactionInfo.Builder` | `clearWithdrawExpireAmount()` `int64 withdraw_expire_amount = 28;` |
    | `Response.TransactionInfo.Builder` | `clone()` |
    | `boolean` | `containsCancelUnfreezeV2Amount(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `java.lang.String` | `getAssetIssueID()` `string assetIssueID = 14;` |
    | `com.google.protobuf.ByteString` | `getAssetIssueIDBytes()` `string assetIssueID = 14;` |
    | `long` | `getBlockNumber()` `int64 blockNumber = 3;` |
    | `long` | `getBlockTimeStamp()` `int64 blockTimeStamp = 4;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2Amount()` Deprecated. |
    | `int` | `getCancelUnfreezeV2AmountCount()` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2AmountMap()` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `long` | `getCancelUnfreezeV2AmountOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `long` | `getCancelUnfreezeV2AmountOrThrow(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 6;` |
    | `com.google.protobuf.ByteString` | `getContractResult(int index)` `repeated bytes contractResult = 5;` |
    | `int` | `getContractResultCount()` `repeated bytes contractResult = 5;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getContractResultList()` `repeated bytes contractResult = 5;` |
    | `Response.TransactionInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getExchangeId()` `int64 exchange_id = 21;` |
    | `long` | `getExchangeInjectAnotherAmount()` `int64 exchange_inject_another_amount = 19;` |
    | `long` | `getExchangeReceivedAmount()` `int64 exchange_received_amount = 18;` |
    | `long` | `getExchangeWithdrawAnotherAmount()` `int64 exchange_withdraw_another_amount = 20;` |
    | `long` | `getFee()` `int64 fee = 2;` |
    | `com.google.protobuf.ByteString` | `getId()` `bytes id = 1;` |
    | `Response.InternalTransaction` | `getInternalTransactions(int index)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.InternalTransaction.Builder` | `getInternalTransactionsBuilder(int index)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `java.util.List<Response.InternalTransaction.Builder>` | `getInternalTransactionsBuilderList()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `int` | `getInternalTransactionsCount()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `java.util.List<Response.InternalTransaction>` | `getInternalTransactionsList()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.InternalTransactionOrBuilder` | `getInternalTransactionsOrBuilder(int index)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `java.util.List<? extends Response.InternalTransactionOrBuilder>` | `getInternalTransactionsOrBuilderList()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Log` | `getLog(int index)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Log.Builder` | `getLogBuilder(int index)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `java.util.List<Response.TransactionInfo.Log.Builder>` | `getLogBuilderList()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `int` | `getLogCount()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `java.util.List<Response.TransactionInfo.Log>` | `getLogList()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.LogOrBuilder` | `getLogOrBuilder(int index)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `java.util.List<? extends Response.TransactionInfo.LogOrBuilder>` | `getLogOrBuilderList()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableCancelUnfreezeV2Amount()` Deprecated. |
    | `Common.MarketOrderDetail` | `getOrderDetails(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetail.Builder` | `getOrderDetailsBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<Common.MarketOrderDetail.Builder>` | `getOrderDetailsBuilderList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `int` | `getOrderDetailsCount()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<Common.MarketOrderDetail>` | `getOrderDetailsList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetailOrBuilder` | `getOrderDetailsOrBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<? extends Common.MarketOrderDetailOrBuilder>` | `getOrderDetailsOrBuilderList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `com.google.protobuf.ByteString` | `getOrderId()` `bytes orderId = 25;` |
    | `long` | `getPackingFee()` `int64 packingFee = 27;` |
    | `Response.ResourceReceipt` | `getReceipt()` `.protocol.ResourceReceipt receipt = 7;` |
    | `Response.ResourceReceipt.Builder` | `getReceiptBuilder()` `.protocol.ResourceReceipt receipt = 7;` |
    | `Response.ResourceReceiptOrBuilder` | `getReceiptOrBuilder()` `.protocol.ResourceReceipt receipt = 7;` |
    | `com.google.protobuf.ByteString` | `getResMessage()` `bytes resMessage = 10;` |
    | `Response.TransactionInfo.code` | `getResult()` `.protocol.TransactionInfo.code result = 9;` |
    | `int` | `getResultValue()` `.protocol.TransactionInfo.code result = 9;` |
    | `long` | `getShieldedTransactionFee()` `int64 shielded_transaction_fee = 22;` |
    | `long` | `getUnfreezeAmount()` `int64 unfreeze_amount = 16;` |
    | `long` | `getWithdrawAmount()` `int64 withdraw_amount = 15;` |
    | `long` | `getWithdrawExpireAmount()` `int64 withdraw_expire_amount = 28;` |
    | `boolean` | `hasReceipt()` `.protocol.ResourceReceipt receipt = 7;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMutableMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionInfo.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionInfo.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionInfo.Builder` | `mergeFrom(Response.TransactionInfo other)` |
    | `Response.TransactionInfo.Builder` | `mergeReceipt(Response.ResourceReceipt value)` `.protocol.ResourceReceipt receipt = 7;` |
    | `Response.TransactionInfo.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionInfo.Builder` | `putAllCancelUnfreezeV2Amount(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `Response.TransactionInfo.Builder` | `putCancelUnfreezeV2Amount(java.lang.String key, long value)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `Response.TransactionInfo.Builder` | `removeCancelUnfreezeV2Amount(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `Response.TransactionInfo.Builder` | `removeInternalTransactions(int index)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Builder` | `removeLog(int index)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Builder` | `removeOrderDetails(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Response.TransactionInfo.Builder` | `setAssetIssueID(java.lang.String value)` `string assetIssueID = 14;` |
    | `Response.TransactionInfo.Builder` | `setAssetIssueIDBytes(com.google.protobuf.ByteString value)` `string assetIssueID = 14;` |
    | `Response.TransactionInfo.Builder` | `setBlockNumber(long value)` `int64 blockNumber = 3;` |
    | `Response.TransactionInfo.Builder` | `setBlockTimeStamp(long value)` `int64 blockTimeStamp = 4;` |
    | `Response.TransactionInfo.Builder` | `setContractAddress(com.google.protobuf.ByteString value)` `bytes contract_address = 6;` |
    | `Response.TransactionInfo.Builder` | `setContractResult(int index, com.google.protobuf.ByteString value)` `repeated bytes contractResult = 5;` |
    | `Response.TransactionInfo.Builder` | `setExchangeId(long value)` `int64 exchange_id = 21;` |
    | `Response.TransactionInfo.Builder` | `setExchangeInjectAnotherAmount(long value)` `int64 exchange_inject_another_amount = 19;` |
    | `Response.TransactionInfo.Builder` | `setExchangeReceivedAmount(long value)` `int64 exchange_received_amount = 18;` |
    | `Response.TransactionInfo.Builder` | `setExchangeWithdrawAnotherAmount(long value)` `int64 exchange_withdraw_another_amount = 20;` |
    | `Response.TransactionInfo.Builder` | `setFee(long value)` `int64 fee = 2;` |
    | `Response.TransactionInfo.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionInfo.Builder` | `setId(com.google.protobuf.ByteString value)` `bytes id = 1;` |
    | `Response.TransactionInfo.Builder` | `setInternalTransactions(int index, Response.InternalTransaction.Builder builderForValue)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Builder` | `setInternalTransactions(int index, Response.InternalTransaction value)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Builder` | `setLog(int index, Response.TransactionInfo.Log.Builder builderForValue)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Builder` | `setLog(int index, Response.TransactionInfo.Log value)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.Builder` | `setOrderDetails(int index, Common.MarketOrderDetail.Builder builderForValue)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Response.TransactionInfo.Builder` | `setOrderDetails(int index, Common.MarketOrderDetail value)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Response.TransactionInfo.Builder` | `setOrderId(com.google.protobuf.ByteString value)` `bytes orderId = 25;` |
    | `Response.TransactionInfo.Builder` | `setPackingFee(long value)` `int64 packingFee = 27;` |
    | `Response.TransactionInfo.Builder` | `setReceipt(Response.ResourceReceipt.Builder builderForValue)` `.protocol.ResourceReceipt receipt = 7;` |
    | `Response.TransactionInfo.Builder` | `setReceipt(Response.ResourceReceipt value)` `.protocol.ResourceReceipt receipt = 7;` |
    | `Response.TransactionInfo.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionInfo.Builder` | `setResMessage(com.google.protobuf.ByteString value)` `bytes resMessage = 10;` |
    | `Response.TransactionInfo.Builder` | `setResult(Response.TransactionInfo.code value)` `.protocol.TransactionInfo.code result = 9;` |
    | `Response.TransactionInfo.Builder` | `setResultValue(int value)` `.protocol.TransactionInfo.code result = 9;` |
    | `Response.TransactionInfo.Builder` | `setShieldedTransactionFee(long value)` `int64 shielded_transaction_fee = 22;` |
    | `Response.TransactionInfo.Builder` | `setUnfreezeAmount(long value)` `int64 unfreeze_amount = 16;` |
    | `Response.TransactionInfo.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionInfo.Builder` | `setWithdrawAmount(long value)` `int64 withdraw_amount = 15;` |
    | `Response.TransactionInfo.Builder` | `setWithdrawExpireAmount(long value)` `int64 withdraw_expire_amount = 28;` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMutableMapField, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage.Builder

      `findInitializationErrors, getInitializationErrorString, internalMergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, newUninitializedMessageException, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite.Builder

      `addAll, addAll, mergeDelimitedFrom, mergeDelimitedFrom, newUninitializedMessageException`
    - ### Methods inherited from class java.lang.Object

      `equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.Message.Builder

      `mergeDelimitedFrom, mergeDelimitedFrom`

* + ### Method Detail

    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### internalGetMutableMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMutableMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### clear

      ```
      public Response.TransactionInfo.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionInfo build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionInfo buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionInfo.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### setField

      ```
      public Response.TransactionInfo.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### clearField

      ```
      public Response.TransactionInfo.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionInfo.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionInfo.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionInfo.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionInfo.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionInfo.Builder mergeFrom(Response.TransactionInfo other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionInfo.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionInfo.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getId

      ```
      public com.google.protobuf.ByteString getId()
      ```

      `bytes id = 1;`

      Specified by:
      :   `getId` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The id.
    - #### setId

      ```
      public Response.TransactionInfo.Builder setId(com.google.protobuf.ByteString value)
      ```

      `bytes id = 1;`

      Parameters:
      :   `value` - The id to set.

      Returns:
      :   This builder for chaining.
    - #### clearId

      ```
      public Response.TransactionInfo.Builder clearId()
      ```

      `bytes id = 1;`

      Returns:
      :   This builder for chaining.
    - #### getFee

      ```
      public long getFee()
      ```

      `int64 fee = 2;`

      Specified by:
      :   `getFee` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The fee.
    - #### setFee

      ```
      public Response.TransactionInfo.Builder setFee(long value)
      ```

      `int64 fee = 2;`

      Parameters:
      :   `value` - The fee to set.

      Returns:
      :   This builder for chaining.
    - #### clearFee

      ```
      public Response.TransactionInfo.Builder clearFee()
      ```

      `int64 fee = 2;`

      Returns:
      :   This builder for chaining.
    - #### getBlockNumber

      ```
      public long getBlockNumber()
      ```

      `int64 blockNumber = 3;`

      Specified by:
      :   `getBlockNumber` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The blockNumber.
    - #### setBlockNumber

      ```
      public Response.TransactionInfo.Builder setBlockNumber(long value)
      ```

      `int64 blockNumber = 3;`

      Parameters:
      :   `value` - The blockNumber to set.

      Returns:
      :   This builder for chaining.
    - #### clearBlockNumber

      ```
      public Response.TransactionInfo.Builder clearBlockNumber()
      ```

      `int64 blockNumber = 3;`

      Returns:
      :   This builder for chaining.
    - #### getBlockTimeStamp

      ```
      public long getBlockTimeStamp()
      ```

      `int64 blockTimeStamp = 4;`

      Specified by:
      :   `getBlockTimeStamp` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The blockTimeStamp.
    - #### setBlockTimeStamp

      ```
      public Response.TransactionInfo.Builder setBlockTimeStamp(long value)
      ```

      `int64 blockTimeStamp = 4;`

      Parameters:
      :   `value` - The blockTimeStamp to set.

      Returns:
      :   This builder for chaining.
    - #### clearBlockTimeStamp

      ```
      public Response.TransactionInfo.Builder clearBlockTimeStamp()
      ```

      `int64 blockTimeStamp = 4;`

      Returns:
      :   This builder for chaining.
    - #### getContractResultList

      ```
      public java.util.List<com.google.protobuf.ByteString> getContractResultList()
      ```

      `repeated bytes contractResult = 5;`

      Specified by:
      :   `getContractResultList` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   A list containing the contractResult.
    - #### getContractResultCount

      ```
      public int getContractResultCount()
      ```

      `repeated bytes contractResult = 5;`

      Specified by:
      :   `getContractResultCount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The count of contractResult.
    - #### getContractResult

      ```
      public com.google.protobuf.ByteString getContractResult(int index)
      ```

      `repeated bytes contractResult = 5;`

      Specified by:
      :   `getContractResult` in interface `Response.TransactionInfoOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The contractResult at the given index.
    - #### setContractResult

      ```
      public Response.TransactionInfo.Builder setContractResult(int index,
                                                                com.google.protobuf.ByteString value)
      ```

      `repeated bytes contractResult = 5;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The contractResult to set.

      Returns:
      :   This builder for chaining.
    - #### addContractResult

      ```
      public Response.TransactionInfo.Builder addContractResult(com.google.protobuf.ByteString value)
      ```

      `repeated bytes contractResult = 5;`

      Parameters:
      :   `value` - The contractResult to add.

      Returns:
      :   This builder for chaining.
    - #### addAllContractResult

      ```
      public Response.TransactionInfo.Builder addAllContractResult(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      `repeated bytes contractResult = 5;`

      Parameters:
      :   `values` - The contractResult to add.

      Returns:
      :   This builder for chaining.
    - #### clearContractResult

      ```
      public Response.TransactionInfo.Builder clearContractResult()
      ```

      `repeated bytes contractResult = 5;`

      Returns:
      :   This builder for chaining.
    - #### getContractAddress

      ```
      public com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 6;`

      Specified by:
      :   `getContractAddress` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The contractAddress.
    - #### setContractAddress

      ```
      public Response.TransactionInfo.Builder setContractAddress(com.google.protobuf.ByteString value)
      ```

      `bytes contract_address = 6;`

      Parameters:
      :   `value` - The contractAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearContractAddress

      ```
      public Response.TransactionInfo.Builder clearContractAddress()
      ```

      `bytes contract_address = 6;`

      Returns:
      :   This builder for chaining.
    - #### hasReceipt

      ```
      public boolean hasReceipt()
      ```

      `.protocol.ResourceReceipt receipt = 7;`

      Specified by:
      :   `hasReceipt` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   Whether the receipt field is set.
    - #### getReceipt

      ```
      public Response.ResourceReceipt getReceipt()
      ```

      `.protocol.ResourceReceipt receipt = 7;`

      Specified by:
      :   `getReceipt` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The receipt.
    - #### setReceipt

      ```
      public Response.TransactionInfo.Builder setReceipt(Response.ResourceReceipt value)
      ```

      `.protocol.ResourceReceipt receipt = 7;`
    - #### setReceipt

      ```
      public Response.TransactionInfo.Builder setReceipt(Response.ResourceReceipt.Builder builderForValue)
      ```

      `.protocol.ResourceReceipt receipt = 7;`
    - #### mergeReceipt

      ```
      public Response.TransactionInfo.Builder mergeReceipt(Response.ResourceReceipt value)
      ```

      `.protocol.ResourceReceipt receipt = 7;`
    - #### clearReceipt

      ```
      public Response.TransactionInfo.Builder clearReceipt()
      ```

      `.protocol.ResourceReceipt receipt = 7;`
    - #### getReceiptBuilder

      ```
      public Response.ResourceReceipt.Builder getReceiptBuilder()
      ```

      `.protocol.ResourceReceipt receipt = 7;`
    - #### getReceiptOrBuilder

      ```
      public Response.ResourceReceiptOrBuilder getReceiptOrBuilder()
      ```

      `.protocol.ResourceReceipt receipt = 7;`

      Specified by:
      :   `getReceiptOrBuilder` in interface `Response.TransactionInfoOrBuilder`
    - #### getLogList

      ```
      public java.util.List<Response.TransactionInfo.Log> getLogList()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`

      Specified by:
      :   `getLogList` in interface `Response.TransactionInfoOrBuilder`
    - #### getLogCount

      ```
      public int getLogCount()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`

      Specified by:
      :   `getLogCount` in interface `Response.TransactionInfoOrBuilder`
    - #### getLog

      ```
      public Response.TransactionInfo.Log getLog(int index)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`

      Specified by:
      :   `getLog` in interface `Response.TransactionInfoOrBuilder`
    - #### setLog

      ```
      public Response.TransactionInfo.Builder setLog(int index,
                                                     Response.TransactionInfo.Log value)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### setLog

      ```
      public Response.TransactionInfo.Builder setLog(int index,
                                                     Response.TransactionInfo.Log.Builder builderForValue)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### addLog

      ```
      public Response.TransactionInfo.Builder addLog(Response.TransactionInfo.Log value)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### addLog

      ```
      public Response.TransactionInfo.Builder addLog(int index,
                                                     Response.TransactionInfo.Log value)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### addLog

      ```
      public Response.TransactionInfo.Builder addLog(Response.TransactionInfo.Log.Builder builderForValue)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### addLog

      ```
      public Response.TransactionInfo.Builder addLog(int index,
                                                     Response.TransactionInfo.Log.Builder builderForValue)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### addAllLog

      ```
      public Response.TransactionInfo.Builder addAllLog(java.lang.Iterable<? extends Response.TransactionInfo.Log> values)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### clearLog

      ```
      public Response.TransactionInfo.Builder clearLog()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### removeLog

      ```
      public Response.TransactionInfo.Builder removeLog(int index)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### getLogBuilder

      ```
      public Response.TransactionInfo.Log.Builder getLogBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### getLogOrBuilder

      ```
      public Response.TransactionInfo.LogOrBuilder getLogOrBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`

      Specified by:
      :   `getLogOrBuilder` in interface `Response.TransactionInfoOrBuilder`
    - #### getLogOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionInfo.LogOrBuilder> getLogOrBuilderList()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`

      Specified by:
      :   `getLogOrBuilderList` in interface `Response.TransactionInfoOrBuilder`
    - #### addLogBuilder

      ```
      public Response.TransactionInfo.Log.Builder addLogBuilder()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### addLogBuilder

      ```
      public Response.TransactionInfo.Log.Builder addLogBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### getLogBuilderList

      ```
      public java.util.List<Response.TransactionInfo.Log.Builder> getLogBuilderList()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### getResultValue

      ```
      public int getResultValue()
      ```

      `.protocol.TransactionInfo.code result = 9;`

      Specified by:
      :   `getResultValue` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The enum numeric value on the wire for result.
    - #### setResultValue

      ```
      public Response.TransactionInfo.Builder setResultValue(int value)
      ```

      `.protocol.TransactionInfo.code result = 9;`

      Parameters:
      :   `value` - The enum numeric value on the wire for result to set.

      Returns:
      :   This builder for chaining.
    - #### getResult

      ```
      public Response.TransactionInfo.code getResult()
      ```

      `.protocol.TransactionInfo.code result = 9;`

      Specified by:
      :   `getResult` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The result.
    - #### setResult

      ```
      public Response.TransactionInfo.Builder setResult(Response.TransactionInfo.code value)
      ```

      `.protocol.TransactionInfo.code result = 9;`

      Parameters:
      :   `value` - The result to set.

      Returns:
      :   This builder for chaining.
    - #### clearResult

      ```
      public Response.TransactionInfo.Builder clearResult()
      ```

      `.protocol.TransactionInfo.code result = 9;`

      Returns:
      :   This builder for chaining.
    - #### getResMessage

      ```
      public com.google.protobuf.ByteString getResMessage()
      ```

      `bytes resMessage = 10;`

      Specified by:
      :   `getResMessage` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The resMessage.
    - #### setResMessage

      ```
      public Response.TransactionInfo.Builder setResMessage(com.google.protobuf.ByteString value)
      ```

      `bytes resMessage = 10;`

      Parameters:
      :   `value` - The resMessage to set.

      Returns:
      :   This builder for chaining.
    - #### clearResMessage

      ```
      public Response.TransactionInfo.Builder clearResMessage()
      ```

      `bytes resMessage = 10;`

      Returns:
      :   This builder for chaining.
    - #### getAssetIssueID

      ```
      public java.lang.String getAssetIssueID()
      ```

      `string assetIssueID = 14;`

      Specified by:
      :   `getAssetIssueID` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The assetIssueID.
    - #### getAssetIssueIDBytes

      ```
      public com.google.protobuf.ByteString getAssetIssueIDBytes()
      ```

      `string assetIssueID = 14;`

      Specified by:
      :   `getAssetIssueIDBytes` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The bytes for assetIssueID.
    - #### setAssetIssueID

      ```
      public Response.TransactionInfo.Builder setAssetIssueID(java.lang.String value)
      ```

      `string assetIssueID = 14;`

      Parameters:
      :   `value` - The assetIssueID to set.

      Returns:
      :   This builder for chaining.
    - #### clearAssetIssueID

      ```
      public Response.TransactionInfo.Builder clearAssetIssueID()
      ```

      `string assetIssueID = 14;`

      Returns:
      :   This builder for chaining.
    - #### setAssetIssueIDBytes

      ```
      public Response.TransactionInfo.Builder setAssetIssueIDBytes(com.google.protobuf.ByteString value)
      ```

      `string assetIssueID = 14;`

      Parameters:
      :   `value` - The bytes for assetIssueID to set.

      Returns:
      :   This builder for chaining.
    - #### getWithdrawAmount

      ```
      public long getWithdrawAmount()
      ```

      `int64 withdraw_amount = 15;`

      Specified by:
      :   `getWithdrawAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The withdrawAmount.
    - #### setWithdrawAmount

      ```
      public Response.TransactionInfo.Builder setWithdrawAmount(long value)
      ```

      `int64 withdraw_amount = 15;`

      Parameters:
      :   `value` - The withdrawAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearWithdrawAmount

      ```
      public Response.TransactionInfo.Builder clearWithdrawAmount()
      ```

      `int64 withdraw_amount = 15;`

      Returns:
      :   This builder for chaining.
    - #### getUnfreezeAmount

      ```
      public long getUnfreezeAmount()
      ```

      `int64 unfreeze_amount = 16;`

      Specified by:
      :   `getUnfreezeAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The unfreezeAmount.
    - #### setUnfreezeAmount

      ```
      public Response.TransactionInfo.Builder setUnfreezeAmount(long value)
      ```

      `int64 unfreeze_amount = 16;`

      Parameters:
      :   `value` - The unfreezeAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearUnfreezeAmount

      ```
      public Response.TransactionInfo.Builder clearUnfreezeAmount()
      ```

      `int64 unfreeze_amount = 16;`

      Returns:
      :   This builder for chaining.
    - #### getInternalTransactionsList

      ```
      public java.util.List<Response.InternalTransaction> getInternalTransactionsList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`

      Specified by:
      :   `getInternalTransactionsList` in interface `Response.TransactionInfoOrBuilder`
    - #### getInternalTransactionsCount

      ```
      public int getInternalTransactionsCount()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`

      Specified by:
      :   `getInternalTransactionsCount` in interface `Response.TransactionInfoOrBuilder`
    - #### getInternalTransactions

      ```
      public Response.InternalTransaction getInternalTransactions(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`

      Specified by:
      :   `getInternalTransactions` in interface `Response.TransactionInfoOrBuilder`
    - #### setInternalTransactions

      ```
      public Response.TransactionInfo.Builder setInternalTransactions(int index,
                                                                      Response.InternalTransaction value)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### setInternalTransactions

      ```
      public Response.TransactionInfo.Builder setInternalTransactions(int index,
                                                                      Response.InternalTransaction.Builder builderForValue)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### addInternalTransactions

      ```
      public Response.TransactionInfo.Builder addInternalTransactions(Response.InternalTransaction value)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### addInternalTransactions

      ```
      public Response.TransactionInfo.Builder addInternalTransactions(int index,
                                                                      Response.InternalTransaction value)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### addInternalTransactions

      ```
      public Response.TransactionInfo.Builder addInternalTransactions(Response.InternalTransaction.Builder builderForValue)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### addInternalTransactions

      ```
      public Response.TransactionInfo.Builder addInternalTransactions(int index,
                                                                      Response.InternalTransaction.Builder builderForValue)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### addAllInternalTransactions

      ```
      public Response.TransactionInfo.Builder addAllInternalTransactions(java.lang.Iterable<? extends Response.InternalTransaction> values)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### clearInternalTransactions

      ```
      public Response.TransactionInfo.Builder clearInternalTransactions()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### removeInternalTransactions

      ```
      public Response.TransactionInfo.Builder removeInternalTransactions(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### getInternalTransactionsBuilder

      ```
      public Response.InternalTransaction.Builder getInternalTransactionsBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### getInternalTransactionsOrBuilder

      ```
      public Response.InternalTransactionOrBuilder getInternalTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`

      Specified by:
      :   `getInternalTransactionsOrBuilder` in interface `Response.TransactionInfoOrBuilder`
    - #### getInternalTransactionsOrBuilderList

      ```
      public java.util.List<? extends Response.InternalTransactionOrBuilder> getInternalTransactionsOrBuilderList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`

      Specified by:
      :   `getInternalTransactionsOrBuilderList` in interface `Response.TransactionInfoOrBuilder`
    - #### addInternalTransactionsBuilder

      ```
      public Response.InternalTransaction.Builder addInternalTransactionsBuilder()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### addInternalTransactionsBuilder

      ```
      public Response.InternalTransaction.Builder addInternalTransactionsBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### getInternalTransactionsBuilderList

      ```
      public java.util.List<Response.InternalTransaction.Builder> getInternalTransactionsBuilderList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### getExchangeReceivedAmount

      ```
      public long getExchangeReceivedAmount()
      ```

      `int64 exchange_received_amount = 18;`

      Specified by:
      :   `getExchangeReceivedAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The exchangeReceivedAmount.
    - #### setExchangeReceivedAmount

      ```
      public Response.TransactionInfo.Builder setExchangeReceivedAmount(long value)
      ```

      `int64 exchange_received_amount = 18;`

      Parameters:
      :   `value` - The exchangeReceivedAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeReceivedAmount

      ```
      public Response.TransactionInfo.Builder clearExchangeReceivedAmount()
      ```

      `int64 exchange_received_amount = 18;`

      Returns:
      :   This builder for chaining.
    - #### getExchangeInjectAnotherAmount

      ```
      public long getExchangeInjectAnotherAmount()
      ```

      `int64 exchange_inject_another_amount = 19;`

      Specified by:
      :   `getExchangeInjectAnotherAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The exchangeInjectAnotherAmount.
    - #### setExchangeInjectAnotherAmount

      ```
      public Response.TransactionInfo.Builder setExchangeInjectAnotherAmount(long value)
      ```

      `int64 exchange_inject_another_amount = 19;`

      Parameters:
      :   `value` - The exchangeInjectAnotherAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeInjectAnotherAmount

      ```
      public Response.TransactionInfo.Builder clearExchangeInjectAnotherAmount()
      ```

      `int64 exchange_inject_another_amount = 19;`

      Returns:
      :   This builder for chaining.
    - #### getExchangeWithdrawAnotherAmount

      ```
      public long getExchangeWithdrawAnotherAmount()
      ```

      `int64 exchange_withdraw_another_amount = 20;`

      Specified by:
      :   `getExchangeWithdrawAnotherAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The exchangeWithdrawAnotherAmount.
    - #### setExchangeWithdrawAnotherAmount

      ```
      public Response.TransactionInfo.Builder setExchangeWithdrawAnotherAmount(long value)
      ```

      `int64 exchange_withdraw_another_amount = 20;`

      Parameters:
      :   `value` - The exchangeWithdrawAnotherAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeWithdrawAnotherAmount

      ```
      public Response.TransactionInfo.Builder clearExchangeWithdrawAnotherAmount()
      ```

      `int64 exchange_withdraw_another_amount = 20;`

      Returns:
      :   This builder for chaining.
    - #### getExchangeId

      ```
      public long getExchangeId()
      ```

      `int64 exchange_id = 21;`

      Specified by:
      :   `getExchangeId` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The exchangeId.
    - #### setExchangeId

      ```
      public Response.TransactionInfo.Builder setExchangeId(long value)
      ```

      `int64 exchange_id = 21;`

      Parameters:
      :   `value` - The exchangeId to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeId

      ```
      public Response.TransactionInfo.Builder clearExchangeId()
      ```

      `int64 exchange_id = 21;`

      Returns:
      :   This builder for chaining.
    - #### getShieldedTransactionFee

      ```
      public long getShieldedTransactionFee()
      ```

      `int64 shielded_transaction_fee = 22;`

      Specified by:
      :   `getShieldedTransactionFee` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The shieldedTransactionFee.
    - #### setShieldedTransactionFee

      ```
      public Response.TransactionInfo.Builder setShieldedTransactionFee(long value)
      ```

      `int64 shielded_transaction_fee = 22;`

      Parameters:
      :   `value` - The shieldedTransactionFee to set.

      Returns:
      :   This builder for chaining.
    - #### clearShieldedTransactionFee

      ```
      public Response.TransactionInfo.Builder clearShieldedTransactionFee()
      ```

      `int64 shielded_transaction_fee = 22;`

      Returns:
      :   This builder for chaining.
    - #### getOrderId

      ```
      public com.google.protobuf.ByteString getOrderId()
      ```

      `bytes orderId = 25;`

      Specified by:
      :   `getOrderId` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The orderId.
    - #### setOrderId

      ```
      public Response.TransactionInfo.Builder setOrderId(com.google.protobuf.ByteString value)
      ```

      `bytes orderId = 25;`

      Parameters:
      :   `value` - The orderId to set.

      Returns:
      :   This builder for chaining.
    - #### clearOrderId

      ```
      public Response.TransactionInfo.Builder clearOrderId()
      ```

      `bytes orderId = 25;`

      Returns:
      :   This builder for chaining.
    - #### getOrderDetailsList

      ```
      public java.util.List<Common.MarketOrderDetail> getOrderDetailsList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsList` in interface `Response.TransactionInfoOrBuilder`
    - #### getOrderDetailsCount

      ```
      public int getOrderDetailsCount()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsCount` in interface `Response.TransactionInfoOrBuilder`
    - #### getOrderDetails

      ```
      public Common.MarketOrderDetail getOrderDetails(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetails` in interface `Response.TransactionInfoOrBuilder`
    - #### setOrderDetails

      ```
      public Response.TransactionInfo.Builder setOrderDetails(int index,
                                                              Common.MarketOrderDetail value)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### setOrderDetails

      ```
      public Response.TransactionInfo.Builder setOrderDetails(int index,
                                                              Common.MarketOrderDetail.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addOrderDetails

      ```
      public Response.TransactionInfo.Builder addOrderDetails(Common.MarketOrderDetail value)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addOrderDetails

      ```
      public Response.TransactionInfo.Builder addOrderDetails(int index,
                                                              Common.MarketOrderDetail value)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addOrderDetails

      ```
      public Response.TransactionInfo.Builder addOrderDetails(Common.MarketOrderDetail.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addOrderDetails

      ```
      public Response.TransactionInfo.Builder addOrderDetails(int index,
                                                              Common.MarketOrderDetail.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addAllOrderDetails

      ```
      public Response.TransactionInfo.Builder addAllOrderDetails(java.lang.Iterable<? extends Common.MarketOrderDetail> values)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### clearOrderDetails

      ```
      public Response.TransactionInfo.Builder clearOrderDetails()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### removeOrderDetails

      ```
      public Response.TransactionInfo.Builder removeOrderDetails(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### getOrderDetailsBuilder

      ```
      public Common.MarketOrderDetail.Builder getOrderDetailsBuilder(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### getOrderDetailsOrBuilder

      ```
      public Common.MarketOrderDetailOrBuilder getOrderDetailsOrBuilder(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsOrBuilder` in interface `Response.TransactionInfoOrBuilder`
    - #### getOrderDetailsOrBuilderList

      ```
      public java.util.List<? extends Common.MarketOrderDetailOrBuilder> getOrderDetailsOrBuilderList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsOrBuilderList` in interface `Response.TransactionInfoOrBuilder`
    - #### addOrderDetailsBuilder

      ```
      public Common.MarketOrderDetail.Builder addOrderDetailsBuilder()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addOrderDetailsBuilder

      ```
      public Common.MarketOrderDetail.Builder addOrderDetailsBuilder(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### getOrderDetailsBuilderList

      ```
      public java.util.List<Common.MarketOrderDetail.Builder> getOrderDetailsBuilderList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### getPackingFee

      ```
      public long getPackingFee()
      ```

      `int64 packingFee = 27;`

      Specified by:
      :   `getPackingFee` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The packingFee.
    - #### setPackingFee

      ```
      public Response.TransactionInfo.Builder setPackingFee(long value)
      ```

      `int64 packingFee = 27;`

      Parameters:
      :   `value` - The packingFee to set.

      Returns:
      :   This builder for chaining.
    - #### clearPackingFee

      ```
      public Response.TransactionInfo.Builder clearPackingFee()
      ```

      `int64 packingFee = 27;`

      Returns:
      :   This builder for chaining.
    - #### getWithdrawExpireAmount

      ```
      public long getWithdrawExpireAmount()
      ```

      `int64 withdraw_expire_amount = 28;`

      Specified by:
      :   `getWithdrawExpireAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The withdrawExpireAmount.
    - #### setWithdrawExpireAmount

      ```
      public Response.TransactionInfo.Builder setWithdrawExpireAmount(long value)
      ```

      `int64 withdraw_expire_amount = 28;`

      Parameters:
      :   `value` - The withdrawExpireAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearWithdrawExpireAmount

      ```
      public Response.TransactionInfo.Builder clearWithdrawExpireAmount()
      ```

      `int64 withdraw_expire_amount = 28;`

      Returns:
      :   This builder for chaining.
    - #### getCancelUnfreezeV2AmountCount

      ```
      public int getCancelUnfreezeV2AmountCount()
      ```

      Description copied from interface: `Response.TransactionInfoOrBuilder`

      `map<string, int64> cancel_unfreezeV2_amount = 29;`

      Specified by:
      :   `getCancelUnfreezeV2AmountCount` in interface `Response.TransactionInfoOrBuilder`
    - #### containsCancelUnfreezeV2Amount

      ```
      public boolean containsCancelUnfreezeV2Amount(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`

      Specified by:
      :   `containsCancelUnfreezeV2Amount` in interface `Response.TransactionInfoOrBuilder`
    - #### getCancelUnfreezeV2Amount

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getCancelUnfreezeV2Amount()
      ```

      Deprecated.

      Use [`getCancelUnfreezeV2AmountMap()`](../../../../org/tron/trident/proto/Response.TransactionInfo.Builder.html#getCancelUnfreezeV2AmountMap--) instead.

      Specified by:
      :   `getCancelUnfreezeV2Amount` in interface `Response.TransactionInfoOrBuilder`
    - #### getCancelUnfreezeV2AmountMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getCancelUnfreezeV2AmountMap()
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`

      Specified by:
      :   `getCancelUnfreezeV2AmountMap` in interface `Response.TransactionInfoOrBuilder`
    - #### getCancelUnfreezeV2AmountOrDefault

      ```
      public long getCancelUnfreezeV2AmountOrDefault(java.lang.String key,
                                                     long defaultValue)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`

      Specified by:
      :   `getCancelUnfreezeV2AmountOrDefault` in interface `Response.TransactionInfoOrBuilder`
    - #### getCancelUnfreezeV2AmountOrThrow

      ```
      public long getCancelUnfreezeV2AmountOrThrow(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`

      Specified by:
      :   `getCancelUnfreezeV2AmountOrThrow` in interface `Response.TransactionInfoOrBuilder`
    - #### clearCancelUnfreezeV2Amount

      ```
      public Response.TransactionInfo.Builder clearCancelUnfreezeV2Amount()
      ```
    - #### removeCancelUnfreezeV2Amount

      ```
      public Response.TransactionInfo.Builder removeCancelUnfreezeV2Amount(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`
    - #### getMutableCancelUnfreezeV2Amount

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableCancelUnfreezeV2Amount()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putCancelUnfreezeV2Amount

      ```
      public Response.TransactionInfo.Builder putCancelUnfreezeV2Amount(java.lang.String key,
                                                                        long value)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`
    - #### putAllCancelUnfreezeV2Amount

      ```
      public Response.TransactionInfo.Builder putAllCancelUnfreezeV2Amount(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`
    - #### setUnknownFields

      ```
      public final Response.TransactionInfo.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionInfo.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Builder>`