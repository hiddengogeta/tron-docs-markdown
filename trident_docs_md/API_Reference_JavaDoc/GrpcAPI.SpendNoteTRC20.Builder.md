

org.tron.trident.api

## Class GrpcAPI.SpendNoteTRC20.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.SpendNoteTRC20.Builder](../../../../org/tron/trident/api/GrpcAPI.SpendNoteTRC20.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.SpendNoteTRC20.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.SpendNoteTRC20OrBuilder](../../../../org/tron/trident/api/GrpcAPI.SpendNoteTRC20OrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.SpendNoteTRC20](../../../../org/tron/trident/api/GrpcAPI.SpendNoteTRC20.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.SpendNoteTRC20.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>
  implements GrpcAPI.SpendNoteTRC20OrBuilder
  ```

  Protobuf type `protocol.SpendNoteTRC20`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.SpendNoteTRC20` | `build()` |
    | `GrpcAPI.SpendNoteTRC20` | `buildPartial()` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `clear()` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `clearAlpha()` `bytes alpha = 2;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `clearNote()` `.protocol.Note note = 1;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `clearPath()` `bytes path = 4;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `clearPos()` `int64 pos = 5;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `clearRoot()` `bytes root = 3;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAlpha()` `bytes alpha = 2;` |
    | `GrpcAPI.SpendNoteTRC20` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.Note.Builder` | `getNoteBuilder()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `com.google.protobuf.ByteString` | `getPath()` `bytes path = 4;` |
    | `long` | `getPos()` `int64 pos = 5;` |
    | `com.google.protobuf.ByteString` | `getRoot()` `bytes root = 3;` |
    | `boolean` | `hasNote()` `.protocol.Note note = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `mergeFrom(GrpcAPI.SpendNoteTRC20 other)` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `mergeNote(Common.Note value)` `.protocol.Note note = 1;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `setAlpha(com.google.protobuf.ByteString value)` `bytes alpha = 2;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `setNote(Common.Note.Builder builderForValue)` `.protocol.Note note = 1;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `setNote(Common.Note value)` `.protocol.Note note = 1;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `setPath(com.google.protobuf.ByteString value)` `bytes path = 4;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `setPos(long value)` `int64 pos = 5;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `setRoot(com.google.protobuf.ByteString value)` `bytes root = 3;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### clear

      ```
      public GrpcAPI.SpendNoteTRC20.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.SpendNoteTRC20 getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.SpendNoteTRC20 build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.SpendNoteTRC20 buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.SpendNoteTRC20.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### setField

      ```
      public GrpcAPI.SpendNoteTRC20.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### clearField

      ```
      public GrpcAPI.SpendNoteTRC20.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.SpendNoteTRC20.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.SpendNoteTRC20.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             int index,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.SpendNoteTRC20.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.SpendNoteTRC20.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.SpendNoteTRC20.Builder mergeFrom(GrpcAPI.SpendNoteTRC20 other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.SpendNoteTRC20.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                               throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.SpendNoteTRC20.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasNote

      ```
      public boolean hasNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `hasNote` in interface `GrpcAPI.SpendNoteTRC20OrBuilder`

      Returns:
      :   Whether the note field is set.
    - #### getNote

      ```
      public Common.Note getNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNote` in interface `GrpcAPI.SpendNoteTRC20OrBuilder`

      Returns:
      :   The note.
    - #### setNote

      ```
      public GrpcAPI.SpendNoteTRC20.Builder setNote(Common.Note value)
      ```

      `.protocol.Note note = 1;`
    - #### setNote

      ```
      public GrpcAPI.SpendNoteTRC20.Builder setNote(Common.Note.Builder builderForValue)
      ```

      `.protocol.Note note = 1;`
    - #### mergeNote

      ```
      public GrpcAPI.SpendNoteTRC20.Builder mergeNote(Common.Note value)
      ```

      `.protocol.Note note = 1;`
    - #### clearNote

      ```
      public GrpcAPI.SpendNoteTRC20.Builder clearNote()
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
      :   `getNoteOrBuilder` in interface `GrpcAPI.SpendNoteTRC20OrBuilder`
    - #### getAlpha

      ```
      public com.google.protobuf.ByteString getAlpha()
      ```

      `bytes alpha = 2;`

      Specified by:
      :   `getAlpha` in interface `GrpcAPI.SpendNoteTRC20OrBuilder`

      Returns:
      :   The alpha.
    - #### setAlpha

      ```
      public GrpcAPI.SpendNoteTRC20.Builder setAlpha(com.google.protobuf.ByteString value)
      ```

      `bytes alpha = 2;`

      Parameters:
      :   `value` - The alpha to set.

      Returns:
      :   This builder for chaining.
    - #### clearAlpha

      ```
      public GrpcAPI.SpendNoteTRC20.Builder clearAlpha()
      ```

      `bytes alpha = 2;`

      Returns:
      :   This builder for chaining.
    - #### getRoot

      ```
      public com.google.protobuf.ByteString getRoot()
      ```

      `bytes root = 3;`

      Specified by:
      :   `getRoot` in interface `GrpcAPI.SpendNoteTRC20OrBuilder`

      Returns:
      :   The root.
    - #### setRoot

      ```
      public GrpcAPI.SpendNoteTRC20.Builder setRoot(com.google.protobuf.ByteString value)
      ```

      `bytes root = 3;`

      Parameters:
      :   `value` - The root to set.

      Returns:
      :   This builder for chaining.
    - #### clearRoot

      ```
      public GrpcAPI.SpendNoteTRC20.Builder clearRoot()
      ```

      `bytes root = 3;`

      Returns:
      :   This builder for chaining.
    - #### getPath

      ```
      public com.google.protobuf.ByteString getPath()
      ```

      `bytes path = 4;`

      Specified by:
      :   `getPath` in interface `GrpcAPI.SpendNoteTRC20OrBuilder`

      Returns:
      :   The path.
    - #### setPath

      ```
      public GrpcAPI.SpendNoteTRC20.Builder setPath(com.google.protobuf.ByteString value)
      ```

      `bytes path = 4;`

      Parameters:
      :   `value` - The path to set.

      Returns:
      :   This builder for chaining.
    - #### clearPath

      ```
      public GrpcAPI.SpendNoteTRC20.Builder clearPath()
      ```

      `bytes path = 4;`

      Returns:
      :   This builder for chaining.
    - #### getPos

      ```
      public long getPos()
      ```

      `int64 pos = 5;`

      Specified by:
      :   `getPos` in interface `GrpcAPI.SpendNoteTRC20OrBuilder`

      Returns:
      :   The pos.
    - #### setPos

      ```
      public GrpcAPI.SpendNoteTRC20.Builder setPos(long value)
      ```

      `int64 pos = 5;`

      Parameters:
      :   `value` - The pos to set.

      Returns:
      :   This builder for chaining.
    - #### clearPos

      ```
      public GrpcAPI.SpendNoteTRC20.Builder clearPos()
      ```

      `int64 pos = 5;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.SpendNoteTRC20.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.SpendNoteTRC20.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendNoteTRC20.Builder>`