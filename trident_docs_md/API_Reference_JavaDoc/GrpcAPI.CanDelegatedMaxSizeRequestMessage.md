

org.tron.trident.api

## Class GrpcAPI.CanDelegatedMaxSizeRequestMessage

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.api.GrpcAPI.CanDelegatedMaxSizeRequestMessage

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.CanDelegatedMaxSizeRequestMessage
  extends com.google.protobuf.GeneratedMessageV3
  implements GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder
  ```

  Protobuf type `protocol.CanDelegatedMaxSizeRequestMessage`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.api.GrpcAPI.CanDelegatedMaxSizeRequestMessage)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` Protobuf type `protocol.CanDelegatedMaxSizeRequestMessage` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `TYPE_FIELD_NUMBER` |

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
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `getDefaultInstance()` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 2;` |
    | `com.google.protobuf.Parser<GrpcAPI.CanDelegatedMaxSizeRequestMessage>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `int` | `getType()` `int32 type = 1;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `newBuilder()` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `newBuilder(GrpcAPI.CanDelegatedMaxSizeRequestMessage prototype)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `newBuilderForType()` |
    | `protected GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(byte[] data)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(java.io.InputStream input)` |
    | `static GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<GrpcAPI.CanDelegatedMaxSizeRequestMessage>` | `parser()` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `toBuilder()` |
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

    - #### TYPE\_FIELD\_NUMBER

      ```
      public static final int TYPE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.CanDelegatedMaxSizeRequestMessage.TYPE_FIELD_NUMBER)
    - #### OWNER\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int OWNER_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.CanDelegatedMaxSizeRequestMessage.OWNER_ADDRESS_FIELD_NUMBER)
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
    - #### getType

      ```
      public int getType()
      ```

      `int32 type = 1;`

      Specified by:
      :   `getType` in interface `GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder`

      Returns:
      :   The type.
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Specified by:
      :   `getOwnerAddress` in interface `GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder`

      Returns:
      :   The ownerAddress.
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
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(java.nio.ByteBuffer data)
                                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(java.nio.ByteBuffer data,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(com.google.protobuf.ByteString data)
                                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(com.google.protobuf.ByteString data,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(byte[] data)
                                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(byte[] data,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(java.io.InputStream input)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(java.io.InputStream input,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseDelimitedFrom(java.io.InputStream input)
                                                                          throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseDelimitedFrom(java.io.InputStream input,
                                                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                          throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(com.google.protobuf.CodedInputStream input)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage parseFrom(com.google.protobuf.CodedInputStream input,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder newBuilder(GrpcAPI.CanDelegatedMaxSizeRequestMessage prototype)
      ```
    - #### toBuilder

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static GrpcAPI.CanDelegatedMaxSizeRequestMessage getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<GrpcAPI.CanDelegatedMaxSizeRequestMessage> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<GrpcAPI.CanDelegatedMaxSizeRequestMessage> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`