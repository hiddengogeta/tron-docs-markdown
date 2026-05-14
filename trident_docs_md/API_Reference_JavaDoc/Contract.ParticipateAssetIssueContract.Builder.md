

org.tron.trident.proto

## Class Contract.ParticipateAssetIssueContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.ParticipateAssetIssueContract.Builder](../../../../org/tron/trident/proto/Contract.ParticipateAssetIssueContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.ParticipateAssetIssueContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.ParticipateAssetIssueContractOrBuilder](../../../../org/tron/trident/proto/Contract.ParticipateAssetIssueContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.ParticipateAssetIssueContract](../../../../org/tron/trident/proto/Contract.ParticipateAssetIssueContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.ParticipateAssetIssueContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>
  implements Contract.ParticipateAssetIssueContractOrBuilder
  ```

  Protobuf type `protocol.ParticipateAssetIssueContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.ParticipateAssetIssueContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ParticipateAssetIssueContract` | `build()` |
    | `Contract.ParticipateAssetIssueContract` | `buildPartial()` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `clear()` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `clearAmount()` ALLOW\_SAME\_TOKEN\_NAME is active, otherwise it is token id and token is should be in string format. |
    | `Contract.ParticipateAssetIssueContract.Builder` | `clearAssetName()` this field is token name before the proposal |
    | `Contract.ParticipateAssetIssueContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `clearToAddress()` `bytes to_address = 2;` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `clone()` |
    | `long` | `getAmount()` ALLOW\_SAME\_TOKEN\_NAME is active, otherwise it is token id and token is should be in string format. |
    | `com.google.protobuf.ByteString` | `getAssetName()` this field is token name before the proposal |
    | `Contract.ParticipateAssetIssueContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes to_address = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `mergeFrom(Contract.ParticipateAssetIssueContract other)` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `setAmount(long value)` ALLOW\_SAME\_TOKEN\_NAME is active, otherwise it is token id and token is should be in string format. |
    | `Contract.ParticipateAssetIssueContract.Builder` | `setAssetName(com.google.protobuf.ByteString value)` this field is token name before the proposal |
    | `Contract.ParticipateAssetIssueContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `setToAddress(com.google.protobuf.ByteString value)` `bytes to_address = 2;` |
    | `Contract.ParticipateAssetIssueContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### clear

      ```
      public Contract.ParticipateAssetIssueContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.ParticipateAssetIssueContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.ParticipateAssetIssueContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.ParticipateAssetIssueContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.ParticipateAssetIssueContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### setField

      ```
      public Contract.ParticipateAssetIssueContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### clearField

      ```
      public Contract.ParticipateAssetIssueContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### clearOneof

      ```
      public Contract.ParticipateAssetIssueContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.ParticipateAssetIssueContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                             int index,
                                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.ParticipateAssetIssueContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                             java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ParticipateAssetIssueContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ParticipateAssetIssueContract.Builder mergeFrom(Contract.ParticipateAssetIssueContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ParticipateAssetIssueContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ParticipateAssetIssueContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.ParticipateAssetIssueContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.ParticipateAssetIssueContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.ParticipateAssetIssueContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getToAddress

      ```
      public com.google.protobuf.ByteString getToAddress()
      ```

      `bytes to_address = 2;`

      Specified by:
      :   `getToAddress` in interface `Contract.ParticipateAssetIssueContractOrBuilder`

      Returns:
      :   The toAddress.
    - #### setToAddress

      ```
      public Contract.ParticipateAssetIssueContract.Builder setToAddress(com.google.protobuf.ByteString value)
      ```

      `bytes to_address = 2;`

      Parameters:
      :   `value` - The toAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearToAddress

      ```
      public Contract.ParticipateAssetIssueContract.Builder clearToAddress()
      ```

      `bytes to_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getAssetName

      ```
      public com.google.protobuf.ByteString getAssetName()
      ```

      ```
       this field is token name before the proposal
      ```

      `bytes asset_name = 3;`

      Specified by:
      :   `getAssetName` in interface `Contract.ParticipateAssetIssueContractOrBuilder`

      Returns:
      :   The assetName.
    - #### setAssetName

      ```
      public Contract.ParticipateAssetIssueContract.Builder setAssetName(com.google.protobuf.ByteString value)
      ```

      ```
       this field is token name before the proposal
      ```

      `bytes asset_name = 3;`

      Parameters:
      :   `value` - The assetName to set.

      Returns:
      :   This builder for chaining.
    - #### clearAssetName

      ```
      public Contract.ParticipateAssetIssueContract.Builder clearAssetName()
      ```

      ```
       this field is token name before the proposal
      ```

      `bytes asset_name = 3;`

      Returns:
      :   This builder for chaining.
    - #### getAmount

      ```
      public long getAmount()
      ```

      ```
       ALLOW_SAME_TOKEN_NAME is active, otherwise it is
       token id and token is should be in string format.
      ```

      `int64 amount = 4;`

      Specified by:
      :   `getAmount` in interface `Contract.ParticipateAssetIssueContractOrBuilder`

      Returns:
      :   The amount.
    - #### setAmount

      ```
      public Contract.ParticipateAssetIssueContract.Builder setAmount(long value)
      ```

      ```
       ALLOW_SAME_TOKEN_NAME is active, otherwise it is
       token id and token is should be in string format.
      ```

      `int64 amount = 4;`

      Parameters:
      :   `value` - The amount to set.

      Returns:
      :   This builder for chaining.
    - #### clearAmount

      ```
      public Contract.ParticipateAssetIssueContract.Builder clearAmount()
      ```

      ```
       ALLOW_SAME_TOKEN_NAME is active, otherwise it is
       token id and token is should be in string format.
      ```

      `int64 amount = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.ParticipateAssetIssueContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.ParticipateAssetIssueContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ParticipateAssetIssueContract.Builder>`