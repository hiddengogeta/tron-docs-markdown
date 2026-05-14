

org.tron.trident.proto

## Class Contract.AccountPermissionUpdateContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Contract.AccountPermissionUpdateContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Contract.AccountPermissionUpdateContractOrBuilder](../../../../org/tron/trident/proto/Contract.AccountPermissionUpdateContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.AccountPermissionUpdateContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Contract.AccountPermissionUpdateContractOrBuilder
  ```

  Protobuf type `protocol.AccountPermissionUpdateContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Contract.AccountPermissionUpdateContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.AccountPermissionUpdateContract.Builder` Protobuf type `protocol.AccountPermissionUpdateContract` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ACTIVES_FIELD_NUMBER` |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `OWNER_FIELD_NUMBER` |
    | `static int` | `WITNESS_FIELD_NUMBER` |

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
    | `Common.Permission` | `getActives(int index)` Empty is invalidate |
    | `int` | `getActivesCount()` Empty is invalidate |
    | `java.util.List<Common.Permission>` | `getActivesList()` Empty is invalidate |
    | `Common.PermissionOrBuilder` | `getActivesOrBuilder(int index)` Empty is invalidate |
    | `java.util.List<? extends Common.PermissionOrBuilder>` | `getActivesOrBuilderList()` Empty is invalidate |
    | `static Contract.AccountPermissionUpdateContract` | `getDefaultInstance()` |
    | `Contract.AccountPermissionUpdateContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `Common.Permission` | `getOwner()` Empty is invalidate |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `Common.PermissionOrBuilder` | `getOwnerOrBuilder()` Empty is invalidate |
    | `com.google.protobuf.Parser<Contract.AccountPermissionUpdateContract>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `Common.Permission` | `getWitness()` Can be empty |
    | `Common.PermissionOrBuilder` | `getWitnessOrBuilder()` Can be empty |
    | `int` | `hashCode()` |
    | `boolean` | `hasOwner()` Empty is invalidate |
    | `boolean` | `hasWitness()` Can be empty |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Contract.AccountPermissionUpdateContract.Builder` | `newBuilder()` |
    | `static Contract.AccountPermissionUpdateContract.Builder` | `newBuilder(Contract.AccountPermissionUpdateContract prototype)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `newBuilderForType()` |
    | `protected Contract.AccountPermissionUpdateContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(byte[] data)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(java.io.InputStream input)` |
    | `static Contract.AccountPermissionUpdateContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Contract.AccountPermissionUpdateContract>` | `parser()` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `toBuilder()` |
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
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AccountPermissionUpdateContract.OWNER_ADDRESS_FIELD_NUMBER)
    - #### OWNER\_FIELD\_NUMBER

      ```
      public static final int OWNER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AccountPermissionUpdateContract.OWNER_FIELD_NUMBER)
    - #### WITNESS\_FIELD\_NUMBER

      ```
      public static final int WITNESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AccountPermissionUpdateContract.WITNESS_FIELD_NUMBER)
    - #### ACTIVES\_FIELD\_NUMBER

      ```
      public static final int ACTIVES_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AccountPermissionUpdateContract.ACTIVES_FIELD_NUMBER)
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
      :   `getOwnerAddress` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### hasOwner

      ```
      public boolean hasOwner()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`

      Specified by:
      :   `hasOwner` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   Whether the owner field is set.
    - #### getOwner

      ```
      public Common.Permission getOwner()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`

      Specified by:
      :   `getOwner` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   The owner.
    - #### getOwnerOrBuilder

      ```
      public Common.PermissionOrBuilder getOwnerOrBuilder()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`

      Specified by:
      :   `getOwnerOrBuilder` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### hasWitness

      ```
      public boolean hasWitness()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`

      Specified by:
      :   `hasWitness` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   Whether the witness field is set.
    - #### getWitness

      ```
      public Common.Permission getWitness()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`

      Specified by:
      :   `getWitness` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   The witness.
    - #### getWitnessOrBuilder

      ```
      public Common.PermissionOrBuilder getWitnessOrBuilder()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`

      Specified by:
      :   `getWitnessOrBuilder` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### getActivesList

      ```
      public java.util.List<Common.Permission> getActivesList()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActivesList` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### getActivesOrBuilderList

      ```
      public java.util.List<? extends Common.PermissionOrBuilder> getActivesOrBuilderList()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActivesOrBuilderList` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### getActivesCount

      ```
      public int getActivesCount()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActivesCount` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### getActives

      ```
      public Common.Permission getActives(int index)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActives` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### getActivesOrBuilder

      ```
      public Common.PermissionOrBuilder getActivesOrBuilder(int index)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActivesOrBuilder` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
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
      public static Contract.AccountPermissionUpdateContract parseFrom(java.nio.ByteBuffer data)
                                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseFrom(java.nio.ByteBuffer data,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseFrom(com.google.protobuf.ByteString data)
                                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseFrom(com.google.protobuf.ByteString data,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseFrom(byte[] data)
                                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseFrom(byte[] data,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseFrom(java.io.InputStream input)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseFrom(java.io.InputStream input,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseDelimitedFrom(java.io.InputStream input)
                                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseDelimitedFrom(java.io.InputStream input,
                                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseFrom(com.google.protobuf.CodedInputStream input)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.AccountPermissionUpdateContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Contract.AccountPermissionUpdateContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Contract.AccountPermissionUpdateContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Contract.AccountPermissionUpdateContract.Builder newBuilder(Contract.AccountPermissionUpdateContract prototype)
      ```
    - #### toBuilder

      ```
      public Contract.AccountPermissionUpdateContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Contract.AccountPermissionUpdateContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Contract.AccountPermissionUpdateContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Contract.AccountPermissionUpdateContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Contract.AccountPermissionUpdateContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Contract.AccountPermissionUpdateContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`