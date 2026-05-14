

org.tron.trident.proto

## Class Contract.ContractState.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.ContractState.Builder](../../../../org/tron/trident/proto/Contract.ContractState.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.ContractState.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.ContractStateOrBuilder](../../../../org/tron/trident/proto/Contract.ContractStateOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.ContractState](../../../../org/tron/trident/proto/Contract.ContractState.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.ContractState.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>
  implements Contract.ContractStateOrBuilder
  ```

  Protobuf type `protocol.ContractState`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.ContractState.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ContractState` | `build()` |
    | `Contract.ContractState` | `buildPartial()` |
    | `Contract.ContractState.Builder` | `clear()` |
    | `Contract.ContractState.Builder` | `clearEnergyFactor()` `int64 energy_factor = 2;` |
    | `Contract.ContractState.Builder` | `clearEnergyUsage()` `int64 energy_usage = 1;` |
    | `Contract.ContractState.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.ContractState.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.ContractState.Builder` | `clearUpdateCycle()` `int64 update_cycle = 3;` |
    | `Contract.ContractState.Builder` | `clone()` |
    | `Contract.ContractState` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEnergyFactor()` `int64 energy_factor = 2;` |
    | `long` | `getEnergyUsage()` `int64 energy_usage = 1;` |
    | `long` | `getUpdateCycle()` `int64 update_cycle = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.ContractState.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.ContractState.Builder` | `mergeFrom(Contract.ContractState other)` |
    | `Contract.ContractState.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.ContractState.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.ContractState.Builder` | `setEnergyFactor(long value)` `int64 energy_factor = 2;` |
    | `Contract.ContractState.Builder` | `setEnergyUsage(long value)` `int64 energy_usage = 1;` |
    | `Contract.ContractState.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ContractState.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.ContractState.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.ContractState.Builder` | `setUpdateCycle(long value)` `int64 update_cycle = 3;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### clear

      ```
      public Contract.ContractState.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.ContractState getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.ContractState build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.ContractState buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.ContractState.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### setField

      ```
      public Contract.ContractState.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### clearField

      ```
      public Contract.ContractState.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### clearOneof

      ```
      public Contract.ContractState.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### setRepeatedField

      ```
      public Contract.ContractState.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             int index,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### addRepeatedField

      ```
      public Contract.ContractState.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### mergeFrom

      ```
      public Contract.ContractState.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ContractState.Builder>`
    - #### mergeFrom

      ```
      public Contract.ContractState.Builder mergeFrom(Contract.ContractState other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### mergeFrom

      ```
      public Contract.ContractState.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                               throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ContractState.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getEnergyUsage

      ```
      public long getEnergyUsage()
      ```

      `int64 energy_usage = 1;`

      Specified by:
      :   `getEnergyUsage` in interface `Contract.ContractStateOrBuilder`

      Returns:
      :   The energyUsage.
    - #### setEnergyUsage

      ```
      public Contract.ContractState.Builder setEnergyUsage(long value)
      ```

      `int64 energy_usage = 1;`

      Parameters:
      :   `value` - The energyUsage to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyUsage

      ```
      public Contract.ContractState.Builder clearEnergyUsage()
      ```

      `int64 energy_usage = 1;`

      Returns:
      :   This builder for chaining.
    - #### getEnergyFactor

      ```
      public long getEnergyFactor()
      ```

      `int64 energy_factor = 2;`

      Specified by:
      :   `getEnergyFactor` in interface `Contract.ContractStateOrBuilder`

      Returns:
      :   The energyFactor.
    - #### setEnergyFactor

      ```
      public Contract.ContractState.Builder setEnergyFactor(long value)
      ```

      `int64 energy_factor = 2;`

      Parameters:
      :   `value` - The energyFactor to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyFactor

      ```
      public Contract.ContractState.Builder clearEnergyFactor()
      ```

      `int64 energy_factor = 2;`

      Returns:
      :   This builder for chaining.
    - #### getUpdateCycle

      ```
      public long getUpdateCycle()
      ```

      `int64 update_cycle = 3;`

      Specified by:
      :   `getUpdateCycle` in interface `Contract.ContractStateOrBuilder`

      Returns:
      :   The updateCycle.
    - #### setUpdateCycle

      ```
      public Contract.ContractState.Builder setUpdateCycle(long value)
      ```

      `int64 update_cycle = 3;`

      Parameters:
      :   `value` - The updateCycle to set.

      Returns:
      :   This builder for chaining.
    - #### clearUpdateCycle

      ```
      public Contract.ContractState.Builder clearUpdateCycle()
      ```

      `int64 update_cycle = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.ContractState.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.ContractState.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ContractState.Builder>`