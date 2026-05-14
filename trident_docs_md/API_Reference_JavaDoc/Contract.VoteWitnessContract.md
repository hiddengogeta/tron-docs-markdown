

org.tron.trident.proto

## Class Contract.VoteWitnessContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Contract.VoteWitnessContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Contract.VoteWitnessContractOrBuilder](../../../../org/tron/trident/proto/Contract.VoteWitnessContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.VoteWitnessContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Contract.VoteWitnessContractOrBuilder
  ```

  Protobuf type `protocol.VoteWitnessContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Contract.VoteWitnessContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.VoteWitnessContract.Builder` Protobuf type `protocol.VoteWitnessContract` |
    | `static class` | `Contract.VoteWitnessContract.Vote` Protobuf type `protocol.VoteWitnessContract.Vote` |
    | `static interface` | `Contract.VoteWitnessContract.VoteOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `SUPPORT_FIELD_NUMBER` |
    | `static int` | `VOTES_FIELD_NUMBER` |

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
    | `static Contract.VoteWitnessContract` | `getDefaultInstance()` |
    | `Contract.VoteWitnessContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.Parser<Contract.VoteWitnessContract>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `boolean` | `getSupport()` `bool support = 3;` |
    | `Contract.VoteWitnessContract.Vote` | `getVotes(int index)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `int` | `getVotesCount()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `java.util.List<Contract.VoteWitnessContract.Vote>` | `getVotesList()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.VoteOrBuilder` | `getVotesOrBuilder(int index)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `java.util.List<? extends Contract.VoteWitnessContract.VoteOrBuilder>` | `getVotesOrBuilderList()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Contract.VoteWitnessContract.Builder` | `newBuilder()` |
    | `static Contract.VoteWitnessContract.Builder` | `newBuilder(Contract.VoteWitnessContract prototype)` |
    | `Contract.VoteWitnessContract.Builder` | `newBuilderForType()` |
    | `protected Contract.VoteWitnessContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Contract.VoteWitnessContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Contract.VoteWitnessContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(byte[] data)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(java.io.InputStream input)` |
    | `static Contract.VoteWitnessContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Contract.VoteWitnessContract>` | `parser()` |
    | `Contract.VoteWitnessContract.Builder` | `toBuilder()` |
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
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.VoteWitnessContract.OWNER_ADDRESS_FIELD_NUMBER)
    - #### VOTES\_FIELD\_NUMBER

      ```
      public static final int VOTES_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.VoteWitnessContract.VOTES_FIELD_NUMBER)
    - #### SUPPORT\_FIELD\_NUMBER

      ```
      public static final int SUPPORT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.VoteWitnessContract.SUPPORT_FIELD_NUMBER)
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
      :   `getOwnerAddress` in interface `Contract.VoteWitnessContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### getVotesList

      ```
      public java.util.List<Contract.VoteWitnessContract.Vote> getVotesList()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`

      Specified by:
      :   `getVotesList` in interface `Contract.VoteWitnessContractOrBuilder`
    - #### getVotesOrBuilderList

      ```
      public java.util.List<? extends Contract.VoteWitnessContract.VoteOrBuilder> getVotesOrBuilderList()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`

      Specified by:
      :   `getVotesOrBuilderList` in interface `Contract.VoteWitnessContractOrBuilder`
    - #### getVotesCount

      ```
      public int getVotesCount()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`

      Specified by:
      :   `getVotesCount` in interface `Contract.VoteWitnessContractOrBuilder`
    - #### getVotes

      ```
      public Contract.VoteWitnessContract.Vote getVotes(int index)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`

      Specified by:
      :   `getVotes` in interface `Contract.VoteWitnessContractOrBuilder`
    - #### getVotesOrBuilder

      ```
      public Contract.VoteWitnessContract.VoteOrBuilder getVotesOrBuilder(int index)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`

      Specified by:
      :   `getVotesOrBuilder` in interface `Contract.VoteWitnessContractOrBuilder`
    - #### getSupport

      ```
      public boolean getSupport()
      ```

      `bool support = 3;`

      Specified by:
      :   `getSupport` in interface `Contract.VoteWitnessContractOrBuilder`

      Returns:
      :   The support.
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
      public static Contract.VoteWitnessContract parseFrom(java.nio.ByteBuffer data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.VoteWitnessContract parseFrom(java.nio.ByteBuffer data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.VoteWitnessContract parseFrom(com.google.protobuf.ByteString data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.VoteWitnessContract parseFrom(com.google.protobuf.ByteString data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.VoteWitnessContract parseFrom(byte[] data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.VoteWitnessContract parseFrom(byte[] data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.VoteWitnessContract parseFrom(java.io.InputStream input)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.VoteWitnessContract parseFrom(java.io.InputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.VoteWitnessContract parseDelimitedFrom(java.io.InputStream input)
                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.VoteWitnessContract parseDelimitedFrom(java.io.InputStream input,
                                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.VoteWitnessContract parseFrom(com.google.protobuf.CodedInputStream input)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.VoteWitnessContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Contract.VoteWitnessContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Contract.VoteWitnessContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Contract.VoteWitnessContract.Builder newBuilder(Contract.VoteWitnessContract prototype)
      ```
    - #### toBuilder

      ```
      public Contract.VoteWitnessContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Contract.VoteWitnessContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Contract.VoteWitnessContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Contract.VoteWitnessContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Contract.VoteWitnessContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Contract.VoteWitnessContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`