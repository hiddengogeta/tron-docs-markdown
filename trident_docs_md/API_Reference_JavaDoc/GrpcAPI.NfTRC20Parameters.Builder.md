

org.tron.trident.api

## Class GrpcAPI.NfTRC20Parameters.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.NfTRC20Parameters.Builder](../../../../org/tron/trident/api/GrpcAPI.NfTRC20Parameters.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.NfTRC20Parameters.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.NfTRC20ParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.NfTRC20ParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.NfTRC20Parameters](../../../../org/tron/trident/api/GrpcAPI.NfTRC20Parameters.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.NfTRC20Parameters.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>
  implements GrpcAPI.NfTRC20ParametersOrBuilder
  ```

  Protobuf type `protocol.NfTRC20Parameters`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.NfTRC20Parameters` | `build()` |
    | `GrpcAPI.NfTRC20Parameters` | `buildPartial()` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `clear()` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `clearAk()` `bytes ak = 2;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `clearNk()` `bytes nk = 3;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `clearNote()` `.protocol.Note note = 1;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `clearPosition()` `int64 position = 4;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `clearShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 5;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAk()` `bytes ak = 2;` |
    | `GrpcAPI.NfTRC20Parameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 3;` |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.Note.Builder` | `getNoteBuilder()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `long` | `getPosition()` `int64 position = 4;` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 5;` |
    | `boolean` | `hasNote()` `.protocol.Note note = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `mergeFrom(GrpcAPI.NfTRC20Parameters other)` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `mergeNote(Common.Note value)` `.protocol.Note note = 1;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `setAk(com.google.protobuf.ByteString value)` `bytes ak = 2;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `setNk(com.google.protobuf.ByteString value)` `bytes nk = 3;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `setNote(Common.Note.Builder builderForValue)` `.protocol.Note note = 1;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `setNote(Common.Note value)` `.protocol.Note note = 1;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `setPosition(long value)` `int64 position = 4;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `setShieldedTRC20ContractAddress(com.google.protobuf.ByteString value)` `bytes shielded_TRC20_contract_address = 5;` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### clear

      ```
      public GrpcAPI.NfTRC20Parameters.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.NfTRC20Parameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.NfTRC20Parameters build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.NfTRC20Parameters buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.NfTRC20Parameters.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### setField

      ```
      public GrpcAPI.NfTRC20Parameters.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### clearField

      ```
      public GrpcAPI.NfTRC20Parameters.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.NfTRC20Parameters.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.NfTRC20Parameters.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                int index,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.NfTRC20Parameters.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.NfTRC20Parameters.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.NfTRC20Parameters.Builder mergeFrom(GrpcAPI.NfTRC20Parameters other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.NfTRC20Parameters.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.NfTRC20Parameters.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasNote

      ```
      public boolean hasNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `hasNote` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   Whether the note field is set.
    - #### getNote

      ```
      public Common.Note getNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNote` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   The note.
    - #### setNote

      ```
      public GrpcAPI.NfTRC20Parameters.Builder setNote(Common.Note value)
      ```

      `.protocol.Note note = 1;`
    - #### setNote

      ```
      public GrpcAPI.NfTRC20Parameters.Builder setNote(Common.Note.Builder builderForValue)
      ```

      `.protocol.Note note = 1;`
    - #### mergeNote

      ```
      public GrpcAPI.NfTRC20Parameters.Builder mergeNote(Common.Note value)
      ```

      `.protocol.Note note = 1;`
    - #### clearNote

      ```
      public GrpcAPI.NfTRC20Parameters.Builder clearNote()
      ```

      `.protocol.Note note = 1;`
    - #### getNoteBuilder

      ```
      public Common.Note.Builder getNoteBuilder()
      ```

      `.protocol.Note note = 1;`
    - #### getNoteOrBuilder

      ```
      public Common.NoteOrBuilder getNoteOrBuilder()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNoteOrBuilder` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`
    - #### getAk

      ```
      public com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 2;`

      Specified by:
      :   `getAk` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   The ak.
    - #### setAk

      ```
      public GrpcAPI.NfTRC20Parameters.Builder setAk(com.google.protobuf.ByteString value)
      ```

      `bytes ak = 2;`

      Parameters:
      :   `value` - The ak to set.

      Returns:
      :   This builder for chaining.
    - #### clearAk

      ```
      public GrpcAPI.NfTRC20Parameters.Builder clearAk()
      ```

      `bytes ak = 2;`

      Returns:
      :   This builder for chaining.
    - #### getNk

      ```
      public com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 3;`

      Specified by:
      :   `getNk` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   The nk.
    - #### setNk

      ```
      public GrpcAPI.NfTRC20Parameters.Builder setNk(com.google.protobuf.ByteString value)
      ```

      `bytes nk = 3;`

      Parameters:
      :   `value` - The nk to set.

      Returns:
      :   This builder for chaining.
    - #### clearNk

      ```
      public GrpcAPI.NfTRC20Parameters.Builder clearNk()
      ```

      `bytes nk = 3;`

      Returns:
      :   This builder for chaining.
    - #### getPosition

      ```
      public long getPosition()
      ```

      `int64 position = 4;`

      Specified by:
      :   `getPosition` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   The position.
    - #### setPosition

      ```
      public GrpcAPI.NfTRC20Parameters.Builder setPosition(long value)
      ```

      `int64 position = 4;`

      Parameters:
      :   `value` - The position to set.

      Returns:
      :   This builder for chaining.
    - #### clearPosition

      ```
      public GrpcAPI.NfTRC20Parameters.Builder clearPosition()
      ```

      `int64 position = 4;`

      Returns:
      :   This builder for chaining.
    - #### getShieldedTRC20ContractAddress

      ```
      public com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 5;`

      Specified by:
      :   `getShieldedTRC20ContractAddress` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   The shieldedTRC20ContractAddress.
    - #### setShieldedTRC20ContractAddress

      ```
      public GrpcAPI.NfTRC20Parameters.Builder setShieldedTRC20ContractAddress(com.google.protobuf.ByteString value)
      ```

      `bytes shielded_TRC20_contract_address = 5;`

      Parameters:
      :   `value` - The shieldedTRC20ContractAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearShieldedTRC20ContractAddress

      ```
      public GrpcAPI.NfTRC20Parameters.Builder clearShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 5;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.NfTRC20Parameters.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.NfTRC20Parameters.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.NfTRC20Parameters.Builder>`