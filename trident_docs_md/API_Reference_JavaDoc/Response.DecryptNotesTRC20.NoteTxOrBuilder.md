

org.tron.trident.proto

## Interface Response.DecryptNotesTRC20.NoteTxOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.DecryptNotesTRC20.NoteTx](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.NoteTx.html "class in org.tron.trident.proto"), [Response.DecryptNotesTRC20.NoteTx.Builder](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.NoteTx.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.DecryptNotesTRC20](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.DecryptNotesTRC20.NoteTxOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `int` | `getIndex()` the index of note in txid |
    | `boolean` | `getIsSpent()` `bool is_spent = 3;` |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `long` | `getPosition()` `int64 position = 2;` |
    | `java.lang.String` | `getToAmount()` `string to_amount = 6;` |
    | `com.google.protobuf.ByteString` | `getToAmountBytes()` `string to_amount = 6;` |
    | `com.google.protobuf.ByteString` | `getTransparentToAddress()` `bytes transparent_to_address = 7;` |
    | `com.google.protobuf.ByteString` | `getTxid()` `bytes txid = 4;` |
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
    - #### getPosition

      ```
      long getPosition()
      ```

      `int64 position = 2;`

      Returns:
      :   The position.
    - #### getIsSpent

      ```
      boolean getIsSpent()
      ```

      `bool is_spent = 3;`

      Returns:
      :   The isSpent.
    - #### getTxid

      ```
      com.google.protobuf.ByteString getTxid()
      ```

      `bytes txid = 4;`

      Returns:
      :   The txid.
    - #### getIndex

      ```
      int getIndex()
      ```

      ```
       the index of note in txid
      ```

      `int32 index = 5;`

      Returns:
      :   The index.
    - #### getToAmount

      ```
      java.lang.String getToAmount()
      ```

      `string to_amount = 6;`

      Returns:
      :   The toAmount.
    - #### getToAmountBytes

      ```
      com.google.protobuf.ByteString getToAmountBytes()
      ```

      `string to_amount = 6;`

      Returns:
      :   The bytes for toAmount.
    - #### getTransparentToAddress

      ```
      com.google.protobuf.ByteString getTransparentToAddress()
      ```

      `bytes transparent_to_address = 7;`

      Returns:
      :   The transparentToAddress.