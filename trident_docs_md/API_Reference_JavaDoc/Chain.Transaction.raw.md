

org.tron.trident.proto

## Class Chain.Transaction.raw

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Chain.Transaction.raw

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Chain.Transaction.rawOrBuilder](../../../../org/tron/trident/proto/Chain.Transaction.rawOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction](../../../../org/tron/trident/proto/Chain.Transaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.Transaction.raw
  extends com.google.protobuf.GeneratedMessageV3
  implements Chain.Transaction.rawOrBuilder
  ```

  Protobuf type `protocol.Transaction.raw`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Chain.Transaction.raw)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Chain.Transaction.raw.Builder` Protobuf type `protocol.Transaction.raw` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `AUTHS_FIELD_NUMBER` |
    | `static int` | `CONTRACT_FIELD_NUMBER` |
    | `static int` | `DATA_FIELD_NUMBER` |
    | `static int` | `EXPIRATION_FIELD_NUMBER` |
    | `static int` | `FEE_LIMIT_FIELD_NUMBER` |
    | `static int` | `REF_BLOCK_BYTES_FIELD_NUMBER` |
    | `static int` | `REF_BLOCK_HASH_FIELD_NUMBER` |
    | `static int` | `REF_BLOCK_NUM_FIELD_NUMBER` |
    | `static int` | `SCRIPTS_FIELD_NUMBER` |
    | `static int` | `TIMESTAMP_FIELD_NUMBER` |

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
    | `Common.authority` | `getAuths(int index)` `repeated .protocol.authority auths = 9;` |
    | `int` | `getAuthsCount()` `repeated .protocol.authority auths = 9;` |
    | `java.util.List<Common.authority>` | `getAuthsList()` `repeated .protocol.authority auths = 9;` |
    | `Common.authorityOrBuilder` | `getAuthsOrBuilder(int index)` `repeated .protocol.authority auths = 9;` |
    | `java.util.List<? extends Common.authorityOrBuilder>` | `getAuthsOrBuilderList()` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.Contract` | `getContract(int index)` only support size = 1, repeated list here for extension |
    | `int` | `getContractCount()` only support size = 1, repeated list here for extension |
    | `java.util.List<Chain.Transaction.Contract>` | `getContractList()` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.ContractOrBuilder` | `getContractOrBuilder(int index)` only support size = 1, repeated list here for extension |
    | `java.util.List<? extends Chain.Transaction.ContractOrBuilder>` | `getContractOrBuilderList()` only support size = 1, repeated list here for extension |
    | `com.google.protobuf.ByteString` | `getData()` data not used |
    | `static Chain.Transaction.raw` | `getDefaultInstance()` |
    | `Chain.Transaction.raw` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getExpiration()` `int64 expiration = 8;` |
    | `long` | `getFeeLimit()` `int64 fee_limit = 18;` |
    | `com.google.protobuf.Parser<Chain.Transaction.raw>` | `getParserForType()` |
    | `com.google.protobuf.ByteString` | `getRefBlockBytes()` `bytes ref_block_bytes = 1;` |
    | `com.google.protobuf.ByteString` | `getRefBlockHash()` `bytes ref_block_hash = 4;` |
    | `long` | `getRefBlockNum()` `int64 ref_block_num = 3;` |
    | `com.google.protobuf.ByteString` | `getScripts()` scripts not used |
    | `int` | `getSerializedSize()` |
    | `long` | `getTimestamp()` `int64 timestamp = 14;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Chain.Transaction.raw.Builder` | `newBuilder()` |
    | `static Chain.Transaction.raw.Builder` | `newBuilder(Chain.Transaction.raw prototype)` |
    | `Chain.Transaction.raw.Builder` | `newBuilderForType()` |
    | `protected Chain.Transaction.raw.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Chain.Transaction.raw` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Chain.Transaction.raw` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.raw` | `parseFrom(byte[] data)` |
    | `static Chain.Transaction.raw` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.raw` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Chain.Transaction.raw` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.raw` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Chain.Transaction.raw` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.raw` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Chain.Transaction.raw` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.raw` | `parseFrom(java.io.InputStream input)` |
    | `static Chain.Transaction.raw` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Chain.Transaction.raw>` | `parser()` |
    | `Chain.Transaction.raw.Builder` | `toBuilder()` |
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

    - #### REF\_BLOCK\_BYTES\_FIELD\_NUMBER

      ```
      public static final int REF_BLOCK_BYTES_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.REF_BLOCK_BYTES_FIELD_NUMBER)
    - #### REF\_BLOCK\_NUM\_FIELD\_NUMBER

      ```
      public static final int REF_BLOCK_NUM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.REF_BLOCK_NUM_FIELD_NUMBER)
    - #### REF\_BLOCK\_HASH\_FIELD\_NUMBER

      ```
      public static final int REF_BLOCK_HASH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.REF_BLOCK_HASH_FIELD_NUMBER)
    - #### EXPIRATION\_FIELD\_NUMBER

      ```
      public static final int EXPIRATION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.EXPIRATION_FIELD_NUMBER)
    - #### AUTHS\_FIELD\_NUMBER

      ```
      public static final int AUTHS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.AUTHS_FIELD_NUMBER)
    - #### DATA\_FIELD\_NUMBER

      ```
      public static final int DATA_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.DATA_FIELD_NUMBER)
    - #### CONTRACT\_FIELD\_NUMBER

      ```
      public static final int CONTRACT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.CONTRACT_FIELD_NUMBER)
    - #### SCRIPTS\_FIELD\_NUMBER

      ```
      public static final int SCRIPTS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.SCRIPTS_FIELD_NUMBER)
    - #### TIMESTAMP\_FIELD\_NUMBER

      ```
      public static final int TIMESTAMP_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.TIMESTAMP_FIELD_NUMBER)
    - #### FEE\_LIMIT\_FIELD\_NUMBER

      ```
      public static final int FEE_LIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.raw.FEE_LIMIT_FIELD_NUMBER)
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
    - #### getRefBlockBytes

      ```
      public com.google.protobuf.ByteString getRefBlockBytes()
      ```

      `bytes ref_block_bytes = 1;`

      Specified by:
      :   `getRefBlockBytes` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The refBlockBytes.
    - #### getRefBlockNum

      ```
      public long getRefBlockNum()
      ```

      `int64 ref_block_num = 3;`

      Specified by:
      :   `getRefBlockNum` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The refBlockNum.
    - #### getRefBlockHash

      ```
      public com.google.protobuf.ByteString getRefBlockHash()
      ```

      `bytes ref_block_hash = 4;`

      Specified by:
      :   `getRefBlockHash` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The refBlockHash.
    - #### getExpiration

      ```
      public long getExpiration()
      ```

      `int64 expiration = 8;`

      Specified by:
      :   `getExpiration` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The expiration.
    - #### getAuthsList

      ```
      public java.util.List<Common.authority> getAuthsList()
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuthsList` in interface `Chain.Transaction.rawOrBuilder`
    - #### getAuthsOrBuilderList

      ```
      public java.util.List<? extends Common.authorityOrBuilder> getAuthsOrBuilderList()
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuthsOrBuilderList` in interface `Chain.Transaction.rawOrBuilder`
    - #### getAuthsCount

      ```
      public int getAuthsCount()
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuthsCount` in interface `Chain.Transaction.rawOrBuilder`
    - #### getAuths

      ```
      public Common.authority getAuths(int index)
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuths` in interface `Chain.Transaction.rawOrBuilder`
    - #### getAuthsOrBuilder

      ```
      public Common.authorityOrBuilder getAuthsOrBuilder(int index)
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuthsOrBuilder` in interface `Chain.Transaction.rawOrBuilder`
    - #### getData

      ```
      public com.google.protobuf.ByteString getData()
      ```

      ```
       data not used
      ```

      `bytes data = 10;`

      Specified by:
      :   `getData` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The data.
    - #### getContractList

      ```
      public java.util.List<Chain.Transaction.Contract> getContractList()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContractList` in interface `Chain.Transaction.rawOrBuilder`
    - #### getContractOrBuilderList

      ```
      public java.util.List<? extends Chain.Transaction.ContractOrBuilder> getContractOrBuilderList()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContractOrBuilderList` in interface `Chain.Transaction.rawOrBuilder`
    - #### getContractCount

      ```
      public int getContractCount()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContractCount` in interface `Chain.Transaction.rawOrBuilder`
    - #### getContract

      ```
      public Chain.Transaction.Contract getContract(int index)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContract` in interface `Chain.Transaction.rawOrBuilder`
    - #### getContractOrBuilder

      ```
      public Chain.Transaction.ContractOrBuilder getContractOrBuilder(int index)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContractOrBuilder` in interface `Chain.Transaction.rawOrBuilder`
    - #### getScripts

      ```
      public com.google.protobuf.ByteString getScripts()
      ```

      ```
       scripts not used
      ```

      `bytes scripts = 12;`

      Specified by:
      :   `getScripts` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The scripts.
    - #### getTimestamp

      ```
      public long getTimestamp()
      ```

      `int64 timestamp = 14;`

      Specified by:
      :   `getTimestamp` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The timestamp.
    - #### getFeeLimit

      ```
      public long getFeeLimit()
      ```

      `int64 fee_limit = 18;`

      Specified by:
      :   `getFeeLimit` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The feeLimit.
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
      public static Chain.Transaction.raw parseFrom(java.nio.ByteBuffer data)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.raw parseFrom(java.nio.ByteBuffer data,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.raw parseFrom(com.google.protobuf.ByteString data)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.raw parseFrom(com.google.protobuf.ByteString data,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.raw parseFrom(byte[] data)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.raw parseFrom(byte[] data,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.raw parseFrom(java.io.InputStream input)
                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction.raw parseFrom(java.io.InputStream input,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.Transaction.raw parseDelimitedFrom(java.io.InputStream input)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.Transaction.raw parseDelimitedFrom(java.io.InputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction.raw parseFrom(com.google.protobuf.CodedInputStream input)
                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction.raw parseFrom(com.google.protobuf.CodedInputStream input,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Chain.Transaction.raw.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Chain.Transaction.raw.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Chain.Transaction.raw.Builder newBuilder(Chain.Transaction.raw prototype)
      ```
    - #### toBuilder

      ```
      public Chain.Transaction.raw.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Chain.Transaction.raw.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Chain.Transaction.raw getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Chain.Transaction.raw> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Chain.Transaction.raw> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Chain.Transaction.raw getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`