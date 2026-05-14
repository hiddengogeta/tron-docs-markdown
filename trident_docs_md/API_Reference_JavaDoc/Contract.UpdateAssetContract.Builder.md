

org.tron.trident.proto

## Class Contract.UpdateAssetContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.UpdateAssetContract.Builder](../../../../org/tron/trident/proto/Contract.UpdateAssetContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.UpdateAssetContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.UpdateAssetContractOrBuilder](../../../../org/tron/trident/proto/Contract.UpdateAssetContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.UpdateAssetContract](../../../../org/tron/trident/proto/Contract.UpdateAssetContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.UpdateAssetContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>
  implements Contract.UpdateAssetContractOrBuilder
  ```

  Protobuf type `protocol.UpdateAssetContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.UpdateAssetContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UpdateAssetContract` | `build()` |
    | `Contract.UpdateAssetContract` | `buildPartial()` |
    | `Contract.UpdateAssetContract.Builder` | `clear()` |
    | `Contract.UpdateAssetContract.Builder` | `clearDescription()` `bytes description = 2;` |
    | `Contract.UpdateAssetContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.UpdateAssetContract.Builder` | `clearNewLimit()` `int64 new_limit = 4;` |
    | `Contract.UpdateAssetContract.Builder` | `clearNewPublicLimit()` `int64 new_public_limit = 5;` |
    | `Contract.UpdateAssetContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.UpdateAssetContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.UpdateAssetContract.Builder` | `clearUrl()` `bytes url = 3;` |
    | `Contract.UpdateAssetContract.Builder` | `clone()` |
    | `Contract.UpdateAssetContract` | `getDefaultInstanceForType()` |
    | `com.google.protobuf.ByteString` | `getDescription()` `bytes description = 2;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getNewLimit()` `int64 new_limit = 4;` |
    | `long` | `getNewPublicLimit()` `int64 new_public_limit = 5;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getUrl()` `bytes url = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.UpdateAssetContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.UpdateAssetContract.Builder` | `mergeFrom(Contract.UpdateAssetContract other)` |
    | `Contract.UpdateAssetContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.UpdateAssetContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.UpdateAssetContract.Builder` | `setDescription(com.google.protobuf.ByteString value)` `bytes description = 2;` |
    | `Contract.UpdateAssetContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UpdateAssetContract.Builder` | `setNewLimit(long value)` `int64 new_limit = 4;` |
    | `Contract.UpdateAssetContract.Builder` | `setNewPublicLimit(long value)` `int64 new_public_limit = 5;` |
    | `Contract.UpdateAssetContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.UpdateAssetContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.UpdateAssetContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.UpdateAssetContract.Builder` | `setUrl(com.google.protobuf.ByteString value)` `bytes url = 3;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### clear

      ```
      public Contract.UpdateAssetContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.UpdateAssetContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.UpdateAssetContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.UpdateAssetContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.UpdateAssetContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### setField

      ```
      public Contract.UpdateAssetContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### clearField

      ```
      public Contract.UpdateAssetContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### clearOneof

      ```
      public Contract.UpdateAssetContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.UpdateAssetContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   int index,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.UpdateAssetContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UpdateAssetContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UpdateAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UpdateAssetContract.Builder mergeFrom(Contract.UpdateAssetContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UpdateAssetContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UpdateAssetContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.UpdateAssetContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.UpdateAssetContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getDescription

      ```
      public com.google.protobuf.ByteString getDescription()
      ```

      `bytes description = 2;`

      Specified by:
      :   `getDescription` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The description.
    - #### setDescription

      ```
      public Contract.UpdateAssetContract.Builder setDescription(com.google.protobuf.ByteString value)
      ```

      `bytes description = 2;`

      Parameters:
      :   `value` - The description to set.

      Returns:
      :   This builder for chaining.
    - #### clearDescription

      ```
      public Contract.UpdateAssetContract.Builder clearDescription()
      ```

      `bytes description = 2;`

      Returns:
      :   This builder for chaining.
    - #### getUrl

      ```
      public com.google.protobuf.ByteString getUrl()
      ```

      `bytes url = 3;`

      Specified by:
      :   `getUrl` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The url.
    - #### setUrl

      ```
      public Contract.UpdateAssetContract.Builder setUrl(com.google.protobuf.ByteString value)
      ```

      `bytes url = 3;`

      Parameters:
      :   `value` - The url to set.

      Returns:
      :   This builder for chaining.
    - #### clearUrl

      ```
      public Contract.UpdateAssetContract.Builder clearUrl()
      ```

      `bytes url = 3;`

      Returns:
      :   This builder for chaining.
    - #### getNewLimit

      ```
      public long getNewLimit()
      ```

      `int64 new_limit = 4;`

      Specified by:
      :   `getNewLimit` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The newLimit.
    - #### setNewLimit

      ```
      public Contract.UpdateAssetContract.Builder setNewLimit(long value)
      ```

      `int64 new_limit = 4;`

      Parameters:
      :   `value` - The newLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearNewLimit

      ```
      public Contract.UpdateAssetContract.Builder clearNewLimit()
      ```

      `int64 new_limit = 4;`

      Returns:
      :   This builder for chaining.
    - #### getNewPublicLimit

      ```
      public long getNewPublicLimit()
      ```

      `int64 new_public_limit = 5;`

      Specified by:
      :   `getNewPublicLimit` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The newPublicLimit.
    - #### setNewPublicLimit

      ```
      public Contract.UpdateAssetContract.Builder setNewPublicLimit(long value)
      ```

      `int64 new_public_limit = 5;`

      Parameters:
      :   `value` - The newPublicLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearNewPublicLimit

      ```
      public Contract.UpdateAssetContract.Builder clearNewPublicLimit()
      ```

      `int64 new_public_limit = 5;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.UpdateAssetContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.UpdateAssetContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateAssetContract.Builder>`