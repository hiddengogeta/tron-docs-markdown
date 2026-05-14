

org.tron.trident.api

## Interface GrpcAPI.ReceiveNoteOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.ReceiveNote](../../../../org/tron/trident/api/GrpcAPI.ReceiveNote.html "class in org.tron.trident.api"), [GrpcAPI.ReceiveNote.Builder](../../../../org/tron/trident/api/GrpcAPI.ReceiveNote.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.ReceiveNoteOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `boolean` | `hasNote()` `.protocol.Note note = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasNote

      ```
      boolean hasNote()
      ```

      `.protocol.Note note = 1;`

      Returns:
      :   Whether the note field is set.
    - #### getNote

      ```
      Common.Note getNote()
      ```

      `.protocol.Note note = 1;`

      Returns:
      :   The note.
    - #### getNoteOrBuilder

      ```
      Common.NoteOrBuilder getNoteOrBuilder()
      ```

      `.protocol.Note note = 1;`