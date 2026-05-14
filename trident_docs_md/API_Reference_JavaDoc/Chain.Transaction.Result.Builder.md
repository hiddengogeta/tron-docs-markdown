

org.tron.trident.proto

## Class Chain.Transaction.Result.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Chain.Transaction.Result.Builder](../../../../org/tron/trident/proto/Chain.Transaction.Result.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Chain.Transaction.Result.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Chain.Transaction.ResultOrBuilder](../../../../org/tron/trident/proto/Chain.Transaction.ResultOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction.Result](../../../../org/tron/trident/proto/Chain.Transaction.Result.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.Transaction.Result.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>
  implements Chain.Transaction.ResultOrBuilder
  ```

  Protobuf type `protocol.Transaction.Result`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Chain.Transaction.Result.Builder` | `addAllOrderDetails(java.lang.Iterable<? extends Common.MarketOrderDetail> values)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Chain.Transaction.Result.Builder` | `addOrderDetails(Common.MarketOrderDetail.Builder builderForValue)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Chain.Transaction.Result.Builder` | `addOrderDetails(Common.MarketOrderDetail value)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Chain.Transaction.Result.Builder` | `addOrderDetails(int index, Common.MarketOrderDetail.Builder builderForValue)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Chain.Transaction.Result.Builder` | `addOrderDetails(int index, Common.MarketOrderDetail value)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetail.Builder` | `addOrderDetailsBuilder()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetail.Builder` | `addOrderDetailsBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Chain.Transaction.Result.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Transaction.Result` | `build()` |
    | `Chain.Transaction.Result` | `buildPartial()` |
    | `Chain.Transaction.Result.Builder` | `clear()` |
    | `Chain.Transaction.Result.Builder` | `clearAssetIssueID()` `string assetIssueID = 14;` |
    | `Chain.Transaction.Result.Builder` | `clearCancelUnfreezeV2Amount()` |
    | `Chain.Transaction.Result.Builder` | `clearContractRet()` `.protocol.Transaction.Result.contractResult contractRet = 3;` |
    | `Chain.Transaction.Result.Builder` | `clearExchangeId()` `int64 exchange_id = 21;` |
    | `Chain.Transaction.Result.Builder` | `clearExchangeInjectAnotherAmount()` `int64 exchange_inject_another_amount = 19;` |
    | `Chain.Transaction.Result.Builder` | `clearExchangeReceivedAmount()` `int64 exchange_received_amount = 18;` |
    | `Chain.Transaction.Result.Builder` | `clearExchangeWithdrawAnotherAmount()` `int64 exchange_withdraw_another_amount = 20;` |
    | `Chain.Transaction.Result.Builder` | `clearFee()` `int64 fee = 1;` |
    | `Chain.Transaction.Result.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Chain.Transaction.Result.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Chain.Transaction.Result.Builder` | `clearOrderDetails()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Chain.Transaction.Result.Builder` | `clearOrderId()` `bytes orderId = 25;` |
    | `Chain.Transaction.Result.Builder` | `clearRet()` `.protocol.Transaction.Result.code ret = 2;` |
    | `Chain.Transaction.Result.Builder` | `clearShieldedTransactionFee()` `int64 shielded_transaction_fee = 22;` |
    | `Chain.Transaction.Result.Builder` | `clearUnfreezeAmount()` `int64 unfreeze_amount = 16;` |
    | `Chain.Transaction.Result.Builder` | `clearWithdrawAmount()` `int64 withdraw_amount = 15;` |
    | `Chain.Transaction.Result.Builder` | `clearWithdrawExpireAmount()` `int64 withdraw_expire_amount = 27;` |
    | `Chain.Transaction.Result.Builder` | `clone()` |
    | `boolean` | `containsCancelUnfreezeV2Amount(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `java.lang.String` | `getAssetIssueID()` `string assetIssueID = 14;` |
    | `com.google.protobuf.ByteString` | `getAssetIssueIDBytes()` `string assetIssueID = 14;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2Amount()` Deprecated. |
    | `int` | `getCancelUnfreezeV2AmountCount()` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2AmountMap()` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `long` | `getCancelUnfreezeV2AmountOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `long` | `getCancelUnfreezeV2AmountOrThrow(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `Chain.Transaction.Result.contractResult` | `getContractRet()` `.protocol.Transaction.Result.contractResult contractRet = 3;` |
    | `int` | `getContractRetValue()` `.protocol.Transaction.Result.contractResult contractRet = 3;` |
    | `Chain.Transaction.Result` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getExchangeId()` `int64 exchange_id = 21;` |
    | `long` | `getExchangeInjectAnotherAmount()` `int64 exchange_inject_another_amount = 19;` |
    | `long` | `getExchangeReceivedAmount()` `int64 exchange_received_amount = 18;` |
    | `long` | `getExchangeWithdrawAnotherAmount()` `int64 exchange_withdraw_another_amount = 20;` |
    | `long` | `getFee()` `int64 fee = 1;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableCancelUnfreezeV2Amount()` Deprecated. |
    | `Common.MarketOrderDetail` | `getOrderDetails(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetail.Builder` | `getOrderDetailsBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<Common.MarketOrderDetail.Builder>` | `getOrderDetailsBuilderList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `int` | `getOrderDetailsCount()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<Common.MarketOrderDetail>` | `getOrderDetailsList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetailOrBuilder` | `getOrderDetailsOrBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<? extends Common.MarketOrderDetailOrBuilder>` | `getOrderDetailsOrBuilderList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `com.google.protobuf.ByteString` | `getOrderId()` `bytes orderId = 25;` |
    | `Chain.Transaction.Result.code` | `getRet()` `.protocol.Transaction.Result.code ret = 2;` |
    | `int` | `getRetValue()` `.protocol.Transaction.Result.code ret = 2;` |
    | `long` | `getShieldedTransactionFee()` `int64 shielded_transaction_fee = 22;` |
    | `long` | `getUnfreezeAmount()` `int64 unfreeze_amount = 16;` |
    | `long` | `getWithdrawAmount()` `int64 withdraw_amount = 15;` |
    | `long` | `getWithdrawExpireAmount()` `int64 withdraw_expire_amount = 27;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMutableMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `Chain.Transaction.Result.Builder` | `mergeFrom(Chain.Transaction.Result other)` |
    | `Chain.Transaction.Result.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Chain.Transaction.Result.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Chain.Transaction.Result.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.Transaction.Result.Builder` | `putAllCancelUnfreezeV2Amount(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `Chain.Transaction.Result.Builder` | `putCancelUnfreezeV2Amount(java.lang.String key, long value)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `Chain.Transaction.Result.Builder` | `removeCancelUnfreezeV2Amount(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `Chain.Transaction.Result.Builder` | `removeOrderDetails(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Chain.Transaction.Result.Builder` | `setAssetIssueID(java.lang.String value)` `string assetIssueID = 14;` |
    | `Chain.Transaction.Result.Builder` | `setAssetIssueIDBytes(com.google.protobuf.ByteString value)` `string assetIssueID = 14;` |
    | `Chain.Transaction.Result.Builder` | `setContractRet(Chain.Transaction.Result.contractResult value)` `.protocol.Transaction.Result.contractResult contractRet = 3;` |
    | `Chain.Transaction.Result.Builder` | `setContractRetValue(int value)` `.protocol.Transaction.Result.contractResult contractRet = 3;` |
    | `Chain.Transaction.Result.Builder` | `setExchangeId(long value)` `int64 exchange_id = 21;` |
    | `Chain.Transaction.Result.Builder` | `setExchangeInjectAnotherAmount(long value)` `int64 exchange_inject_another_amount = 19;` |
    | `Chain.Transaction.Result.Builder` | `setExchangeReceivedAmount(long value)` `int64 exchange_received_amount = 18;` |
    | `Chain.Transaction.Result.Builder` | `setExchangeWithdrawAnotherAmount(long value)` `int64 exchange_withdraw_another_amount = 20;` |
    | `Chain.Transaction.Result.Builder` | `setFee(long value)` `int64 fee = 1;` |
    | `Chain.Transaction.Result.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Transaction.Result.Builder` | `setOrderDetails(int index, Common.MarketOrderDetail.Builder builderForValue)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Chain.Transaction.Result.Builder` | `setOrderDetails(int index, Common.MarketOrderDetail value)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Chain.Transaction.Result.Builder` | `setOrderId(com.google.protobuf.ByteString value)` `bytes orderId = 25;` |
    | `Chain.Transaction.Result.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Chain.Transaction.Result.Builder` | `setRet(Chain.Transaction.Result.code value)` `.protocol.Transaction.Result.code ret = 2;` |
    | `Chain.Transaction.Result.Builder` | `setRetValue(int value)` `.protocol.Transaction.Result.code ret = 2;` |
    | `Chain.Transaction.Result.Builder` | `setShieldedTransactionFee(long value)` `int64 shielded_transaction_fee = 22;` |
    | `Chain.Transaction.Result.Builder` | `setUnfreezeAmount(long value)` `int64 unfreeze_amount = 16;` |
    | `Chain.Transaction.Result.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.Transaction.Result.Builder` | `setWithdrawAmount(long value)` `int64 withdraw_amount = 15;` |
    | `Chain.Transaction.Result.Builder` | `setWithdrawExpireAmount(long value)` `int64 withdraw_expire_amount = 27;` |

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
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### internalGetMutableMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMutableMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### clear

      ```
      public Chain.Transaction.Result.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Chain.Transaction.Result getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Chain.Transaction.Result build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Chain.Transaction.Result buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Chain.Transaction.Result.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### setField

      ```
      public Chain.Transaction.Result.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### clearField

      ```
      public Chain.Transaction.Result.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### clearOneof

      ```
      public Chain.Transaction.Result.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### setRepeatedField

      ```
      public Chain.Transaction.Result.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### addRepeatedField

      ```
      public Chain.Transaction.Result.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.Result.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Transaction.Result.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.Result.Builder mergeFrom(Chain.Transaction.Result other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.Result.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Transaction.Result.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getFee

      ```
      public long getFee()
      ```

      `int64 fee = 1;`

      Specified by:
      :   `getFee` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The fee.
    - #### setFee

      ```
      public Chain.Transaction.Result.Builder setFee(long value)
      ```

      `int64 fee = 1;`

      Parameters:
      :   `value` - The fee to set.

      Returns:
      :   This builder for chaining.
    - #### clearFee

      ```
      public Chain.Transaction.Result.Builder clearFee()
      ```

      `int64 fee = 1;`

      Returns:
      :   This builder for chaining.
    - #### getRetValue

      ```
      public int getRetValue()
      ```

      `.protocol.Transaction.Result.code ret = 2;`

      Specified by:
      :   `getRetValue` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The enum numeric value on the wire for ret.
    - #### setRetValue

      ```
      public Chain.Transaction.Result.Builder setRetValue(int value)
      ```

      `.protocol.Transaction.Result.code ret = 2;`

      Parameters:
      :   `value` - The enum numeric value on the wire for ret to set.

      Returns:
      :   This builder for chaining.
    - #### getRet

      ```
      public Chain.Transaction.Result.code getRet()
      ```

      `.protocol.Transaction.Result.code ret = 2;`

      Specified by:
      :   `getRet` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The ret.
    - #### setRet

      ```
      public Chain.Transaction.Result.Builder setRet(Chain.Transaction.Result.code value)
      ```

      `.protocol.Transaction.Result.code ret = 2;`

      Parameters:
      :   `value` - The ret to set.

      Returns:
      :   This builder for chaining.
    - #### clearRet

      ```
      public Chain.Transaction.Result.Builder clearRet()
      ```

      `.protocol.Transaction.Result.code ret = 2;`

      Returns:
      :   This builder for chaining.
    - #### getContractRetValue

      ```
      public int getContractRetValue()
      ```

      `.protocol.Transaction.Result.contractResult contractRet = 3;`

      Specified by:
      :   `getContractRetValue` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The enum numeric value on the wire for contractRet.
    - #### setContractRetValue

      ```
      public Chain.Transaction.Result.Builder setContractRetValue(int value)
      ```

      `.protocol.Transaction.Result.contractResult contractRet = 3;`

      Parameters:
      :   `value` - The enum numeric value on the wire for contractRet to set.

      Returns:
      :   This builder for chaining.
    - #### getContractRet

      ```
      public Chain.Transaction.Result.contractResult getContractRet()
      ```

      `.protocol.Transaction.Result.contractResult contractRet = 3;`

      Specified by:
      :   `getContractRet` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The contractRet.
    - #### setContractRet

      ```
      public Chain.Transaction.Result.Builder setContractRet(Chain.Transaction.Result.contractResult value)
      ```

      `.protocol.Transaction.Result.contractResult contractRet = 3;`

      Parameters:
      :   `value` - The contractRet to set.

      Returns:
      :   This builder for chaining.
    - #### clearContractRet

      ```
      public Chain.Transaction.Result.Builder clearContractRet()
      ```

      `.protocol.Transaction.Result.contractResult contractRet = 3;`

      Returns:
      :   This builder for chaining.
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
    - #### setAssetIssueID

      ```
      public Chain.Transaction.Result.Builder setAssetIssueID(java.lang.String value)
      ```

      `string assetIssueID = 14;`

      Parameters:
      :   `value` - The assetIssueID to set.

      Returns:
      :   This builder for chaining.
    - #### clearAssetIssueID

      ```
      public Chain.Transaction.Result.Builder clearAssetIssueID()
      ```

      `string assetIssueID = 14;`

      Returns:
      :   This builder for chaining.
    - #### setAssetIssueIDBytes

      ```
      public Chain.Transaction.Result.Builder setAssetIssueIDBytes(com.google.protobuf.ByteString value)
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
      :   `getWithdrawAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The withdrawAmount.
    - #### setWithdrawAmount

      ```
      public Chain.Transaction.Result.Builder setWithdrawAmount(long value)
      ```

      `int64 withdraw_amount = 15;`

      Parameters:
      :   `value` - The withdrawAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearWithdrawAmount

      ```
      public Chain.Transaction.Result.Builder clearWithdrawAmount()
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
      :   `getUnfreezeAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The unfreezeAmount.
    - #### setUnfreezeAmount

      ```
      public Chain.Transaction.Result.Builder setUnfreezeAmount(long value)
      ```

      `int64 unfreeze_amount = 16;`

      Parameters:
      :   `value` - The unfreezeAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearUnfreezeAmount

      ```
      public Chain.Transaction.Result.Builder clearUnfreezeAmount()
      ```

      `int64 unfreeze_amount = 16;`

      Returns:
      :   This builder for chaining.
    - #### getExchangeReceivedAmount

      ```
      public long getExchangeReceivedAmount()
      ```

      `int64 exchange_received_amount = 18;`

      Specified by:
      :   `getExchangeReceivedAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The exchangeReceivedAmount.
    - #### setExchangeReceivedAmount

      ```
      public Chain.Transaction.Result.Builder setExchangeReceivedAmount(long value)
      ```

      `int64 exchange_received_amount = 18;`

      Parameters:
      :   `value` - The exchangeReceivedAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeReceivedAmount

      ```
      public Chain.Transaction.Result.Builder clearExchangeReceivedAmount()
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
      :   `getExchangeInjectAnotherAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The exchangeInjectAnotherAmount.
    - #### setExchangeInjectAnotherAmount

      ```
      public Chain.Transaction.Result.Builder setExchangeInjectAnotherAmount(long value)
      ```

      `int64 exchange_inject_another_amount = 19;`

      Parameters:
      :   `value` - The exchangeInjectAnotherAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeInjectAnotherAmount

      ```
      public Chain.Transaction.Result.Builder clearExchangeInjectAnotherAmount()
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
      :   `getExchangeWithdrawAnotherAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The exchangeWithdrawAnotherAmount.
    - #### setExchangeWithdrawAnotherAmount

      ```
      public Chain.Transaction.Result.Builder setExchangeWithdrawAnotherAmount(long value)
      ```

      `int64 exchange_withdraw_another_amount = 20;`

      Parameters:
      :   `value` - The exchangeWithdrawAnotherAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeWithdrawAnotherAmount

      ```
      public Chain.Transaction.Result.Builder clearExchangeWithdrawAnotherAmount()
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
      :   `getExchangeId` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The exchangeId.
    - #### setExchangeId

      ```
      public Chain.Transaction.Result.Builder setExchangeId(long value)
      ```

      `int64 exchange_id = 21;`

      Parameters:
      :   `value` - The exchangeId to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeId

      ```
      public Chain.Transaction.Result.Builder clearExchangeId()
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
      :   `getShieldedTransactionFee` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The shieldedTransactionFee.
    - #### setShieldedTransactionFee

      ```
      public Chain.Transaction.Result.Builder setShieldedTransactionFee(long value)
      ```

      `int64 shielded_transaction_fee = 22;`

      Parameters:
      :   `value` - The shieldedTransactionFee to set.

      Returns:
      :   This builder for chaining.
    - #### clearShieldedTransactionFee

      ```
      public Chain.Transaction.Result.Builder clearShieldedTransactionFee()
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
      :   `getOrderId` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The orderId.
    - #### setOrderId

      ```
      public Chain.Transaction.Result.Builder setOrderId(com.google.protobuf.ByteString value)
      ```

      `bytes orderId = 25;`

      Parameters:
      :   `value` - The orderId to set.

      Returns:
      :   This builder for chaining.
    - #### clearOrderId

      ```
      public Chain.Transaction.Result.Builder clearOrderId()
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
      :   `getOrderDetailsList` in interface `Chain.Transaction.ResultOrBuilder`
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
    - #### setOrderDetails

      ```
      public Chain.Transaction.Result.Builder setOrderDetails(int index,
                                                              Common.MarketOrderDetail value)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### setOrderDetails

      ```
      public Chain.Transaction.Result.Builder setOrderDetails(int index,
                                                              Common.MarketOrderDetail.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addOrderDetails

      ```
      public Chain.Transaction.Result.Builder addOrderDetails(Common.MarketOrderDetail value)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addOrderDetails

      ```
      public Chain.Transaction.Result.Builder addOrderDetails(int index,
                                                              Common.MarketOrderDetail value)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addOrderDetails

      ```
      public Chain.Transaction.Result.Builder addOrderDetails(Common.MarketOrderDetail.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addOrderDetails

      ```
      public Chain.Transaction.Result.Builder addOrderDetails(int index,
                                                              Common.MarketOrderDetail.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### addAllOrderDetails

      ```
      public Chain.Transaction.Result.Builder addAllOrderDetails(java.lang.Iterable<? extends Common.MarketOrderDetail> values)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### clearOrderDetails

      ```
      public Chain.Transaction.Result.Builder clearOrderDetails()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### removeOrderDetails

      ```
      public Chain.Transaction.Result.Builder removeOrderDetails(int index)
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
      :   `getOrderDetailsOrBuilder` in interface `Chain.Transaction.ResultOrBuilder`
    - #### getOrderDetailsOrBuilderList

      ```
      public java.util.List<? extends Common.MarketOrderDetailOrBuilder> getOrderDetailsOrBuilderList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`

      Specified by:
      :   `getOrderDetailsOrBuilderList` in interface `Chain.Transaction.ResultOrBuilder`
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
    - #### getWithdrawExpireAmount

      ```
      public long getWithdrawExpireAmount()
      ```

      `int64 withdraw_expire_amount = 27;`

      Specified by:
      :   `getWithdrawExpireAmount` in interface `Chain.Transaction.ResultOrBuilder`

      Returns:
      :   The withdrawExpireAmount.
    - #### setWithdrawExpireAmount

      ```
      public Chain.Transaction.Result.Builder setWithdrawExpireAmount(long value)
      ```

      `int64 withdraw_expire_amount = 27;`

      Parameters:
      :   `value` - The withdrawExpireAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearWithdrawExpireAmount

      ```
      public Chain.Transaction.Result.Builder clearWithdrawExpireAmount()
      ```

      `int64 withdraw_expire_amount = 27;`

      Returns:
      :   This builder for chaining.
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

      Use [`getCancelUnfreezeV2AmountMap()`](../../../../org/tron/trident/proto/Chain.Transaction.Result.Builder.html#getCancelUnfreezeV2AmountMap--) instead.

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
    - #### clearCancelUnfreezeV2Amount

      ```
      public Chain.Transaction.Result.Builder clearCancelUnfreezeV2Amount()
      ```
    - #### removeCancelUnfreezeV2Amount

      ```
      public Chain.Transaction.Result.Builder removeCancelUnfreezeV2Amount(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`
    - #### getMutableCancelUnfreezeV2Amount

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableCancelUnfreezeV2Amount()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putCancelUnfreezeV2Amount

      ```
      public Chain.Transaction.Result.Builder putCancelUnfreezeV2Amount(java.lang.String key,
                                                                        long value)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`
    - #### putAllCancelUnfreezeV2Amount

      ```
      public Chain.Transaction.Result.Builder putAllCancelUnfreezeV2Amount(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`
    - #### setUnknownFields

      ```
      public final Chain.Transaction.Result.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`
    - #### mergeUnknownFields

      ```
      public final Chain.Transaction.Result.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Result.Builder>`