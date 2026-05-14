

org.tron.trident.proto

## Class Response.Proposal

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.Proposal

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.ProposalOrBuilder](../../../../org/tron/trident/proto/Response.ProposalOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Proposal
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.ProposalOrBuilder
  ```

  Protobuf type `protocol.Proposal`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.Proposal)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.Proposal.Builder` Protobuf type `protocol.Proposal` |
    | `static class` | `Response.Proposal.State` Protobuf enum `protocol.Proposal.State` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `APPROVALS_FIELD_NUMBER` |
    | `static int` | `CREATE_TIME_FIELD_NUMBER` |
    | `static int` | `EXPIRATION_TIME_FIELD_NUMBER` |
    | `static int` | `PARAMETERS_FIELD_NUMBER` |
    | `static int` | `PROPOSAL_ID_FIELD_NUMBER` |
    | `static int` | `PROPOSER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `STATE_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsParameters(long key)` `map<int64, int64> parameters = 3;` |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `com.google.protobuf.ByteString` | `getApprovals(int index)` `repeated bytes approvals = 6;` |
    | `int` | `getApprovalsCount()` `repeated bytes approvals = 6;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getApprovalsList()` `repeated bytes approvals = 6;` |
    | `long` | `getCreateTime()` `int64 create_time = 5;` |
    | `static Response.Proposal` | `getDefaultInstance()` |
    | `Response.Proposal` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getExpirationTime()` `int64 expiration_time = 4;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParameters()` Deprecated. |
    | `int` | `getParametersCount()` `map<int64, int64> parameters = 3;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParametersMap()` `map<int64, int64> parameters = 3;` |
    | `long` | `getParametersOrDefault(long key, long defaultValue)` `map<int64, int64> parameters = 3;` |
    | `long` | `getParametersOrThrow(long key)` `map<int64, int64> parameters = 3;` |
    | `com.google.protobuf.Parser<Response.Proposal>` | `getParserForType()` |
    | `long` | `getProposalId()` `int64 proposal_id = 1;` |
    | `com.google.protobuf.ByteString` | `getProposerAddress()` `bytes proposer_address = 2;` |
    | `int` | `getSerializedSize()` |
    | `Response.Proposal.State` | `getState()` `.protocol.Proposal.State state = 7;` |
    | `int` | `getStateValue()` `.protocol.Proposal.State state = 7;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `static Response.Proposal.Builder` | `newBuilder()` |
    | `static Response.Proposal.Builder` | `newBuilder(Response.Proposal prototype)` |
    | `Response.Proposal.Builder` | `newBuilderForType()` |
    | `protected Response.Proposal.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.Proposal` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.Proposal` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Proposal` | `parseFrom(byte[] data)` |
    | `static Response.Proposal` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Proposal` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.Proposal` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Proposal` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.Proposal` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Proposal` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.Proposal` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Proposal` | `parseFrom(java.io.InputStream input)` |
    | `static Response.Proposal` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.Proposal>` | `parser()` |
    | `Response.Proposal.Builder` | `toBuilder()` |
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

    - #### PROPOSAL\_ID\_FIELD\_NUMBER

      ```
      public static final int PROPOSAL_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.PROPOSAL_ID_FIELD_NUMBER)
    - #### PROPOSER\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int PROPOSER_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.PROPOSER_ADDRESS_FIELD_NUMBER)
    - #### PARAMETERS\_FIELD\_NUMBER

      ```
      public static final int PARAMETERS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.PARAMETERS_FIELD_NUMBER)
    - #### EXPIRATION\_TIME\_FIELD\_NUMBER

      ```
      public static final int EXPIRATION_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.EXPIRATION_TIME_FIELD_NUMBER)
    - #### CREATE\_TIME\_FIELD\_NUMBER

      ```
      public static final int CREATE_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.CREATE_TIME_FIELD_NUMBER)
    - #### APPROVALS\_FIELD\_NUMBER

      ```
      public static final int APPROVALS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.APPROVALS_FIELD_NUMBER)
    - #### STATE\_FIELD\_NUMBER

      ```
      public static final int STATE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.STATE_FIELD_NUMBER)
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
    - #### getProposalId

      ```
      public long getProposalId()
      ```

      `int64 proposal_id = 1;`

      Specified by:
      :   `getProposalId` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The proposalId.
    - #### getProposerAddress

      ```
      public com.google.protobuf.ByteString getProposerAddress()
      ```

      `bytes proposer_address = 2;`

      Specified by:
      :   `getProposerAddress` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The proposerAddress.
    - #### getParametersCount

      ```
      public int getParametersCount()
      ```

      Description copied from interface: `Response.ProposalOrBuilder`

      `map<int64, int64> parameters = 3;`

      Specified by:
      :   `getParametersCount` in interface `Response.ProposalOrBuilder`
    - #### containsParameters

      ```
      public boolean containsParameters(long key)
      ```

      `map<int64, int64> parameters = 3;`

      Specified by:
      :   `containsParameters` in interface `Response.ProposalOrBuilder`
    - #### getParameters

      ```
      @Deprecated
      public java.util.Map<java.lang.Long,java.lang.Long> getParameters()
      ```

      Deprecated.

      Use [`getParametersMap()`](../../../../org/tron/trident/proto/Response.Proposal.html#getParametersMap--) instead.

      Specified by:
      :   `getParameters` in interface `Response.ProposalOrBuilder`
    - #### getParametersMap

      ```
      public java.util.Map<java.lang.Long,java.lang.Long> getParametersMap()
      ```

      `map<int64, int64> parameters = 3;`

      Specified by:
      :   `getParametersMap` in interface `Response.ProposalOrBuilder`
    - #### getParametersOrDefault

      ```
      public long getParametersOrDefault(long key,
                                         long defaultValue)
      ```

      `map<int64, int64> parameters = 3;`

      Specified by:
      :   `getParametersOrDefault` in interface `Response.ProposalOrBuilder`
    - #### getParametersOrThrow

      ```
      public long getParametersOrThrow(long key)
      ```

      `map<int64, int64> parameters = 3;`

      Specified by:
      :   `getParametersOrThrow` in interface `Response.ProposalOrBuilder`
    - #### getExpirationTime

      ```
      public long getExpirationTime()
      ```

      `int64 expiration_time = 4;`

      Specified by:
      :   `getExpirationTime` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The expirationTime.
    - #### getCreateTime

      ```
      public long getCreateTime()
      ```

      `int64 create_time = 5;`

      Specified by:
      :   `getCreateTime` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The createTime.
    - #### getApprovalsList

      ```
      public java.util.List<com.google.protobuf.ByteString> getApprovalsList()
      ```

      `repeated bytes approvals = 6;`

      Specified by:
      :   `getApprovalsList` in interface `Response.ProposalOrBuilder`

      Returns:
      :   A list containing the approvals.
    - #### getApprovalsCount

      ```
      public int getApprovalsCount()
      ```

      `repeated bytes approvals = 6;`

      Specified by:
      :   `getApprovalsCount` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The count of approvals.
    - #### getApprovals

      ```
      public com.google.protobuf.ByteString getApprovals(int index)
      ```

      `repeated bytes approvals = 6;`

      Specified by:
      :   `getApprovals` in interface `Response.ProposalOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The approvals at the given index.
    - #### getStateValue

      ```
      public int getStateValue()
      ```

      `.protocol.Proposal.State state = 7;`

      Specified by:
      :   `getStateValue` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The enum numeric value on the wire for state.
    - #### getState

      ```
      public Response.Proposal.State getState()
      ```

      `.protocol.Proposal.State state = 7;`

      Specified by:
      :   `getState` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The state.
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
      public static Response.Proposal parseFrom(java.nio.ByteBuffer data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Proposal parseFrom(java.nio.ByteBuffer data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Proposal parseFrom(com.google.protobuf.ByteString data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Proposal parseFrom(com.google.protobuf.ByteString data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Proposal parseFrom(byte[] data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Proposal parseFrom(byte[] data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Proposal parseFrom(java.io.InputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Proposal parseFrom(java.io.InputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Proposal parseDelimitedFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Proposal parseDelimitedFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Proposal parseFrom(com.google.protobuf.CodedInputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Proposal parseFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.Proposal.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.Proposal.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.Proposal.Builder newBuilder(Response.Proposal prototype)
      ```
    - #### toBuilder

      ```
      public Response.Proposal.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.Proposal.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.Proposal getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.Proposal> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.Proposal> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.Proposal getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`