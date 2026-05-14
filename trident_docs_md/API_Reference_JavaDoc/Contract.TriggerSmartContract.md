

org.tron.trident.proto

## Class Contract.TriggerSmartContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Contract.TriggerSmartContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Contract.TriggerSmartContractOrBuilder](../../../../org/tron/trident/proto/Contract.TriggerSmartContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.TriggerSmartContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Contract.TriggerSmartContractOrBuilder
  ```

  Protobuf type `protocol.TriggerSmartContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Contract.TriggerSmartContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.TriggerSmartContract.Builder` Protobuf type `protocol.TriggerSmartContract` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `CALL_TOKEN_VALUE_FIELD_NUMBER` |
    | `static int` | `CALL_VALUE_FIELD_NUMBER` |
    | `static int` | `CONTRACT_ADDRESS_FIELD_NUMBER` |
    | `static int` | `DATA_FIELD_NUMBER` |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `TOKEN_ID_FIELD_NUMBER` |

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
    | `long` | `getCallTokenValue()` `int64 call_token_value = 5;` |
    | `long` | `getCallValue()` `int64 call_value = 3;` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 2;` |
    | `com.google.protobuf.ByteString` | `getData()` `bytes data = 4;` |
    | `static Contract.TriggerSmartContract` | `getDefaultInstance()` |
    | `Contract.TriggerSmartContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.Parser<Contract.TriggerSmartContract>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `long` | `getTokenId()` `int64 token_id = 6;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Contract.TriggerSmartContract.Builder` | `newBuilder()` |
    | `static Contract.TriggerSmartContract.Builder` | `newBuilder(Contract.TriggerSmartContract prototype)` |
    | `Contract.TriggerSmartContract.Builder` | `newBuilderForType()` |
    | `protected Contract.TriggerSmartContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Contract.TriggerSmartContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Contract.TriggerSmartContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(byte[] data)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(java.io.InputStream input)` |
    | `static Contract.TriggerSmartContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Contract.TriggerSmartContract>` | `parser()` |
    | `Contract.TriggerSmartContract.Builder` | `toBuilder()` |
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

    - #### OWNER\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int OWNER_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.TriggerSmartContract.OWNER_ADDRESS_FIELD_NUMBER)
    - #### CONTRACT\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int CONTRACT_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.TriggerSmartContract.CONTRACT_ADDRESS_FIELD_NUMBER)
    - #### CALL\_VALUE\_FIELD\_NUMBER

      ```
      public static final int CALL_VALUE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.TriggerSmartContract.CALL_VALUE_FIELD_NUMBER)
    - #### DATA\_FIELD\_NUMBER

      ```
      public static final int DATA_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.TriggerSmartContract.DATA_FIELD_NUMBER)
    - #### CALL\_TOKEN\_VALUE\_FIELD\_NUMBER

      ```
      public static final int CALL_TOKEN_VALUE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.TriggerSmartContract.CALL_TOKEN_VALUE_FIELD_NUMBER)
    - #### TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.TriggerSmartContract.TOKEN_ID_FIELD_NUMBER)
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
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### getContractAddress

      ```
      public com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 2;`

      Specified by:
      :   `getContractAddress` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The contractAddress.
    - #### getCallValue

      ```
      public long getCallValue()
      ```

      `int64 call_value = 3;`

      Specified by:
      :   `getCallValue` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The callValue.
    - #### getData

      ```
      public com.google.protobuf.ByteString getData()
      ```

      `bytes data = 4;`

      Specified by:
      :   `getData` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The data.
    - #### getCallTokenValue

      ```
      public long getCallTokenValue()
      ```

      `int64 call_token_value = 5;`

      Specified by:
      :   `getCallTokenValue` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The callTokenValue.
    - #### getTokenId

      ```
      public long getTokenId()
      ```

      `int64 token_id = 6;`

      Specified by:
      :   `getTokenId` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The tokenId.
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
      public static Contract.TriggerSmartContract parseFrom(java.nio.ByteBuffer data)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.TriggerSmartContract parseFrom(java.nio.ByteBuffer data,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.TriggerSmartContract parseFrom(com.google.protobuf.ByteString data)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.TriggerSmartContract parseFrom(com.google.protobuf.ByteString data,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.TriggerSmartContract parseFrom(byte[] data)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.TriggerSmartContract parseFrom(byte[] data,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.TriggerSmartContract parseFrom(java.io.InputStream input)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.TriggerSmartContract parseFrom(java.io.InputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.TriggerSmartContract parseDelimitedFrom(java.io.InputStream input)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.TriggerSmartContract parseDelimitedFrom(java.io.InputStream input,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.TriggerSmartContract parseFrom(com.google.protobuf.CodedInputStream input)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.TriggerSmartContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Contract.TriggerSmartContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Contract.TriggerSmartContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Contract.TriggerSmartContract.Builder newBuilder(Contract.TriggerSmartContract prototype)
      ```
    - #### toBuilder

      ```
      public Contract.TriggerSmartContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Contract.TriggerSmartContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Contract.TriggerSmartContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Contract.TriggerSmartContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Contract.TriggerSmartContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Contract.TriggerSmartContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`