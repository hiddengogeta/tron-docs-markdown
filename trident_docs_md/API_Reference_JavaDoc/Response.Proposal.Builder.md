

org.tron.trident.proto

## Class Response.Proposal.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.Proposal.Builder](../../../../org/tron/trident/proto/Response.Proposal.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.Proposal.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.ProposalOrBuilder](../../../../org/tron/trident/proto/Response.ProposalOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Proposal](../../../../org/tron/trident/proto/Response.Proposal.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Proposal.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>
  implements Response.ProposalOrBuilder
  ```

  Protobuf type `protocol.Proposal`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Response.Proposal.Builder` | `addAllApprovals(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` `repeated bytes approvals = 6;` |
    | `Response.Proposal.Builder` | `addApprovals(com.google.protobuf.ByteString value)` `repeated bytes approvals = 6;` |
    | `Response.Proposal.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Proposal` | `build()` |
    | `Response.Proposal` | `buildPartial()` |
    | `Response.Proposal.Builder` | `clear()` |
    | `Response.Proposal.Builder` | `clearApprovals()` `repeated bytes approvals = 6;` |
    | `Response.Proposal.Builder` | `clearCreateTime()` `int64 create_time = 5;` |
    | `Response.Proposal.Builder` | `clearExpirationTime()` `int64 expiration_time = 4;` |
    | `Response.Proposal.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.Proposal.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.Proposal.Builder` | `clearParameters()` |
    | `Response.Proposal.Builder` | `clearProposalId()` `int64 proposal_id = 1;` |
    | `Response.Proposal.Builder` | `clearProposerAddress()` `bytes proposer_address = 2;` |
    | `Response.Proposal.Builder` | `clearState()` `.protocol.Proposal.State state = 7;` |
    | `Response.Proposal.Builder` | `clone()` |
    | `boolean` | `containsParameters(long key)` `map<int64, int64> parameters = 3;` |
    | `com.google.protobuf.ByteString` | `getApprovals(int index)` `repeated bytes approvals = 6;` |
    | `int` | `getApprovalsCount()` `repeated bytes approvals = 6;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getApprovalsList()` `repeated bytes approvals = 6;` |
    | `long` | `getCreateTime()` `int64 create_time = 5;` |
    | `Response.Proposal` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getExpirationTime()` `int64 expiration_time = 4;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getMutableParameters()` Deprecated. |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParameters()` Deprecated. |
    | `int` | `getParametersCount()` `map<int64, int64> parameters = 3;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParametersMap()` `map<int64, int64> parameters = 3;` |
    | `long` | `getParametersOrDefault(long key, long defaultValue)` `map<int64, int64> parameters = 3;` |
    | `long` | `getParametersOrThrow(long key)` `map<int64, int64> parameters = 3;` |
    | `long` | `getProposalId()` `int64 proposal_id = 1;` |
    | `com.google.protobuf.ByteString` | `getProposerAddress()` `bytes proposer_address = 2;` |
    | `Response.Proposal.State` | `getState()` `.protocol.Proposal.State state = 7;` |
    | `int` | `getStateValue()` `.protocol.Proposal.State state = 7;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMutableMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `Response.Proposal.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.Proposal.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.Proposal.Builder` | `mergeFrom(Response.Proposal other)` |
    | `Response.Proposal.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.Proposal.Builder` | `putAllParameters(java.util.Map<java.lang.Long,java.lang.Long> values)` `map<int64, int64> parameters = 3;` |
    | `Response.Proposal.Builder` | `putParameters(long key, long value)` `map<int64, int64> parameters = 3;` |
    | `Response.Proposal.Builder` | `removeParameters(long key)` `map<int64, int64> parameters = 3;` |
    | `Response.Proposal.Builder` | `setApprovals(int index, com.google.protobuf.ByteString value)` `repeated bytes approvals = 6;` |
    | `Response.Proposal.Builder` | `setCreateTime(long value)` `int64 create_time = 5;` |
    | `Response.Proposal.Builder` | `setExpirationTime(long value)` `int64 expiration_time = 4;` |
    | `Response.Proposal.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Proposal.Builder` | `setProposalId(long value)` `int64 proposal_id = 1;` |
    | `Response.Proposal.Builder` | `setProposerAddress(com.google.protobuf.ByteString value)` `bytes proposer_address = 2;` |
    | `Response.Proposal.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.Proposal.Builder` | `setState(Response.Proposal.State value)` `.protocol.Proposal.State state = 7;` |
    | `Response.Proposal.Builder` | `setStateValue(int value)` `.protocol.Proposal.State state = 7;` |
    | `Response.Proposal.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMutableMapField, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage.Builder

      `findInitializationErrors, getInitializationErrorString, internalMergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, newUninitializedMessageException, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite.Builder

      `addAll, addAll, mergeDelimitedFrom, mergeDelimitedFrom, newUninitializedMessageException`
    - ### Methods inherited from class java.lang.Object

      `equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.Message.Builder

      `mergeDelimitedFrom, mergeDelimitedFrom`

