

org.tron.trident.proto

## Class Chain.BlockHeader.raw

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Chain.BlockHeader.raw

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Chain.BlockHeader.rawOrBuilder](../../../../org/tron/trident/proto/Chain.BlockHeader.rawOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.BlockHeader](../../../../org/tron/trident/proto/Chain.BlockHeader.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.BlockHeader.raw
  extends com.google.protobuf.GeneratedMessageV3
  implements Chain.BlockHeader.rawOrBuilder
  ```

  Protobuf type `protocol.BlockHeader.raw`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Chain.BlockHeader.raw)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Chain.BlockHeader.raw.Builder` Protobuf type `protocol.BlockHeader.raw` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ACCOUNTSTATEROOT_FIELD_NUMBER` |
    | `static int` | `NUMBER_FIELD_NUMBER` |
    | `static int` | `PARENTHASH_FIELD_NUMBER` |
    | `static int` | `TIMESTAMP_FIELD_NUMBER` |
    | `static int` | `TXTRIEROOT_FIELD_NUMBER` |
    | `static int` | `VERSION_FIELD_NUMBER` |
    | `static int` | `WITNESS_ADDRESS_FIELD_NUMBER` |
    | `static int` | `WITNESS_ID_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getAccountStateRoot()` `bytes accountStateRoot = 11;` |
    | `static Chain.BlockHeader.raw` | `getDefaultInstance()` |
    | `Chain.BlockHeader.raw` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getNumber()` bytes nonce = 5; bytes difficulty = 6; |
    | `com.google.protobuf.ByteString` | `getParentHash()` `bytes parentHash = 3;` |
    | `com.google.protobuf.Parser<Chain.BlockHeader.raw>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `long` | `getTimestamp()` `int64 timestamp = 1;` |
    | `com.google.protobuf.ByteString` | `getTxTrieRoot()` `bytes txTrieRoot = 2;` |
    | `int` | `getVersion()` `int32 version = 10;` |
    | `com.google.protobuf.ByteString` | `getWitnessAddress()` `bytes witness_address = 9;` |
    | `long` | `getWitnessId()` `int64 witness_id = 8;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Chain.BlockHeader.raw.Builder` | `newBuilder()` |
    | `static Chain.BlockHeader.raw.Builder` | `newBuilder(Chain.BlockHeader.raw prototype)` |
    | `Chain.BlockHeader.raw.Builder` | `newBuilderForType()` |
    | `protected Chain.BlockHeader.raw.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Chain.BlockHeader.raw` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Chain.BlockHeader.raw` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(byte[] data)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(java.io.InputStream input)` |
    | `static Chain.BlockHeader.raw` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Chain.BlockHeader.raw>` | `parser()` |
    | `Chain.BlockHeader.raw.Builder` | `toBuilder()` |
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

    - #### TIMESTAMP\_FIELD\_NUMBER

      ```
      public static final int TIMESTAMP_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.raw.TIMESTAMP_FIELD_NUMBER)
    - #### TXTRIEROOT\_FIELD\_NUMBER

      ```
      public static final int TXTRIEROOT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.raw.TXTRIEROOT_FIELD_NUMBER)
    - #### PARENTHASH\_FIELD\_NUMBER

      ```
      public static final int PARENTHASH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.raw.PARENTHASH_FIELD_NUMBER)
    - #### NUMBER\_FIELD\_NUMBER

      ```
      public static final int NUMBER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.raw.NUMBER_FIELD_NUMBER)
    - #### WITNESS\_ID\_FIELD\_NUMBER

      ```
      public static final int WITNESS_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.raw.WITNESS_ID_FIELD_NUMBER)
    - #### WITNESS\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int WITNESS_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.raw.WITNESS_ADDRESS_FIELD_NUMBER)
    - #### VERSION\_FIELD\_NUMBER

      ```
      public static final int VERSION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.raw.VERSION_FIELD_NUMBER)
    - #### ACCOUNTSTATEROOT\_FIELD\_NUMBER

      ```
      public static final int ACCOUNTSTATEROOT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.BlockHeader.raw.ACCOUNTSTATEROOT_FIELD_NUMBER)
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
    - #### getTimestamp

      ```
      public long getTimestamp()
      ```

      `int64 timestamp = 1;`

      Specified by:
      :   `getTimestamp` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The timestamp.
    - #### getTxTrieRoot

      ```
      public com.google.protobuf.ByteString getTxTrieRoot()
      ```

      `bytes txTrieRoot = 2;`

      Specified by:
      :   `getTxTrieRoot` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The txTrieRoot.
    - #### getParentHash

      ```
      public com.google.protobuf.ByteString getParentHash()
      ```

      `bytes parentHash = 3;`

      Specified by:
      :   `getParentHash` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The parentHash.
    - #### getNumber

      ```
      public long getNumber()
      ```

      ```
       bytes nonce = 5;
       bytes difficulty = 6;
      ```

      `int64 number = 7;`

      Specified by:
      :   `getNumber` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The number.
    - #### getWitnessId

      ```
      public long getWitnessId()
      ```

      `int64 witness_id = 8;`

      Specified by:
      :   `getWitnessId` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The witnessId.
    - #### getWitnessAddress

      ```
      public com.google.protobuf.ByteString getWitnessAddress()
      ```

      `bytes witness_address = 9;`

      Specified by:
      :   `getWitnessAddress` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The witnessAddress.
    - #### getVersion

      ```
      public int getVersion()
      ```

      `int32 version = 10;`

      Specified by:
      :   `getVersion` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The version.
    - #### getAccountStateRoot

      ```
      public com.google.protobuf.ByteString getAccountStateRoot()
      ```

      `bytes accountStateRoot = 11;`

      Specified by:
      :   `getAccountStateRoot` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The accountStateRoot.
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
      public static Chain.BlockHeader.raw parseFrom(java.nio.ByteBuffer data)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader.raw parseFrom(java.nio.ByteBuffer data,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader.raw parseFrom(com.google.protobuf.ByteString data)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader.raw parseFrom(com.google.protobuf.ByteString data,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader.raw parseFrom(byte[] data)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader.raw parseFrom(byte[] data,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader.raw parseFrom(java.io.InputStream input)
                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader.raw parseFrom(java.io.InputStream input,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.BlockHeader.raw parseDelimitedFrom(java.io.InputStream input)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.BlockHeader.raw parseDelimitedFrom(java.io.InputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader.raw parseFrom(com.google.protobuf.CodedInputStream input)
                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.BlockHeader.raw parseFrom(com.google.protobuf.CodedInputStream input,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Chain.BlockHeader.raw.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Chain.BlockHeader.raw.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Chain.BlockHeader.raw.Builder newBuilder(Chain.BlockHeader.raw prototype)
      ```
    - #### toBuilder

      ```
      public Chain.BlockHeader.raw.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Chain.BlockHeader.raw.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Chain.BlockHeader.raw getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Chain.BlockHeader.raw> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Chain.BlockHeader.raw> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Chain.BlockHeader.raw getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`