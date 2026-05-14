

org.tron.trident.api

## Class GrpcAPI.ReceiveNote.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.ReceiveNote.Builder](../../../../org/tron/trident/api/GrpcAPI.ReceiveNote.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.ReceiveNote.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.ReceiveNoteOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ReceiveNoteOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.ReceiveNote](../../../../org/tron/trident/api/GrpcAPI.ReceiveNote.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ReceiveNote.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>
  implements GrpcAPI.ReceiveNoteOrBuilder
  ```

  Protobuf type `protocol.ReceiveNote`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.ReceiveNote.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ReceiveNote` | `build()` |
    | `GrpcAPI.ReceiveNote` | `buildPartial()` |
    | `GrpcAPI.ReceiveNote.Builder` | `clear()` |
    | `GrpcAPI.ReceiveNote.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.ReceiveNote.Builder` | `clearNote()` `.protocol.Note note = 1;` |
    | `GrpcAPI.ReceiveNote.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.ReceiveNote.Builder` | `clone()` |
    | `GrpcAPI.ReceiveNote` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.Note.Builder` | `getNoteBuilder()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `boolean` | `hasNote()` `.protocol.Note note = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.ReceiveNote.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.ReceiveNote.Builder` | `mergeFrom(GrpcAPI.ReceiveNote other)` |
    | `GrpcAPI.ReceiveNote.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.ReceiveNote.Builder` | `mergeNote(Common.Note value)` `.protocol.Note note = 1;` |
    | `GrpcAPI.ReceiveNote.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.ReceiveNote.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ReceiveNote.Builder` | `setNote(Common.Note.Builder builderForValue)` `.protocol.Note note = 1;` |
    | `GrpcAPI.ReceiveNote.Builder` | `setNote(Common.Note value)` `.protocol.Note note = 1;` |
    | `GrpcAPI.ReceiveNote.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.ReceiveNote.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### clear

      ```
      public GrpcAPI.ReceiveNote.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ReceiveNote getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.ReceiveNote build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.ReceiveNote buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.ReceiveNote.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### setField

      ```
      public GrpcAPI.ReceiveNote.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                  java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### clearField

      ```
      public GrpcAPI.ReceiveNote.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.ReceiveNote.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.ReceiveNote.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                          int index,
                                                          java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.ReceiveNote.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                          java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ReceiveNote.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ReceiveNote.Builder mergeFrom(GrpcAPI.ReceiveNote other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ReceiveNote.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                            throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ReceiveNote.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasNote

      ```
      public boolean hasNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `hasNote` in interface `GrpcAPI.ReceiveNoteOrBuilder`

      Returns:
      :   Whether the note field is set.
    - #### getNote

      ```
      public Common.Note getNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNote` in interface `GrpcAPI.ReceiveNoteOrBuilder`

      Returns:
      :   The note.
    - #### setNote

      ```
      public GrpcAPI.ReceiveNote.Builder setNote(Common.Note value)
      ```

      `.protocol.Note note = 1;`
    - #### setNote

      ```
      public GrpcAPI.ReceiveNote.Builder setNote(Common.Note.Builder builderForValue)
      ```

      `.protocol.Note note = 1;`
    - #### mergeNote

      ```
      public GrpcAPI.ReceiveNote.Builder mergeNote(Common.Note value)
      ```

      `.protocol.Note note = 1;`
    - #### clearNote

      ```
      public GrpcAPI.ReceiveNote.Builder clearNote()
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
      :   `getNoteOrBuilder` in interface `GrpcAPI.ReceiveNoteOrBuilder`
    - #### setUnknownFields

      ```
      public final GrpcAPI.ReceiveNote.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.ReceiveNote.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveNote.Builder>`