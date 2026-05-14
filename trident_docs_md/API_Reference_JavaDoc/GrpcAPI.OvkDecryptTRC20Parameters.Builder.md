

org.tron.trident.api

## Class GrpcAPI.OvkDecryptTRC20Parameters.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.OvkDecryptTRC20Parameters.Builder](../../../../org/tron/trident/api/GrpcAPI.OvkDecryptTRC20Parameters.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.OvkDecryptTRC20Parameters.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.OvkDecryptTRC20ParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.OvkDecryptTRC20ParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.OvkDecryptTRC20Parameters](../../../../org/tron/trident/api/GrpcAPI.OvkDecryptTRC20Parameters.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.OvkDecryptTRC20Parameters.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>
  implements GrpcAPI.OvkDecryptTRC20ParametersOrBuilder
  ```

  Protobuf type `protocol.OvkDecryptTRC20Parameters`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `addAllEvents(java.lang.Iterable<java.lang.String> values)` `repeated string events = 5;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `addEvents(java.lang.String value)` `repeated string events = 5;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `addEventsBytes(com.google.protobuf.ByteString value)` `repeated string events = 5;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.OvkDecryptTRC20Parameters` | `build()` |
    | `GrpcAPI.OvkDecryptTRC20Parameters` | `buildPartial()` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `clear()` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `clearEndBlockIndex()` `int64 end_block_index = 2;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `clearEvents()` `repeated string events = 5;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `clearOvk()` `bytes ovk = 3;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `clearShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 4;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `clearStartBlockIndex()` `int64 start_block_index = 1;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `clone()` |
    | `GrpcAPI.OvkDecryptTRC20Parameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEndBlockIndex()` `int64 end_block_index = 2;` |
    | `java.lang.String` | `getEvents(int index)` `repeated string events = 5;` |
    | `com.google.protobuf.ByteString` | `getEventsBytes(int index)` `repeated string events = 5;` |
    | `int` | `getEventsCount()` `repeated string events = 5;` |
    | `com.google.protobuf.ProtocolStringList` | `getEventsList()` `repeated string events = 5;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 3;` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 4;` |
    | `long` | `getStartBlockIndex()` `int64 start_block_index = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `mergeFrom(GrpcAPI.OvkDecryptTRC20Parameters other)` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `setEndBlockIndex(long value)` `int64 end_block_index = 2;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `setEvents(int index, java.lang.String value)` `repeated string events = 5;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `setOvk(com.google.protobuf.ByteString value)` `bytes ovk = 3;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `setShieldedTRC20ContractAddress(com.google.protobuf.ByteString value)` `bytes shielded_TRC20_contract_address = 4;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `setStartBlockIndex(long value)` `int64 start_block_index = 1;` |
    | `GrpcAPI.OvkDecryptTRC20Parameters.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### clear

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### setField

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### clearField

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        int index,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder mergeFrom(GrpcAPI.OvkDecryptTRC20Parameters other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getStartBlockIndex

      ```
      public long getStartBlockIndex()
      ```

      `int64 start_block_index = 1;`

      Specified by:
      :   `getStartBlockIndex` in interface `GrpcAPI.OvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The startBlockIndex.
    - #### setStartBlockIndex

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder setStartBlockIndex(long value)
      ```

      `int64 start_block_index = 1;`

      Parameters:
      :   `value` - The startBlockIndex to set.

      Returns:
      :   This builder for chaining.
    - #### clearStartBlockIndex

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder clearStartBlockIndex()
      ```

      `int64 start_block_index = 1;`

      Returns:
      :   This builder for chaining.
    - #### getEndBlockIndex

      ```
      public long getEndBlockIndex()
      ```

      `int64 end_block_index = 2;`

      Specified by:
      :   `getEndBlockIndex` in interface `GrpcAPI.OvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The endBlockIndex.
    - #### setEndBlockIndex

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder setEndBlockIndex(long value)
      ```

      `int64 end_block_index = 2;`

      Parameters:
      :   `value` - The endBlockIndex to set.

      Returns:
      :   This builder for chaining.
    - #### clearEndBlockIndex

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder clearEndBlockIndex()
      ```

      `int64 end_block_index = 2;`

      Returns:
      :   This builder for chaining.
    - #### getOvk

      ```
      public com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 3;`

      Specified by:
      :   `getOvk` in interface `GrpcAPI.OvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The ovk.
    - #### setOvk

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder setOvk(com.google.protobuf.ByteString value)
      ```

      `bytes ovk = 3;`

      Parameters:
      :   `value` - The ovk to set.

      Returns:
      :   This builder for chaining.
    - #### clearOvk

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder clearOvk()
      ```

      `bytes ovk = 3;`

      Returns:
      :   This builder for chaining.
    - #### getShieldedTRC20ContractAddress

      ```
      public com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 4;`

      Specified by:
      :   `getShieldedTRC20ContractAddress` in interface `GrpcAPI.OvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The shieldedTRC20ContractAddress.
    - #### setShieldedTRC20ContractAddress

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder setShieldedTRC20ContractAddress(com.google.protobuf.ByteString value)
      ```

      `bytes shielded_TRC20_contract_address = 4;`

      Parameters:
      :   `value` - The shieldedTRC20ContractAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearShieldedTRC20ContractAddress

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder clearShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 4;`

      Returns:
      :   This builder for chaining.
    - #### getEventsList

      ```
      public com.google.protobuf.ProtocolStringList getEventsList()
      ```

      `repeated string events = 5;`

      Specified by:
      :   `getEventsList` in interface `GrpcAPI.OvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   A list containing the events.
    - #### getEventsCount

      ```
      public int getEventsCount()
      ```

      `repeated string events = 5;`

      Specified by:
      :   `getEventsCount` in interface `GrpcAPI.OvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The count of events.
    - #### getEvents

      ```
      public java.lang.String getEvents(int index)
      ```

      `repeated string events = 5;`

      Specified by:
      :   `getEvents` in interface `GrpcAPI.OvkDecryptTRC20ParametersOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The events at the given index.
    - #### getEventsBytes

      ```
      public com.google.protobuf.ByteString getEventsBytes(int index)
      ```

      `repeated string events = 5;`

      Specified by:
      :   `getEventsBytes` in interface `GrpcAPI.OvkDecryptTRC20ParametersOrBuilder`

      Parameters:
      :   `index` - The index of the value to return.

      Returns:
      :   The bytes of the events at the given index.
    - #### setEvents

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder setEvents(int index,
                                                                 java.lang.String value)
      ```

      `repeated string events = 5;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The events to set.

      Returns:
      :   This builder for chaining.
    - #### addEvents

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder addEvents(java.lang.String value)
      ```

      `repeated string events = 5;`

      Parameters:
      :   `value` - The events to add.

      Returns:
      :   This builder for chaining.
    - #### addAllEvents

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder addAllEvents(java.lang.Iterable<java.lang.String> values)
      ```

      `repeated string events = 5;`

      Parameters:
      :   `values` - The events to add.

      Returns:
      :   This builder for chaining.
    - #### clearEvents

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder clearEvents()
      ```

      `repeated string events = 5;`

      Returns:
      :   This builder for chaining.
    - #### addEventsBytes

      ```
      public GrpcAPI.OvkDecryptTRC20Parameters.Builder addEventsBytes(com.google.protobuf.ByteString value)
      ```

      `repeated string events = 5;`

      Parameters:
      :   `value` - The bytes of the events to add.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.OvkDecryptTRC20Parameters.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.OvkDecryptTRC20Parameters.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.OvkDecryptTRC20Parameters.Builder>`