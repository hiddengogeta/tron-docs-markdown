

org.tron.trident.api

## Class GrpcAPI.IvkDecryptTRC20Parameters.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.IvkDecryptTRC20Parameters.Builder](../../../../org/tron/trident/api/GrpcAPI.IvkDecryptTRC20Parameters.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.IvkDecryptTRC20ParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.IvkDecryptTRC20ParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.IvkDecryptTRC20Parameters](../../../../org/tron/trident/api/GrpcAPI.IvkDecryptTRC20Parameters.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.IvkDecryptTRC20Parameters.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>
  implements GrpcAPI.IvkDecryptTRC20ParametersOrBuilder
  ```

  Protobuf type `protocol.IvkDecryptTRC20Parameters`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `addAllEvents(java.lang.Iterable<java.lang.String> values)` `repeated string events = 7;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `addEvents(java.lang.String value)` `repeated string events = 7;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `addEventsBytes(com.google.protobuf.ByteString value)` `repeated string events = 7;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters` | `build()` |
    | `GrpcAPI.IvkDecryptTRC20Parameters` | `buildPartial()` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clear()` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clearAk()` `bytes ak = 5;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clearEndBlockIndex()` `int64 end_block_index = 2;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clearEvents()` `repeated string events = 7;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clearIvk()` `bytes ivk = 4;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clearNk()` `bytes nk = 6;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clearShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 3;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clearStartBlockIndex()` `int64 start_block_index = 1;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAk()` `bytes ak = 5;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEndBlockIndex()` `int64 end_block_index = 2;` |
    | `java.lang.String` | `getEvents(int index)` `repeated string events = 7;` |
    | `com.google.protobuf.ByteString` | `getEventsBytes(int index)` `repeated string events = 7;` |
    | `int` | `getEventsCount()` `repeated string events = 7;` |
    | `com.google.protobuf.ProtocolStringList` | `getEventsList()` `repeated string events = 7;` |
    | `com.google.protobuf.ByteString` | `getIvk()` `bytes ivk = 4;` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 6;` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 3;` |
    | `long` | `getStartBlockIndex()` `int64 start_block_index = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `mergeFrom(GrpcAPI.IvkDecryptTRC20Parameters other)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setAk(com.google.protobuf.ByteString value)` `bytes ak = 5;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setEndBlockIndex(long value)` `int64 end_block_index = 2;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setEvents(int index, java.lang.String value)` `repeated string events = 7;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setIvk(com.google.protobuf.ByteString value)` `bytes ivk = 4;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setNk(com.google.protobuf.ByteString value)` `bytes nk = 6;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setShieldedTRC20ContractAddress(com.google.protobuf.ByteString value)` `bytes shielded_TRC20_contract_address = 3;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setStartBlockIndex(long value)` `int64 start_block_index = 1;` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### clear

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### setField

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### clearField

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        int index,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder mergeFrom(GrpcAPI.IvkDecryptTRC20Parameters other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getStartBlockIndex

      ```
      public long getStartBlockIndex()
      ```

      `int64 start_block_index = 1;`

      Specified by:
      :   `getStartBlockIndex` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The startBlockIndex.
    - #### setStartBlockIndex

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder setStartBlockIndex(long value)
      ```

      `int64 start_block_index = 1;`

      Parameters:
      :   `value` - The startBlockIndex to set.

      Returns:
      :   This builder for chaining.
    - #### clearStartBlockIndex

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clearStartBlockIndex()
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
      :   `getEndBlockIndex` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The endBlockIndex.
    - #### setEndBlockIndex

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder setEndBlockIndex(long value)
      ```

      `int64 end_block_index = 2;`

      Parameters:
      :   `value` - The endBlockIndex to set.

      Returns:
      :   This builder for chaining.
    - #### clearEndBlockIndex

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clearEndBlockIndex()
      ```

      `int64 end_block_index = 2;`

      Returns:
      :   This builder for chaining.
    - #### getShieldedTRC20ContractAddress

      ```
      public com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 3;`

      Specified by:
      :   `getShieldedTRC20ContractAddress` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The shieldedTRC20ContractAddress.
    - #### setShieldedTRC20ContractAddress

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder setShieldedTRC20ContractAddress(com.google.protobuf.ByteString value)
      ```

      `bytes shielded_TRC20_contract_address = 3;`

      Parameters:
      :   `value` - The shieldedTRC20ContractAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearShieldedTRC20ContractAddress

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clearShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 3;`

      Returns:
      :   This builder for chaining.
    - #### getIvk

      ```
      public com.google.protobuf.ByteString getIvk()
      ```

      `bytes ivk = 4;`

      Specified by:
      :   `getIvk` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The ivk.
    - #### setIvk

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder setIvk(com.google.protobuf.ByteString value)
      ```

      `bytes ivk = 4;`

      Parameters:
      :   `value` - The ivk to set.

      Returns:
      :   This builder for chaining.
    - #### clearIvk

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clearIvk()
      ```

      `bytes ivk = 4;`

      Returns:
      :   This builder for chaining.
    - #### getAk

      ```
      public com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 5;`

      Specified by:
      :   `getAk` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The ak.
    - #### setAk

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder setAk(com.google.protobuf.ByteString value)
      ```

      `bytes ak = 5;`

      Parameters:
      :   `value` - The ak to set.

      Returns:
      :   This builder for chaining.
    - #### clearAk

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clearAk()
      ```

      `bytes ak = 5;`

      Returns:
      :   This builder for chaining.
    - #### getNk

      ```
      public com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 6;`

      Specified by:
      :   `getNk` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The nk.
    - #### setNk

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder setNk(com.google.protobuf.ByteString value)
      ```

      `bytes nk = 6;`

      Parameters:
      :   `value` - The nk to set.

      Returns:
      :   This builder for chaining.
    - #### clearNk

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clearNk()
      ```

      `bytes nk = 6;`

      Returns:
      :   This builder for chaining.
    - #### getEventsList

      ```
      public com.google.protobuf.ProtocolStringList getEventsList()
      ```

      `repeated string events = 7;`

      Specified by:
      :   `getEventsList` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   A list containing the events.
    - #### getEventsCount

      ```
      public int getEventsCount()
      ```

      `repeated string events = 7;`

      Specified by:
      :   `getEventsCount` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The count of events.
    - #### getEvents

      ```
      public java.lang.String getEvents(int index)
      ```

      `repeated string events = 7;`

      Specified by:
      :   `getEvents` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The events at the given index.
    - #### getEventsBytes

      ```
      public com.google.protobuf.ByteString getEventsBytes(int index)
      ```

      `repeated string events = 7;`

      Specified by:
      :   `getEventsBytes` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Parameters:
      :   `index` - The index of the value to return.

      Returns:
      :   The bytes of the events at the given index.
    - #### setEvents

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder setEvents(int index,
                                                                 java.lang.String value)
      ```

      `repeated string events = 7;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The events to set.

      Returns:
      :   This builder for chaining.
    - #### addEvents

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder addEvents(java.lang.String value)
      ```

      `repeated string events = 7;`

      Parameters:
      :   `value` - The events to add.

      Returns:
      :   This builder for chaining.
    - #### addAllEvents

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder addAllEvents(java.lang.Iterable<java.lang.String> values)
      ```

      `repeated string events = 7;`

      Parameters:
      :   `values` - The events to add.

      Returns:
      :   This builder for chaining.
    - #### clearEvents

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder clearEvents()
      ```

      `repeated string events = 7;`

      Returns:
      :   This builder for chaining.
    - #### addEventsBytes

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder addEventsBytes(com.google.protobuf.ByteString value)
      ```

      `repeated string events = 7;`

      Parameters:
      :   `value` - The bytes of the events to add.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.IvkDecryptTRC20Parameters.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.IvkDecryptTRC20Parameters.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IvkDecryptTRC20Parameters.Builder>`