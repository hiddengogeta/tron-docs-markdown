

org.tron.trident.api

## Class GrpcAPI.EasyTransferMessage

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.api.GrpcAPI.EasyTransferMessage

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [GrpcAPI.EasyTransferMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.EasyTransferMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.EasyTransferMessage
  extends com.google.protobuf.GeneratedMessageV3
  implements GrpcAPI.EasyTransferMessageOrBuilder
  ```

  Protobuf type `protocol.EasyTransferMessage`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.api.GrpcAPI.EasyTransferMessage)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.EasyTransferMessage.Builder` Protobuf type `protocol.EasyTransferMessage` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `AMOUNT_FIELD_NUMBER` |
    | `static int` | `PASSPHRASE_FIELD_NUMBER` |
    | `static int` | `TOADDRESS_FIELD_NUMBER` |

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
    | `long` | `getAmount()` `int64 amount = 3;` |
    | `static GrpcAPI.EasyTransferMessage` | `getDefaultInstance()` |
    | `GrpcAPI.EasyTransferMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Parser<GrpcAPI.EasyTransferMessage>` | `getParserForType()` |
    | `com.google.protobuf.ByteString` | `getPassPhrase()` `bytes passPhrase = 1;` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes toAddress = 2;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static GrpcAPI.EasyTransferMessage.Builder` | `newBuilder()` |
    | `static GrpcAPI.EasyTransferMessage.Builder` | `newBuilder(GrpcAPI.EasyTransferMessage prototype)` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `newBuilderForType()` |
    | `protected GrpcAPI.EasyTransferMessage.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(byte[] data)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(java.io.InputStream input)` |
    | `static GrpcAPI.EasyTransferMessage` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<GrpcAPI.EasyTransferMessage>` | `parser()` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `toBuilder()` |
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

    - #### PASSPHRASE\_FIELD\_NUMBER

      ```
      public static final int PASSPHRASE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.EasyTransferMessage.PASSPHRASE_FIELD_NUMBER)
    - #### TOADDRESS\_FIELD\_NUMBER

      ```
      public static final int TOADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.EasyTransferMessage.TOADDRESS_FIELD_NUMBER)
    - #### AMOUNT\_FIELD\_NUMBER

      ```
      public static final int AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.EasyTransferMessage.AMOUNT_FIELD_NUMBER)
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
    - #### getPassPhrase

      ```
      public com.google.protobuf.ByteString getPassPhrase()
      ```

      `bytes passPhrase = 1;`

      Specified by:
      :   `getPassPhrase` in interface `GrpcAPI.EasyTransferMessageOrBuilder`

      Returns:
      :   The passPhrase.
    - #### getToAddress

      ```
      public com.google.protobuf.ByteString getToAddress()
      ```

      `bytes toAddress = 2;`

      Specified by:
      :   `getToAddress` in interface `GrpcAPI.EasyTransferMessageOrBuilder`

      Returns:
      :   The toAddress.
    - #### getAmount

      ```
      public long getAmount()
      ```

      `int64 amount = 3;`

      Specified by:
      :   `getAmount` in interface `GrpcAPI.EasyTransferMessageOrBuilder`

      Returns:
      :   The amount.
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
      public static GrpcAPI.EasyTransferMessage parseFrom(java.nio.ByteBuffer data)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseFrom(java.nio.ByteBuffer data,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseFrom(com.google.protobuf.ByteString data)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseFrom(com.google.protobuf.ByteString data,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseFrom(byte[] data)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseFrom(byte[] data,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseFrom(java.io.InputStream input)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseFrom(java.io.InputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseDelimitedFrom(java.io.InputStream input)
                                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseDelimitedFrom(java.io.InputStream input,
                                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseFrom(com.google.protobuf.CodedInputStream input)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.EasyTransferMessage parseFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public GrpcAPI.EasyTransferMessage.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static GrpcAPI.EasyTransferMessage.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static GrpcAPI.EasyTransferMessage.Builder newBuilder(GrpcAPI.EasyTransferMessage prototype)
      ```
    - #### toBuilder

      ```
      public GrpcAPI.EasyTransferMessage.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected GrpcAPI.EasyTransferMessage.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static GrpcAPI.EasyTransferMessage getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<GrpcAPI.EasyTransferMessage> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<GrpcAPI.EasyTransferMessage> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.EasyTransferMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`