

org.tron.trident.proto

## Class Response.InternalTransaction.CallValueInfo

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.InternalTransaction.CallValueInfo

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.InternalTransaction.CallValueInfoOrBuilder](../../../../org/tron/trident/proto/Response.InternalTransaction.CallValueInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.InternalTransaction](../../../../org/tron/trident/proto/Response.InternalTransaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.InternalTransaction.CallValueInfo
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.InternalTransaction.CallValueInfoOrBuilder
  ```

  Protobuf type `protocol.InternalTransaction.CallValueInfo`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.InternalTransaction.CallValueInfo)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.InternalTransaction.CallValueInfo.Builder` Protobuf type `protocol.InternalTransaction.CallValueInfo` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `CALLVALUE_FIELD_NUMBER` |
    | `static int` | `TOKENID_FIELD_NUMBER` |

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
    | `long` | `getCallValue()` trx (TBD: or token) value |
    | `static Response.InternalTransaction.CallValueInfo` | `getDefaultInstance()` |
    | `Response.InternalTransaction.CallValueInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Parser<Response.InternalTransaction.CallValueInfo>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `java.lang.String` | `getTokenId()` TBD: tokenName, trx should be empty |
    | `com.google.protobuf.ByteString` | `getTokenIdBytes()` TBD: tokenName, trx should be empty |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.InternalTransaction.CallValueInfo.Builder` | `newBuilder()` |
    | `static Response.InternalTransaction.CallValueInfo.Builder` | `newBuilder(Response.InternalTransaction.CallValueInfo prototype)` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `newBuilderForType()` |
    | `protected Response.InternalTransaction.CallValueInfo.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(byte[] data)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(java.io.InputStream input)` |
    | `static Response.InternalTransaction.CallValueInfo` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.InternalTransaction.CallValueInfo>` | `parser()` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `toBuilder()` |
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

    - #### CALLVALUE\_FIELD\_NUMBER

      ```
      public static final int CALLVALUE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.InternalTransaction.CallValueInfo.CALLVALUE_FIELD_NUMBER)
    - #### TOKENID\_FIELD\_NUMBER

      ```
      public static final int TOKENID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.InternalTransaction.CallValueInfo.TOKENID_FIELD_NUMBER)
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
    - #### getCallValue

      ```
      public long getCallValue()
      ```

      ```
       trx (TBD: or token) value
      ```

      `int64 callValue = 1;`

      Specified by:
      :   `getCallValue` in interface `Response.InternalTransaction.CallValueInfoOrBuilder`

      Returns:
      :   The callValue.
    - #### getTokenId

      ```
      public java.lang.String getTokenId()
      ```

      ```
       TBD: tokenName, trx should be empty
      ```

      `string tokenId = 2;`

      Specified by:
      :   `getTokenId` in interface `Response.InternalTransaction.CallValueInfoOrBuilder`

      Returns:
      :   The tokenId.
    - #### getTokenIdBytes

      ```
      public com.google.protobuf.ByteString getTokenIdBytes()
      ```

      ```
       TBD: tokenName, trx should be empty
      ```

      `string tokenId = 2;`

      Specified by:
      :   `getTokenIdBytes` in interface `Response.InternalTransaction.CallValueInfoOrBuilder`

      Returns:
      :   The bytes for tokenId.
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
      public static Response.InternalTransaction.CallValueInfo parseFrom(java.nio.ByteBuffer data)
                                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseFrom(java.nio.ByteBuffer data,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseFrom(com.google.protobuf.ByteString data)
                                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseFrom(com.google.protobuf.ByteString data,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseFrom(byte[] data)
                                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseFrom(byte[] data,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseFrom(java.io.InputStream input)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseFrom(java.io.InputStream input,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseDelimitedFrom(java.io.InputStream input)
                                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseDelimitedFrom(java.io.InputStream input,
                                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseFrom(com.google.protobuf.CodedInputStream input)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction.CallValueInfo parseFrom(com.google.protobuf.CodedInputStream input,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.InternalTransaction.CallValueInfo.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.InternalTransaction.CallValueInfo.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.InternalTransaction.CallValueInfo.Builder newBuilder(Response.InternalTransaction.CallValueInfo prototype)
      ```
    - #### toBuilder

      ```
      public Response.InternalTransaction.CallValueInfo.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.InternalTransaction.CallValueInfo.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.InternalTransaction.CallValueInfo getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.InternalTransaction.CallValueInfo> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.InternalTransaction.CallValueInfo> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.InternalTransaction.CallValueInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`