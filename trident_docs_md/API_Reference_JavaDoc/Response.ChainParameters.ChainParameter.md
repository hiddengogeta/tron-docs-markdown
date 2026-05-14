

org.tron.trident.proto

## Class Response.ChainParameters.ChainParameter

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.ChainParameters.ChainParameter

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.ChainParameters.ChainParameterOrBuilder](../../../../org/tron/trident/proto/Response.ChainParameters.ChainParameterOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.ChainParameters](../../../../org/tron/trident/proto/Response.ChainParameters.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.ChainParameters.ChainParameter
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.ChainParameters.ChainParameterOrBuilder
  ```

  Protobuf type `protocol.ChainParameters.ChainParameter`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.ChainParameters.ChainParameter)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.ChainParameters.ChainParameter.Builder` Protobuf type `protocol.ChainParameters.ChainParameter` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `KEY_FIELD_NUMBER` |
    | `static int` | `VALUE_FIELD_NUMBER` |

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
    | `static Response.ChainParameters.ChainParameter` | `getDefaultInstance()` |
    | `Response.ChainParameters.ChainParameter` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `java.lang.String` | `getKey()` `string key = 1;` |
    | `com.google.protobuf.ByteString` | `getKeyBytes()` `string key = 1;` |
    | `com.google.protobuf.Parser<Response.ChainParameters.ChainParameter>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `long` | `getValue()` `int64 value = 2;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.ChainParameters.ChainParameter.Builder` | `newBuilder()` |
    | `static Response.ChainParameters.ChainParameter.Builder` | `newBuilder(Response.ChainParameters.ChainParameter prototype)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `newBuilderForType()` |
    | `protected Response.ChainParameters.ChainParameter.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.ChainParameters.ChainParameter` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.ChainParameters.ChainParameter` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(byte[] data)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(java.io.InputStream input)` |
    | `static Response.ChainParameters.ChainParameter` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.ChainParameters.ChainParameter>` | `parser()` |
    | `Response.ChainParameters.ChainParameter.Builder` | `toBuilder()` |
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

    - #### KEY\_FIELD\_NUMBER

      ```
      public static final int KEY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ChainParameters.ChainParameter.KEY_FIELD_NUMBER)
    - #### VALUE\_FIELD\_NUMBER

      ```
      public static final int VALUE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ChainParameters.ChainParameter.VALUE_FIELD_NUMBER)
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
    - #### getKey

      ```
      public java.lang.String getKey()
      ```

      `string key = 1;`

      Specified by:
      :   `getKey` in interface `Response.ChainParameters.ChainParameterOrBuilder`

      Returns:
      :   The key.
    - #### getKeyBytes

      ```
      public com.google.protobuf.ByteString getKeyBytes()
      ```

      `string key = 1;`

      Specified by:
      :   `getKeyBytes` in interface `Response.ChainParameters.ChainParameterOrBuilder`

      Returns:
      :   The bytes for key.
    - #### getValue

      ```
      public long getValue()
      ```

      `int64 value = 2;`

      Specified by:
      :   `getValue` in interface `Response.ChainParameters.ChainParameterOrBuilder`

      Returns:
      :   The value.
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
      public static Response.ChainParameters.ChainParameter parseFrom(java.nio.ByteBuffer data)
                                                               throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ChainParameters.ChainParameter parseFrom(java.nio.ByteBuffer data,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ChainParameters.ChainParameter parseFrom(com.google.protobuf.ByteString data)
                                                               throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ChainParameters.ChainParameter parseFrom(com.google.protobuf.ByteString data,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ChainParameters.ChainParameter parseFrom(byte[] data)
                                                               throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ChainParameters.ChainParameter parseFrom(byte[] data,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ChainParameters.ChainParameter parseFrom(java.io.InputStream input)
                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.ChainParameters.ChainParameter parseFrom(java.io.InputStream input,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.ChainParameters.ChainParameter parseDelimitedFrom(java.io.InputStream input)
                                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.ChainParameters.ChainParameter parseDelimitedFrom(java.io.InputStream input,
                                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.ChainParameters.ChainParameter parseFrom(com.google.protobuf.CodedInputStream input)
                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.ChainParameters.ChainParameter parseFrom(com.google.protobuf.CodedInputStream input,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.ChainParameters.ChainParameter.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.ChainParameters.ChainParameter.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.ChainParameters.ChainParameter.Builder newBuilder(Response.ChainParameters.ChainParameter prototype)
      ```
    - #### toBuilder

      ```
      public Response.ChainParameters.ChainParameter.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.ChainParameters.ChainParameter.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.ChainParameters.ChainParameter getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.ChainParameters.ChainParameter> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.ChainParameters.ChainParameter> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.ChainParameters.ChainParameter getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`