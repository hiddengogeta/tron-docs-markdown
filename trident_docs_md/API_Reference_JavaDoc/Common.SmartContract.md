

org.tron.trident.proto

## Class Common.SmartContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Common.SmartContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Common.SmartContractOrBuilder](../../../../org/tron/trident/proto/Common.SmartContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.SmartContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Common.SmartContractOrBuilder
  ```

  Protobuf type `protocol.SmartContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Common.SmartContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Common.SmartContract.ABI` Protobuf type `protocol.SmartContract.ABI` |
    | `static interface` | `Common.SmartContract.ABIOrBuilder` |
    | `static class` | `Common.SmartContract.Builder` Protobuf type `protocol.SmartContract` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ABI_FIELD_NUMBER` |
    | `static int` | `BYTECODE_FIELD_NUMBER` |
    | `static int` | `CALL_VALUE_FIELD_NUMBER` |
    | `static int` | `CODE_HASH_FIELD_NUMBER` |
    | `static int` | `CONSUME_USER_RESOURCE_PERCENT_FIELD_NUMBER` |
    | `static int` | `CONTRACT_ADDRESS_FIELD_NUMBER` |
    | `static int` | `NAME_FIELD_NUMBER` |
    | `static int` | `ORIGIN_ADDRESS_FIELD_NUMBER` |
    | `static int` | `ORIGIN_ENERGY_LIMIT_FIELD_NUMBER` |
    | `static int` | `TRX_HASH_FIELD_NUMBER` |
    | `static int` | `VERSION_FIELD_NUMBER` |

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
    | `Common.SmartContract.ABI` | `getAbi()` `.protocol.SmartContract.ABI abi = 3;` |
    | `Common.SmartContract.ABIOrBuilder` | `getAbiOrBuilder()` `.protocol.SmartContract.ABI abi = 3;` |
    | `com.google.protobuf.ByteString` | `getBytecode()` `bytes bytecode = 4;` |
    | `long` | `getCallValue()` `int64 call_value = 5;` |
    | `com.google.protobuf.ByteString` | `getCodeHash()` `bytes code_hash = 9;` |
    | `long` | `getConsumeUserResourcePercent()` `int64 consume_user_resource_percent = 6;` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 2;` |
    | `static Common.SmartContract` | `getDefaultInstance()` |
    | `Common.SmartContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `java.lang.String` | `getName()` `string name = 7;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 7;` |
    | `com.google.protobuf.ByteString` | `getOriginAddress()` `bytes origin_address = 1;` |
    | `long` | `getOriginEnergyLimit()` `int64 origin_energy_limit = 8;` |
    | `com.google.protobuf.Parser<Common.SmartContract>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getTrxHash()` `bytes trx_hash = 10;` |
    | `int` | `getVersion()` `int32 version = 11;` |
    | `boolean` | `hasAbi()` `.protocol.SmartContract.ABI abi = 3;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Common.SmartContract.Builder` | `newBuilder()` |
    | `static Common.SmartContract.Builder` | `newBuilder(Common.SmartContract prototype)` |
    | `Common.SmartContract.Builder` | `newBuilderForType()` |
    | `protected Common.SmartContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Common.SmartContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Common.SmartContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract` | `parseFrom(byte[] data)` |
    | `static Common.SmartContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Common.SmartContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Common.SmartContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Common.SmartContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract` | `parseFrom(java.io.InputStream input)` |
    | `static Common.SmartContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Common.SmartContract>` | `parser()` |
    | `Common.SmartContract.Builder` | `toBuilder()` |
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

    - #### ORIGIN\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int ORIGIN_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ORIGIN_ADDRESS_FIELD_NUMBER)
    - #### CONTRACT\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int CONTRACT_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.CONTRACT_ADDRESS_FIELD_NUMBER)
    - #### ABI\_FIELD\_NUMBER

      ```
      public static final int ABI_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI_FIELD_NUMBER)
    - #### BYTECODE\_FIELD\_NUMBER

      ```
      public static final int BYTECODE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.BYTECODE_FIELD_NUMBER)
    - #### CALL\_VALUE\_FIELD\_NUMBER

      ```
      public static final int CALL_VALUE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.CALL_VALUE_FIELD_NUMBER)
    - #### CONSUME\_USER\_RESOURCE\_PERCENT\_FIELD\_NUMBER

      ```
      public static final int CONSUME_USER_RESOURCE_PERCENT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.CONSUME_USER_RESOURCE_PERCENT_FIELD_NUMBER)
    - #### NAME\_FIELD\_NUMBER

      ```
      public static final int NAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.NAME_FIELD_NUMBER)
    - #### ORIGIN\_ENERGY\_LIMIT\_FIELD\_NUMBER

      ```
      public static final int ORIGIN_ENERGY_LIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ORIGIN_ENERGY_LIMIT_FIELD_NUMBER)
    - #### CODE\_HASH\_FIELD\_NUMBER

      ```
      public static final int CODE_HASH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.CODE_HASH_FIELD_NUMBER)
    - #### TRX\_HASH\_FIELD\_NUMBER

      ```
      public static final int TRX_HASH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.TRX_HASH_FIELD_NUMBER)
    - #### VERSION\_FIELD\_NUMBER

      ```
      public static final int VERSION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.VERSION_FIELD_NUMBER)
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
    - #### getOriginAddress

      ```
      public com.google.protobuf.ByteString getOriginAddress()
      ```

      `bytes origin_address = 1;`

      Specified by:
      :   `getOriginAddress` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The originAddress.
    - #### getContractAddress

      ```
      public com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 2;`

      Specified by:
      :   `getContractAddress` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The contractAddress.
    - #### hasAbi

      ```
      public boolean hasAbi()
      ```

      `.protocol.SmartContract.ABI abi = 3;`

      Specified by:
      :   `hasAbi` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   Whether the abi field is set.
    - #### getAbi

      ```
      public Common.SmartContract.ABI getAbi()
      ```

      `.protocol.SmartContract.ABI abi = 3;`

      Specified by:
      :   `getAbi` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The abi.
    - #### getAbiOrBuilder

      ```
      public Common.SmartContract.ABIOrBuilder getAbiOrBuilder()
      ```

      `.protocol.SmartContract.ABI abi = 3;`

      Specified by:
      :   `getAbiOrBuilder` in interface `Common.SmartContractOrBuilder`
    - #### getBytecode

      ```
      public com.google.protobuf.ByteString getBytecode()
      ```

      `bytes bytecode = 4;`

      Specified by:
      :   `getBytecode` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The bytecode.
    - #### getCallValue

      ```
      public long getCallValue()
      ```

      `int64 call_value = 5;`

      Specified by:
      :   `getCallValue` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The callValue.
    - #### getConsumeUserResourcePercent

      ```
      public long getConsumeUserResourcePercent()
      ```

      `int64 consume_user_resource_percent = 6;`

      Specified by:
      :   `getConsumeUserResourcePercent` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The consumeUserResourcePercent.
    - #### getName

      ```
      public java.lang.String getName()
      ```

      `string name = 7;`

      Specified by:
      :   `getName` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      public com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 7;`

      Specified by:
      :   `getNameBytes` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The bytes for name.
    - #### getOriginEnergyLimit

      ```
      public long getOriginEnergyLimit()
      ```

      `int64 origin_energy_limit = 8;`

      Specified by:
      :   `getOriginEnergyLimit` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The originEnergyLimit.
    - #### getCodeHash

      ```
      public com.google.protobuf.ByteString getCodeHash()
      ```

      `bytes code_hash = 9;`

      Specified by:
      :   `getCodeHash` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The codeHash.
    - #### getTrxHash

      ```
      public com.google.protobuf.ByteString getTrxHash()
      ```

      `bytes trx_hash = 10;`

      Specified by:
      :   `getTrxHash` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The trxHash.
    - #### getVersion

      ```
      public int getVersion()
      ```

      `int32 version = 11;`

      Specified by:
      :   `getVersion` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The version.
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
      public static Common.SmartContract parseFrom(java.nio.ByteBuffer data)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract parseFrom(java.nio.ByteBuffer data,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract parseFrom(com.google.protobuf.ByteString data)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract parseFrom(com.google.protobuf.ByteString data,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract parseFrom(byte[] data)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract parseFrom(byte[] data,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract parseFrom(java.io.InputStream input)
                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.SmartContract parseFrom(java.io.InputStream input,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.SmartContract parseDelimitedFrom(java.io.InputStream input)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.SmartContract parseDelimitedFrom(java.io.InputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.SmartContract parseFrom(com.google.protobuf.CodedInputStream input)
                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.SmartContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Common.SmartContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Common.SmartContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Common.SmartContract.Builder newBuilder(Common.SmartContract prototype)
      ```
    - #### toBuilder

      ```
      public Common.SmartContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Common.SmartContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Common.SmartContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Common.SmartContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Common.SmartContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Common.SmartContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`