

org.tron.trident.proto

## Class Contract.ProposalCreateContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Contract.ProposalCreateContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Contract.ProposalCreateContractOrBuilder](../../../../org/tron/trident/proto/Contract.ProposalCreateContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.ProposalCreateContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Contract.ProposalCreateContractOrBuilder
  ```

  Protobuf type `protocol.ProposalCreateContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Contract.ProposalCreateContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.ProposalCreateContract.Builder` Protobuf type `protocol.ProposalCreateContract` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `PARAMETERS_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsParameters(long key)` `map<int64, int64> parameters = 2;` |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `static Contract.ProposalCreateContract` | `getDefaultInstance()` |
    | `Contract.ProposalCreateContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParameters()` Deprecated. |
    | `int` | `getParametersCount()` `map<int64, int64> parameters = 2;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParametersMap()` `map<int64, int64> parameters = 2;` |
    | `long` | `getParametersOrDefault(long key, long defaultValue)` `map<int64, int64> parameters = 2;` |
    | `long` | `getParametersOrThrow(long key)` `map<int64, int64> parameters = 2;` |
    | `com.google.protobuf.Parser<Contract.ProposalCreateContract>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `static Contract.ProposalCreateContract.Builder` | `newBuilder()` |
    | `static Contract.ProposalCreateContract.Builder` | `newBuilder(Contract.ProposalCreateContract prototype)` |
    | `Contract.ProposalCreateContract.Builder` | `newBuilderForType()` |
    | `protected Contract.ProposalCreateContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Contract.ProposalCreateContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Contract.ProposalCreateContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(byte[] data)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(java.io.InputStream input)` |
    | `static Contract.ProposalCreateContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Contract.ProposalCreateContract>` | `parser()` |
    | `Contract.ProposalCreateContract.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
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
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.ProposalCreateContract.OWNER_ADDRESS_FIELD_NUMBER)
    - #### PARAMETERS\_FIELD\_NUMBER

      ```
      public static final int PARAMETERS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.ProposalCreateContract.PARAMETERS_FIELD_NUMBER)
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
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3`
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
      :   `getOwnerAddress` in interface `Contract.ProposalCreateContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### getParametersCount

      ```
      public int getParametersCount()
      ```

      Description copied from interface: `Contract.ProposalCreateContractOrBuilder`

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `getParametersCount` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### containsParameters

      ```
      public boolean containsParameters(long key)
      ```

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `containsParameters` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### getParameters

      ```
      @Deprecated
      public java.util.Map<java.lang.Long,java.lang.Long> getParameters()
      ```

      Deprecated.

      Use [`getParametersMap()`](../../../../org/tron/trident/proto/Contract.ProposalCreateContract.html#getParametersMap--) instead.

      Specified by:
      :   `getParameters` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### getParametersMap

      ```
      public java.util.Map<java.lang.Long,java.lang.Long> getParametersMap()
      ```

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `getParametersMap` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### getParametersOrDefault

      ```
      public long getParametersOrDefault(long key,
                                         long defaultValue)
      ```

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `getParametersOrDefault` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### getParametersOrThrow

      ```
      public long getParametersOrThrow(long key)
      ```

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `getParametersOrThrow` in interface `Contract.ProposalCreateContractOrBuilder`
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
      public static Contract.ProposalCreateContract parseFrom(java.nio.ByteBuffer data)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.ProposalCreateContract parseFrom(java.nio.ByteBuffer data,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.ProposalCreateContract parseFrom(com.google.protobuf.ByteString data)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.ProposalCreateContract parseFrom(com.google.protobuf.ByteString data,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.ProposalCreateContract parseFrom(byte[] data)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.ProposalCreateContract parseFrom(byte[] data,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.ProposalCreateContract parseFrom(java.io.InputStream input)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.ProposalCreateContract parseFrom(java.io.InputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.ProposalCreateContract parseDelimitedFrom(java.io.InputStream input)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.ProposalCreateContract parseDelimitedFrom(java.io.InputStream input,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.ProposalCreateContract parseFrom(com.google.protobuf.CodedInputStream input)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.ProposalCreateContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Contract.ProposalCreateContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Contract.ProposalCreateContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Contract.ProposalCreateContract.Builder newBuilder(Contract.ProposalCreateContract prototype)
      ```
    - #### toBuilder

      ```
      public Contract.ProposalCreateContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Contract.ProposalCreateContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Contract.ProposalCreateContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Contract.ProposalCreateContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Contract.ProposalCreateContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Contract.ProposalCreateContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`