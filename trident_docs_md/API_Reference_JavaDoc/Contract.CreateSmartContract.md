

org.tron.trident.proto

## Class Contract.CreateSmartContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Contract.CreateSmartContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Contract.CreateSmartContractOrBuilder](../../../../org/tron/trident/proto/Contract.CreateSmartContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.CreateSmartContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Contract.CreateSmartContractOrBuilder
  ```

  Protobuf type `protocol.CreateSmartContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Contract.CreateSmartContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.CreateSmartContract.Builder` Protobuf type `protocol.CreateSmartContract` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `CALL_TOKEN_VALUE_FIELD_NUMBER` |
    | `static int` | `NEW_CONTRACT_FIELD_NUMBER` |
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
    | `long` | `getCallTokenValue()` `int64 call_token_value = 3;` |
    | `static Contract.CreateSmartContract` | `getDefaultInstance()` |
    | `Contract.CreateSmartContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `Common.SmartContract` | `getNewContract()` `.protocol.SmartContract new_contract = 2;` |
    | `Common.SmartContractOrBuilder` | `getNewContractOrBuilder()` `.protocol.SmartContract new_contract = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.Parser<Contract.CreateSmartContract>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `long` | `getTokenId()` `int64 token_id = 4;` |
    | `int` | `hashCode()` |
    | `boolean` | `hasNewContract()` `.protocol.SmartContract new_contract = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Contract.CreateSmartContract.Builder` | `newBuilder()` |
    | `static Contract.CreateSmartContract.Builder` | `newBuilder(Contract.CreateSmartContract prototype)` |
    | `Contract.CreateSmartContract.Builder` | `newBuilderForType()` |
    | `protected Contract.CreateSmartContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Contract.CreateSmartContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Contract.CreateSmartContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.CreateSmartContract` | `parseFrom(byte[] data)` |
    | `static Contract.CreateSmartContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.CreateSmartContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Contract.CreateSmartContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.CreateSmartContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Contract.CreateSmartContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.CreateSmartContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Contract.CreateSmartContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.CreateSmartContract` | `parseFrom(java.io.InputStream input)` |
    | `static Contract.CreateSmartContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Contract.CreateSmartContract>` | `parser()` |
    | `Contract.CreateSmartContract.Builder` | `toBuilder()` |
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
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.CreateSmartContract.OWNER_ADDRESS_FIELD_NUMBER)
    - #### NEW\_CONTRACT\_FIELD\_NUMBER

      ```
      public static final int NEW_CONTRACT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.CreateSmartContract.NEW_CONTRACT_FIELD_NUMBER)
    - #### CALL\_TOKEN\_VALUE\_FIELD\_NUMBER

      ```
      public static final int CALL_TOKEN_VALUE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.CreateSmartContract.CALL_TOKEN_VALUE_FIELD_NUMBER)
    - #### TOKEN\_ID\_FIELD\_NUMBER

      ```
      public static final int TOKEN_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.CreateSmartContract.TOKEN_ID_FIELD_NUMBER)
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
      :   `getOwnerAddress` in interface `Contract.CreateSmartContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### hasNewContract

      ```
      public boolean hasNewContract()
      ```

      `.protocol.SmartContract new_contract = 2;`

      Specified by:
      :   `hasNewContract` in interface `Contract.CreateSmartContractOrBuilder`

      Returns:
      :   Whether the newContract field is set.
    - #### getNewContract

      ```
      public Common.SmartContract getNewContract()
      ```

      `.protocol.SmartContract new_contract = 2;`

      Specified by:
      :   `getNewContract` in interface `Contract.CreateSmartContractOrBuilder`

      Returns:
      :   The newContract.
    - #### getNewContractOrBuilder

      ```
      public Common.SmartContractOrBuilder getNewContractOrBuilder()
      ```

      `.protocol.SmartContract new_contract = 2;`

      Specified by:
      :   `getNewContractOrBuilder` in interface `Contract.CreateSmartContractOrBuilder`
    - #### getCallTokenValue

      ```
      public long getCallTokenValue()
      ```

      `int64 call_token_value = 3;`

      Specified by:
      :   `getCallTokenValue` in interface `Contract.CreateSmartContractOrBuilder`

      Returns:
      :   The callTokenValue.
    - #### getTokenId

      ```
      public long getTokenId()
      ```

      `int64 token_id = 4;`

      Specified by:
      :   `getTokenId` in interface `Contract.CreateSmartContractOrBuilder`

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
      public static Contract.CreateSmartContract parseFrom(java.nio.ByteBuffer data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.CreateSmartContract parseFrom(java.nio.ByteBuffer data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.CreateSmartContract parseFrom(com.google.protobuf.ByteString data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.CreateSmartContract parseFrom(com.google.protobuf.ByteString data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.CreateSmartContract parseFrom(byte[] data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.CreateSmartContract parseFrom(byte[] data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.CreateSmartContract parseFrom(java.io.InputStream input)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.CreateSmartContract parseFrom(java.io.InputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.CreateSmartContract parseDelimitedFrom(java.io.InputStream input)
                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.CreateSmartContract parseDelimitedFrom(java.io.InputStream input,
                                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.CreateSmartContract parseFrom(com.google.protobuf.CodedInputStream input)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.CreateSmartContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Contract.CreateSmartContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Contract.CreateSmartContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Contract.CreateSmartContract.Builder newBuilder(Contract.CreateSmartContract prototype)
      ```
    - #### toBuilder

      ```
      public Contract.CreateSmartContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Contract.CreateSmartContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Contract.CreateSmartContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Contract.CreateSmartContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Contract.CreateSmartContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Contract.CreateSmartContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`