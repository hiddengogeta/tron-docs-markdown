

org.tron.trident.proto

## Class Contract.UpdateEnergyLimitContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.UpdateEnergyLimitContract.Builder](../../../../org/tron/trident/proto/Contract.UpdateEnergyLimitContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.UpdateEnergyLimitContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.UpdateEnergyLimitContractOrBuilder](../../../../org/tron/trident/proto/Contract.UpdateEnergyLimitContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.UpdateEnergyLimitContract](../../../../org/tron/trident/proto/Contract.UpdateEnergyLimitContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.UpdateEnergyLimitContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>
  implements Contract.UpdateEnergyLimitContractOrBuilder
  ```

  Protobuf type `protocol.UpdateEnergyLimitContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.UpdateEnergyLimitContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UpdateEnergyLimitContract` | `build()` |
    | `Contract.UpdateEnergyLimitContract` | `buildPartial()` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `clear()` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `clearContractAddress()` `bytes contract_address = 2;` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `clearOriginEnergyLimit()` `int64 origin_energy_limit = 3;` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 2;` |
    | `Contract.UpdateEnergyLimitContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getOriginEnergyLimit()` `int64 origin_energy_limit = 3;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `mergeFrom(Contract.UpdateEnergyLimitContract other)` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `setContractAddress(com.google.protobuf.ByteString value)` `bytes contract_address = 2;` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `setOriginEnergyLimit(long value)` `int64 origin_energy_limit = 3;` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.UpdateEnergyLimitContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### clear

      ```
      public Contract.UpdateEnergyLimitContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.UpdateEnergyLimitContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.UpdateEnergyLimitContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.UpdateEnergyLimitContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.UpdateEnergyLimitContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### setField

      ```
      public Contract.UpdateEnergyLimitContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### clearField

      ```
      public Contract.UpdateEnergyLimitContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### clearOneof

      ```
      public Contract.UpdateEnergyLimitContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.UpdateEnergyLimitContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         int index,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.UpdateEnergyLimitContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UpdateEnergyLimitContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UpdateEnergyLimitContract.Builder mergeFrom(Contract.UpdateEnergyLimitContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UpdateEnergyLimitContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UpdateEnergyLimitContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.UpdateEnergyLimitContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.UpdateEnergyLimitContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.UpdateEnergyLimitContract.Builder clearOwnerAddress()
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
      :   `getContractAddress` in interface `Contract.UpdateEnergyLimitContractOrBuilder`

      Returns:
      :   The contractAddress.
    - #### setContractAddress

      ```
      public Contract.UpdateEnergyLimitContract.Builder setContractAddress(com.google.protobuf.ByteString value)
      ```

      `bytes contract_address = 2;`

      Parameters:
      :   `value` - The contractAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearContractAddress

      ```
      public Contract.UpdateEnergyLimitContract.Builder clearContractAddress()
      ```

      `bytes contract_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getOriginEnergyLimit

      ```
      public long getOriginEnergyLimit()
      ```

      `int64 origin_energy_limit = 3;`

      Specified by:
      :   `getOriginEnergyLimit` in interface `Contract.UpdateEnergyLimitContractOrBuilder`

      Returns:
      :   The originEnergyLimit.
    - #### setOriginEnergyLimit

      ```
      public Contract.UpdateEnergyLimitContract.Builder setOriginEnergyLimit(long value)
      ```

      `int64 origin_energy_limit = 3;`

      Parameters:
      :   `value` - The originEnergyLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearOriginEnergyLimit

      ```
      public Contract.UpdateEnergyLimitContract.Builder clearOriginEnergyLimit()
      ```

      `int64 origin_energy_limit = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.UpdateEnergyLimitContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.UpdateEnergyLimitContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UpdateEnergyLimitContract.Builder>`