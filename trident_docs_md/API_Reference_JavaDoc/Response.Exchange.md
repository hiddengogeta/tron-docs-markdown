

org.tron.trident.proto

## Class Response.Exchange

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.Exchange

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.ExchangeOrBuilder](../../../../org/tron/trident/proto/Response.ExchangeOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Exchange
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.ExchangeOrBuilder
  ```

  Protobuf type `protocol.Exchange`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.Exchange)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.Exchange.Builder` Protobuf type `protocol.Exchange` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `CREATE_TIME_FIELD_NUMBER` |
    | `static int` | `CREATOR_ADDRESS_FIELD_NUMBER` |
    | `static int` | `EXCHANGE_ID_FIELD_NUMBER` |
    | `static int` | `FIRST_TOKEN_BALANCE_FIELD_NUMBER` |
    | `static int` | `FIRST_TOKEN_ID_FIELD_NUMBER` |
    | `static int` | `SECOND_TOKEN_BALANCE_FIELD_NUMBER` |
    | `static int` | `SECOND_TOKEN_ID_FIELD_NUMBER` |

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
    | `long` | `getCreateTime()` `int64 create_time = 3;` |
    | `com.google.protobuf.ByteString` | `getCreatorAddress()` `bytes creator_address = 2;` |
    | `static Response.Exchange` | `getDefaultInstance()` |
    | `Response.Exchange` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getExchangeId()` `int64 exchange_id = 1;` |
    | `long` | `getFirstTokenBalance()` `int64 first_token_balance = 7;` |
    | `com.google.protobuf.ByteString` | `getFirstTokenId()` `bytes first_token_id = 6;` |
    | `com.google.protobuf.Parser<Response.Exchange>` | `getParserForType()` |
    | `long` | `getSecondTokenBalance()` `int64 second_token_balance = 9;` |
    | `com.google.protobuf.ByteString` | `getSecondTokenId()` `bytes second_token_id = 8;` |
    | `int` | `getSerializedSize()` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.Exchange.Builder` | `newBuilder()` |
    | `static Response.Exchange.Builder` | `newBuilder(Response.Exchange prototype)` |
    | `Response.Exchange.Builder` | `newBuilderForType()` |
    | `protected Response.Exchange.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.Exchange` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.Exchange` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Exchange` | `parseFrom(byte[] data)` |
    | `static Response.Exchange` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Exchange` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.Exchange` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Exchange` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.Exchange` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Exchange` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.Exchange` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Exchange` | `parseFrom(java.io.InputStream input)` |
    | `static Response.Exchange` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.Exchange>` | `parser()` |
    | `Response.Exchange.Builder` | `toBuilder()` |
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

    - #### EXCHANGE\_ID\_FIELD\_NUMBER

      ```
      public static final int EXCHANGE_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Exchange.EXCHANGE_ID_FIELD_NUMBER)
    - #### CREATOR\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int CREATOR_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Exchange.CREATOR_ADDRESS_FIELD_NUMBER)
    - #### CREATE\_TIME\_FIELD\_NUMBER

      ```
      public static final int CREATE_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Exchange.CREATE_TIME_FIELD_NUMBER)
    - #### FIRST\_TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int FIRST_TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Exchange.FIRST_TOKEN_ID_FIELD_NUMBER)
    - #### FIRST\_TOKEN\_BALANCE\_FIELD\_NUMBER

      ```
      public static final int FIRST_TOKEN_BALANCE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Exchange.FIRST_TOKEN_BALANCE_FIELD_NUMBER)
    - #### SECOND\_TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int SECOND_TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Exchange.SECOND_TOKEN_ID_FIELD_NUMBER)
    - #### SECOND\_TOKEN\_BALANCE\_FIELD\_NUMBER

      ```
      public static final int SECOND_TOKEN_BALANCE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Exchange.SECOND_TOKEN_BALANCE_FIELD_NUMBER)
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
    - #### getExchangeId

      ```
      public long getExchangeId()
      ```

      `int64 exchange_id = 1;`

      Specified by:
      :   `getExchangeId` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The exchangeId.
    - #### getCreatorAddress

      ```
      public com.google.protobuf.ByteString getCreatorAddress()
      ```

      `bytes creator_address = 2;`

      Specified by:
      :   `getCreatorAddress` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The creatorAddress.
    - #### getCreateTime

      ```
      public long getCreateTime()
      ```

      `int64 create_time = 3;`

      Specified by:
      :   `getCreateTime` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The createTime.
    - #### getFirstTokenId

      ```
      public com.google.protobuf.ByteString getFirstTokenId()
      ```

      `bytes first_token_id = 6;`

      Specified by:
      :   `getFirstTokenId` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The firstTokenId.
    - #### getFirstTokenBalance

      ```
      public long getFirstTokenBalance()
      ```

      `int64 first_token_balance = 7;`

      Specified by:
      :   `getFirstTokenBalance` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The firstTokenBalance.
    - #### getSecondTokenId

      ```
      public com.google.protobuf.ByteString getSecondTokenId()
      ```

      `bytes second_token_id = 8;`

      Specified by:
      :   `getSecondTokenId` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The secondTokenId.
    - #### getSecondTokenBalance

      ```
      public long getSecondTokenBalance()
      ```

      `int64 second_token_balance = 9;`

      Specified by:
      :   `getSecondTokenBalance` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The secondTokenBalance.
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
      public static Response.Exchange parseFrom(java.nio.ByteBuffer data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Exchange parseFrom(java.nio.ByteBuffer data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Exchange parseFrom(com.google.protobuf.ByteString data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Exchange parseFrom(com.google.protobuf.ByteString data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Exchange parseFrom(byte[] data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Exchange parseFrom(byte[] data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Exchange parseFrom(java.io.InputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Exchange parseFrom(java.io.InputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Exchange parseDelimitedFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Exchange parseDelimitedFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Exchange parseFrom(com.google.protobuf.CodedInputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Exchange parseFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.Exchange.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.Exchange.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.Exchange.Builder newBuilder(Response.Exchange prototype)
      ```
    - #### toBuilder

      ```
      public Response.Exchange.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.Exchange.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.Exchange getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.Exchange> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.Exchange> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.Exchange getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`