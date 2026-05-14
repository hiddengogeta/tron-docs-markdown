

org.tron.trident.proto

## Class Contract.VoteWitnessContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.VoteWitnessContract.Builder](../../../../org/tron/trident/proto/Contract.VoteWitnessContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.VoteWitnessContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.VoteWitnessContractOrBuilder](../../../../org/tron/trident/proto/Contract.VoteWitnessContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.VoteWitnessContract](../../../../org/tron/trident/proto/Contract.VoteWitnessContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.VoteWitnessContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>
  implements Contract.VoteWitnessContractOrBuilder
  ```

  Protobuf type `protocol.VoteWitnessContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.VoteWitnessContract.Builder` | `addAllVotes(java.lang.Iterable<? extends Contract.VoteWitnessContract.Vote> values)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.VoteWitnessContract.Builder` | `addVotes(Contract.VoteWitnessContract.Vote.Builder builderForValue)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Builder` | `addVotes(Contract.VoteWitnessContract.Vote value)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Builder` | `addVotes(int index, Contract.VoteWitnessContract.Vote.Builder builderForValue)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Builder` | `addVotes(int index, Contract.VoteWitnessContract.Vote value)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Vote.Builder` | `addVotesBuilder()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Vote.Builder` | `addVotesBuilder(int index)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract` | `build()` |
    | `Contract.VoteWitnessContract` | `buildPartial()` |
    | `Contract.VoteWitnessContract.Builder` | `clear()` |
    | `Contract.VoteWitnessContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.VoteWitnessContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.VoteWitnessContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.VoteWitnessContract.Builder` | `clearSupport()` `bool support = 3;` |
    | `Contract.VoteWitnessContract.Builder` | `clearVotes()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Builder` | `clone()` |
    | `Contract.VoteWitnessContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `boolean` | `getSupport()` `bool support = 3;` |
    | `Contract.VoteWitnessContract.Vote` | `getVotes(int index)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Vote.Builder` | `getVotesBuilder(int index)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `java.util.List<Contract.VoteWitnessContract.Vote.Builder>` | `getVotesBuilderList()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `int` | `getVotesCount()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `java.util.List<Contract.VoteWitnessContract.Vote>` | `getVotesList()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.VoteOrBuilder` | `getVotesOrBuilder(int index)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `java.util.List<? extends Contract.VoteWitnessContract.VoteOrBuilder>` | `getVotesOrBuilderList()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.VoteWitnessContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.VoteWitnessContract.Builder` | `mergeFrom(Contract.VoteWitnessContract other)` |
    | `Contract.VoteWitnessContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.VoteWitnessContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.VoteWitnessContract.Builder` | `removeVotes(int index)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.VoteWitnessContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.VoteWitnessContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.VoteWitnessContract.Builder` | `setSupport(boolean value)` `bool support = 3;` |
    | `Contract.VoteWitnessContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.VoteWitnessContract.Builder` | `setVotes(int index, Contract.VoteWitnessContract.Vote.Builder builderForValue)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.Builder` | `setVotes(int index, Contract.VoteWitnessContract.Vote value)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### clear

      ```
      public Contract.VoteWitnessContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.VoteWitnessContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.VoteWitnessContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.VoteWitnessContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.VoteWitnessContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### setField

      ```
      public Contract.VoteWitnessContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### clearField

      ```
      public Contract.VoteWitnessContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### clearOneof

      ```
      public Contract.VoteWitnessContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.VoteWitnessContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   int index,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.VoteWitnessContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.VoteWitnessContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.VoteWitnessContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.VoteWitnessContract.Builder mergeFrom(Contract.VoteWitnessContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.VoteWitnessContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.VoteWitnessContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.VoteWitnessContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.VoteWitnessContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.VoteWitnessContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getVotesList

      ```
      public java.util.List<Contract.VoteWitnessContract.Vote> getVotesList()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`

      Specified by:
      :   `getVotesList` in interface `Contract.VoteWitnessContractOrBuilder`
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
    - #### setVotes

      ```
      public Contract.VoteWitnessContract.Builder setVotes(int index,
                                                           Contract.VoteWitnessContract.Vote value)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### setVotes

      ```
      public Contract.VoteWitnessContract.Builder setVotes(int index,
                                                           Contract.VoteWitnessContract.Vote.Builder builderForValue)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### addVotes

      ```
      public Contract.VoteWitnessContract.Builder addVotes(Contract.VoteWitnessContract.Vote value)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### addVotes

      ```
      public Contract.VoteWitnessContract.Builder addVotes(int index,
                                                           Contract.VoteWitnessContract.Vote value)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### addVotes

      ```
      public Contract.VoteWitnessContract.Builder addVotes(Contract.VoteWitnessContract.Vote.Builder builderForValue)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### addVotes

      ```
      public Contract.VoteWitnessContract.Builder addVotes(int index,
                                                           Contract.VoteWitnessContract.Vote.Builder builderForValue)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### addAllVotes

      ```
      public Contract.VoteWitnessContract.Builder addAllVotes(java.lang.Iterable<? extends Contract.VoteWitnessContract.Vote> values)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### clearVotes

      ```
      public Contract.VoteWitnessContract.Builder clearVotes()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### removeVotes

      ```
      public Contract.VoteWitnessContract.Builder removeVotes(int index)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### getVotesBuilder

      ```
      public Contract.VoteWitnessContract.Vote.Builder getVotesBuilder(int index)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### getVotesOrBuilder

      ```
      public Contract.VoteWitnessContract.VoteOrBuilder getVotesOrBuilder(int index)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`

      Specified by:
      :   `getVotesOrBuilder` in interface `Contract.VoteWitnessContractOrBuilder`
    - #### getVotesOrBuilderList

      ```
      public java.util.List<? extends Contract.VoteWitnessContract.VoteOrBuilder> getVotesOrBuilderList()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`

      Specified by:
      :   `getVotesOrBuilderList` in interface `Contract.VoteWitnessContractOrBuilder`
    - #### addVotesBuilder

      ```
      public Contract.VoteWitnessContract.Vote.Builder addVotesBuilder()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### addVotesBuilder

      ```
      public Contract.VoteWitnessContract.Vote.Builder addVotesBuilder(int index)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### getVotesBuilderList

      ```
      public java.util.List<Contract.VoteWitnessContract.Vote.Builder> getVotesBuilderList()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### getSupport

      ```
      public boolean getSupport()
      ```

      `bool support = 3;`

      Specified by:
      :   `getSupport` in interface `Contract.VoteWitnessContractOrBuilder`

      Returns:
      :   The support.
    - #### setSupport

      ```
      public Contract.VoteWitnessContract.Builder setSupport(boolean value)
      ```

      `bool support = 3;`

      Parameters:
      :   `value` - The support to set.

      Returns:
      :   This builder for chaining.
    - #### clearSupport

      ```
      public Contract.VoteWitnessContract.Builder clearSupport()
      ```

      `bool support = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.VoteWitnessContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.VoteWitnessContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteWitnessContract.Builder>`