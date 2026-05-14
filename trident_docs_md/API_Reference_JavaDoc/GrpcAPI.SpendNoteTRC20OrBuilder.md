

org.tron.trident.api

## Interface GrpcAPI.SpendNoteTRC20OrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.SpendNoteTRC20](../../../../org/tron/trident/api/GrpcAPI.SpendNoteTRC20.html "class in org.tron.trident.api"), [GrpcAPI.SpendNoteTRC20.Builder](../../../../org/tron/trident/api/GrpcAPI.SpendNoteTRC20.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.SpendNoteTRC20OrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAlpha()` `bytes alpha = 2;` |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `com.google.protobuf.ByteString` | `getPath()` `bytes path = 4;` |
    | `long` | `getPos()` `int64 pos = 5;` |
    | `com.google.protobuf.ByteString` | `getRoot()` `bytes root = 3;` |
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
    - #### getAlpha

      ```
      com.google.protobuf.ByteString getAlpha()
      ```

      `bytes alpha = 2;`

      Returns:
      :   The alpha.
    - #### getRoot

      ```
      com.google.protobuf.ByteString getRoot()
      ```

      `bytes root = 3;`

      Returns:
      :   The root.
    - #### getPath

      ```
      com.google.protobuf.ByteString getPath()
      ```

      `bytes path = 4;`

      Returns:
      :   The path.
    - #### getPos

      ```
      long getPos()
      ```

      `int64 pos = 5;`

      Returns:
      :   The pos.