

org.tron.trident.proto

## Class Response.MarketOrder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.MarketOrder

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.MarketOrderOrBuilder](../../../../org/tron/trident/proto/Response.MarketOrderOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.MarketOrder
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.MarketOrderOrBuilder
  ```

  Protobuf type `protocol.MarketOrder`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.MarketOrder)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.MarketOrder.Builder` Protobuf type `protocol.MarketOrder` |
    | `static class` | `Response.MarketOrder.State` Protobuf enum `protocol.MarketOrder.State` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BUY_TOKEN_ID_FIELD_NUMBER` |
    | `static int` | `BUY_TOKEN_QUANTITY_FIELD_NUMBER` |
    | `static int` | `CREATE_TIME_FIELD_NUMBER` |
    | `static int` | `NEXT_FIELD_NUMBER` |
    | `static int` | `ORDER_ID_FIELD_NUMBER` |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `PREV_FIELD_NUMBER` |
    | `static int` | `SELL_TOKEN_ID_FIELD_NUMBER` |
    | `static int` | `SELL_TOKEN_QUANTITY_FIELD_NUMBER` |
    | `static int` | `SELL_TOKEN_QUANTITY_REMAIN_FIELD_NUMBER` |
    | `static int` | `SELL_TOKEN_QUANTITY_RETURN_FIELD_NUMBER` |
    | `static int` | `STATE_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 6;` |
    | `long` | `getBuyTokenQuantity()` min to receive |
    | `long` | `getCreateTime()` `int64 create_time = 3;` |
    | `static Response.MarketOrder` | `getDefaultInstance()` |
    | `Response.MarketOrder` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getNext()` `bytes next = 13;` |
    | `com.google.protobuf.ByteString` | `getOrderId()` `bytes order_id = 1;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 2;` |
    | `com.google.protobuf.Parser<Response.MarketOrder>` | `getParserForType()` |
    | `com.google.protobuf.ByteString` | `getPrev()` `bytes prev = 12;` |
    | `com.google.protobuf.ByteString` | `getSellTokenId()` `bytes sell_token_id = 4;` |
    | `long` | `getSellTokenQuantity()` `int64 sell_token_quantity = 5;` |
    | `long` | `getSellTokenQuantityRemain()` `int64 sell_token_quantity_remain = 9;` |
    | `long` | `getSellTokenQuantityReturn()` When state != ACTIVE and sell\_token\_quantity\_return !=0, it means that some sell tokens are returned to the account due to insufficient remaining amount |
    | `int` | `getSerializedSize()` |
    | `Response.MarketOrder.State` | `getState()` `.protocol.MarketOrder.State state = 11;` |
    | `int` | `getStateValue()` `.protocol.MarketOrder.State state = 11;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.MarketOrder.Builder` | `newBuilder()` |
    | `static Response.MarketOrder.Builder` | `newBuilder(Response.MarketOrder prototype)` |
    | `Response.MarketOrder.Builder` | `newBuilderForType()` |
    | `protected Response.MarketOrder.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.MarketOrder` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.MarketOrder` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketOrder` | `parseFrom(byte[] data)` |
    | `static Response.MarketOrder` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketOrder` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.MarketOrder` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketOrder` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.MarketOrder` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketOrder` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.MarketOrder` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketOrder` | `parseFrom(java.io.InputStream input)` |
    | `static Response.MarketOrder` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.MarketOrder>` | `parser()` |
    | `Response.MarketOrder.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
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

    - #### ORDER\_ID\_FIELD\_NUMBER

      ```
      public static final int ORDER_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.ORDER_ID_FIELD_NUMBER)
    - #### OWNER\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int OWNER_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.OWNER_ADDRESS_FIELD_NUMBER)
    - #### CREATE\_TIME\_FIELD\_NUMBER

      ```
      public static final int CREATE_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.CREATE_TIME_FIELD_NUMBER)
    - #### SELL\_TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int SELL_TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.SELL_TOKEN_ID_FIELD_NUMBER)
    - #### SELL\_TOKEN\_QUANTITY\_FIELD\_NUMBER

      ```
      public static final int SELL_TOKEN_QUANTITY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.SELL_TOKEN_QUANTITY_FIELD_NUMBER)
    - #### BUY\_TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int BUY_TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.BUY_TOKEN_ID_FIELD_NUMBER)
    - #### BUY\_TOKEN\_QUANTITY\_FIELD\_NUMBER

      ```
      public static final int BUY_TOKEN_QUANTITY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.BUY_TOKEN_QUANTITY_FIELD_NUMBER)
    - #### SELL\_TOKEN\_QUANTITY\_REMAIN\_FIELD\_NUMBER

      ```
      public static final int SELL_TOKEN_QUANTITY_REMAIN_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.SELL_TOKEN_QUANTITY_REMAIN_FIELD_NUMBER)
    - #### SELL\_TOKEN\_QUANTITY\_RETURN\_FIELD\_NUMBER

      ```
      public static final int SELL_TOKEN_QUANTITY_RETURN_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.SELL_TOKEN_QUANTITY_RETURN_FIELD_NUMBER)
    - #### STATE\_FIELD\_NUMBER

      ```
      public static final int STATE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.STATE_FIELD_NUMBER)
    - #### PREV\_FIELD\_NUMBER

      ```
      public static final int PREV_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.PREV_FIELD_NUMBER)
    - #### NEXT\_FIELD\_NUMBER

      ```
      public static final int NEXT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.NEXT_FIELD_NUMBER)
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
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getOrderId

      ```
      public com.google.protobuf.ByteString getOrderId()
      ```

      `bytes order_id = 1;`

      Specified by:
      :   `getOrderId` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The orderId.
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Specified by:
      :   `getOwnerAddress` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### getCreateTime

      ```
      public long getCreateTime()
      ```

      `int64 create_time = 3;`

      Specified by:
      :   `getCreateTime` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The createTime.
    - #### getSellTokenId

      ```
      public com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 4;`

      Specified by:
      :   `getSellTokenId` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The sellTokenId.
    - #### getSellTokenQuantity

      ```
      public long getSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 5;`

      Specified by:
      :   `getSellTokenQuantity` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The sellTokenQuantity.
    - #### getBuyTokenId

      ```
      public com.google.protobuf.ByteString getBuyTokenId()
      ```

      `bytes buy_token_id = 6;`

      Specified by:
      :   `getBuyTokenId` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The buyTokenId.
    - #### getBuyTokenQuantity

      ```
      public long getBuyTokenQuantity()
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 7;`

      Specified by:
      :   `getBuyTokenQuantity` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The buyTokenQuantity.
    - #### getSellTokenQuantityRemain

      ```
      public long getSellTokenQuantityRemain()
      ```

      `int64 sell_token_quantity_remain = 9;`

      Specified by:
      :   `getSellTokenQuantityRemain` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The sellTokenQuantityRemain.
    - #### getSellTokenQuantityReturn

      ```
      public long getSellTokenQuantityReturn()
      ```

      ```
       When state != ACTIVE and sell_token_quantity_return !=0,
       it means that some sell tokens are returned to the account due to
       insufficient remaining amount
      ```

      `int64 sell_token_quantity_return = 10;`

      Specified by:
      :   `getSellTokenQuantityReturn` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The sellTokenQuantityReturn.
    - #### getStateValue

      ```
      public int getStateValue()
      ```

      `.protocol.MarketOrder.State state = 11;`

      Specified by:
      :   `getStateValue` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The enum numeric value on the wire for state.
    - #### getState

      ```
      public Response.MarketOrder.State getState()
      ```

      `.protocol.MarketOrder.State state = 11;`

      Specified by:
      :   `getState` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The state.
    - #### getPrev

      ```
      public com.google.protobuf.ByteString getPrev()
      ```

      `bytes prev = 12;`

      Specified by:
      :   `getPrev` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The prev.
    - #### getNext

      ```
      public com.google.protobuf.ByteString getNext()
      ```

      `bytes next = 13;`

      Specified by:
      :   `getNext` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The next.
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
      public static Response.MarketOrder parseFrom(java.nio.ByteBuffer data)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketOrder parseFrom(java.nio.ByteBuffer data,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketOrder parseFrom(com.google.protobuf.ByteString data)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketOrder parseFrom(com.google.protobuf.ByteString data,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketOrder parseFrom(byte[] data)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketOrder parseFrom(byte[] data,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketOrder parseFrom(java.io.InputStream input)
                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.MarketOrder parseFrom(java.io.InputStream input,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.MarketOrder parseDelimitedFrom(java.io.InputStream input)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.MarketOrder parseDelimitedFrom(java.io.InputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.MarketOrder parseFrom(com.google.protobuf.CodedInputStream input)
                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.MarketOrder parseFrom(com.google.protobuf.CodedInputStream input,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.MarketOrder.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.MarketOrder.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.MarketOrder.Builder newBuilder(Response.MarketOrder prototype)
      ```
    - #### toBuilder

      ```
      public Response.MarketOrder.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.MarketOrder.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.MarketOrder getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.MarketOrder> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.MarketOrder> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.MarketOrder getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`