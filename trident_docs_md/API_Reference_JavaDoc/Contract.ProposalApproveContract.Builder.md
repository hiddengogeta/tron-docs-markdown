

org.tron.trident.proto

## Class Contract.ProposalApproveContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.ProposalApproveContract.Builder](../../../../org/tron/trident/proto/Contract.ProposalApproveContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.ProposalApproveContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.ProposalApproveContractOrBuilder](../../../../org/tron/trident/proto/Contract.ProposalApproveContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.ProposalApproveContract](../../../../org/tron/trident/proto/Contract.ProposalApproveContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.ProposalApproveContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>
  implements Contract.ProposalApproveContractOrBuilder
  ```

  Protobuf type `protocol.ProposalApproveContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.ProposalApproveContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ProposalApproveContract` | `build()` |
    | `Contract.ProposalApproveContract` | `buildPartial()` |
    | `Contract.ProposalApproveContract.Builder` | `clear()` |
    | `Contract.ProposalApproveContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.ProposalApproveContract.Builder` | `clearIsAddApproval()` add or remove approval |
    | `Contract.ProposalApproveContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.ProposalApproveContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.ProposalApproveContract.Builder` | `clearProposalId()` `int64 proposal_id = 2;` |
    | `Contract.ProposalApproveContract.Builder` | `clone()` |
    | `Contract.ProposalApproveContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `boolean` | `getIsAddApproval()` add or remove approval |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getProposalId()` `int64 proposal_id = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.ProposalApproveContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.ProposalApproveContract.Builder` | `mergeFrom(Contract.ProposalApproveContract other)` |
    | `Contract.ProposalApproveContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.ProposalApproveContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.ProposalApproveContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ProposalApproveContract.Builder` | `setIsAddApproval(boolean value)` add or remove approval |
    | `Contract.ProposalApproveContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.ProposalApproveContract.Builder` | `setProposalId(long value)` `int64 proposal_id = 2;` |
    | `Contract.ProposalApproveContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.ProposalApproveContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, internalGetMutableMapField, internalGetMutableMapFieldReflection, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
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
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### clear

      ```
      public Contract.ProposalApproveContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.ProposalApproveContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.ProposalApproveContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.ProposalApproveContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.ProposalApproveContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### setField

      ```
      public Contract.ProposalApproveContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### clearField

      ```
      public Contract.ProposalApproveContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### clearOneof

      ```
      public Contract.ProposalApproveContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.ProposalApproveContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       int index,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.ProposalApproveContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ProposalApproveContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ProposalApproveContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ProposalApproveContract.Builder mergeFrom(Contract.ProposalApproveContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ProposalApproveContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ProposalApproveContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.ProposalApproveContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.ProposalApproveContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.ProposalApproveContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getProposalId

      ```
      public long getProposalId()
      ```

      `int64 proposal_id = 2;`

      Specified by:
      :   `getProposalId` in interface `Contract.ProposalApproveContractOrBuilder`

      Returns:
      :   The proposalId.
    - #### setProposalId

      ```
      public Contract.ProposalApproveContract.Builder setProposalId(long value)
      ```

      `int64 proposal_id = 2;`

      Parameters:
      :   `value` - The proposalId to set.

      Returns:
      :   This builder for chaining.
    - #### clearProposalId

      ```
      public Contract.ProposalApproveContract.Builder clearProposalId()
      ```

      `int64 proposal_id = 2;`

      Returns:
      :   This builder for chaining.
    - #### getIsAddApproval

      ```
      public boolean getIsAddApproval()
      ```

      ```
       add or remove approval
      ```

      `bool is_add_approval = 3;`

      Specified by:
      :   `getIsAddApproval` in interface `Contract.ProposalApproveContractOrBuilder`

      Returns:
      :   The isAddApproval.
    - #### setIsAddApproval

      ```
      public Contract.ProposalApproveContract.Builder setIsAddApproval(boolean value)
      ```

      ```
       add or remove approval
      ```

      `bool is_add_approval = 3;`

      Parameters:
      :   `value` - The isAddApproval to set.

      Returns:
      :   This builder for chaining.
    - #### clearIsAddApproval

      ```
      public Contract.ProposalApproveContract.Builder clearIsAddApproval()
      ```

      ```
       add or remove approval
      ```

      `bool is_add_approval = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.ProposalApproveContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.ProposalApproveContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalApproveContract.Builder>`