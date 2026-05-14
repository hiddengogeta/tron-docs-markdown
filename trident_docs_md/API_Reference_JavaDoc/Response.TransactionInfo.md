

org.tron.trident.proto

## Class Response.TransactionInfo

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.TransactionInfo

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.TransactionInfoOrBuilder](../../../../org/tron/trident/proto/Response.TransactionInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionInfo
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.TransactionInfoOrBuilder
  ```

  Protobuf type `protocol.TransactionInfo`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.TransactionInfo)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.TransactionInfo.Builder` Protobuf type `protocol.TransactionInfo` |
    | `static class` | `Response.TransactionInfo.code` Protobuf enum `protocol.TransactionInfo.code` |
    | `static class` | `Response.TransactionInfo.Log` Protobuf type `protocol.TransactionInfo.Log` |
    | `static interface` | `Response.TransactionInfo.LogOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ASSETISSUEID_FIELD_NUMBER` |
    | `static int` | `BLOCKNUMBER_FIELD_NUMBER` |
    | `static int` | `BLOCKTIMESTAMP_FIELD_NUMBER` |
    | `static int` | `CANCEL_UNFREEZEV2_AMOUNT_FIELD_NUMBER` |
    | `static int` | `CONTRACT_ADDRESS_FIELD_NUMBER` |
    | `static int` | `CONTRACTRESULT_FIELD_NUMBER` |
    | `static int` | `EXCHANGE_ID_FIELD_NUMBER` |
    | `static int` | `EXCHANGE_INJECT_ANOTHER_AMOUNT_FIELD_NUMBER` |
    | `static int` | `EXCHANGE_RECEIVED_AMOUNT_FIELD_NUMBER` |
    | `static int` | `EXCHANGE_WITHDRAW_ANOTHER_AMOUNT_FIELD_NUMBER` |
    | `static int` | `FEE_FIELD_NUMBER` |
    | `static int` | `ID_FIELD_NUMBER` |
    | `static int` | `INTERNAL_TRANSACTIONS_FIELD_NUMBER` |
    | `static int` | `LOG_FIELD_NUMBER` |
    | `static int` | `ORDERDETAILS_FIELD_NUMBER` |
    | `static int` | `ORDERID_FIELD_NUMBER` |
    | `static int` | `PACKINGFEE_FIELD_NUMBER` |
    | `static int` | `RECEIPT_FIELD_NUMBER` |
    | `static int` | `RESMESSAGE_FIELD_NUMBER` |
    | `static int` | `RESULT_FIELD_NUMBER` |
    | `static int` | `SHIELDED_TRANSACTION_FEE_FIELD_NUMBER` |
    | `static int` | `UNFREEZE_AMOUNT_FIELD_NUMBER` |
    | `static int` | `WITHDRAW_AMOUNT_FIELD_NUMBER` |
    | `static int` | `WITHDRAW_EXPIRE_AMOUNT_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsCancelUnfreezeV2Amount(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `boolean` | `equals(java.lang.Object obj)` |
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
    | `static Response.TransactionInfo` | `getDefaultInstance()` |
    | `Response.TransactionInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getExchangeId()` `int64 exchange_id = 21;` |
    | `long` | `getExchangeInjectAnotherAmount()` `int64 exchange_inject_another_amount = 19;` |
    | `long` | `getExchangeReceivedAmount()` `int64 exchange_received_amount = 18;` |
    | `long` | `getExchangeWithdrawAnotherAmount()` `int64 exchange_withdraw_another_amount = 20;` |
    | `long` | `getFee()` `int64 fee = 2;` |
    | `com.google.protobuf.ByteString` | `getId()` `bytes id = 1;` |
    | `Response.InternalTransaction` | `getInternalTransactions(int index)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `int` | `getInternalTransactionsCount()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `java.util.List<Response.InternalTransaction>` | `getInternalTransactionsList()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.InternalTransactionOrBuilder` | `getInternalTransactionsOrBuilder(int index)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `java.util.List<? extends Response.InternalTransactionOrBuilder>` | `getInternalTransactionsOrBuilderList()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Log` | `getLog(int index)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `int` | `getLogCount()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `java.util.List<Response.TransactionInfo.Log>` | `getLogList()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.LogOrBuilder` | `getLogOrBuilder(int index)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `java.util.List<? extends Response.TransactionInfo.LogOrBuilder>` | `getLogOrBuilderList()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Common.MarketOrderDetail` | `getOrderDetails(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `int` | `getOrderDetailsCount()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<Common.MarketOrderDetail>` | `getOrderDetailsList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetailOrBuilder` | `getOrderDetailsOrBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<? extends Common.MarketOrderDetailOrBuilder>` | `getOrderDetailsOrBuilderList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `com.google.protobuf.ByteString` | `getOrderId()` `bytes orderId = 25;` |
    | `long` | `getPackingFee()` `int64 packingFee = 27;` |
    | `com.google.protobuf.Parser<Response.TransactionInfo>` | `getParserForType()` |
    | `Response.ResourceReceipt` | `getReceipt()` `.protocol.ResourceReceipt receipt = 7;` |
    | `Response.ResourceReceiptOrBuilder` | `getReceiptOrBuilder()` `.protocol.ResourceReceipt receipt = 7;` |
    | `com.google.protobuf.ByteString` | `getResMessage()` `bytes resMessage = 10;` |
    | `Response.TransactionInfo.code` | `getResult()` `.protocol.TransactionInfo.code result = 9;` |
    | `int` | `getResultValue()` `.protocol.TransactionInfo.code result = 9;` |
    | `int` | `getSerializedSize()` |
    | `long` | `getShieldedTransactionFee()` `int64 shielded_transaction_fee = 22;` |
    | `long` | `getUnfreezeAmount()` `int64 unfreeze_amount = 16;` |
    | `long` | `getWithdrawAmount()` `int64 withdraw_amount = 15;` |
    | `long` | `getWithdrawExpireAmount()` `int64 withdraw_expire_amount = 28;` |
    | `int` | `hashCode()` |
    | `boolean` | `hasReceipt()` `.protocol.ResourceReceipt receipt = 7;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `static Response.TransactionInfo.Builder` | `newBuilder()` |
    | `static Response.TransactionInfo.Builder` | `newBuilder(Response.TransactionInfo prototype)` |
    | `Response.TransactionInfo.Builder` | `newBuilderForType()` |
    | `protected Response.TransactionInfo.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.TransactionInfo` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.TransactionInfo` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionInfo` | `parseFrom(byte[] data)` |
    | `static Response.TransactionInfo` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionInfo` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.TransactionInfo` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionInfo` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.TransactionInfo` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionInfo` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.TransactionInfo` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionInfo` | `parseFrom(java.io.InputStream input)` |
    | `static Response.TransactionInfo` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.TransactionInfo>` | `parser()` |
    | `Response.TransactionInfo.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage

      `findInitializationErrors, getInitializationErrorString, hashBoolean, hashEnum, hashEnumList, hashFields, hashLong, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite

      `addAll, addAll, checkByteStringIsUtf8, toByteArray, toByteString, writeDelimitedTo, writeTo`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLite

      `toByteArray, toByteString, writeDelimitedTo, writeTo`

* + ### Field Detail

    - #### ID\_FIELD\_NUMBER

      ```
      public static final int ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.ID_FIELD_NUMBER)
    - #### FEE\_FIELD\_NUMBER

      ```
      public static final int FEE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.FEE_FIELD_NUMBER)
    - #### BLOCKNUMBER\_FIELD\_NUMBER

      ```
      public static final int BLOCKNUMBER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.BLOCKNUMBER_FIELD_NUMBER)
    - #### BLOCKTIMESTAMP\_FIELD\_NUMBER

      ```
      public static final int BLOCKTIMESTAMP_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.BLOCKTIMESTAMP_FIELD_NUMBER)
    - #### CONTRACTRESULT\_FIELD\_NUMBER

      ```
      public static final int CONTRACTRESULT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.CONTRACTRESULT_FIELD_NUMBER)
    - #### CONTRACT\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int CONTRACT_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.CONTRACT_ADDRESS_FIELD_NUMBER)
    - #### RECEIPT\_FIELD\_NUMBER

      ```
      public static final int RECEIPT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.RECEIPT_FIELD_NUMBER)
    - #### LOG\_FIELD\_NUMBER

      ```
      public static final int LOG_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.LOG_FIELD_NUMBER)
    - #### RESULT\_FIELD\_NUMBER

      ```
      public static final int RESULT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.RESULT_FIELD_NUMBER)
    - #### RESMESSAGE\_FIELD\_NUMBER

      ```
      public static final int RESMESSAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.RESMESSAGE_FIELD_NUMBER)
    - #### ASSETISSUEID\_FIELD\_NUMBER

      ```
      public static final int ASSETISSUEID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.ASSETISSUEID_FIELD_NUMBER)
    - #### WITHDRAW\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int WITHDRAW_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.WITHDRAW_AMOUNT_FIELD_NUMBER)
    - #### UNFREEZE\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int UNFREEZE_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.UNFREEZE_AMOUNT_FIELD_NUMBER)
    - #### INTERNAL\_TRANSACTIONS\_FIELD\_NUMBER

      ```
      public static final int INTERNAL_TRANSACTIONS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.INTERNAL_TRANSACTIONS_FIELD_NUMBER)
    - #### EXCHANGE\_RECEIVED\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int EXCHANGE_RECEIVED_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.EXCHANGE_RECEIVED_AMOUNT_FIELD_NUMBER)
    - #### EXCHANGE\_INJECT\_ANOTHER\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int EXCHANGE_INJECT_ANOTHER_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.EXCHANGE_INJECT_ANOTHER_AMOUNT_FIELD_NUMBER)
    - #### EXCHANGE\_WITHDRAW\_ANOTHER\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int EXCHANGE_WITHDRAW_ANOTHER_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.EXCHANGE_WITHDRAW_ANOTHER_AMOUNT_FIELD_NUMBER)
    - #### EXCHANGE\_ID\_FIELD\_NUMBER

      ```
      public static final int EXCHANGE_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.EXCHANGE_ID_FIELD_NUMBER)
    - #### SHIELDED\_TRANSACTION\_FEE\_FIELD\_NUMBER

      ```
      public static final int SHIELDED_TRANSACTION_FEE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.SHIELDED_TRANSACTION_FEE_FIELD_NUMBER)
    - #### ORDERID\_FIELD\_NUMBER

      ```
      public static final int ORDERID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.ORDERID_FIELD_NUMBER)
    - #### ORDERDETAILS\_FIELD\_NUMBER

      ```
      public static final int ORDERDETAILS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.ORDERDETAILS_FIELD_NUMBER)
    - #### PACKINGFEE\_FIELD\_NUMBER

      ```
      public static final int PACKINGFEE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.PACKINGFEE_FIELD_NUMBER)
    - #### WITHDRAW\_EXPIRE\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int WITHDRAW_EXPIRE_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.WITHDRAW_EXPIRE_AMOUNT_FIELD_NUMBER)
    - #### CANCEL\_UNFREEZEV2\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int CANCEL_UNFREEZEV2_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.CANCEL_UNFREEZEV2_AMOUNT_FIELD_NUMBER)
  + ### Method Detail

    - #### newInstance

      ```
      protected java.lang.Object newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)
      ```

      Overrides:
      :   `newInstance` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getId

      ```
      public com.google.protobuf.ByteString getId()
      ```

      `bytes id = 1;`

      Specified by:
      :   `getId` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The id.
    - #### getFee

      ```
      public long getFee()
      ```

      `int64 fee = 2;`

      Specified by:
      :   `getFee` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The fee.
    - #### getBlockNumber

      ```
      public long getBlockNumber()
      ```

      `int64 blockNumber = 3;`

      Specified by:
      :   `getBlockNumber` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The blockNumber.
    - #### getBlockTimeStamp

      ```
      public long getBlockTimeStamp()
      ```

      `int64 blockTimeStamp = 4;`

      Specified by:
      :   `getBlockTimeStamp` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The blockTimeStamp.
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
    - #### getContractAddress

      ```
      public com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 6;`

      Specified by:
      :   `getContractAddress` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The contractAddress.
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
    - #### getLogOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionInfo.LogOrBuilder> getLogOrBuilderList()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`

      Specified by:
      :   `getLogOrBuilderList` in interface `Response.TransactionInfoOrBuilder`
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
    - #### getLogOrBuilder

      ```
      public Response.TransactionInfo.LogOrBuilder getLogOrBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`

      Specified by:
      :   `getLogOrBuilder` in interface `Response.TransactionInfoOrBuilder`
    - #### getResultValue

      ```
      public int getResultValue()
      ```

      `.protocol.TransactionInfo.code result = 9;`

      Specified by:
      :   `getResultValue` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The enum numeric value on the wire for result.
    - #### getResult

      ```
      public Response.TransactionInfo.code getResult()
      ```

      `.protocol.TransactionInfo.code result = 9;`

      Specified by:
      :   `getResult` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The result.
    - #### getResMessage

      ```
      public com.google.protobuf.ByteString getResMessage()
      ```

      `bytes resMessage = 10;`

      Specified by:
      :   `getResMessage` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The resMessage.
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
    - #### getWithdrawAmount

      ```
      public long getWithdrawAmount()
      ```

      `int64 withdraw_amount = 15;`

      Specified by:
      :   `getWithdrawAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The withdrawAmount.
    - #### getUnfreezeAmount

      ```
      public long getUnfreezeAmount()
      ```

      `int64 unfreeze_amount = 16;`

      Specified by:
      :   `getUnfreezeAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The unfreezeAmount.
    - #### getInternalTransactionsList

      ```
      public java.util.List<Response.InternalTransaction> getInternalTransactionsList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`

      Specified by:
      :   `getInternalTransactionsList` in interface `Response.TransactionInfoOrBuilder`
    - #### getInternalTransactionsOrBuilderList

      ```
      public java.util.List<? extends Response.InternalTransactionOrBuilder> getInternalTransactionsOrBuilderList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`

      Specified by:
      :   `getInternalTransactionsOrBuilderList` in interface `Response.TransactionInfoOrBuilder`
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
    - #### getInternalTransactionsOrBuilder

      ```
      public Response.InternalTransactionOrBuilder getInternalTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`

      Specified by:
      :   `getInternalTransactionsOrBuilder` in interface `Response.TransactionInfoOrBuilder`
    - #### getExchangeReceivedAmount

      ```
      public long getExchangeReceivedAmount()
      ```

      `int64 exchange_received_amount = 18;`

      Specified by:
      :   `getExchangeReceivedAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The exchangeReceivedAmount.
    - #### getExchangeInjectAnotherAmount

      ```
      public long getExchangeInjectAnotherAmount()
      ```

      `int64 exchange_inject_another_amount = 19;`

      Specified by:
      :   `getExchangeInjectAnotherAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The exchangeInjectAnotherAmount.
    - #### getExchangeWithdrawAnotherAmount

      ```
      public long getExchangeWithdrawAnotherAmount()
      ```

      `int64 exchange_withdraw_another_amount = 20;`

      Specified by:
      :   `getExchangeWithdrawAnotherAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The exchangeWithdrawAnotherAmount.
    - #### getExchangeId

      ```
      public long getExchangeId()
      ```

      `int64 exchange_id = 21;`

      Specified by:
      :   `getExchangeId` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The exchangeId.
    - #### getShieldedTransactionFee

      ```
      public long getShieldedTransactionFee()
      ```

      `int64 shielded_transaction_fee = 22;`

      Specified by:
      :   `getShieldedTransactionFee` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The shieldedTransactionFee.
    - #### getOrderId

      ```
      public com.google.protobuf.ByteString getOrderId()
      ```

      `bytes orderId = 25;`

      Specified by:
      :   `getOrderId` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The orderId.
    - #### getOrderDetailsList

      ```
      public java.util.List<Common.MarketOrderDetail> getOrderDetailsList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsList` in interface `Response.TransactionInfoOrBuilder`
    - #### getOrderDetailsOrBuilderList

      ```
      public java.util.List<? extends Common.MarketOrderDetailOrBuilder> getOrderDetailsOrBuilderList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsOrBuilderList` in interface `Response.TransactionInfoOrBuilder`
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
    - #### getOrderDetailsOrBuilder

      ```
      public Common.MarketOrderDetailOrBuilder getOrderDetailsOrBuilder(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsOrBuilder` in interface `Response.TransactionInfoOrBuilder`
    - #### getPackingFee

      ```
      public long getPackingFee()
      ```

      `int64 packingFee = 27;`

      Specified by:
      :   `getPackingFee` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The packingFee.
    - #### getWithdrawExpireAmount

      ```
      public long getWithdrawExpireAmount()
      ```

      `int64 withdraw_expire_amount = 28;`

      Specified by:
      :   `getWithdrawExpireAmount` in interface `Response.TransactionInfoOrBuilder`

      Returns:
      :   The withdrawExpireAmount.
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

      Use [`getCancelUnfreezeV2AmountMap()`](../../../../org/tron/trident/proto/Response.TransactionInfo.html#getCancelUnfreezeV2AmountMap--) instead.

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
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3`
    - #### writeTo

      ```
      public void writeTo(com.google.protobuf.CodedOutputStream output)
                   throws java.io.IOException
      ```

      Specified by:
      :   `writeTo` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `writeTo` in class `com.google.protobuf.GeneratedMessageV3`

      Throws:
      :   `java.io.IOException`
    - #### getSerializedSize

      ```
      public int getSerializedSize()
      ```

      Specified by:
      :   `getSerializedSize` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getSerializedSize` in class `com.google.protobuf.GeneratedMessageV3`
    - #### equals

      ```
      public boolean equals(java.lang.Object obj)
      ```

      Specified by:
      :   `equals` in interface `com.google.protobuf.Message`

      Overrides:
      :   `equals` in class `com.google.protobuf.AbstractMessage`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Specified by:
      :   `hashCode` in interface `com.google.protobuf.Message`

      Overrides:
      :   `hashCode` in class `com.google.protobuf.AbstractMessage`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(java.nio.ByteBuffer data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(java.nio.ByteBuffer data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(com.google.protobuf.ByteString data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(com.google.protobuf.ByteString data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(byte[] data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(byte[] data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(java.io.InputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(java.io.InputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.TransactionInfo parseDelimitedFrom(java.io.InputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.TransactionInfo parseDelimitedFrom(java.io.InputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(com.google.protobuf.CodedInputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionInfo parseFrom(com.google.protobuf.CodedInputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.TransactionInfo.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.TransactionInfo.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.TransactionInfo.Builder newBuilder(Response.TransactionInfo prototype)
      ```
    - #### toBuilder

      ```
      public Response.TransactionInfo.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.TransactionInfo.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.TransactionInfo getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.TransactionInfo> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.TransactionInfo> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`