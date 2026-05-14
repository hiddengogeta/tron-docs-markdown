

org.tron.trident.proto

## Class Contract.VoteAssetContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.VoteAssetContract.Builder](../../../../org/tron/trident/proto/Contract.VoteAssetContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.VoteAssetContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.VoteAssetContractOrBuilder](../../../../org/tron/trident/proto/Contract.VoteAssetContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.VoteAssetContract](../../../../org/tron/trident/proto/Contract.VoteAssetContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.VoteAssetContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>
  implements Contract.VoteAssetContractOrBuilder
  ```

  Protobuf type `protocol.VoteAssetContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.VoteAssetContract.Builder` | `addAllVoteAddress(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` `repeated bytes vote_address = 2;` |
    | `Contract.VoteAssetContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.VoteAssetContract.Builder` | `addVoteAddress(com.google.protobuf.ByteString value)` `repeated bytes vote_address = 2;` |
    | `Contract.VoteAssetContract` | `build()` |
    | `Contract.VoteAssetContract` | `buildPartial()` |
    | `Contract.VoteAssetContract.Builder` | `clear()` |
    | `Contract.VoteAssetContract.Builder` | `clearCount()` `int32 count = 5;` |
    | `Contract.VoteAssetContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.VoteAssetContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.VoteAssetContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.VoteAssetContract.Builder` | `clearSupport()` `bool support = 3;` |
    | `Contract.VoteAssetContract.Builder` | `clearVoteAddress()` `repeated bytes vote_address = 2;` |
    | `Contract.VoteAssetContract.Builder` | `clone()` |
    | `int` | `getCount()` `int32 count = 5;` |
    | `Contract.VoteAssetContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `boolean` | `getSupport()` `bool support = 3;` |
    | `com.google.protobuf.ByteString` | `getVoteAddress(int index)` `repeated bytes vote_address = 2;` |
    | `int` | `getVoteAddressCount()` `repeated bytes vote_address = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getVoteAddressList()` `repeated bytes vote_address = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.VoteAssetContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.VoteAssetContract.Builder` | `mergeFrom(Contract.VoteAssetContract other)` |
    | `Contract.VoteAssetContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.VoteAssetContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.VoteAssetContract.Builder` | `setCount(int value)` `int32 count = 5;` |
    | `Contract.VoteAssetContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.VoteAssetContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.VoteAssetContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.VoteAssetContract.Builder` | `setSupport(boolean value)` `bool support = 3;` |
    | `Contract.VoteAssetContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.VoteAssetContract.Builder` | `setVoteAddress(int index, com.google.protobuf.ByteString value)` `repeated bytes vote_address = 2;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### clear

      ```
      public Contract.VoteAssetContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.VoteAssetContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.VoteAssetContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.VoteAssetContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.VoteAssetContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### setField

      ```
      public Contract.VoteAssetContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### clearField

      ```
      public Contract.VoteAssetContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### clearOneof

      ```
      public Contract.VoteAssetContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.VoteAssetContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 int index,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.VoteAssetContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.VoteAssetContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.VoteAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.VoteAssetContract.Builder mergeFrom(Contract.VoteAssetContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.VoteAssetContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.VoteAssetContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.VoteAssetContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.VoteAssetContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.VoteAssetContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getVoteAddressList

      ```
      public java.util.List<com.google.protobuf.ByteString> getVoteAddressList()
      ```

      `repeated bytes vote_address = 2;`

      Specified by:
      :   `getVoteAddressList` in interface `Contract.VoteAssetContractOrBuilder`

      Returns:
      :   A list containing the voteAddress.
    - #### getVoteAddressCount

      ```
      public int getVoteAddressCount()
      ```

      `repeated bytes vote_address = 2;`

      Specified by:
      :   `getVoteAddressCount` in interface `Contract.VoteAssetContractOrBuilder`

      Returns:
      :   The count of voteAddress.
    - #### getVoteAddress

      ```
      public com.google.protobuf.ByteString getVoteAddress(int index)
      ```

      `repeated bytes vote_address = 2;`

      Specified by:
      :   `getVoteAddress` in interface `Contract.VoteAssetContractOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The voteAddress at the given index.
    - #### setVoteAddress

      ```
      public Contract.VoteAssetContract.Builder setVoteAddress(int index,
                                                               com.google.protobuf.ByteString value)
      ```

      `repeated bytes vote_address = 2;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The voteAddress to set.

      Returns:
      :   This builder for chaining.
    - #### addVoteAddress

      ```
      public Contract.VoteAssetContract.Builder addVoteAddress(com.google.protobuf.ByteString value)
      ```

      `repeated bytes vote_address = 2;`

      Parameters:
      :   `value` - The voteAddress to add.

      Returns:
      :   This builder for chaining.
    - #### addAllVoteAddress

      ```
      public Contract.VoteAssetContract.Builder addAllVoteAddress(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      `repeated bytes vote_address = 2;`

      Parameters:
      :   `values` - The voteAddress to add.

      Returns:
      :   This builder for chaining.
    - #### clearVoteAddress

      ```
      public Contract.VoteAssetContract.Builder clearVoteAddress()
      ```

      `repeated bytes vote_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getSupport

      ```
      public boolean getSupport()
      ```

      `bool support = 3;`

      Specified by:
      :   `getSupport` in interface `Contract.VoteAssetContractOrBuilder`

      Returns:
      :   The support.
    - #### setSupport

      ```
      public Contract.VoteAssetContract.Builder setSupport(boolean value)
      ```

      `bool support = 3;`

      Parameters:
      :   `value` - The support to set.

      Returns:
      :   This builder for chaining.
    - #### clearSupport

      ```
      public Contract.VoteAssetContract.Builder clearSupport()
      ```

      `bool support = 3;`

      Returns:
      :   This builder for chaining.
    - #### getCount

      ```
      public int getCount()
      ```

      `int32 count = 5;`

      Specified by:
      :   `getCount` in interface `Contract.VoteAssetContractOrBuilder`

      Returns:
      :   The count.
    - #### setCount

      ```
      public Contract.VoteAssetContract.Builder setCount(int value)
      ```

      `int32 count = 5;`

      Parameters:
      :   `value` - The count to set.

      Returns:
      :   This builder for chaining.
    - #### clearCount

      ```
      public Contract.VoteAssetContract.Builder clearCount()
      ```

      `int32 count = 5;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.VoteAssetContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.VoteAssetContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.VoteAssetContract.Builder>`