* + ### Method Detail

    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### internalGetMutableMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMutableMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### clear

      ```
      public Response.Proposal.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.Proposal getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.Proposal build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.Proposal buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.Proposal.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### setField

      ```
      public Response.Proposal.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### clearField

      ```
      public Response.Proposal.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### clearOneof

      ```
      public Response.Proposal.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### setRepeatedField

      ```
      public Response.Proposal.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        int index,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### addRepeatedField

      ```
      public Response.Proposal.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### mergeFrom

      ```
      public Response.Proposal.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Proposal.Builder>`
    - #### mergeFrom

      ```
      public Response.Proposal.Builder mergeFrom(Response.Proposal other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### mergeFrom

      ```
      public Response.Proposal.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Proposal.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getProposalId

      ```
      public long getProposalId()
      ```

      `int64 proposal_id = 1;`

      Specified by:
      :   `getProposalId` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The proposalId.
    - #### setProposalId

      ```
      public Response.Proposal.Builder setProposalId(long value)
      ```

      `int64 proposal_id = 1;`

      Parameters:
      :   `value` - The proposalId to set.

      Returns:
      :   This builder for chaining.
    - #### clearProposalId

      ```
      public Response.Proposal.Builder clearProposalId()
      ```

      `int64 proposal_id = 1;`

      Returns:
      :   This builder for chaining.
    - #### getProposerAddress

      ```
      public com.google.protobuf.ByteString getProposerAddress()
      ```

      `bytes proposer_address = 2;`

      Specified by:
      :   `getProposerAddress` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The proposerAddress.
    - #### setProposerAddress

      ```
      public Response.Proposal.Builder setProposerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes proposer_address = 2;`

      Parameters:
      :   `value` - The proposerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearProposerAddress

      ```
      public Response.Proposal.Builder clearProposerAddress()
      ```

      `bytes proposer_address = 2;`

      Returns:
      :   This builder for chaining.
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

      Use [`getParametersMap()`](../../../../org/tron/trident/proto/Response.Proposal.Builder.html#getParametersMap--) instead.

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
    - #### clearParameters

      ```
      public Response.Proposal.Builder clearParameters()
      ```
    - #### removeParameters

      ```
      public Response.Proposal.Builder removeParameters(long key)
      ```

      `map<int64, int64> parameters = 3;`
    - #### getMutableParameters

      ```
      @Deprecated
      public java.util.Map<java.lang.Long,java.lang.Long> getMutableParameters()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putParameters

      ```
      public Response.Proposal.Builder putParameters(long key,
                                                     long value)
      ```

      `map<int64, int64> parameters = 3;`
    - #### putAllParameters

      ```
      public Response.Proposal.Builder putAllParameters(java.util.Map<java.lang.Long,java.lang.Long> values)
      ```

      `map<int64, int64> parameters = 3;`
    - #### getExpirationTime

      ```
      public long getExpirationTime()
      ```

      `int64 expiration_time = 4;`

      Specified by:
      :   `getExpirationTime` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The expirationTime.
    - #### setExpirationTime

      ```
      public Response.Proposal.Builder setExpirationTime(long value)
      ```

      `int64 expiration_time = 4;`

      Parameters:
      :   `value` - The expirationTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearExpirationTime

      ```
      public Response.Proposal.Builder clearExpirationTime()
      ```

      `int64 expiration_time = 4;`

      Returns:
      :   This builder for chaining.
    - #### getCreateTime

      ```
      public long getCreateTime()
      ```

      `int64 create_time = 5;`

      Specified by:
      :   `getCreateTime` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The createTime.
    - #### setCreateTime

      ```
      public Response.Proposal.Builder setCreateTime(long value)
      ```

      `int64 create_time = 5;`

      Parameters:
      :   `value` - The createTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearCreateTime

      ```
      public Response.Proposal.Builder clearCreateTime()
      ```

      `int64 create_time = 5;`

      Returns:
      :   This builder for chaining.
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
    - #### setApprovals

      ```
      public Response.Proposal.Builder setApprovals(int index,
                                                    com.google.protobuf.ByteString value)
      ```

      `repeated bytes approvals = 6;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The approvals to set.

      Returns:
      :   This builder for chaining.
    - #### addApprovals

      ```
      public Response.Proposal.Builder addApprovals(com.google.protobuf.ByteString value)
      ```

      `repeated bytes approvals = 6;`

      Parameters:
      :   `value` - The approvals to add.

      Returns:
      :   This builder for chaining.
    - #### addAllApprovals

      ```
      public Response.Proposal.Builder addAllApprovals(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      `repeated bytes approvals = 6;`

      Parameters:
      :   `values` - The approvals to add.

      Returns:
      :   This builder for chaining.
    - #### clearApprovals

      ```
      public Response.Proposal.Builder clearApprovals()
      ```

      `repeated bytes approvals = 6;`

      Returns:
      :   This builder for chaining.
    - #### getStateValue

      ```
      public int getStateValue()
      ```

      `.protocol.Proposal.State state = 7;`

      Specified by:
      :   `getStateValue` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The enum numeric value on the wire for state.
    - #### setStateValue

      ```
      public Response.Proposal.Builder setStateValue(int value)
      ```

      `.protocol.Proposal.State state = 7;`

      Parameters:
      :   `value` - The enum numeric value on the wire for state to set.

      Returns:
      :   This builder for chaining.
    - #### getState

      ```
      public Response.Proposal.State getState()
      ```

      `.protocol.Proposal.State state = 7;`

      Specified by:
      :   `getState` in interface `Response.ProposalOrBuilder`

      Returns:
      :   The state.
    - #### setState

      ```
      public Response.Proposal.Builder setState(Response.Proposal.State value)
      ```

      `.protocol.Proposal.State state = 7;`

      Parameters:
      :   `value` - The state to set.

      Returns:
      :   This builder for chaining.
    - #### clearState

      ```
      public Response.Proposal.Builder clearState()
      ```

      `.protocol.Proposal.State state = 7;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.Proposal.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.Proposal.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Proposal.Builder>`