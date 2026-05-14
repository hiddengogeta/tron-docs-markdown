

org.tron.trident.proto

## Class Chain.BlockHeader

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Chain.BlockHeader

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Chain.BlockHeaderOrBuilder](../../../../org/tron/trident/proto/Chain.BlockHeaderOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain](../../../../org/tron/trident/proto/Chain.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.BlockHeader
  extends com.google.protobuf.GeneratedMessageV3
  implements Chain.BlockHeaderOrBuilder
  ```

  Protobuf type `protocol.BlockHeader`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Chain.BlockHeader)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Chain.BlockHeader.Builder` Protobuf type `protocol.BlockHeader` |
    | `static class` | `Chain.BlockHeader.raw` Protobuf type `protocol.BlockHeader.raw` |
    | `static interface` | `Chain.BlockHeader.rawOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `RAW_DATA_FIELD_NUMBER` |
    | `static int` | `WITNESS_SIGNATURE_FIELD_NUMBER` |

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
    | `static Chain.BlockHeader` | `getDefaultInstance()` |
    | `Chain.BlockHeader` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Parser<Chain.BlockHeader>` | `getParserForType()` |
    | `Chain.BlockHeader.raw` | `getRawData()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `Chain.BlockHeader.rawOrBuilder` | `getRawDataOrBuilder()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getWitnessSignature()` `bytes witness_signature = 2;` |
    | `int` | `hashCode()` |
    | `boolean` | `hasRawData()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Chain.BlockHeader.Builder` | `newBuilder()` |
    | `static Chain.BlockHeader.Builder` | `newBuilder(Chain.BlockHeader prototype)` |
    | `Chain.BlockHeader.Builder` | `newBuilderForType()` |
    | `protected Chain.BlockHeader.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Chain.BlockHeader` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Chain.BlockHeader` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader` | `parseFrom(byte[] data)` |
    | `static Chain.BlockHeader` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Chain.BlockHeader` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Chain.BlockHeader` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Chain.BlockHeader` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader` | `parseFrom(java.io.InputStream input)` |
    | `static Chain.BlockHeader` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Chain.BlockHeader>` | `parser()` |
    | `Chain.BlockHeader.Builder` | `toBuilder()` |
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

    - #### RAW\_DATA\_FIELD\_NUMBER

      ```
      public static final int RAW_DATA_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.RAW_DATA_FIELD_NUMBER)
    - #### WITNESS\_SIGNATURE\_FIELD\_NUMBER

      ```
      public static final int WITNESS_SIGNATURE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.WITNESS_SIGNATURE_FIELD_NUMBER)
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
    - #### hasRawData

      ```
      public boolean hasRawData()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`

      Specified by:
      :   `hasRawData` in interface `Chain.BlockHeaderOrBuilder`

      Returns:
      :   Whether the rawData field is set.
    - #### getRawData

      ```
      public Chain.BlockHeader.raw getRawData()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`

      Specified by:
      :   `getRawData` in interface `Chain.BlockHeaderOrBuilder`

      Returns:
      :   The rawData.
    - #### getRawDataOrBuilder

      ```
      public Chain.BlockHeader.rawOrBuilder getRawDataOrBuilder()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`

      Specified by:
      :   `getRawDataOrBuilder` in interface `Chain.BlockHeaderOrBuilder`
    - #### getWitnessSignature

      ```
      public com.google.protobuf.ByteString getWitnessSignature()
      ```

      `bytes witness_signature = 2;`

      Specified by:
      :   `getWitnessSignature` in interface `Chain.BlockHeaderOrBuilder`

      Returns:
      :   The witnessSignature.
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
      public static Chain.BlockHeader parseFrom(java.nio.ByteBuffer data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader parseFrom(java.nio.ByteBuffer data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader parseFrom(com.google.protobuf.ByteString data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader parseFrom(com.google.protobuf.ByteString data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader parseFrom(byte[] data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader parseFrom(byte[] data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader parseFrom(java.io.InputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader parseFrom(java.io.InputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.BlockHeader parseDelimitedFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.BlockHeader parseDelimitedFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader parseFrom(com.google.protobuf.CodedInputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader parseFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Chain.BlockHeader.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Chain.BlockHeader.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Chain.BlockHeader.Builder newBuilder(Chain.BlockHeader prototype)
      ```
    - #### toBuilder

      ```
      public Chain.BlockHeader.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Chain.BlockHeader.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Chain.BlockHeader getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Chain.BlockHeader> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Chain.BlockHeader> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Chain.BlockHeader getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`