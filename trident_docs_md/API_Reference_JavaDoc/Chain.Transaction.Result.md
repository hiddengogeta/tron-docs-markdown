

org.tron.trident.proto

## Class Chain.Transaction.Result

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Chain.Transaction.Result

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Chain.Transaction.ResultOrBuilder](../../../../org/tron/trident/proto/Chain.Transaction.ResultOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction](../../../../org/tron/trident/proto/Chain.Transaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.Transaction.Result
  extends com.google.protobuf.GeneratedMessageV3
  implements Chain.Transaction.ResultOrBuilder
  ```

  Protobuf type `protocol.Transaction.Result`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Chain.Transaction.Result)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Chain.Transaction.Result.Builder` Protobuf type `protocol.Transaction.Result` |
    | `static class` | `Chain.Transaction.Result.code` Protobuf enum `protocol.Transaction.Result.code` |
    | `static class` | `Chain.Transaction.Result.contractResult` Protobuf enum `protocol.Transaction.Result.contractResult` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ASSETISSUEID_FIELD_NUMBER` |
    | `static int` | `CANCEL_UNFREEZEV2_AMOUNT_FIELD_NUMBER` |
    | `static int` | `CONTRACTRET_FIELD_NUMBER` |
    | `static int` | `EXCHANGE_ID_FIELD_NUMBER` |
    | `static int` | `EXCHANGE_INJECT_ANOTHER_AMOUNT_FIELD_NUMBER` |
    | `static int` | `EXCHANGE_RECEIVED_AMOUNT_FIELD_NUMBER` |
    | `static int` | `EXCHANGE_WITHDRAW_ANOTHER_AMOUNT_FIELD_NUMBER` |
    | `static int` | `FEE_FIELD_NUMBER` |
    | `static int` | `ORDERDETAILS_FIELD_NUMBER` |
    | `static int` | `ORDERID_FIELD_NUMBER` |
    | `static int` | `RET_FIELD_NUMBER` |
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
    | `boolean` | `containsCancelUnfreezeV2Amount(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `java.lang.String` | `getAssetIssueID()` `string assetIssueID = 14;` |
    | `com.google.protobuf.ByteString` | `getAssetIssueIDBytes()` `string assetIssueID = 14;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2Amount()` Deprecated. |
    | `int` | `getCancelUnfreezeV2AmountCount()` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2AmountMap()` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `long` | `getCancelUnfreezeV2AmountOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `long` | `getCancelUnfreezeV2AmountOrThrow(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `Chain.Transaction.Result.contractResult` | `getContractRet()` `.protocol.Transaction.Result.contractResult contractRet = 3;` |
    | `int` | `getContractRetValue()` `.protocol.Transaction.Result.contractResult contractRet = 3;` |
    | `static Chain.Transaction.Result` | `getDefaultInstance()` |
    | `Chain.Transaction.Result` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getExchangeId()` `int64 exchange_id = 21;` |
    | `long` | `getExchangeInjectAnotherAmount()` `int64 exchange_inject_another_amount = 19;` |
    | `long` | `getExchangeReceivedAmount()` `int64 exchange_received_amount = 18;` |
    | `long` | `getExchangeWithdrawAnotherAmount()` `int64 exchange_withdraw_another_amount = 20;` |
    | `long` | `getFee()` `int64 fee = 1;` |
    | `Common.MarketOrderDetail` | `getOrderDetails(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `int` | `getOrderDetailsCount()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<Common.MarketOrderDetail>` | `getOrderDetailsList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetailOrBuilder` | `getOrderDetailsOrBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<? extends Common.MarketOrderDetailOrBuilder>` | `getOrderDetailsOrBuilderList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `com.google.protobuf.ByteString` | `getOrderId()` `bytes orderId = 25;` |
    | `com.google.protobuf.Parser<Chain.Transaction.Result>` | `getParserForType()` |
    | `Chain.Transaction.Result.code` | `getRet()` `.protocol.Transaction.Result.code ret = 2;` |
    | `int` | `getRetValue()` `.protocol.Transaction.Result.code ret = 2;` |
    | `int` | `getSerializedSize()` |
    | `long` | `getShieldedTransactionFee()` `int64 shielded_transaction_fee = 22;` |
    | `long` | `getUnfreezeAmount()` `int64 unfreeze_amount = 16;` |
    | `long` | `getWithdrawAmount()` `int64 withdraw_amount = 15;` |
    | `long` | `getWithdrawExpireAmount()` `int64 withdraw_expire_amount = 27;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `static Chain.Transaction.Result.Builder` | `newBuilder()` |
    | `static Chain.Transaction.Result.Builder` | `newBuilder(Chain.Transaction.Result prototype)` |
    | `Chain.Transaction.Result.Builder` | `newBuilderForType()` |
    | `protected Chain.Transaction.Result.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Chain.Transaction.Result` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Chain.Transaction.Result` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Result` | `parseFrom(byte[] data)` |
    | `static Chain.Transaction.Result` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Result` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Chain.Transaction.Result` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Result` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Chain.Transaction.Result` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Result` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Chain.Transaction.Result` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Result` | `parseFrom(java.io.InputStream input)` |
    | `static Chain.Transaction.Result` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Chain.Transaction.Result>` | `parser()` |
    | `Chain.Transaction.Result.Builder` | `toBuilder()` |
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

    - #### FEE\_FIELD\_NUMBER

      ```
      public static final int FEE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.FEE_FIELD_NUMBER)
    - #### RET\_FIELD\_NUMBER

      ```
      public static final int RET_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.RET_FIELD_NUMBER)
    - #### CONTRACTRET\_FIELD\_NUMBER

      ```
      public static final int CONTRACTRET_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.CONTRACTRET_FIELD_NUMBER)
    - #### ASSETISSUEID\_FIELD\_NUMBER

      ```
      public static final int ASSETISSUEID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.ASSETISSUEID_FIELD_NUMBER)
    - #### WITHDRAW\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int WITHDRAW_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.WITHDRAW_AMOUNT_FIELD_NUMBER)
    - #### UNFREEZE\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int UNFREEZE_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.UNFREEZE_AMOUNT_FIELD_NUMBER)
    - #### EXCHANGE\_RECEIVED\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int EXCHANGE_RECEIVED_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.EXCHANGE_RECEIVED_AMOUNT_FIELD_NUMBER)
    - #### EXCHANGE\_INJECT\_ANOTHER\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int EXCHANGE_INJECT_ANOTHER_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.EXCHANGE_INJECT_ANOTHER_AMOUNT_FIELD_NUMBER)
    - #### EXCHANGE\_WITHDRAW\_ANOTHER\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int EXCHANGE_WITHDRAW_ANOTHER_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.EXCHANGE_WITHDRAW_ANOTHER_AMOUNT_FIELD_NUMBER)
    - #### EXCHANGE\_ID\_FIELD\_NUMBER

      ```
      public static final int EXCHANGE_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.EXCHANGE_ID_FIELD_NUMBER)
    - #### SHIELDED\_TRANSACTION\_FEE\_FIELD\_NUMBER

      ```
      public static final int SHIELDED_TRANSACTION_FEE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.SHIELDED_TRANSACTION_FEE_FIELD_NUMBER)
    - #### ORDERID\_FIELD\_NUMBER

      ```
      public static final int ORDERID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.ORDERID_FIELD_NUMBER)
    - #### ORDERDETAILS\_FIELD\_NUMBER

      ```
      public static final int ORDERDETAILS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.ORDERDETAILS_FIELD_NUMBER)
    - #### WITHDRAW\_EXPIRE\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int WITHDRAW_EXPIRE_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.WITHDRAW_EXPIRE_AMOUNT_FIELD_NUMBER)
    - #### CANCEL\_UNFREEZEV2\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int CANCEL_UNFREEZEV2_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.CANCEL_UNFREEZEV2_AMOUNT_FIELD_NUMBER)
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
    - #### getFee

      ```
      public long getFee()
      ```

      `int64 fee = 1;`

      Specified by:
      :   `getFee` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The fee.
    - #### getRetValue

      ```
      public int getRetValue()
      ```

      `.protocol.Transaction.Result.code ret = 2;`

      Specified by:
      :   `getRetValue` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The enum numeric value on the wire for ret.
    - #### getRet

      ```
      public Chain.Transaction.Result.code getRet()
      ```

      `.protocol.Transaction.Result.code ret = 2;`

      Specified by:
      :   `getRet` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The ret.
    - #### getContractRetValue

      ```
      public int getContractRetValue()
      ```

      `.protocol.Transaction.Result.contractResult contractRet = 3;`

      Specified by:
      :   `getContractRetValue` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The enum numeric value on the wire for contractRet.
    - #### getContractRet

      ```
      public Chain.Transaction.Result.contractResult getContractRet()
      ```

      `.protocol.Transaction.Result.contractResult contractRet = 3;`

      Specified by:
      :   `getContractRet` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The contractRet.
    - #### getAssetIssueID

      ```
      public java.lang.String getAssetIssueID()
      ```

      `string assetIssueID = 14;`

      Specified by:
      :   `getAssetIssueID` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The assetIssueID.
    - #### getAssetIssueIDBytes

      ```
      public com.google.protobuf.ByteString getAssetIssueIDBytes()
      ```

      `string assetIssueID = 14;`

      Specified by:
      :   `getAssetIssueIDBytes` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The bytes for assetIssueID.
    - #### getWithdrawAmount

      ```
      public long getWithdrawAmount()
      ```

      `int64 withdraw_amount = 15;`

      Specified by:
      :   `getWithdrawAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The withdrawAmount.
    - #### getUnfreezeAmount

      ```
      public long getUnfreezeAmount()
      ```

      `int64 unfreeze_amount = 16;`

      Specified by:
      :   `getUnfreezeAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The unfreezeAmount.
    - #### getExchangeReceivedAmount

      ```
      public long getExchangeReceivedAmount()
      ```

      `int64 exchange_received_amount = 18;`

      Specified by:
      :   `getExchangeReceivedAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The exchangeReceivedAmount.
    - #### getExchangeInjectAnotherAmount

      ```
      public long getExchangeInjectAnotherAmount()
      ```

      `int64 exchange_inject_another_amount = 19;`

      Specified by:
      :   `getExchangeInjectAnotherAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The exchangeInjectAnotherAmount.
    - #### getExchangeWithdrawAnotherAmount

      ```
      public long getExchangeWithdrawAnotherAmount()
      ```

      `int64 exchange_withdraw_another_amount = 20;`

      Specified by:
      :   `getExchangeWithdrawAnotherAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The exchangeWithdrawAnotherAmount.
    - #### getExchangeId

      ```
      public long getExchangeId()
      ```

      `int64 exchange_id = 21;`

      Specified by:
      :   `getExchangeId` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The exchangeId.
    - #### getShieldedTransactionFee

      ```
      public long getShieldedTransactionFee()
      ```

      `int64 shielded_transaction_fee = 22;`

      Specified by:
      :   `getShieldedTransactionFee` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The shieldedTransactionFee.
    - #### getOrderId

      ```
      public com.google.protobuf.ByteString getOrderId()
      ```

      `bytes orderId = 25;`

      Specified by:
      :   `getOrderId` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The orderId.
    - #### getOrderDetailsList

      ```
      public java.util.List<Common.MarketOrderDetail> getOrderDetailsList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsList` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getOrderDetailsOrBuilderList

      ```
      public java.util.List<? extends Common.MarketOrderDetailOrBuilder> getOrderDetailsOrBuilderList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsOrBuilderList` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getOrderDetailsCount

      ```
      public int getOrderDetailsCount()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsCount` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getOrderDetails

      ```
      public Common.MarketOrderDetail getOrderDetails(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetails` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getOrderDetailsOrBuilder

      ```
      public Common.MarketOrderDetailOrBuilder getOrderDetailsOrBuilder(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsOrBuilder` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getWithdrawExpireAmount

      ```
      public long getWithdrawExpireAmount()
      ```

      `int64 withdraw_expire_amount = 27;`

      Specified by:
      :   `getWithdrawExpireAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The withdrawExpireAmount.
    - #### getCancelUnfreezeV2AmountCount

      ```
      public int getCancelUnfreezeV2AmountCount()
      ```

      Description copied from interface: `Chain.Transaction.ResultOrBuilder`

      `map<string, int64> cancel_unfreezeV2_amount = 28;`

      Specified by:
      :   `getCancelUnfreezeV2AmountCount` in interface `Chain.Transaction.ResultOrBuilder`
    - #### containsCancelUnfreezeV2Amount

      ```
      public boolean containsCancelUnfreezeV2Amount(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`

      Specified by:
      :   `containsCancelUnfreezeV2Amount` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getCancelUnfreezeV2Amount

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getCancelUnfreezeV2Amount()
      ```

      Deprecated.

      Use [`getCancelUnfreezeV2AmountMap()`](../../../../org/tron/trident/proto/Chain.Transaction.Result.html#getCancelUnfreezeV2AmountMap--) instead.

      Specified by:
      :   `getCancelUnfreezeV2Amount` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getCancelUnfreezeV2AmountMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getCancelUnfreezeV2AmountMap()
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`

      Specified by:
      :   `getCancelUnfreezeV2AmountMap` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getCancelUnfreezeV2AmountOrDefault

      ```
      public long getCancelUnfreezeV2AmountOrDefault(java.lang.String key,
                                                     long defaultValue)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`

      Specified by:
      :   `getCancelUnfreezeV2AmountOrDefault` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getCancelUnfreezeV2AmountOrThrow

      ```
      public long getCancelUnfreezeV2AmountOrThrow(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`

      Specified by:
      :   `getCancelUnfreezeV2AmountOrThrow` in interface `Chain.Transaction.ResultOrBuilder`
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
      public static Chain.Transaction.Result parseFrom(java.nio.ByteBuffer data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Result parseFrom(java.nio.ByteBuffer data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Result parseFrom(com.google.protobuf.ByteString data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Result parseFrom(com.google.protobuf.ByteString data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Result parseFrom(byte[] data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Result parseFrom(byte[] data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Result parseFrom(java.io.InputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Result parseFrom(java.io.InputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.Transaction.Result parseDelimitedFrom(java.io.InputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.Transaction.Result parseDelimitedFrom(java.io.InputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Result parseFrom(com.google.protobuf.CodedInputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Result parseFrom(com.google.protobuf.CodedInputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Chain.Transaction.Result.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Chain.Transaction.Result.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Chain.Transaction.Result.Builder newBuilder(Chain.Transaction.Result prototype)
      ```
    - #### toBuilder

      ```
      public Chain.Transaction.Result.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Chain.Transaction.Result.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Chain.Transaction.Result getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Chain.Transaction.Result> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Chain.Transaction.Result> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Chain.Transaction.Result getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`