

org.tron.trident.proto

## Class Contract.TransferAssetContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.TransferAssetContract.Builder](../../../../org/tron/trident/proto/Contract.TransferAssetContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.TransferAssetContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.TransferAssetContractOrBuilder](../../../../org/tron/trident/proto/Contract.TransferAssetContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.TransferAssetContract](../../../../org/tron/trident/proto/Contract.TransferAssetContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.TransferAssetContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>
  implements Contract.TransferAssetContractOrBuilder
  ```

  Protobuf type `protocol.TransferAssetContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.TransferAssetContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.TransferAssetContract` | `build()` |
    | `Contract.TransferAssetContract` | `buildPartial()` |
    | `Contract.TransferAssetContract.Builder` | `clear()` |
    | `Contract.TransferAssetContract.Builder` | `clearAmount()` `int64 amount = 4;` |
    | `Contract.TransferAssetContract.Builder` | `clearAssetName()` this field is token name before the proposal |
    | `Contract.TransferAssetContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.TransferAssetContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.TransferAssetContract.Builder` | `clearOwnerAddress()` ALLOW\_SAME\_TOKEN\_NAME is active, otherwise it is token id and token is should be in string format. |
    | `Contract.TransferAssetContract.Builder` | `clearToAddress()` `bytes to_address = 3;` |
    | `Contract.TransferAssetContract.Builder` | `clone()` |
    | `long` | `getAmount()` `int64 amount = 4;` |
    | `com.google.protobuf.ByteString` | `getAssetName()` this field is token name before the proposal |
    | `Contract.TransferAssetContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` ALLOW\_SAME\_TOKEN\_NAME is active, otherwise it is token id and token is should be in string format. |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes to_address = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.TransferAssetContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.TransferAssetContract.Builder` | `mergeFrom(Contract.TransferAssetContract other)` |
    | `Contract.TransferAssetContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.TransferAssetContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.TransferAssetContract.Builder` | `setAmount(long value)` `int64 amount = 4;` |
    | `Contract.TransferAssetContract.Builder` | `setAssetName(com.google.protobuf.ByteString value)` this field is token name before the proposal |
    | `Contract.TransferAssetContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.TransferAssetContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` ALLOW\_SAME\_TOKEN\_NAME is active, otherwise it is token id and token is should be in string format. |
    | `Contract.TransferAssetContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.TransferAssetContract.Builder` | `setToAddress(com.google.protobuf.ByteString value)` `bytes to_address = 3;` |
    | `Contract.TransferAssetContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### clear

      ```
      public Contract.TransferAssetContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.TransferAssetContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.TransferAssetContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.TransferAssetContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.TransferAssetContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### setField

      ```
      public Contract.TransferAssetContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### clearField

      ```
      public Contract.TransferAssetContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### clearOneof

      ```
      public Contract.TransferAssetContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.TransferAssetContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.TransferAssetContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.TransferAssetContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.TransferAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.TransferAssetContract.Builder mergeFrom(Contract.TransferAssetContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.TransferAssetContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.TransferAssetContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAssetName

      ```
      public com.google.protobuf.ByteString getAssetName()
      ```

      ```
       this field is token name before the proposal
      ```

      `bytes asset_name = 1;`

      Specified by:
      :   `getAssetName` in interface `Contract.TransferAssetContractOrBuilder`

      Returns:
      :   The assetName.
    - #### setAssetName

      ```
      public Contract.TransferAssetContract.Builder setAssetName(com.google.protobuf.ByteString value)
      ```

      ```
       this field is token name before the proposal
      ```

      `bytes asset_name = 1;`

      Parameters:
      :   `value` - The assetName to set.

      Returns:
      :   This builder for chaining.
    - #### clearAssetName

      ```
      public Contract.TransferAssetContract.Builder clearAssetName()
      ```

      ```
       this field is token name before the proposal
      ```

      `bytes asset_name = 1;`

      Returns:
      :   This builder for chaining.
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      ```
       ALLOW_SAME_TOKEN_NAME is active, otherwise it is
       token id and token is should be in string format.
      ```

      `bytes owner_address = 2;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.TransferAssetContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.TransferAssetContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      ```
       ALLOW_SAME_TOKEN_NAME is active, otherwise it is
       token id and token is should be in string format.
      ```

      `bytes owner_address = 2;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.TransferAssetContract.Builder clearOwnerAddress()
      ```

      ```
       ALLOW_SAME_TOKEN_NAME is active, otherwise it is
       token id and token is should be in string format.
      ```

      `bytes owner_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getToAddress

      ```
      public com.google.protobuf.ByteString getToAddress()
      ```

      `bytes to_address = 3;`

      Specified by:
      :   `getToAddress` in interface `Contract.TransferAssetContractOrBuilder`

      Returns:
      :   The toAddress.
    - #### setToAddress

      ```
      public Contract.TransferAssetContract.Builder setToAddress(com.google.protobuf.ByteString value)
      ```

      `bytes to_address = 3;`

      Parameters:
      :   `value` - The toAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearToAddress

      ```
      public Contract.TransferAssetContract.Builder clearToAddress()
      ```

      `bytes to_address = 3;`

      Returns:
      :   This builder for chaining.
    - #### getAmount

      ```
      public long getAmount()
      ```

      `int64 amount = 4;`

      Specified by:
      :   `getAmount` in interface `Contract.TransferAssetContractOrBuilder`

      Returns:
      :   The amount.
    - #### setAmount

      ```
      public Contract.TransferAssetContract.Builder setAmount(long value)
      ```

      `int64 amount = 4;`

      Parameters:
      :   `value` - The amount to set.

      Returns:
      :   This builder for chaining.
    - #### clearAmount

      ```
      public Contract.TransferAssetContract.Builder clearAmount()
      ```

      `int64 amount = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.TransferAssetContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.TransferAssetContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TransferAssetContract.Builder>`