

org.tron.trident.proto

## Class Contract.MarketSellAssetContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Contract.MarketSellAssetContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Contract.MarketSellAssetContractOrBuilder](../../../../org/tron/trident/proto/Contract.MarketSellAssetContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.MarketSellAssetContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Contract.MarketSellAssetContractOrBuilder
  ```

  Protobuf type `protocol.MarketSellAssetContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Contract.MarketSellAssetContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.MarketSellAssetContract.Builder` Protobuf type `protocol.MarketSellAssetContract` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BUY_TOKEN_ID_FIELD_NUMBER` |
    | `static int` | `BUY_TOKEN_QUANTITY_FIELD_NUMBER` |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `SELL_TOKEN_ID_FIELD_NUMBER` |
    | `static int` | `SELL_TOKEN_QUANTITY_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 4;` |
    | `long` | `getBuyTokenQuantity()` min to receive |
    | `static Contract.MarketSellAssetContract` | `getDefaultInstance()` |
    | `Contract.MarketSellAssetContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.Parser<Contract.MarketSellAssetContract>` | `getParserForType()` |
    | `com.google.protobuf.ByteString` | `getSellTokenId()` `bytes sell_token_id = 2;` |
    | `long` | `getSellTokenQuantity()` `int64 sell_token_quantity = 3;` |
    | `int` | `getSerializedSize()` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Contract.MarketSellAssetContract.Builder` | `newBuilder()` |
    | `static Contract.MarketSellAssetContract.Builder` | `newBuilder(Contract.MarketSellAssetContract prototype)` |
    | `Contract.MarketSellAssetContract.Builder` | `newBuilderForType()` |
    | `protected Contract.MarketSellAssetContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Contract.MarketSellAssetContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Contract.MarketSellAssetContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(byte[] data)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(java.io.InputStream input)` |
    | `static Contract.MarketSellAssetContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Contract.MarketSellAssetContract>` | `parser()` |
    | `Contract.MarketSellAssetContract.Builder` | `toBuilder()` |
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

    - #### OWNER\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int OWNER_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.MarketSellAssetContract.OWNER_ADDRESS_FIELD_NUMBER)
    - #### SELL\_TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int SELL_TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.MarketSellAssetContract.SELL_TOKEN_ID_FIELD_NUMBER)
    - #### SELL\_TOKEN\_QUANTITY\_FIELD\_NUMBER

      ```
      public static final int SELL_TOKEN_QUANTITY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.MarketSellAssetContract.SELL_TOKEN_QUANTITY_FIELD_NUMBER)
    - #### BUY\_TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int BUY_TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.MarketSellAssetContract.BUY_TOKEN_ID_FIELD_NUMBER)
    - #### BUY\_TOKEN\_QUANTITY\_FIELD\_NUMBER

      ```
      public static final int BUY_TOKEN_QUANTITY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.MarketSellAssetContract.BUY_TOKEN_QUANTITY_FIELD_NUMBER)
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
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### getSellTokenId

      ```
      public com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 2;`

      Specified by:
      :   `getSellTokenId` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The sellTokenId.
    - #### getSellTokenQuantity

      ```
      public long getSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 3;`

      Specified by:
      :   `getSellTokenQuantity` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The sellTokenQuantity.
    - #### getBuyTokenId

      ```
      public com.google.protobuf.ByteString getBuyTokenId()
      ```

      `bytes buy_token_id = 4;`

      Specified by:
      :   `getBuyTokenId` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The buyTokenId.
    - #### getBuyTokenQuantity

      ```
      public long getBuyTokenQuantity()
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 5;`

      Specified by:
      :   `getBuyTokenQuantity` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The buyTokenQuantity.
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
      public static Contract.MarketSellAssetContract parseFrom(java.nio.ByteBuffer data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.MarketSellAssetContract parseFrom(java.nio.ByteBuffer data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.MarketSellAssetContract parseFrom(com.google.protobuf.ByteString data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.MarketSellAssetContract parseFrom(com.google.protobuf.ByteString data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.MarketSellAssetContract parseFrom(byte[] data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.MarketSellAssetContract parseFrom(byte[] data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.MarketSellAssetContract parseFrom(java.io.InputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.MarketSellAssetContract parseFrom(java.io.InputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.MarketSellAssetContract parseDelimitedFrom(java.io.InputStream input)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.MarketSellAssetContract parseDelimitedFrom(java.io.InputStream input,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.MarketSellAssetContract parseFrom(com.google.protobuf.CodedInputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.MarketSellAssetContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Contract.MarketSellAssetContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Contract.MarketSellAssetContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Contract.MarketSellAssetContract.Builder newBuilder(Contract.MarketSellAssetContract prototype)
      ```
    - #### toBuilder

      ```
      public Contract.MarketSellAssetContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Contract.MarketSellAssetContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Contract.MarketSellAssetContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Contract.MarketSellAssetContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Contract.MarketSellAssetContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Contract.MarketSellAssetContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`