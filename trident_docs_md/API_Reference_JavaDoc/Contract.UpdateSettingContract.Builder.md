

org.tron.trident.proto

## Class Contract.UpdateSettingContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.UpdateSettingContract.Builder](../../../../org/tron/trident/proto/Contract.UpdateSettingContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.UpdateSettingContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.UpdateSettingContractOrBuilder](../../../../org/tron/trident/proto/Contract.UpdateSettingContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.UpdateSettingContract](../../../../org/tron/trident/proto/Contract.UpdateSettingContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.UpdateSettingContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>
  implements Contract.UpdateSettingContractOrBuilder
  ```

  Protobuf type `protocol.UpdateSettingContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.UpdateSettingContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UpdateSettingContract` | `build()` |
    | `Contract.UpdateSettingContract` | `buildPartial()` |
    | `Contract.UpdateSettingContract.Builder` | `clear()` |
    | `Contract.UpdateSettingContract.Builder` | `clearConsumeUserResourcePercent()` `int64 consume_user_resource_percent = 3;` |
    | `Contract.UpdateSettingContract.Builder` | `clearContractAddress()` `bytes contract_address = 2;` |
    | `Contract.UpdateSettingContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.UpdateSettingContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.UpdateSettingContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.UpdateSettingContract.Builder` | `clone()` |
    | `long` | `getConsumeUserResourcePercent()` `int64 consume_user_resource_percent = 3;` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 2;` |
    | `Contract.UpdateSettingContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.UpdateSettingContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.UpdateSettingContract.Builder` | `mergeFrom(Contract.UpdateSettingContract other)` |
    | `Contract.UpdateSettingContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.UpdateSettingContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.UpdateSettingContract.Builder` | `setConsumeUserResourcePercent(long value)` `int64 consume_user_resource_percent = 3;` |
    | `Contract.UpdateSettingContract.Builder` | `setContractAddress(com.google.protobuf.ByteString value)` `bytes contract_address = 2;` |
    | `Contract.UpdateSettingContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UpdateSettingContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.UpdateSettingContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.UpdateSettingContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### clear

      ```
      public Contract.UpdateSettingContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.UpdateSettingContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.UpdateSettingContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.UpdateSettingContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.UpdateSettingContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### setField

      ```
      public Contract.UpdateSettingContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### clearField

      ```
      public Contract.UpdateSettingContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### clearOneof

      ```
      public Contract.UpdateSettingContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.UpdateSettingContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.UpdateSettingContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UpdateSettingContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UpdateSettingContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UpdateSettingContract.Builder mergeFrom(Contract.UpdateSettingContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UpdateSettingContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UpdateSettingContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.UpdateSettingContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.UpdateSettingContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.UpdateSettingContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getContractAddress

      ```
      public com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 2;`

      Specified by:
      :   `getContractAddress` in interface `Contract.UpdateSettingContractOrBuilder`

      Returns:
      :   The contractAddress.
    - #### setContractAddress

      ```
      public Contract.UpdateSettingContract.Builder setContractAddress(com.google.protobuf.ByteString value)
      ```

      `bytes contract_address = 2;`

      Parameters:
      :   `value` - The contractAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearContractAddress

      ```
      public Contract.UpdateSettingContract.Builder clearContractAddress()
      ```

      `bytes contract_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getConsumeUserResourcePercent

      ```
      public long getConsumeUserResourcePercent()
      ```

      `int64 consume_user_resource_percent = 3;`

      Specified by:
      :   `getConsumeUserResourcePercent` in interface `Contract.UpdateSettingContractOrBuilder`

      Returns:
      :   The consumeUserResourcePercent.
    - #### setConsumeUserResourcePercent

      ```
      public Contract.UpdateSettingContract.Builder setConsumeUserResourcePercent(long value)
      ```

      `int64 consume_user_resource_percent = 3;`

      Parameters:
      :   `value` - The consumeUserResourcePercent to set.

      Returns:
      :   This builder for chaining.
    - #### clearConsumeUserResourcePercent

      ```
      public Contract.UpdateSettingContract.Builder clearConsumeUserResourcePercent()
      ```

      `int64 consume_user_resource_percent = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.UpdateSettingContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.UpdateSettingContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateSettingContract.Builder>`