

org.tron.trident.proto

## Class Contract.DelegateResourceContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Contract.DelegateResourceContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Contract.DelegateResourceContractOrBuilder](../../../../org/tron/trident/proto/Contract.DelegateResourceContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.DelegateResourceContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Contract.DelegateResourceContractOrBuilder
  ```

  Protobuf type `protocol.DelegateResourceContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Contract.DelegateResourceContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.DelegateResourceContract.Builder` Protobuf type `protocol.DelegateResourceContract` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BALANCE_FIELD_NUMBER` |
    | `static int` | `LOCK_FIELD_NUMBER` |
    | `static int` | `LOCK_PERIOD_FIELD_NUMBER` |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `RECEIVER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `RESOURCE_FIELD_NUMBER` |

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
    | `long` | `getBalance()` `int64 balance = 3;` |
    | `static Contract.DelegateResourceContract` | `getDefaultInstance()` |
    | `Contract.DelegateResourceContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `boolean` | `getLock()` `bool lock = 5;` |
    | `long` | `getLockPeriod()` `int64 lock_period = 6;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.Parser<Contract.DelegateResourceContract>` | `getParserForType()` |
    | `com.google.protobuf.ByteString` | `getReceiverAddress()` `bytes receiver_address = 4;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 2;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 2;` |
    | `int` | `getSerializedSize()` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Contract.DelegateResourceContract.Builder` | `newBuilder()` |
    | `static Contract.DelegateResourceContract.Builder` | `newBuilder(Contract.DelegateResourceContract prototype)` |
    | `Contract.DelegateResourceContract.Builder` | `newBuilderForType()` |
    | `protected Contract.DelegateResourceContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Contract.DelegateResourceContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Contract.DelegateResourceContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(byte[] data)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(java.io.InputStream input)` |
    | `static Contract.DelegateResourceContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Contract.DelegateResourceContract>` | `parser()` |
    | `Contract.DelegateResourceContract.Builder` | `toBuilder()` |
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
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.DelegateResourceContract.OWNER_ADDRESS_FIELD_NUMBER)
    - #### RESOURCE\_FIELD\_NUMBER

      ```
      public static final int RESOURCE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.DelegateResourceContract.RESOURCE_FIELD_NUMBER)
    - #### BALANCE\_FIELD\_NUMBER

      ```
      public static final int BALANCE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.DelegateResourceContract.BALANCE_FIELD_NUMBER)
    - #### RECEIVER\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int RECEIVER_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.DelegateResourceContract.RECEIVER_ADDRESS_FIELD_NUMBER)
    - #### LOCK\_FIELD\_NUMBER

      ```
      public static final int LOCK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.DelegateResourceContract.LOCK_FIELD_NUMBER)
    - #### LOCK\_PERIOD\_FIELD\_NUMBER

      ```
      public static final int LOCK_PERIOD_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.DelegateResourceContract.LOCK_PERIOD_FIELD_NUMBER)
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
      :   `getOwnerAddress` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### getResourceValue

      ```
      public int getResourceValue()
      ```

      `.protocol.ResourceCode resource = 2;`

      Specified by:
      :   `getResourceValue` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### getResource

      ```
      public Common.ResourceCode getResource()
      ```

      `.protocol.ResourceCode resource = 2;`

      Specified by:
      :   `getResource` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The resource.
    - #### getBalance

      ```
      public long getBalance()
      ```

      `int64 balance = 3;`

      Specified by:
      :   `getBalance` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The balance.
    - #### getReceiverAddress

      ```
      public com.google.protobuf.ByteString getReceiverAddress()
      ```

      `bytes receiver_address = 4;`

      Specified by:
      :   `getReceiverAddress` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The receiverAddress.
    - #### getLock

      ```
      public boolean getLock()
      ```

      `bool lock = 5;`

      Specified by:
      :   `getLock` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The lock.
    - #### getLockPeriod

      ```
      public long getLockPeriod()
      ```

      `int64 lock_period = 6;`

      Specified by:
      :   `getLockPeriod` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The lockPeriod.
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
      public static Contract.DelegateResourceContract parseFrom(java.nio.ByteBuffer data)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.DelegateResourceContract parseFrom(java.nio.ByteBuffer data,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.DelegateResourceContract parseFrom(com.google.protobuf.ByteString data)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.DelegateResourceContract parseFrom(com.google.protobuf.ByteString data,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.DelegateResourceContract parseFrom(byte[] data)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.DelegateResourceContract parseFrom(byte[] data,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.DelegateResourceContract parseFrom(java.io.InputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.DelegateResourceContract parseFrom(java.io.InputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.DelegateResourceContract parseDelimitedFrom(java.io.InputStream input)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.DelegateResourceContract parseDelimitedFrom(java.io.InputStream input,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.DelegateResourceContract parseFrom(com.google.protobuf.CodedInputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.DelegateResourceContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Contract.DelegateResourceContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Contract.DelegateResourceContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Contract.DelegateResourceContract.Builder newBuilder(Contract.DelegateResourceContract prototype)
      ```
    - #### toBuilder

      ```
      public Contract.DelegateResourceContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Contract.DelegateResourceContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Contract.DelegateResourceContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Contract.DelegateResourceContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Contract.DelegateResourceContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Contract.DelegateResourceContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`