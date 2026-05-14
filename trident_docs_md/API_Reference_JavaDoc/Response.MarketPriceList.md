

org.tron.trident.proto

## Class Response.MarketPriceList

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.MarketPriceList

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.MarketPriceListOrBuilder](../../../../org/tron/trident/proto/Response.MarketPriceListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.MarketPriceList
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.MarketPriceListOrBuilder
  ```

  Protobuf type `protocol.MarketPriceList`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.MarketPriceList)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.MarketPriceList.Builder` Protobuf type `protocol.MarketPriceList` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BUY_TOKEN_ID_FIELD_NUMBER` |
    | `static int` | `PRICES_FIELD_NUMBER` |
    | `static int` | `SELL_TOKEN_ID_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 2;` |
    | `static Response.MarketPriceList` | `getDefaultInstance()` |
    | `Response.MarketPriceList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Parser<Response.MarketPriceList>` | `getParserForType()` |
    | `Response.MarketPrice` | `getPrices(int index)` `repeated .protocol.MarketPrice prices = 3;` |
    | `int` | `getPricesCount()` `repeated .protocol.MarketPrice prices = 3;` |
    | `java.util.List<Response.MarketPrice>` | `getPricesList()` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceOrBuilder` | `getPricesOrBuilder(int index)` `repeated .protocol.MarketPrice prices = 3;` |
    | `java.util.List<? extends Response.MarketPriceOrBuilder>` | `getPricesOrBuilderList()` `repeated .protocol.MarketPrice prices = 3;` |
    | `com.google.protobuf.ByteString` | `getSellTokenId()` `bytes sell_token_id = 1;` |
    | `int` | `getSerializedSize()` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.MarketPriceList.Builder` | `newBuilder()` |
    | `static Response.MarketPriceList.Builder` | `newBuilder(Response.MarketPriceList prototype)` |
    | `Response.MarketPriceList.Builder` | `newBuilderForType()` |
    | `protected Response.MarketPriceList.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.MarketPriceList` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.MarketPriceList` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketPriceList` | `parseFrom(byte[] data)` |
    | `static Response.MarketPriceList` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketPriceList` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.MarketPriceList` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketPriceList` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.MarketPriceList` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketPriceList` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.MarketPriceList` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.MarketPriceList` | `parseFrom(java.io.InputStream input)` |
    | `static Response.MarketPriceList` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.MarketPriceList>` | `parser()` |
    | `Response.MarketPriceList.Builder` | `toBuilder()` |
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

    - #### SELL\_TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int SELL_TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketPriceList.SELL_TOKEN_ID_FIELD_NUMBER)
    - #### BUY\_TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int BUY_TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketPriceList.BUY_TOKEN_ID_FIELD_NUMBER)
    - #### PRICES\_FIELD\_NUMBER

      ```
      public static final int PRICES_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketPriceList.PRICES_FIELD_NUMBER)
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
    - #### getSellTokenId

      ```
      public com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 1;`

      Specified by:
      :   `getSellTokenId` in interface `Response.MarketPriceListOrBuilder`

      Returns:
      :   The sellTokenId.
    - #### getBuyTokenId

      ```
      public com.google.protobuf.ByteString getBuyTokenId()
      ```

      `bytes buy_token_id = 2;`

      Specified by:
      :   `getBuyTokenId` in interface `Response.MarketPriceListOrBuilder`

      Returns:
      :   The buyTokenId.
    - #### getPricesList

      ```
      public java.util.List<Response.MarketPrice> getPricesList()
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPricesList` in interface `Response.MarketPriceListOrBuilder`
    - #### getPricesOrBuilderList

      ```
      public java.util.List<? extends Response.MarketPriceOrBuilder> getPricesOrBuilderList()
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPricesOrBuilderList` in interface `Response.MarketPriceListOrBuilder`
    - #### getPricesCount

      ```
      public int getPricesCount()
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPricesCount` in interface `Response.MarketPriceListOrBuilder`
    - #### getPrices

      ```
      public Response.MarketPrice getPrices(int index)
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPrices` in interface `Response.MarketPriceListOrBuilder`
    - #### getPricesOrBuilder

      ```
      public Response.MarketPriceOrBuilder getPricesOrBuilder(int index)
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPricesOrBuilder` in interface `Response.MarketPriceListOrBuilder`
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
      public static Response.MarketPriceList parseFrom(java.nio.ByteBuffer data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketPriceList parseFrom(java.nio.ByteBuffer data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketPriceList parseFrom(com.google.protobuf.ByteString data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketPriceList parseFrom(com.google.protobuf.ByteString data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketPriceList parseFrom(byte[] data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketPriceList parseFrom(byte[] data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.MarketPriceList parseFrom(java.io.InputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.MarketPriceList parseFrom(java.io.InputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.MarketPriceList parseDelimitedFrom(java.io.InputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.MarketPriceList parseDelimitedFrom(java.io.InputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.MarketPriceList parseFrom(com.google.protobuf.CodedInputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.MarketPriceList parseFrom(com.google.protobuf.CodedInputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.MarketPriceList.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.MarketPriceList.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.MarketPriceList.Builder newBuilder(Response.MarketPriceList prototype)
      ```
    - #### toBuilder

      ```
      public Response.MarketPriceList.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.MarketPriceList.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.MarketPriceList getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.MarketPriceList> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.MarketPriceList> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.MarketPriceList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`